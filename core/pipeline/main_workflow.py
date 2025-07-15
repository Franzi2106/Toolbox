# assembles steps from __main__.py into a Nipype Workflow

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
        from core.pipeline.io_workflow import io_workflow
        wf_io = io_workflow(config)
        self.add_nodes([wf_io])

        # 2) Parcellation step
        from core.pipeline.parc_workflow import parc_workflow
        wf_parc = parc_workflow(config)
        self.add_nodes([wf_parc])

        # 3) Subject‐dict assembly
        from core.pipeline.subjectdict_workflow import subjectdict_workflow
        wf_sd = subjectdict_workflow(config)
        self.add_nodes([wf_sd])

        # Connect sub-workflows
        self.connect([
            (wf_io.get_node('make_paths'), 't1_path',
             wf_parc.get_node('apply_parcellation'), 't1_path'),
            (wf_io.get_node('make_paths'), 'atlas_path',
             wf_parc.get_node('apply_parcellation'), 'atlas_path'),
            (wf_io.get_node('make_paths'), 't1_path',
             wf_sd.get_node('build_subject_dict'), 't1_path'),
            (wf_parc.get_node('apply_parcellation'), 'label_map',
             wf_sd.get_node('build_subject_dict'), 'label_map'),
        ])
