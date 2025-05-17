import pandas as pd

def filter_india_data(csv_file, output_file):
    """Sirf India-specific fire detections extract karta hai."""
    df = pd.read_csv(csv_file)

    df_india = df[(df["latitude"] >= 8) & (df["latitude"] <= 37) &
                  (df["longitude"] >= 68) & (df["longitude"] <= 97)]

    df_india.to_csv(output_file, index=False)
    print(f"✅ India-specific fire data saved as '{output_file}'!")

# Usage Example
filter_india_data("data/fire_data.csv", "data/india_fire_data.csv")
