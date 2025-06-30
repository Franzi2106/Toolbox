"""Parcellation workflow."""
from pathlib import Path
from nipype import Workflow, Node, Function


def apply_parcellation(t1_path: str, atlas_path: str, out_dir: str = "."):
    """Return the expected output label map path (placeholder)."""

    atlas_base = Path(atlas_path).with_suffix("").stem
    out_fname = f"{atlas_base}_in_subject.nii.gz"
    out_path = str(Path(out_dir) / out_fname)

    # TODO: call registration tools here (e.g. FLIRT via Singularity)
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

