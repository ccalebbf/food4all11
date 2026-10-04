import streamlit as st
import folium
from folium plugins import MarkerCluster
from streamlit_folium import st_folium
from sync_updated import data_to_db
from map import time_to_colour

# format of dict: for block in block, block no: [post_code, [latitude, longitude]]
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

marker_cluster = MarkerCluster().add_to(m)

if neighbourhood:

    for block in neighbourhood.blocks:

        popup_text = f"<b>Block {block.block}</b><br>Days since Last Distribution: {block.time_since_last_distribution()}<br>Total Distributions: {len(block.distributions)}"

        block_popup = folium.Popup(popup_text, max_width = 310)

        folium.Marker(location = block.coordinates, 
                      popup = block_popup, 
                      icon = folium.Icon(color = time_to_colour(block.time_since_last_distribution()), 
                                         icon = 'info-sign',
                                         icon_color = time_to_colour(block.time_since_last_distribution())
                                        )
                    ).add_to(marker_cluster)

st_data = st_folium(m, width=800, height=550, returned_objects = [])