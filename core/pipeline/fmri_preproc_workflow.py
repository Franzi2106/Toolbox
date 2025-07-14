## aus Nipype Tutorial 


from nipype import Node, Workflow
from nipype.interfaces.matlab import MatlabCommand
MatlabCommand.set_default_paths('/opt/spm12-r7219/spm12_mcr/spm12')
from nipype.algorithms.misc import Gunzip
from nipype.interfaces.fsl import MCFLIRT
from nipype.algorithms.rapidart import ArtifactDetect
from nipype.interfaces.spm import NewSegment
from nipype.interfaces.fsl import FLIRT
from nipype.interfaces.fsl import Threshold
from nipype.workflows.fmri.fsl.preprocess import create_susan_smooth
from nipype.interfaces.fsl import FLIRT
from nipype.interfaces.fsl import Threshold
from nipype.interfaces.fsl import ApplyMask
from nipype import MapNode
from nipype.algorithms.confounds import TSNR


# Create the workflow here
# Hint: use 'base_dir' to specify where to store the working directory

preproc = Workflow(name='work_preproc', base_dir='/output/')

# Specify example input file
func_file = '/data/rawdata-archive/IndivConn/sub-IndivConn000002/ses-01/func/sub-IndivConn000002_ses-01_task-Phrases_run-01_bold.nii.gz'

# Initiate Gunzip node
gunzip_func = Node(Gunzip(in_file=func_file), name='gunzip_func')

# Motion Correction 
# Initiate MCFLIRT node here
mcflirt = Node(MCFLIRT(mean_vol=True,
                       save_plots=True),
               name="mcflirt")

# Connect MCFLIRT node to the other nodes here
preproc.connect([(gunzip_func, mcflirt, [('out_file', 'in_file')])])

# Artifact Detection
art = Node(ArtifactDetect(norm_threshold=2,
                          zintensity_threshold=2,
                          mask_type='spm_global',
                          parameter_source='FSL',
                          use_differences=[True, False],
                          plot_type='svg'),
           name="art")

preproc.connect([(mcflirt, art, [('out_file', 'realigned_files'),
                                 ('par_file', 'realignment_parameters')])
                 ])

# Segmentation of anatomical image 
# Use the following tissue specification to get a GM and WM probability map
tpm_img ='/opt/spm12-r7219/spm12_mcr/spm12/tpm/TPM.nii'
tissue1 = ((tpm_img, 1), 1, (True,False), (False, False))
tissue2 = ((tpm_img, 2), 1, (True,False), (False, False))
tissue3 = ((tpm_img, 3), 2, (True,False), (False, False))
tissue4 = ((tpm_img, 4), 3, (False,False), (False, False))
tissue5 = ((tpm_img, 5), 4, (False,False), (False, False))
tissue6 = ((tpm_img, 6), 2, (False,False), (False, False))
tissues = [tissue1, tissue2, tissue3, tissue4, tissue5, tissue6]


# Initiate NewSegment node here
segment = Node(NewSegment(tissues=tissues), name='segment')
# Specify example input file
anat_file = '/data/rawdata-archive/IndivConn/sub-IndivConn000002/ses-01/anat/sub-IndivConn000002_ses-01_run-01_T1w.nii.gz'

# Initiate Gunzip node
gunzip_anat = Node(Gunzip(in_file=anat_file), name='gunzip_anat')
# Connect NewSegment node to the other nodes here
preproc.connect([(gunzip_anat, segment, [('out_file', 'channel_files')])])

# Initiate FLIRT node here

coreg = Node(FLIRT(dof=6,
                   cost='bbr',
                   schedule='/usr/share/fsl/5.0/etc/flirtsch/bbr.sch',
                   output_type='NIFTI'),
             name="coreg")

# Connect FLIRT node to the other nodes here
preproc.connect([(gunzip_anat, coreg, [('out_file', 'reference')]),
                 (mcflirt, coreg, [('mean_img', 'in_file')])
                 ])

# Threshold - Threshold WM probability image
threshold_WM = Node(Threshold(thresh=0.5,
                              args='-bin',
                              output_type='NIFTI'),
                name="threshold_WM")

# Select WM segmentation file from segmentation output
def get_wm(files):
    return files[1][0]

# Connecting the segmentation node with the threshold node
preproc.connect([(segment, threshold_WM, [(('native_class_images', get_wm),
                                           'in_file')])])

# Connect Threshold node to coregistration node above here
preproc.connect([(threshold_WM, coreg, [('out_file', 'wm_seg')])])

# Specify the isometric voxel resolution you want after coregistration
desired_voxel_iso = 4

# Apply coregistration warp to functional images
applywarp = Node(FLIRT(interp='spline',
                       apply_isoxfm=desired_voxel_iso,
                       output_type='NIFTI'),
                 name="applywarp")

# Connecting the ApplyWarp node to all the other nodes
preproc.connect([(mcflirt, applywarp, [('out_file', 'in_file')]),
                 (coreg, applywarp, [('out_matrix_file', 'in_matrix_file')]),
                 (gunzip_anat, applywarp, [('out_file', 'reference')])
                 ])

# Initiate SUSAN workflow here
susan = create_susan_smooth(name='susan')
susan.inputs.inputnode.fwhm = 4
# Connect Threshold node to coregistration node above here
preproc.connect([(applywarp, susan, [('out_file', 'inputnode.in_files')])])

# Initiate resample node
resample = Node(FLIRT(apply_isoxfm=desired_voxel_iso,
                      output_type='NIFTI'),
                name="resample")

# Threshold - Threshold GM probability image
mask_GM = Node(Threshold(thresh=0.5,
                         args='-bin -dilF',
                         output_type='NIFTI'),
                name="mask_GM")

# Select GM segmentation file from segmentation output
def get_gm(files):
    return files[0][0]
preproc.connect([(segment, resample, [(('native_class_images', get_gm), 'in_file'),
                                      (('native_class_images', get_gm), 'reference')
                                      ]),
                 (resample, mask_GM, [('out_file', 'in_file')])
                 ])

# Connect gray matter Mask node to the susan workflow here
preproc.connect([(mask_GM, susan, [('out_file', 'inputnode.mask_file')])])

# Initiate ApplyMask node here
mask_func = MapNode(ApplyMask(output_type='NIFTI'),
                    name="mask_func",
                    iterfield=["in_file"])
# Connect smoothed susan output file to ApplyMask node here
preproc.connect([(susan, mask_func, [('outputnode.smoothed_files', 'in_file')]),
                 (mask_GM, mask_func, [('out_file', 'mask_file')])
                 ])

# Initiate TSNR node here
detrend = Node(TSNR(regress_poly=2), name="detrend")
# Connect the detrend node to the other nodes here
preproc.connect([(mask_func, detrend, [('out_file', 'in_file')])])

# Create preproc output graph
preproc.write_graph(graph2use='colored', format='png', simple_form=True)

# Visualize the graph
from IPython.display import Image
Image(filename='/output/work_preproc/graph.png', width=750)

preproc.run('MultiProc', plugin_args={'n_procs': 8})