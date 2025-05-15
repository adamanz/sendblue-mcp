#!/usr/bin/env python3
import os
import sys
import subprocess

# Change to the project directory
project_dir = "/Users/adamanzuoni/sendblue-mcp"
os.chdir(project_dir)

# Run the server module directly
sys.path.insert(0, project_dir)
subprocess.run([sys.executable, "-m", "src.main"])