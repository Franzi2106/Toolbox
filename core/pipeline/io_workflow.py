# Nipype Workflow for finding the correct file paths for T1 image and  atlas based on configuration settings.

"""I/O discovery workflow."""

from pathlib import Path
from nipype import Workflow, Node, Function


def make_paths(subject_id, bids_root, reference_T1, atlas_path):
    """Return absolute paths for the subject T1 and atlas. Checks whether a BIDS root directory or a direct reference_T1 path is given. """

    if bids_root:
        t1_file = Path(bids_root) / subject_id / "ses-01" / "anat" / f"{subject_id}_ses-01_run-01_T1w.nii.gz"
        t1_path = str(t1_file)
    elif reference_T1:
        t1_path = reference_T1
    else:
        raise ValueError("No bids_root or reference_T1 set in config – cannot find T1.")

    if not atlas_path:
        raise ValueError("No atlas_path set in config – cannot find atlas.")

    return t1_path, atlas_path


def io_workflow(config):
    """Create a Nipype workflow that discovers input file paths."""
    wf = Workflow(name="io_workflow")

    make_paths_node = Node(
        Function(
            input_names=["subject_id", "bids_root", "reference_T1", "atlas_path"],
            output_names=["t1_path",     "atlas_path"],
            function=make_paths,
        ),
        name="make_paths",
    )

# Inputs füllen
    make_paths_node.inputs.subject_id   = config.get("APP",   "subject_id",   fallback="testsubj")
    make_paths_node.inputs.bids_root    = config.get("PATHS", "bids_root",    fallback="")
    make_paths_node.inputs.reference_T1 = config.get("PATHS", "reference_T1", fallback="")
    make_paths_node.inputs.atlas_path   = config.get("PATHS", "atlas_path",   fallback="")

    wf.add_nodes([make_paths_node])
    return wf 
    