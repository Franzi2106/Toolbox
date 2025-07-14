from nipype import Node, IdentityInterface, Merge, SelectFiles
from nipype.algorithms.modelgen import SpecifyModel
from nipype.algorithms.rapidart import ArtifactDetect
from nipype.interfaces.fsl import (ImageMaths, ExtractROI, MCFLIRT, BET, ImageStats, SUSAN, FLIRT, Level1Design,
                                   FEATModel, FILMGLS, SmoothEstimate, Cluster, ApplyXFM)
from configparser import SectionProxy
from swane.nipype_pipeline.engine.CustomWorkflow import CustomWorkflow
from swane.nipype_pipeline.nodes.FslNVols import FslNVols
from swane.nipype_pipeline.nodes.FMRIGenSpec import FMRIGenSpec
from swane.nipype_pipeline.nodes.CustomSliceTimer import CustomSliceTimer
from swane.nipype_pipeline.nodes.GetNiftiTR import GetNiftiTR
from swane.nipype_pipeline.nodes.ForceOrient import ForceOrient
from swane.nipype_pipeline.nodes.DeleteVolumes import DeleteVolumes
from swane.config.config_enums import BLOCK_DESIGN


def task_fMRI_workflow(name: str, fmri_file: str, config: SectionProxy, base_dir: str = "/") -> CustomWorkflow:
    """
    fMRI first level anlysis for a single task with constant task-rest paradigm.

    Parameters
    ----------
    name : str
        The workflow name.
    fmri_file : path
        Path to the 4D fMRI NIfTI file.
    config: SectionProxy
        workflow settings.
    base_dir : path, optional
        The base directory path relative to parent workflow. The default is "/".

    Input Node Fields
    ----------
    ref_BET : path
        Betted T13D.
    fmri_file : path
        4D functional image (already converted to NIfTI).

    Output Node Fields
    ----------
    threshold_file_1 : path
        Cluster of activation (task A vs rest or Task A vs Task B) in T13D reference space.
    threshold_file_2 : path
        Cluster of activation (task b vs Task) in T13D reference space.

    Returns
    -------
    workflow : CustomWorkflow
        The fMRI workflow.

    """

    workflow = CustomWorkflow(name=name, base_dir=base_dir)
    
    # Input Node
    inputnode = Node(
        IdentityInterface(
            fields=['ref_BET', 'fmri_file']),
        name='inputnode')

    task_a_name = config["task_a_name"].replace(" ", "_")
    task_b_name = config["task_b_name"].replace(" ", "_")
    task_duration = config.getint_safe('task_duration')
    rest_duration = config.getint_safe('rest_duration')
    TR = config.getfloat_safe('tr')
    slice_timing = config.getenum_safe('slice_timing')
    n_vols = config.getint_safe('n_vols')
    del_start_vols = config.getint_safe('del_start_vols')
    del_end_vols = config.getint_safe('del_end_vols')
    block_design = config.getenum_safe('block_design')
    
    # Output Node
    outputnode = Node(
        IdentityInterface(fields=['threshold_file_cont1_thresh1', 'threshold_file_cont1_thresh2', 'threshold_file_cont1_thresh3',
                                  'threshold_file_cont2_thresh1', 'threshold_file_cont2_thresh2', 'threshold_file_cont2_thresh3']),
        name='outputnode')

    # NODE 1: Get EPI volume numbers
    nvols = Node(FslNVols(), name="%s_nvols" % name)
    nvols.long_name = "EPI volumes count"
    nvols.inputs.force_value = n_vols
    workflow.connect(inputnode, 'fmri_file', nvols, 'in_file')
    # NODE 2: Get Repetition Time
    getTR = Node(GetNiftiTR(), name="%s_getTR" % name)
    getTR.long_name = "get TR"
    getTR.inputs.force_value = TR

    workflow.connect(inputnode, 'fmri_file', getTR, 'in_file')
    # NODE 3: Delete specified volumes at start and end of sequence
    del_vols = Node(DeleteVolumes(), name="%s_del_vols" % name)
    del_vols.long_name = "Extreme volumes deletion"
    del_vols.inputs.del_start_vols = del_start_vols
    del_vols.inputs.del_end_vols = del_end_vols
    workflow.connect(inputnode, 'fmri_file', del_vols, "in_file")
    workflow.connect(nvols, 'nvols', del_vols, "nvols")

    # NODE 4: Orienting in radiological convention
    reorient = Node(ForceOrient(), name='%s_reorient' % name)
    workflow.connect(del_vols, "out_file", reorient, "in_file")

    # NODE 5: Convert functional images to float representation.
    img2float = Node(ImageMaths(), name="%s_img2float" % name)
    img2float.long_name = "Intensity in float values"
    img2float.inputs.out_data_type = 'float'
    img2float.inputs.op_string = ''
    img2float.inputs.suffix = '_dtype'
    workflow.connect(reorient, 'out_file', img2float, 'in_file')

    # NODE 6: Extract the middle volume of the first run as the reference
    extract_ref = Node(ExtractROI(), name="%s_extract_ref" % name)
    extract_ref.long_name = "Reference volume selection"
    extract_ref.inputs.t_size = 1

    # Function to extract the middle volume number
    def get_middle_volume(func):
        from nibabel import load
        funcfile = func
        if isinstance(func, list):
            funcfile = func[0]
        _, _, _, timepoints = load(funcfile).shape
        middle = int(timepoints / 2)
        return middle
