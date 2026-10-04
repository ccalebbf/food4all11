# -- Function that deals with all things maps related --

import folium
from streamlit_folium import st_folium
from sync_updated import data_to_db

# -- helper that converts days since last distribution to colour visualised on map --
# Purple - no record
# Blue - within 1 week
# Green - 1 to 2 weeks
# Orange - 2 to 4 weeks
# Red - more than 4 weeks
def time_to_colour(time):
    if time == "No Record" or time < 0:
        return 'purple'
    elif time <= 7:
        return 'blue'
    elif time <= 14:
        return 'green'
    elif time <= 28:
        return 'orange'
    else:
        return 'red'

# -- map constructor helper --
def create_pg_map():
    pearl_garden = {98: [460098, [1.334225, 103.939826]], 
                99: [460099, [1.333908, 103.939446]] , 
                100: [460100, [1.334289, 103.938856]], 
                101: [460101, [1.334461, 103.937938]], 
                102: [460102, [1.333882, 103.937461]], 
                103: [460103, [1.333458, 103.937525]], 
                104: [460104, [1.333297, 103.936613]], 
                105: [460105, [1.333705, 103.936565]], 
                106: [460106, [1.334439, 103.937123]]}

    neighbourhood = data_to_db('Pearl Garden', pearl_garden)

    m = folium.Map(location=[1.3338677218136072, 103.93803744309989], zoom_start = 17.5)

    if neighbourhood:

        for block in neighbourhood.blocks:
            
            if block.latest_distribution:
                popup_text = f"<b><u>Block {block.block}</u></b><br><b>Latest Distribution 📦</b><br> Date: {block.latest_distribution.date} <br> Organisation: {block.latest_distribution.org} <br> Type: {block.latest_distribution.type} <br> Number of People (approx): {block.latest_distribution.pax} <br> Halal-Certified?: {block.latest_distribution.isHalal} <br><b>Days since Last Distribution 🗓️</b><br> {block.time_since_last_distribution()}<br><b>Total Distributions 📖</b><br> {len(block.distributions)}"
            else:
                popup_text = f"<b><u>Block {block.block}</u></b><br><b>Latest Distribution 📦</b><br> No Distribution Records <br><b>Days since Last Distribution 🗓️</b><br> {block.time_since_last_distribution()}<br><b>Total Distributions 📖</b><br> {len(block.distributions)}"
            
            block_popup = folium.Popup(popup_text, max_width = 1000)

            folium.Marker(location = block.coordinates, 
                        popup = block_popup, 
                        icon = folium.Icon(color = time_to_colour(block.time_since_last_distribution()), 
                                            icon = 'info-sign',
                                            icon_color = time_to_colour(block.time_since_last_distribution())
                                            )
                        ).add_to(m)

    return m