import nibabel as nib
def extract_nifti_info(nt1):
    """
    Extrahiert relevante Informationen aus NIfTI-Bild und gibt sie als Dictionary zurück.
    """
    img = nib.load(nt1)
    data = img.get_fdata()
    header = img.header
    
    info = {
        "file_path": nt1,
        "data_shape": data.shape,
        "voxel_size": header.get_zooms(),         # (x, y, z) in mm
        "affine": img.affine.tolist(),            
        "data_dtype": str(data.dtype),
        "header_dtype": str(header.get_data_dtype()),
        "min_intensity": float(data.min()),
        "max_intensity": float(data.max()),
        "mean_intensity": float(data.mean()),
    }
    return info

