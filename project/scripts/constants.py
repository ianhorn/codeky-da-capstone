import os
import pandas as pd
import json
import httpx

from folium import Map, TileLayer



def create_scenes_df():
    
    """
       SAR Data:
        These files were obtained using the ASF Vertex Data Search.
        They were submitted for Radio Terrain Correctiom.
        radiometry: gamma0
        scale: decibel
        pixel spacing: 10m
       
        Digital Elevation Model processing:
         The dem processing folder contains the DEM used for radio-
         terrain correction and derivative produces used to create 
         a HAND and water mask.
    """

    box_data = {
        'zipfile': ['S1A_IW_20250124T233956_DVP_RTC10_G_gdufem_8285.zip',
                    'S1A_IW_20250217T233955_DVP_RTC10_G_gdufem_E701.zip',
                    'dem_processing.zip'],
        'link': ['https://ky.box.com/shared/static/oiowba0ne7y0wohbavhv0usjzyob3fwm.zip', 
                'https://ky.box.com/shared/static/81wf3fabzhzsux29nhe4ojdaq0qtwp89.zip',
                'https://ky.box.com/shared/static/rz15mqljj1m0tcejhu647haey6sfrfkf.zip']
            }
    scenes_df = pd.DataFrame(data=box_data)

    # calculate some fields
    scenes_df['scene_folder'] = scenes_df['zipfile'].apply(lambda x: os.path.splitext(x)[0])
    if not scenes_df['scene_folder'].eq('dem_processing.zip').any():
        scenes_df['input_dem'] = scenes_df['scene_folder'] + '_dem.tif'
        scenes_df['rgb'] = scenes_df['scene_folder'] +  '_rgb.png'
        scenes_df['vv'] = scenes_df['scene_folder'] + '_vv.tif'
        scenes_df['vh'] = scenes_df['scene_folder'] + '_vh.tif'
        scenes_df['shapefile'] = scenes_df['scene_folder'] + '_shape.shp'
    else:
        print("dem processing is not a scene")
    return scenes_df
