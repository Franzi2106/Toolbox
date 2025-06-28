# core/pipeline/parcellation.py

import os

def apply_parcellation(t1_path, atlas_path, out_dir="."):
    """
    Stub for atlas→subject‐space parcellation.
    Returns the “label_map” filepath that you will later load.
    """
    # Build an output filename in out_dir
    atlas_base = os.path.basename(atlas_path).replace(".nii.gz", "")
    out_fname  = f"{atlas_base}_in_subject.nii.gz"
    out_path   = os.path.join(out_dir, out_fname)

    # TODO: here you’d call your singularity/ANTS or FLIRT command,
    #       e.g. `singularity exec fsl.simg flirt ... -o out_path`
    # For now, just pretend the file was created:
    return out_path


def parc_workflow(config):
    """Return a workflow that runs the parcellation step."""
    from nipype import Workflow, Node
    from nipype.interfaces.utility import Function

    wf = Workflow(name="parc_workflow")

    node = Node(
        Function(
            input_names=["t1_path", "atlas_path", "out_dir"],
            output_names=["label_map"],
            function=apply_parcellation,
        ),
        name="apply_parcellation",
    )

    node.inputs.out_dir = config.get("PATHS", "output_dir", fallback=".")

    wf.add_nodes([node])
    return wf
