import unittest
import numpy as np
from src.anomaly_detector import AnomalyDetector

class TestAnomalyDetector(unittest.TestCase):

    def setUp(self):
        self.detector = AnomalyDetector(contamination=0.1)
        self.data = np.array([10, 12, 14, 16, 18, 50])

    def test_fit(self):
        self.detector.fit(self.data)
        self.assertIsNotNone(self.detector.model)

    def test_detect(self):
        self.detector.fit(self.data)
        anomalies = []
        for value in self.data:
            if self.detector.detect(value):
                anomalies.append(value)
        
        self.assertEqual(anomalies, [50])
        self.assertEqual(self.detector.anomalies, [50])

if __name__ == '__main__':
    unittest.main()