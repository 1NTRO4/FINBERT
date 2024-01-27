import subprocess
import sys
import os

# Replace 'your_environment_name' with the actual name of your Conda environment
conda_env = 'python'

try:
    subprocess.check_call(f'conda activate {conda_env}', shell=True)
except subprocess.CalledProcessError:
    sys.exit('Failed to activate Conda environment.')

# Now continue with the rest of your script