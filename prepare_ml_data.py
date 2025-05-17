import pandas as pd
from sklearn.preprocessing import StandardScaler

def prepare_ml_data(csv_file, output_file):
    """Fire data ko ML model ke liye scale karta hai."""
    df = pd.read_csv(csv_file)

    scaler = StandardScaler()
    df[["brightness"]] = scaler.fit_transform(df[["brightness"]])

    df.to_csv(output_file, index=False)
    print(f"✅ ML-ready dataset '{output_file}' saved!")

# Usage Example
prepare_ml_data("data/india_fire_data.csv", "data/ml_ready_fire_data.csv")
