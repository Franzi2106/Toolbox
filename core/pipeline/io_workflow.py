"""I/O discovery workflow."""

from nipype import Workflow, Node, Function


def make_paths(subject_id):
    """Return placeholder paths for T1 and atlas images."""
    t1_path = f"/data/rawdata-archive/IndivConn/{subject_id}/anat/{subject_id}_T1w.nii.gz"
    atlas_path = "/data/atlases/Schaefer2018_400Parcels.nii.gz"
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

