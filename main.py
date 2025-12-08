# at the start of the session activate .venv by "source .venv/bin/activate"
# pip install -r requirements.txt   to reinstall all dependancies
# Core numerical computing
import numpy as np
from numpy import sin, cos, tan, arctan2 as atan2, arccos, arcsin, sqrt, pi

# Symbolic mathematics (for deriving and verifying equations)
import sympy as sp
from sympy import symbols, Matrix, simplify, trigsimp

# GUI Framework
import PyQt6
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

# 3D Visualization
import matplotlib.pyplot as plot
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation


from scipy.spatial.transform import Rotation as R

# For better 3D visualization
import plotly.graph_objects as go
import plotly.express as px

# For robot visualization (highly recommended!)
import roboticstoolbox as rtb
from spatialmath import SE3

# Data handling
import pandas as pd

# System utilities
import os
import json # maybe deleted later if not used
from datetime import datetime


# ```

# ## Recommended Project Structure
# ```
# robot_kinematics_project/
# │
# ├── Makefile
# ├── requirements.txt
# ├── README.md
# ├── config.json
# │
# ├── src/
# │   ├── __init__.py
# │   ├── main.py                    # Entry point
# │   ├── gui/
# │   │   ├── __init__.py
# │   │   ├── main_window.py         # Main GUI class
# │   │   ├── robot_selector.py      # Robot selection interface
# │   │   ├── fk_panel.py            # Forward kinematics panel
# │   │   ├── ik_panel.py            # Inverse kinematics panel
# │   │   └── visualization.py       # 3D/2D plotting
# │   │
# │   ├── kinematics/
# │   │   ├── __init__.py
# │   │   ├── base_robot.py          # Abstract base class
# │   │   ├── abb_irb1400.py         # ABB IRB 1400 (5 DOF)
# │   │   ├── ur5.py                 # UR5 (6 DOF)
# │   │   ├── abb_irb1600.py         # ABB IRB 1600 (6 DOF)
# │   │   ├── dh_parameters.py       # DH parameter utilities
# │   │   └── transformations.py     # Homogeneous transformations
# │   │
# │   ├── utils/
# │   │   ├── __init__.py
# │   │   ├── math_utils.py          # Mathematical helper functions
# │   │   ├── validation.py          # FK/IK validation
# │   │   ├── singularity_check.py   # Singularity detection
# │   │   └── export.py              # Export results to file
# │   │
# │   └── data/
# │       ├── robot_specs.json       # Robot specifications
# │       └── dh_tables.json         # DH parameters
# │
# ├── tests/
# │   ├── __init__.py
# │   ├── test_fk.py
# │   ├── test_ik.py
# │   └── test_validation.py
# │
# ├── docs/
# │   ├── equations.md
# │   └── user_guide.md
# │
# └── outputs/
#     ├── plots/
#     ├── results/
#     └── logs/

print("hi")