from sklearn.ensemble import IsolationForest

class AnomalyDetector:
    #Initializing Model
    def __init__(self, contamination=0.01):
        self.contamination = contamination
        self.model = IsolationForest(contamination=self.contamination)
        self.anomalies = []
    #fit tha data into the model
    def fit(self, data):
        self.model.fit(data.reshape(-1, 1))
    #detects anamolies
    def detect(self, value):
        prediction = self.model.predict([[value]])
        if prediction == -1:
            self.anomalies.append(value)
            return True
        return False