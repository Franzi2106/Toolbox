# core/utils/environment.py
import subprocess
import shutil
import os

# Path to your FSL Singularity image is now provided via config

def fsl_conflict_check(singularity_image: str) -> bool:
    """
    Return True if we can call FSL’s 'flirt' inside the Singularity container.
    """
    try:
        if shutil.which("singularity") is None:
            print("ERROR: Singularity not found on PATH.")
            return False

        if not os.path.exists(singularity_image):
            print(f"ERROR: FSL container not found at {singularity_image}")
            return False

        cmd = [
            "singularity", "exec", singularity_image,
            "flirt", "-version"
        ]
        res = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
            text=True,
        )
        print("FSL detected:", res.stdout.splitlines()[0])
        return True
    except subprocess.CalledProcessError as e:
        print("ERROR: Could not run 'flirt' in container:", e)
        return False
