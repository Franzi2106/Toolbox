"""Subject dictionary assembly workflow."""

from nipype import Workflow, Node, Function


def build_subject_dict(subject_id: str, t1_path: str, label_map: str):
    """Return a basic dictionary describing the subject."""

    return {
        "subject_id": subject_id,
        "t1_file": t1_path,
        "label_map": label_map,
    }


def subjectdict_workflow(config):
    """Create a Nipype workflow that builds the subject dictionary."""

    wf = Workflow(name="subjectdict_workflow")

    sd_node = Node(
        Function(
            input_names=["subject_id", "t1_path", "label_map"],
            output_names=["subject_dict"],
            function=build_subject_dict,
        ),
        name="build_subject_dict",
    )

    sd_node.inputs.subject_id = config.get("APP", "subject_id", fallback="testsubj")

    wf.add_nodes([sd_node])
    return wf