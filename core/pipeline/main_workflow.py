# core/pipeline/main_workflow.py
from nipype import Workflow

class MainWorkflow(Workflow):
    """
    Top‐level workflow: stitches together all sub‐workflows.
    """
    def __init__(self, config):
        super().__init__(name="MainWorkflow")
        self.config = config

        # 1) I/O step
        from core.pipeline.io import io_workflow
        wf_io = io_workflow(config)
        # Pull all nodes from the I/O workflow into this one
        self.add_nodes(wf_io._get_all_nodes())

        # 2) Parcellation step
        from core.pipeline.parcellation import parc_workflow
        wf_parc = parc_workflow(config)
        self.add_nodes(wf_parc._get_all_nodes())

        # 3) Subject‐dict assembly
        from core.pipeline.subjectdict import subjectdict_workflow
        wf_sd = subjectdict_workflow(config)
        self.add_nodes(wf_sd._get_all_nodes())

        # Connect outputs between sub-workflows
        self.connect([
            (
                wf_io.get_node('make_paths'),
                wf_parc.get_node('apply_parcellation'),
                [('t1_path', 't1_path'), ('atlas_path', 'atlas_path')],
            ),
            (
                wf_io.get_node('make_paths'),
                wf_sd.get_node('build_subject_dict'),
                [('t1_path', 't1_path')],
            ),
            (
                wf_parc.get_node('apply_parcellation'),
                wf_sd.get_node('build_subject_dict'),
                [('label_map', 'label_map')],
            ),
        ])

