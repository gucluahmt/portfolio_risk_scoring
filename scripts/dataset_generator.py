# dataset_generator.py

import pandas as pd
import numpy as np
import os

# Dataset Parameters
NUM_RECORDS = 100000  # 100K records

# Data Generation
def generate_portfolio_data(num_records):
    np.random.seed(42)  # For reproducibility

    client_ids = [f"CUST-{i+1:06d}" for i in range(num_records)]

    equity = np.random.uniform(10, 90, num_records)
    bond = np.random.uniform(5, 70, num_records)
    cash = np.random.uniform(0, 30, num_records)
    other = 100 - (equity + bond + cash)

    # Ensure that total percentages are logical
    portfolio_df = pd.DataFrame({
        "Client_ID": client_ids,
        "Equity %": np.clip(equity, 0, 100),
        "Bond %": np.clip(bond, 0, 100),
        "Cash %": np.clip(cash, 0, 100),
        "Other Assets %": np.clip(other, 0, 100)
    })

    return portfolio_df

# Save Dataset
def save_dataset(df, output_path):
    df.to_csv(output_path, index=False)
    print(f"Dataset successfully saved to: {output_path}")

# Main Execution
if __name__ == "__main__":
    # Go up one directory and find the data/ folder
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_folder = os.path.join(project_root, "data")
    output_file = os.path.join(data_folder, "portfolio_data.csv")

    os.makedirs(data_folder, exist_ok=True)

    portfolio_data = generate_portfolio_data(NUM_RECORDS)
    save_dataset(portfolio_data, output_file)
