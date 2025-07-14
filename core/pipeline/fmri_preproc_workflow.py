## aus Nipype Tutorial 


from nipype import Node, Workflow
from nipype.interfaces.matlab import MatlabCommand
MatlabCommand.set_default_paths('/opt/spm12-r7219/spm12_mcr/spm12')
from nipype.algorithms.misc import Gunzip



# Create the workflow here
# Hint: use 'base_dir' to specify where to store the working directory

preproc = Workflow(name='work_preproc', base_dir='/output/')

# Specify example input file
func_file = '

# Initiate Gunzip node
gunzip_func = Node(Gunzip(in_file=func_file), name='gunzip_func')