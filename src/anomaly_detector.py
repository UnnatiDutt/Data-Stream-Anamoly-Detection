class AnomalyDetector:
    def __init__(self, alpha=0.1, threshold=1):
        self.alpha = alpha
        self.threshold = threshold
        self.ema = None
        self.anomalies = []

    def detect(self, value):
        if self.ema is None:
            self.ema = value
        else:
            self.ema = self.alpha * value + (1 - self.alpha) * self.ema
        
        deviation = abs(value - self.ema)
        if deviation > self.threshold:
            self.anomalies.append(value)
            return True
        return False