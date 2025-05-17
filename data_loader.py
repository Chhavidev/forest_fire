import pandas as pd

def load_csv(csv_file):
    """CSV file ko load karne aur verify karne ka function."""
    try:
        df = pd.read_csv(csv_file)
        print(f"✅ Successfully loaded '{csv_file}'!")
        print(df.head())  # Pehli 5 rows dekho
        return df
    except FileNotFoundError:
        print(f"❌ File '{csv_file}' not found!")

# Usage Example
df = load_csv("data/fire_data.csv")
