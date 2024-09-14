import unittest
import numpy as np
from src.data_stream_simulation import data_stream_simulation

class TestDataStreamSimulation(unittest.TestCase):

    def test_data_stream_length(self):
        file_path = 'src/ec2_cpu_utilization.csv'
        size = 1000
        data = data_stream_simulation(file_path, size)
        self.assertEqual(len(data), size)

    def test_data_stream_type(self):
        file_path = 'src/ec2_cpu_utilization.csv'
        size = 1000
        data = data_stream_simulation(file_path, size)
        self.assertIsInstance(data, np.ndarray)

    def test_data_stream_values(self):
        file_path = 'src/ec2_cpu_utilization.csv'
        size = 1000
        data = data_stream_simulation(file_path, size)
        self.assertTrue(np.all(np.isfinite(data)), "All values should be finite numbers")

    def test_data_stream_error_handling(self):
        file_path = 'non_existent_file.csv'
        data = data_stream_simulation(file_path, 1000)
        self.assertEqual(len(data), 0, "Should return an empty array for invalid file path")

if __name__ == '__main__':
    unittest.main()