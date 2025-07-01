"""Parcellation workflow."""

from pathlib import Path
import os
import shutil
import subprocess

from nipype import Workflow, Node, Function


def apply_parcellation(t1_path: str, atlas_path: str, out_dir: str = "."):
    """Warp ``atlas_path`` into ``t1_path`` space using FSL's FLIRT."""

    atlas_base = Path(atlas_path).with_suffix("").stem
    out_fname = f"{atlas_base}_in_subject.nii.gz"
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = str(out_dir / out_fname)

    # Build FLIRT command.  We support running either directly if ``flirt`` is
    # available on ``PATH`` or through a Singularity container specified via the
    # ``FSL_SINGULARITY_IMAGE`` environment variable.
    flirt_exec = shutil.which("flirt")
    singularity_img = os.environ.get("FSL_SINGULARITY_IMAGE")

    if singularity_img:
        cmd = ["singularity", "exec", singularity_img, "flirt"]
    elif flirt_exec:
        cmd = [flirt_exec]
    else:
        raise RuntimeError("FLIRT not found – install FSL or set FSL_SINGULARITY_IMAGE")

    cmd += [
        "-in",
        atlas_path,
        "-ref",
        t1_path,
        "-out",
        out_path,
        "-interp",
        "nearestneighbour",
    ]

    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as exc:
        raise RuntimeError(f"FLIRT failed with exit code {exc.returncode}") from exc

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
