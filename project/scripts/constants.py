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

    # print an example
    # print(scenes_df)

    # base_scene = scenes_df.at[0,'scene_folder']
    # flood_scene = scenes_df.at[1,'scene_folder']

    # print(f'Base Scene Directory:  {base_scene}\nFlood Scene Directory: {flood_scene}')
    
    return scenes_df

# setup Whitebox Workflows envrionment
wbe = WbEnvironment()

# fill remove depressions in the dem
def dem_fill(file, temp_dir):
    
    """
    the `wbe.fill_depressions` function is used to fill any voids and anomolies in the dem
    """

    wbe.verbose = True
    wbe.work_directory = temp_dir
    print(f'Working directory: {wbe.work_directory}')

    # set up so that you don't have to do the fill depressions process if already in memory
    # I don't think this will actually work
    try:
        input_dem_raster
    except NameError:
        input_dem_raster = wbe.read_raster(file)
        print(input_dem_raster.file_name)
        display("Starting DEM filling process...")
        filled_dem_raster = wbe.fill_depressions(input_dem_raster)  # leave default parameter, recommended by documetation
        display("DEM filling complete.")
            # write to file
        output_file = os.path.join(temp_dir, 'filled_dem.tif')
        filled_dem_raster = wbe.write_raster(filled_dem_raster, output_file)
    else:
        output_file = os.path.join(temp_dir, 'filled_dem.tif')
        filled_dem_raster = wbe.write_raster(filled_dem_raster, output_file)
   
    return output_file

def flow_direction(filled_dem, temp_dir):

    """
    The d8_pointer function calculates flow direction from the filled
    """
    wbe.verbose = True
    wbe.work_directory = temp_dir
    print(f'Working directory: {wbe.work_directory}')


        # read the filled dem
    input_filled_dem = wbe.read_raster(filled_dem)
    
    # run the d8_pointer functino to get flow directions
    display("Start d8_pointer function . . . ")
    flow_direction_dem = wbe.d8_pointer(input_filled_dem)
    display("d8_pointer function call complete")

    # write output to file
    output_file = os.path.join(temp_dir, 'flow_dem.tif')
    flow_direction_dem = wbe.write_raster(flow_direction_dem, output_file)
    
    return output_file 

# create flow accumulation
def flow_accumulation(flow_dem, temp_dir):

    wbe.verbose = True
    wbe.work_directory = temp_dir
    print(f'Working directory: {wbe.work_directory}')

    try:
        input_flow_dem = wbe.read_raster(os.path.join(temp_dir, 'flow_dem.tif'))
        flow_accumulation = wbe.d8_flow_accum(input_flow_dem)
        
        # write to file
        output_file = os.path.join(temp_dir, 'flow_accum.tif')
        flow_accumulation = wbe.write_raster(flow_accumulation, output_file)
    
    except Exception as e:
        print(e)    

    return output_file