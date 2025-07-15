# NOT Swane inspired. Try Out Code 

"""Parcellation workflow."""
from pathlib import Path
import os
import shutil
import subprocess
import tempfile

from nipype import Workflow, Node, Function


def apply_parcellation(t1_path: str, atlas_path: str, out_dir: str = "."):
    """Warp ``atlas_path`` into ``t1_path`` space using FSL's FLIRT."""

    atlas_base = Path(atlas_path).with_suffix("").stem
    out_fname = f"{atlas_base}_in_subject.nii.gz"
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = str(out_dir / out_fname)

    def get_cmd(tool: str):
        local = shutil.which(tool)
        singularity_img = os.environ.get("FSL_SINGULARITY_IMAGE")
        if singularity_img:
            return ["singularity", "exec", singularity_img, tool]
        if local:
            return [local]
        raise RuntimeError(f"{tool} not found – install FSL or set FSL_SINGULARITY_IMAGE")

    flirt_cmd = get_cmd("flirt")
    bet_cmd = get_cmd("bet")

    def run(cmd):
        try:
            subprocess.run(cmd, check=True)
        except subprocess.CalledProcessError as exc:
            raise RuntimeError(f"Command {' '.join(cmd)} failed with exit code {exc.returncode}") from exc

    with tempfile.TemporaryDirectory() as tmpdir:
        t1_brain = Path(tmpdir) / "t1_brain.nii.gz"
        # Skull-strip the reference T1 to improve registration accuracy
        bet_cmd_full = bet_cmd + [t1_path, str(t1_brain), "-R", "-f", "0.5"]
        run(bet_cmd_full)

        flirt_full = flirt_cmd + [
            "-in",
            atlas_path,
            "-ref",
            str(t1_brain),
            "-out",
            out_path,
            "-interp",
            "nearestneighbour",
            "-cost",
            "mutualinfo",
            "-searchrx",
            "-90",
            "90",
            "-searchry",
            "-90",
            "90",
            "-searchrz",
            "-90",
            "90",
            "-dof",
            "6",
        ]
        run(flirt_full)

    return out_path


def parc_workflow(config):
    """Create a Nipype workflow that performs atlas parcellation."""

    wf = Workflow(name="parc_workflow")

    parc_node = Node(
        Function(
            input_names=["t1_path", "atlas_path", "out_dir"],
            output_names=["label_map"],
            function=apply_parcellation,
        ),
        name="apply_parcellation",
    )

    parc_node.inputs.out_dir = config.get("PATHS", "output_dir", fallback=".")

    wf.add_nodes([parc_node])
    return wf

