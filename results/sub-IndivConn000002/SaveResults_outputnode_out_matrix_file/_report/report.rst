Node: SaveResults_outputnode_out_matrix_file (io)
=================================================


 Hierarchy : sub-IndivConn000002.SaveResults_outputnode_out_matrix_file
 Exec ID : SaveResults_outputnode_out_matrix_file


Original Inputs
---------------


* _outputs : {'out_matrix_file': <undefined>}
* base_directory : ./results/output
* bucket : <undefined>
* container : <undefined>
* creds_path : <undefined>
* encrypt_bucket_keys : <undefined>
* local_copy : <undefined>
* out_matrix_file : <undefined>
* parameterization : True
* regexp_substitutions : <undefined>
* remove_dest_dir : False
* strip_dir : <undefined>
* substitutions : <undefined>


Execution Inputs
----------------


* _outputs : {'out_matrix_file': <undefined>}
* base_directory : ./results/output
* bucket : <undefined>
* container : <undefined>
* creds_path : <undefined>
* encrypt_bucket_keys : <undefined>
* local_copy : <undefined>
* out_matrix_file : <undefined>
* parameterization : True
* regexp_substitutions : <undefined>
* remove_dest_dir : False
* strip_dir : <undefined>
* substitutions : <undefined>


Execution Outputs
-----------------


* out_file : []


Runtime info
------------


* duration : 0.004839
* hostname : e5316fa00b75
* prev_wd : /data/data_fbaum/Toolbox
* working_dir : /data/data_fbaum/Toolbox/results/sub-IndivConn000002/SaveResults_outputnode_out_matrix_file


Environment
~~~~~~~~~~~


* APPTAINERENV_SUBJECTS_DIR : /home/jovyan/freesurfer-subjects-dir
* APPTAINER_BINDPATH : /data,/mnt,/neurodesktop-storage,/tmp,/cvmfs
* BASH_FUNC_ml%% : () {  eval "$($LMOD_DIR/ml_cmd "$@")"
}
* BASH_FUNC_module%% : () {  local __lmod_my_status;
 local __lmod_sh_dbg;
 if [ -z "${LMOD_SH_DBG_ON+x}" ]; then
 case "$-" in 
 *v*x*)
 __lmod_sh_dbg='vx'
 ;;
 *v*)
 __lmod_sh_dbg='v'
 ;;
 *x*)
 __lmod_sh_dbg='x'
 ;;
 esac;
 fi;
 if [ -n "${__lmod_sh_dbg:-}" ]; then
 set +$__lmod_sh_dbg;
 echo "Shell debugging temporarily silenced: export LMOD_SH_DBG_ON=1 for Lmod's output" 1>&2;
 fi;
 eval "$($LMOD_CMD bash "$@")" && eval $(${LMOD_SETTARG_CMD:-:} -s sh);
 __lmod_my_status=$?;
 if [ -n "${__lmod_sh_dbg:-}" ]; then
 echo "Shell debugging restarted" 1>&2;
 set -$__lmod_sh_dbg;
 fi;
 return $__lmod_my_status
}
* COLUMNS : 205
* CONDA_DEFAULT_ENV : base
* CONDA_DIR : /opt/conda
* CONDA_EXE : /opt/conda/bin/conda
* CONDA_PREFIX : /opt/conda
* CONDA_PROMPT_MODIFIER : (base) 
* CONDA_PYTHON_EXE : /opt/conda/bin/python
* CONDA_SHLVL : 1
* CVMFS_DISABLE : false
* CVMFS_MODULES : /cvmfs/neurodesk.ardc.edu.au/neurodesk-modules/
* DEBIAN_FRONTEND : noninteractive
* DONT_PROMPT_WSL_INSTALL : 1
* FSL_SINGULARITY_IMAGE : /cvmfs/neurodesk.ardc.edu.au/containers/fsl_6.0.4_20210105/fsl_6.0.4_20210105.simg
* GIT_PYTHON_REFRESH : quiet
* GRANT_SUDO : yes
* HOME : /home/jovyan
* HOSTNAME : e5316fa00b75
* JUPYTER_PORT : 8888
* JUPYTER_SERVER_ROOT : /home/jovyan
* JUPYTER_SERVER_URL : http://localhost:8888/
* KMP_DUPLICATE_LIB_OK : True
* LANG : 
* LANGUAGE : 
* LC_ALL : 
* LC_CTYPE : C.UTF-8
* LD_LIBRARY_PATH : 
* LESSCLOSE : /usr/bin/lesspipe %s %s
* LESSOPEN : | /usr/bin/lesspipe %s
* LINES : 60
* LMOD_CMD : /usr/share/lmod/lmod/libexec/lmod
* LMOD_DIR : /usr/share/lmod/lmod/libexec
* LMOD_PKG : /usr/share/lmod/lmod
* LMOD_ROOT : /usr/share/lmod
* LMOD_SETTARG_FULL_SUPPORT : no
* LMOD_VERSION : 8.6.19
* LOGNAME : jovyan
* LS_COLORS : rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=00:su=37;41:sg=30;43:ca=00:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.zst=01;31:*.tzst=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.wim=01;31:*.swm=01;31:*.dwm=01;31:*.esd=01;31:*.avif=01;35:*.jpg=01;35:*.jpeg=01;35:*.mjpg=01;35:*.mjpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.webp=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.m4a=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.oga=00;36:*.opus=00;36:*.spx=00;36:*.xspf=00;36:*~=00;90:*#=00;90:*.bak=00;90:*.crdownload=00;90:*.dpkg-dist=00;90:*.dpkg-new=00;90:*.dpkg-old=00;90:*.dpkg-tmp=00;90:*.old=00;90:*.orig=00;90:*.part=00;90:*.rej=00;90:*.rpmnew=00;90:*.rpmorig=00;90:*.rpmsave=00;90:*.swp=00;90:*.tmp=00;90:*.ucf-dist=00;90:*.ucf-new=00;90:*.ucf-old=00;90:
* MODULEPATH : /neurodesktop-storage/containers/modules/:/cvmfs/neurodesk.ardc.edu.au/neurodesk-modules/bids_apps:/cvmfs/neurodesk.ardc.edu.au/neurodesk-modules/body:/cvmfs/neurodesk.ardc.edu.au/neurodesk-modules/cryo_EM:/cvmfs/neurodesk.ardc.edu.au/neurodesk-modules/data_organisation:/cvmfs/neurodesk.ardc.edu.au/neurodesk-modules/diffusion_imaging:/cvmfs/neurodesk.ardc.edu.au/neurodesk-modules/electrophysiology:/cvmfs/neurodesk.ardc.edu.au/neurodesk-modules/functional_imaging:/cvmfs/neurodesk.ardc.edu.au/neurodesk-modules/hippocampus:/cvmfs/neurodesk.ardc.edu.au/neurodesk-modules/image_reconstruction:/cvmfs/neurodesk.ardc.edu.au/neurodesk-modules/image_registration:/cvmfs/neurodesk.ardc.edu.au/neurodesk-modules/image_segmentation:/cvmfs/neurodesk.ardc.edu.au/neurodesk-modules/machine_learning:/cvmfs/neurodesk.ardc.edu.au/neurodesk-modules/molecular_biology:/cvmfs/neurodesk.ardc.edu.au/neurodesk-modules/other:/cvmfs/neurodesk.ardc.edu.au/neurodesk-modules/phase_processing:/cvmfs/neurodesk.ardc.edu.au/neurodesk-modules/programming:/cvmfs/neurodesk.ardc.edu.au/neurodesk-modules/quality_control:/cvmfs/neurodesk.ardc.edu.au/neurodesk-modules/quantitative_imaging:/cvmfs/neurodesk.ardc.edu.au/neurodesk-modules/rodent_imaging:/cvmfs/neurodesk.ardc.edu.au/neurodesk-modules/shape_analysis:/cvmfs/neurodesk.ardc.edu.au/neurodesk-modules/spectroscopy:/cvmfs/neurodesk.ardc.edu.au/neurodesk-modules/spine:/cvmfs/neurodesk.ardc.edu.au/neurodesk-modules/statistics:/cvmfs/neurodesk.ardc.edu.au/neurodesk-modules/structural_imaging:/cvmfs/neurodesk.ardc.edu.au/neurodesk-modules/visualization:/cvmfs/neurodesk.ardc.edu.au/neurodesk-modules/workflows
* MODULESHOME : /usr/share/lmod/lmod
* MPLCONFIGDIR : /home/jovyan/.config/matplotlib-mpldir
* NB_GID : 2042
* NB_UID : 2040
* NB_UMASK : 002
* NB_USER : jovyan
* NEURODESKTOP_VERSION : latest
* OFFLINE_MODULES : /neurodesktop-storage/containers/modules/
* OLDPWD : /home/jovyan/data_fbaum
* PATH : /opt/conda/bin:/opt/conda/condabin:/opt/conda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/home/jovyan/.local/bin:/opt/conda/bin:/opt/conda/condabin
* PS1 : (base) \u@neurodesktop-$NEURODESKTOP_VERSION:\w$ 
* PWD : /home/jovyan/data_fbaum/Toolbox
* PYTHONPATH : 
* PYXTERM_DIMENSIONS : 80x25
* RESTARTABLE : yes
* SHELL : /bin/bash
* SHLVL : 1
* SUDO_COMMAND : /usr/local/bin/start-notebook.py
* SUDO_GID : 0
* SUDO_UID : 0
* SUDO_USER : root
* TERM : xterm-256color
* TIKTOKEN_CACHE_DIR : /opt/conda/lib/python3.12/site-packages/litellm/litellm_core_utils/tokenizers
* USER : jovyan
* XML_CATALOG_FILES : file:///opt/conda/etc/xml/catalog file:///etc/xml/catalog
* _ : /opt/conda/bin/python
* _START_SH_EXECUTED : 1
* neurodesk_singularity_opts :  --overlay /tmp/apptainer_overlay 

