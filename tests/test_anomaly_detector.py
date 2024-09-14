import unittest
from src.anomaly_detector import AnomalyDetector

class TestAnomalyDetector(unittest.TestCase):

    def setUp(self):
        self.detector = AnomalyDetector(alpha=0.1, threshold=3)

    def test_initialization(self):
        self.assertIsNotNone(self.detector)
        self.assertEqual(self.detector.alpha, 0.1)
        self.assertEqual(self.detector.threshold, 3)
        self.assertIsNone(self.detector.ema)
        self.assertEqual(self.detector.anomalies, [])

    def test_first_value(self):
        value = 10
        is_anomaly = self.detector.detect(value)
        self.assertFalse(is_anomaly)
        self.assertEqual(self.detector.ema, value)

    def test_subsequent_values(self):
        values = [10, 12, 14, 16, 18]
        for value in values:
            is_anomaly = self.detector.detect(value)
            self.assertFalse(is_anomaly)
        
        # Check if EMA is updated correctly
        expected_ema = 10 * (1 - 0.1) ** 4 + 12 * 0.1 * (1 - 0.1) ** 3 + 14 * 0.1 * (1 - 0.1) ** 2 + 16 * 0.1 * (1 - 0.1) + 18 * 0.1
        self.assertAlmostEqual(self.detector.ema, expected_ema, places=5)

    def test_anomaly_detection(self):
        values = [10, 12, 14, 16, 50]  # 50 should be detected as an anomaly
        anomalies = []
        for value in values:
            if self.detector.detect(value):
                anomalies.append(value)
        
        self.assertEqual(anomalies, [50])
        self.assertEqual(self.detector.anomalies, [50])

if __name__ == '__main__':
    unittest.main()