# main entry point, where workflow runs (uses config)
# sets workflow steps 
# calls each step when the module is run

#!/usr/bin/env python3
import sys, os
from core.utils.environment import fsl_conflict_check
from core.config.config_manager import ConfigManager

from core.pipeline.io_workflow           import make_paths
from core.pipeline.parc_workflow import apply_parcellation
from core.pipeline.subjectdict_workflow  import build_subject_dict

def main():
    # 1) Load config
    cfg = ConfigManager("toolbox.ini")

    # 1b) FSL-Container-Pfad als ENV-Variable exportieren
    sing_img = cfg.get("FSL", "singularity_image", fallback=None)
    if sing_img:
        os.environ["FSL_SINGULARITY_IMAGE"] = sing_img

    if cfg.getboolean("APP", "show_config_on_startup"):
        print(cfg)
        sys.exit(0)

    # 2) Env check
    fsl_img = cfg.get("FSL", "singularity_image", fallback="")
    if not fsl_conflict_check(fsl_img):
        print("FSL check failed. Aborting.")
        sys.exit(1)

    # 3) Discover files
    subj = cfg.get("APP", "subject_id", fallback="testsubj")
    print(f"Discovering files for {subj}")
    bids_root = cfg.get("PATHS", "bids_root", fallback="")
    reference_T1 = cfg.get("PATHS", "reference_T1", fallback="")
    atlas_cfg = cfg.get("PATHS", "atlas_path", fallback="")
    t1_path, atlas_path = make_paths(subj, bids_root, reference_T1, atlas_cfg)
    print("    T1 →", t1_path)
    print("    Atlas →", atlas_path)

    # 4) Parcellate
    out_dir = cfg.get("PATHS", "output_dir", fallback=".")
    print("Parcellating atlas into subject space…")
    label_map = apply_parcellation(t1_path, atlas_path, out_dir=out_dir)
    print("    Label map →", label_map)

    # 5) Build subject dict
    print("Building subject dictionary…")
    subj_dict = build_subject_dict(subj, t1_path, label_map)
    print("    Subject dict →", subj_dict)

    print("All steps completed.")
    sys.exit(0)

if __name__ == "__main__":
    main()