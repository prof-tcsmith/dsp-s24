import pandas as pd
import numpy as np

# Seed for reproducibility
np.random.seed(42)

# Generate synthetic transaction data
num_records = 10000
num_features = 30

# Simulate normal transactions (95% of the data)
normal_data = np.random.normal(loc=0, scale=1, size=(int(num_records * 0.95), num_features))

# Simulate anomalies (5% of the data)
anomalies_data = np.random.normal(loc=0, scale=5, size=(int(num_records * 0.05), num_features))

# Combine the data
data = np.vstack((normal_data, anomalies_data))

# Labels: 0 for normal, 1 for anomalies
labels = np.array([0] * int(num_records * 0.95) + [1] * int(num_records * 0.05))

# Shuffle the dataset to mix anomalies with normal data
indices = np.arange(num_records)
np.random.shuffle(indices)

data = data[indices]
labels = labels[indices]

# Create a DataFrame
df = pd.DataFrame(data, columns=[f'Feature_{i+1}' for i in range(num_features)])
df['Class'] = labels

# Save to CSV
csv_path = "/mnt/data/SyntheticTransactionData.csv"
df.to_csv(csv_path, index=False)
csv_path
