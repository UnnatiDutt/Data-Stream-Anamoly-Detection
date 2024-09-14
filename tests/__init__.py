# This file marks the tests directory as a Python package.

# Common imports for all test modules
import unittest
import numpy as np

# You can also import the modules you want to test
from src.data_stream_simulation import data_stream_simulation
from src.anomaly_detector import AnomalyDetector
from src.visualization import visualize

# Any common setup code for tests can go here
print("Initializing test package")