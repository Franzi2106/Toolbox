# core/utils/environment.py
import subprocess
import os

# Path to your FSL Singularity image
FSL_SIMG = "/cvmfs/neurodesk.ardc.edu.au/containers/fsl_6.0.4_20210105/fsl_6.0.4_20210105.simg"

def fsl_conflict_check() -> bool:
    """
    Return True if we can call FSL’s 'flirt' inside the Singularity container.
    """
    try:
        cmd = [
            "singularity", "exec", FSL_SIMG,
            "flirt", "-version"
        ]
        res = subprocess.run(cmd,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE,
                              check=True,
                              text=True)
        # flirt prints version on stdout
        print("FSL detected:", res.stdout.splitlines()[0])
        return True
    except FileNotFoundError:
        print("ERROR: Singularity not found on PATH.")
        return False
    except subprocess.CalledProcessError as e:
        print("ERROR: Could not run 'flirt' in container:", e)
        return False