import sys
from pathlib import Path

# Let tests import the project modules from the parent folder
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
