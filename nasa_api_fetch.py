import requests

API_URL = "https://firms.modaps.eosdis.nasa.gov/api/active_fire/south_asia.csv"

def fetch_fire_data(output_file):
    """NASA FIRMS API se real-time fire detection data fetch karta hai."""
    response = requests.get(API_URL)

    if response.status_code == 200:
        with open(output_file, "wb") as file:
            file.write(response.content)
        print(f"✅ Real-time fire data saved as '{output_file}'!")
    else:
        print("❌ Failed to fetch data.")

# Usage Example
fetch_fire_data("real_time_fire_data.csv")
