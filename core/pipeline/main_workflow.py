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
        # Pull all nodes from the I/O workflow into this one
        self.add_nodes(wf_io.nodes)

        # 2) Parcellation step
        from core.pipeline.parc_workflow import parc_workflow
        wf_parc = parc_workflow(config)
        self.add_nodes(wf_parc.nodes)

        # 3) Subject‐dict assembly
        from core.pipeline.subjectdict_workflow import subjectdict_workflow
        wf_sd = subjectdict_workflow(config)
        self.add_nodes(wf_sd.nodes)

        # (Optional) if you need to connect outputs of one to inputs of another:
        # self.connect([
        #     (wf_io.get_node('output'), 't1_file',
        #      wf_parc.get_node('input'), 't1_file'),
        #     # ... etc.
        # ])