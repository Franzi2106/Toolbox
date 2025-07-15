Node: io_workflow (make_paths (utility)
=======================================


 Hierarchy : MainWorkflow.io_workflow.make_paths
 Exec ID : make_paths


Original Inputs
---------------


* function_str : """I/O discovery workflow."""

from pathlib import Path
from nipype import Workflow, Node, Function


def make_paths(subject_id, bids_root, reference_T1, atlas_path):
    """Return absolute paths for the subject T1 and atlas."""

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

* subject_id : sub-IndivConn000002

