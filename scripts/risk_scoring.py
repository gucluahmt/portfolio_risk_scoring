# risk_scoring.py

import pandas as pd
import numpy as np
import os

# Load Dataset
def load_data(file_path):
    """
    Loads the portfolio dataset from the given path.
    """
    return pd.read_csv(file_path)

# Calculate Risk Category
def calculate_risk_category(row):
    """
    Determines the client's risk category based on their Equity percentage.
    """
    if row['Equity %'] >= 70:
        return 'High Risk'
    elif 40 <= row['Equity %'] < 70:
        return 'Medium Risk'
    else:
        return 'Low Risk'

# Calculate Diversification Score
def calculate_diversification_score(row):
    """
    Calculates how diversified the portfolio is based on the distribution of assets.
    """
    categories = [row['Equity %'], row['Bond %'], row['Cash %'], row['Other Assets %']]
    diversified_assets = [asset for asset in categories if asset > 10]
    return len(diversified_assets)

# Save Output
def save_output(df, output_path):
    """
    Saves the processed portfolio with risk categories and diversification scores.
    """
    df.to_csv(output_path, index=False)
    print(f"Processed portfolio saved to: {output_path}")

# Main Process
if __name__ == "__main__":
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_folder = os.path.join(project_root, "data")
    output_folder = os.path.join(project_root, "output")

    input_file = os.path.join(data_folder, "portfolio_data.csv")
    output_file = os.path.join(output_folder, "portfolio_risk_scored.csv")

    os.makedirs(output_folder, exist_ok=True)

    portfolio_df = load_data(input_file)

    portfolio_df['Risk Category'] = portfolio_df.apply(calculate_risk_category, axis=1)
    portfolio_df['Diversification Score'] = portfolio_df.apply(calculate_diversification_score, axis=1)

    save_output(portfolio_df, output_file)
