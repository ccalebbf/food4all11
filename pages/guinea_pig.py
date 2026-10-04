import streamlit as st
import folium
from streamlit_folium import st_folium
from sync_updated import data_to_db
from map import time_to_colour

# format of dict: for block in block, block no: [post_code, [latitude, longitude]]
pearl_garden = {98: [460098, [1.33429725783725, 103.93986643128832]], 
                99: [460099, [1.333887121833775, 103.9394561840746]] , 
                100: [460100, [1.3343449481580134, 103.93880989153601]], 
                101: [460101, [1.3344575703838415, 103.93783893187799]], 
                102: [460102, [1.333894459203151, 103.93740977843797]], 
                103: [460103, [1.33346542202661, 103.93753852446999]], 
                104: [460104, [1.3332348145085486, 103.93646027644773]], 
                105: [460105, [1.3336370369014425, 103.93650855620973]], 
                106: [460106, [1.334420029637709, 103.93705572684574]]}

neighbourhood = data_to_db('Pearl Garden', pearl_garden)

m = folium.Map(location=[1.3338677218136072, 103.93803744309989], zoom_start = 17.5)

if neighbourhood:

    for block in neighbourhood.blocks:

        popup_text = f"<b>Block {block.block}</b><br>Days since last distribution: {block.time_since_last_distribution()}<br>Total distributions: {len(block.distributions)}"

        block_popup = folium.Popup(popup_text, max_width = 310)

        folium.Marker(location = block.coordinates, 
                      popup = block_popup, 
                      tooltip = f"Block {block.block}",
                      icon = folium.Icon(color = time_to_colour(block.time_since_last_distribution()), 
                                         icon = 'info-sign',
                                         icon_color = time_to_colour(block.time_since_last_distribution())
                                        )
                    ).add_to(m)

st_data = st_folium(m, width=800, height=550, returned_objects = [])