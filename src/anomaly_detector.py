from sklearn.ensemble import IsolationForest

class AnomalyDetector:
    def __init__(self, contamination=0.01):
        self.contamination = contamination
        self.model = IsolationForest(contamination=self.contamination)
        self.anomalies = []

    def fit(self, data):
        self.model.fit(data.reshape(-1, 1))

    def detect(self, value):
        prediction = self.model.predict([[value]])
        if prediction == -1:
            self.anomalies.append(value)
            return True
        return False