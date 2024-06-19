import os, sys, subprocess

# Set the name of the driver (does not have to be Python)
python_file = "C:/RoboDK/Library/Scripts/Comau_LIS_Import.py"
program_run = "\"" + sys.executable + "\" \"" + python_file + "\""

print("Running command: " + program_run)

# Modify driver environment
environment = os.environ.copy()
#my_env["PATH"] = "/addtopath/folder:" + my_env["PATH"]

p = subprocess.Popen(program_run, shell=True, env=environment)
p.wait()
print("Done")