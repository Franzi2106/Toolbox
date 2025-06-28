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