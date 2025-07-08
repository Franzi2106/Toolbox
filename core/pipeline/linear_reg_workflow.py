"""Simple linear registration workflow using FSL's FLIRT."""
from pathlib import Path
import os
import shutil
import subprocess

from nipype import Workflow, Node, Function


def linear_register(moving_image: str, reference_image: str, out_dir: str = "."):
    """Register ``moving_image`` to ``reference_image`` using FLIRT."""
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    base = Path(moving_image).with_suffix("").stem
    out_path = str(out_dir / f"{base}_reg.nii.gz")

    def get_cmd(tool: str):
        local = shutil.which(tool)
        img = os.environ.get("FSL_SINGULARITY_IMAGE")
        if img:
            return ["singularity", "exec", img, tool]
        if local:
            return [local]
        raise RuntimeError(
            f"{tool} not found – install FSL or set FSL_SINGULARITY_IMAGE"
        )

    cmd = get_cmd("flirt") + [
        "-in",
        moving_image,
        "-ref",
        reference_image,
        "-out",
        out_path,
        "-interp",
        "trilinear",
        "-cost",
        "mutualinfo",
        "-dof",
        "6",
    ]
    subprocess.run(cmd, check=True)
    return out_path


def linear_reg_workflow(config):
    """Create a Nipype workflow for linear registration."""
    wf = Workflow(name="linear_reg_workflow")

    reg_node = Node(
        Function(
            input_names=["moving_image", "reference_image", "out_dir"],
            output_names=["registered_file"],
            function=linear_register,
        ),
        name="linear_register",
    )

    reg_node.inputs.moving_image = config.get("PATHS", "moving_image", fallback="")
    reg_node.inputs.out_dir = config.get("PATHS", "output_dir", fallback=".")

    wf.add_nodes([reg_node])
    return wf
