# core/pipeline/subjectdict.py

def build_subject_dict(subject_id, t1_path, label_map):
    """
    Assemble your subject dictionary of results.
    """
    return {
        "subject_id": subject_id,
        "t1_file": t1_path,
        "label_map": label_map,
        # later: add {roi_index: feature_value} here
    }


def subjectdict_workflow(config):
    """Return a workflow that assembles the subject dictionary."""
    from nipype import Workflow, Node
    from nipype.interfaces.utility import Function

    wf = Workflow(name="subjectdict_workflow")

    node = Node(
        Function(
            input_names=["subject_id", "t1_path", "label_map"],
            output_names=["subject_dict"],
            function=build_subject_dict,
        ),
        name="build_subject_dict",
    )

    node.inputs.subject_id = config.get("APP", "subject_id", fallback="")

    wf.add_nodes([node])
    return wf
