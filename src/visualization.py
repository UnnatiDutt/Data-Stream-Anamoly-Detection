import matplotlib.pyplot as plt
import matplotlib.animation as animation
from .data_stream_simulation import data_stream_simulation
from .anomaly_detector import AnomalyDetector
import numpy as np

def visualize(file_path):
    data_stream = data_stream_simulation(file_path)
    
    if len(data_stream) == 0:
        print("No data available for visualization.")
        return

    detector = AnomalyDetector()
    detector.fit(data_stream)

    fig, ax = plt.subplots()
    line, = ax.plot([], [], lw=2)
    anomaly_points, = ax.plot([], [], 'ro')

    def init():
        ax.set_xlim(0, len(data_stream))
        ax.set_ylim(np.min(data_stream) - 5, np.max(data_stream) + 5)
        line.set_data([], [])
        anomaly_points.set_data([], [])
        return line, anomaly_points

    def update(frame):
        xdata = np.arange(frame)
        ydata = data_stream[:frame]
        line.set_data(xdata, ydata)
        
        anomalies = [i for i in range(frame) if detector.detect(data_stream[i])]
        anomaly_ydata = [data_stream[i] for i in anomalies]
        anomaly_points.set_data(anomalies, anomaly_ydata)
        
        return line, anomaly_points

    ani = animation.FuncAnimation(fig, update, frames=len(data_stream), init_func=init, blit=True)
    plt.show()

# Example usage
if __name__ == "__main__":
    file_path = 'src/ec2_cpu_utilization.csv'
    visualize(file_path)