import unittest
from unittest.mock import patch, MagicMock
from src.visualization import visualize

class TestVisualization(unittest.TestCase):

    @patch('src.visualization.plt.show')
    @patch('src.visualization.animation.FuncAnimation')
    @patch('src.visualization.AnomalyDetector')
    @patch('src.visualization.data_stream_simulation')
    def test_visualize(self, mock_data_stream_simulation, mock_AnomalyDetector, mock_FuncAnimation, mock_plt_show):
        # Mock the data stream
        mock_data_stream_simulation.return_value = [10, 12, 14, 16, 18, 50]
        
        # Mock the AnomalyDetector
        mock_detector_instance = MagicMock()
        mock_detector_instance.detect.side_effect = [False, False, False, False, False, True]
        mock_AnomalyDetector.return_value = mock_detector_instance
        
        # Call the visualize function
        file_path = 'src/ec2_cpu_utilization.csv'
        visualize(file_path)
        
        # Check if data_stream_simulation was called
        mock_data_stream_simulation.assert_called_once_with(file_path)
        
        # Check if AnomalyDetector was instantiated
        mock_AnomalyDetector.assert_called_once()
        
        # Check if FuncAnimation was called
        mock_FuncAnimation.assert_called_once()
        
        # Check if plt.show was called
        mock_plt_show.assert_called_once()

if __name__ == '__main__':
    unittest.main()