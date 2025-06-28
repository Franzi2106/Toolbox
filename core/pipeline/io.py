# core/pipeline/io.py

def make_paths(subject_id):
    """
    Given a subject_id, return the two key file‐paths:
      - T1 image file path
      - Atlas file path
    (In practice you’d discover these under your BIDS/data_dir.)
    """
    # TODO: point this at your real BIDS tree
    t1_path    = f"/data/rawdata-archive/IndivConn/{subject_id}/anat/{subject_id}_T1w.nii.gz"
    atlas_path = "/data/atlases/Schaefer2018_400Parcels.nii.gz"
    return t1_path, atlas_path


def io_workflow(config):
    """Return a simple workflow that discovers file paths."""
    from nipype import Workflow, Node
    from nipype.interfaces.utility import Function

    wf = Workflow(name="io_workflow")

    node = Node(
        Function(
            input_names=["subject_id"],
            output_names=["t1_path", "atlas_path"],
            function=make_paths,
        ),
        name="make_paths",
    )

    subject_id = config.get("APP", "subject_id", fallback="")
    node.inputs.subject_id = subject_id

    wf.add_nodes([node])
    return wf
