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