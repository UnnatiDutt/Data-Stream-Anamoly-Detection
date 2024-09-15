Steps To run :
1. Install basic requirements
2. Paste the dataset in the data folder and make sure to rename its colume name   (which contains the data) to "value" 
3. Navigate THroud the project directory in Command Prompt or COde editor then run python main.py

Algorithm used for Anomaly Detection : ISOLATION FOREST

The Isolation Forest algorithm is an unsupervised machine learning algorithm used for anomaly detection. It is particularly effective in identifying outliers or anomalies in a dataset.

The main idea behind the Isolation Forest algorithm is to isolate anomalies by randomly partitioning the data into subsets. This is done by creating a binary tree structure, where each internal node represents a splitting rule and each leaf node represents an isolated subset of the data.

During the training phase, the algorithm randomly selects a feature and a split value to create a partition. The process is repeated recursively until all instances are isolated in individual leaf nodes. The number of splits required to isolate an instance is used as a measure of its anomaly score. Anomalies are expected to have shorter paths in the tree, as they are easier to isolate.

To detect anomalies in new data, the algorithm traverses the tree and calculates the average path length for each instance. If the average path length is significantly shorter than the expected length for normal instances, the instance is classified as an anomaly.

We have used the skicit-learn for implementing Isolation forest algorithm.

The src directory Contains 4 files 
1. data_stream_simulation.py - This imports the data from csv file and send data in a stream
2. visualization.py - This file is shows the plot on a real time graph with normal values in blue and detected anomaly in red colour
3. anomaly_detector.py - This file implements the ISolation forest algorithm on the data stream imported for data_stream_simulation file
