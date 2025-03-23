import os
import pandas as pd
from whitebox_workflows import WbEnvironment
from IPython.display import display

# create a data from for the scenes
def create_scenes_df():
    
    """
        These files were obtained using the ASF Vertex Data Search.
        They were submitted for Radio Terrain Correctiom.
        radiometry: gamma0
        scale: decibel
        pixel spacing: 10m
    """

    box_data = {
        'zipfile': ['S1A_IW_20250205T233956_DVP_RTC10_G_gdufem_246A.zip',
                    'S1A_IW_20250217T233955_DVP_RTC10_G_gdufem_E701.zip'],
        'link': ['https://ky.box.com/shared/static/xwhzpb6entefdhsi8jfhgii1f4ehh6x6.zip', 
                'https://ky.box.com/shared/static/81wf3fabzhzsux29nhe4ojdaq0qtwp89.zip']
            }
    scenes_df = pd.DataFrame(data=box_data)

    # calculate some fields
    scenes_df['scene_folder'] = scenes_df['zipfile'].apply(lambda x: os.path.splitext(x)[0])
    scenes_df['input_dem'] = scenes_df['scene_folder'] + '_dem.tif'
    scenes_df['rgb'] = scenes_df['scene_folder'] +  '_rgb.png'
    scenes_df['vv'] = scenes_df['scene_folder'] + '_vv.tif'
    scenes_df['vh'] = scenes_df['scene_folder'] + '_vh.tif'
    scenes_df['shapefile'] = scenes_df['scene_folder'] + '_shape.shp'
  
    return scenes_df