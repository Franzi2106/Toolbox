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

# Test: fmri preprocessing 
def launch_fMRI_analysis(self):
        # Check for Task FMRI sequences
        for y in range(FMRI_NUM):

            if not self.subject_input_state_list[DIL["FMRI_%d" % y]].loaded:
                continue

            fmri_file = self.subject_input_state_list.get_dicom_dir(DIL["FMRI_%d" % y])
            self.fMRI = task_fMRI_workflow(␊
                name=DIL["FMRI_%d" % y].value.workflow_name,␊
                fmri_file=fmri_file,
                config=self.subject_config[DIL["FMRI_%d" % y]],␊
                base_dir=self.base_dir,␊
            )␊
            self.fMRI.long_name = "Task fMRI analysis - %d" % y
            self.connect(
                self.t1, "outputnode.ref_brain", self.fMRI, "inputnode.ref_BET"
            )
            for thresh_i in range(1, 4):
                self.fMRI.sink_result(
                    save_path=self.base_dir,
                    result_node="outputnode",
                    result_name="threshold_file_cont1_thresh%d" % thresh_i,
                    sub_folder=self.Result_DIR + ".fMRI",
                )
                if (
                    self.subject_config.getenum_safe(DIL["FMRI_%d" % y], "block_design")
                    == BLOCK_DESIGN.RARB
                ):
                    self.fMRI.sink_result(
                        save_path=self.base_dir,
                        result_node="outputnode",
                        result_name="threshold_file_cont2_thresh%d" % thresh_i,
                        sub_folder=self.Result_DIR + ".fMRI",
                    )