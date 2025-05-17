import folium
import pandas as pd

def generate_fire_map(csv_file, output_html):
    """Fire data se interactive folium map generate karta hai."""
    df = pd.read_csv(csv_file)
    m = folium.Map(location=[22, 78], zoom_start=5)

    for _, row in df.iterrows():
        folium.CircleMarker(location=[row["latitude"], row["longitude"]],
                            radius=5, color="red", fill=True).add_to(m)

    m.save(output_html)
    print(f"✅ Interactive fire map '{output_html}' created!")

# Usage Example
generate_fire_map("data/india_fire_data.csv", "data/fire_map.html")
