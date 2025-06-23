A lightweight, modular Python toolbox for generating and visualizing subject‐specific, ROI‐based connectome maps from any combination of continuous neuroimaging modalities (e.g. fMRI, PET, DTI, EEG) in native T1 space.

⸻

Key Features
	•	Atlas‐Driven Parcellation
Warp a standard atlas (e.g. Schaefer-400) once into each subject’s T1 and reuse for all modalities.
	•	Flexible Modality Alignment
Linear‐only registration (FSL FLIRT or NiBabel) to coregister any new scan (PET, fMRI, DTI, CT, etc.) into T1 space.
	•	ROI‐Wise Feature Extraction
Vectorized NumPy pipeline to compute mean, median, or sum of voxel values per parcel—no Python loops.
	•	Centralized Subject Dictionary
Collects all inputs, transforms, ROI masks, and feature vectors in one nested Python dict for easy downstream analysis.
	•	3D Visualization Module
Overlay parcel‐wise values on the subject’s T1 volume or cortical surface; optional node‐and‐edge graph support.
	•	BIDS Compatibility
Accepts any preprocessed NIfTI inputs organized in BIDS, SPM, or FSL conventions.

Pipeline Overview
	1.	Initialization
	•	Load subject T1
	•	Register standard atlas → T1
	•	Save ROI label‐map
	2.	Add Modality
	•	Linear coregistration (FLIRT or affine via NiBabel)
	•	Resample modality → T1 grid
	•	Extract ROI‐wise summary (mean/median/sum)
	3.	Visualization
	•	Volumetric overlay on T1 slices
	•	Surface rendering or 3D node plot
	•	Optional edges for connectivity
