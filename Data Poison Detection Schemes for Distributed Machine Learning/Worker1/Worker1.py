import socket
import json
import pandas as pd
import numpy as np
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Create a server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 2222))  # Listen on port 2222
server.listen(5)
print("Worker1 server started. Listening on port 2222...")

while True:
    # Accept client connections
    client, addr = server.accept()
    print(f"Connection from {addr}")
    
    # Receive data from client
    received_data = client.recv(100000).decode()
    data = json.loads(received_data)
    
    if data["type"] == "basicDML":
        # Parse the dataset
        dataset_str = data["dataset"]
        
        # Save the dataset to a temporary file
        with open("temp_dataset.csv", "w") as f:
            f.write(dataset_str)
        
        # Read the dataset
        dataset = pd.read_csv("temp_dataset.csv")
        dataset = dataset.values
        
        # Split features and target
        X, Y = dataset[:, :-1], dataset[:, -1]
        X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
        
        # Existing SVM
        cls = svm.SVC()
        cls.fit(X_train, y_train)
        prediction_data = cls.predict(X_test)
        existing_acc = accuracy_score(y_test, prediction_data) * 100
        
        # Basic DML approach (simplified for demonstration)
        # In a real implementation, this would involve some distributed learning aspects
        # Here we're just using a different parameter setup
        cls_dml = svm.SVC(kernel='rbf', C=1.0)
        cls_dml.fit(X_train, y_train)
        prediction_data_dml = cls_dml.predict(X_test)
        dml_acc = accuracy_score(y_test, prediction_data_dml) * 100
        
        # Send results back to client
        response = {
            "existing": existing_acc,
            "dml": dml_acc
        }
        client.send(json.dumps(response).encode())
    
    # Close the connection
    client.close()