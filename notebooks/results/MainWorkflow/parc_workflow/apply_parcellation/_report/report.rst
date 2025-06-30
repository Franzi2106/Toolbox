Node: parc_workflow (apply_parcellation (utility)
=================================================


 Hierarchy : MainWorkflow.parc_workflow.apply_parcellation
 Exec ID : apply_parcellation


Original Inputs
---------------


* atlas_path : /data/env/parcellations_atlases/AtlasPack/Schaefer/tpl-MNI152NLin6Asym_atlas-Schaefer2018v0143_res-01_desc-400ParcelsAllNetworks_dseg.nii.gz
* function_str : def apply_parcellation(t1_path: str, atlas_path: str, out_dir: str = "."):
    """Return the expected output label map path (placeholder)."""

    # Function nodes execute in a new Python context.  Import dependencies
    # inside the function so they are available when the node runs.
    from pathlib import Path

    atlas_base = Path(atlas_path).with_suffix("").stem
    out_fname = f"{atlas_base}_in_subject.nii.gz"
    out_path = str(Path(out_dir) / out_fname)

    # TODO: call registration tools here (e.g. FLIRT via Singularity)
    return out_path

* out_dir : ./results
* t1_path : /data/rawdata-archive/IndivConn/sub-IndivConn000002/ses-01/anat/sub-IndivConn000002_ses-01_run-01_T1w.nii.gz


Execution Inputs
----------------


* atlas_path : /data/env/parcellations_atlases/AtlasPack/Schaefer/tpl-MNI152NLin6Asym_atlas-Schaefer2018v0143_res-01_desc-400ParcelsAllNetworks_dseg.nii.gz
* function_str : def apply_parcellation(t1_path: str, atlas_path: str, out_dir: str = "."):
    """Return the expected output label map path (placeholder)."""

    # Function nodes execute in a new Python context.  Import dependencies
    # inside the function so they are available when the node runs.
    from pathlib import Path

    atlas_base = Path(atlas_path).with_suffix("").stem
    out_fname = f"{atlas_base}_in_subject.nii.gz"
    out_path = str(Path(out_dir) / out_fname)

    # TODO: call registration tools here (e.g. FLIRT via Singularity)
    return out_path

* out_dir : ./results
* t1_path : /data/rawdata-archive/IndivConn/sub-IndivConn000002/ses-01/anat/sub-IndivConn000002_ses-01_run-01_T1w.nii.gz


Execution Outputs
-----------------


* label_map : results/tpl-MNI152NLin6Asym_atlas-Schaefer2018v0143_res-01_desc-400ParcelsAllNetworks_dseg_in_subject.nii.gz


Runtime info
------------


* duration : 0.000466
* hostname : a08856ec1e9f
* prev_wd : /data/data_fbaum/Toolbox/notebooks
* working_dir : /data/data_fbaum/Toolbox/notebooks/results/MainWorkflow/parc_workflow/apply_parcellation


Environment
~~~~~~~~~~~


* APPTAINER_BINDPATH : /data,/mnt,/neurodesktop-storage,/tmp,/cvmfs
* CHOWN_HOME : yes
* CHOWN_HOME_OPTS : -R
* CLICOLOR : 1
* CLICOLOR_FORCE : 1
* CONDA_DEFAULT_ENV : base
* CONDA_DIR : /opt/conda
* CONDA_EXE : /opt/conda/bin/conda
* CONDA_PREFIX : /opt/conda
* CONDA_PROMPT_MODIFIER : (base) 
* CONDA_PYTHON_EXE : /opt/conda/bin/python
* CONDA_SHLVL : 1
* CVMFS_DISABLE : false
* DEBIAN_FRONTEND : noninteractive
* DONT_PROMPT_WSL_INSTALL : 1
* FORCE_COLOR : 1
* GIT_PAGER : cat
* GIT_PYTHON_REFRESH : quiet
* GRANT_SUDO : yes
* HOME : /home/jovyan
* HOSTNAME : a08856ec1e9f
* JPY_PARENT_PID : 179
* JPY_SESSION_NAME : /home/jovyan/data_fbaum/Toolbox/notebooks/Untitled.ipynb
* JUPYTER_PORT : 8888
* KMP_DUPLICATE_LIB_OK : True
* LANG : 
* LANGUAGE : 
* LC_ALL : 
* LC_CTYPE : C.UTF-8
* LD_LIBRARY_PATH : 
* LMOD_CMD : /usr/share/lmod/lmod/libexec/lmod
* LOGNAME : jovyan
* MODULEPATH : /neurodesktop-storage/containers/modules/:/cvmfs/neurodesk.ardc.edu.au/containers/modules/
* MPLBACKEND : module://matplotlib_inline.backend_inline
* NB_GID : 2042
* NB_UID : 2040
* NB_UMASK : 002
* NB_USER : jovyan
* NEURODESKTOP_VERSION : latest
* PAGER : cat
* PATH : /opt/conda/bin:/opt/conda/condabin:/opt/conda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
* PWD : /home/jovyan
* PYDEVD_USE_FRAME_EVAL : NO
* PYTHONPATH : 
* RESTARTABLE : yes
* SHELL : /bin/bash
* SHLVL : 0
* SUDO_COMMAND : /usr/local/bin/start-notebook.py
* SUDO_GID : 0
* SUDO_UID : 0
* SUDO_USER : root
* TERM : xterm-color
* TIKTOKEN_CACHE_DIR : /opt/conda/lib/python3.12/site-packages/litellm/litellm_core_utils/tokenizers
* USER : jovyan
* XML_CATALOG_FILES : file:///opt/conda/etc/xml/catalog file:///etc/xml/catalog
* _START_SH_EXECUTED : 1
* neurodesk_singularity_opts :  --overlay /tmp/apptainer_overlay 

