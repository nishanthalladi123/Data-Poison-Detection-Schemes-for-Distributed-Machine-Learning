Data Poison Detection Schemes for Distributed Machine Learning

A secure, lightweight framework to detect and mitigate data poisoning attacks in distributed machine learning environments using Isolation Forest and Support Vector Machines (SVM), integrated with a user-friendly GUI.

🚀 Project Overview
This project presents a defense mechanism against data poisoning attacks in distributed machine learning (DML). It simulates a multi-worker environment where malicious data can be injected during the training phase. The framework combines anomaly detection (via Isolation Forest) and classification (via SVM) to identify and eliminate poisoned data before model aggregation.

It includes:

Semi-distributed learning simulation

Poisoned data detection using Isolation Forest

Robust classification using SVM

Interactive GUI using Tkinter

Accuracy comparison visualization

🧠 Key Concepts
Data Poisoning Attacks: Injection of malicious data into the training set to manipulate model behavior.

Isolation Forest: Anomaly detection method to isolate outliers (potentially poisoned data).

SVM: A robust classifier trained on cleaned datasets to ensure higher accuracy.

Semi-Distributed Learning: Simulated federated-like setup using multiple workers and a central server.

🛠️ Tech Stack
Python 3.8+

Tkinter for GUI

Scikit-learn for ML models

Matplotlib / Seaborn for visualization

Socket Programming for simulating distributed nodes

📂 Project Structure
bash
Copy
Edit
📁 Data Poison Detection Schemes for Distributed Machine Learning
├── centralserver.py        # Main GUI + logic
├── worker1.py              # Worker node 1
├── worker2.py              # Worker node 2
├── sample_dataset.csv      # Test dataset
└── README.md
🔧 Setup & Installation
Clone the repo:

bash
Copy
Edit
git clone https://github.com/nishanthalladi123/Data-Poison-Detection-Schemes-for-Distributed-Machine-Learning.git
cd Data-Poison-Detection-Schemes-for-Distributed-Machine-Learning
Install dependencies:

bash
Copy
Edit
pip install pandas scikit-learn matplotlib seaborn
Run the workers in separate terminals:

bash
Copy
Edit
python worker1.py
python worker2.py
Launch the central GUI server:

bash
Copy
Edit
python centralserver.py
💡 Features
📂 Upload CSV datasets

⚖️ Dataset splitting and distribution to worker nodes

🧪 SVM and DML-based accuracy comparison

🧼 Isolation Forest-based anomaly filtering

📊 Graphical accuracy comparison (SVM vs Basic DML vs Semi-DML)

🖼️ GUI for non-technical users
