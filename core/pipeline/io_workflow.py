"""I/O discovery workflow."""

from nipype import Workflow, Node, Function


def make_paths(subject_id):
    """Return absolute paths for the subject T1 and atlas."""

    t1_path = (
        "/data/rawdata-archive/IndivConn/"
        "sub-IndivConn000002/ses-01/anat/"
        "sub-IndivConn000002_ses-01_run-01_T1w.nii.gz"
    )
    atlas_path = (
        "/data/env/parcellations_atlases/AtlasPack/Schaefer/"
        "tpl-MNI152NLin6Asym_atlas-Schaefer2018v0143_res-01_desc-"
        "400ParcelsAllNetworks_dseg.nii.gz"
    )
    return t1_path, atlas_path


def io_workflow(config):
    """Create a Nipype workflow that discovers input file paths."""
    wf = Workflow(name="io_workflow")

    make_paths_node = Node(
        Function(
            input_names=["subject_id"],
            output_names=["t1_path", "atlas_path"],
            function=make_paths,
        ),
        name="make_paths",
    )

    make_paths_node.inputs.subject_id = config.get("APP", "subject_id", fallback="testsubj")

    wf.add_nodes([make_paths_node])
    return wf

