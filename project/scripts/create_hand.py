import os
from constants import create_scenes_df
# set up Whitebox Environment, get available functions
from whitebox_workflows import WbEnvironment
import shutil

wbe = WbEnvironment()

scenes_df = create_scenes_df()

data_folder = 'project/data'
input_dem = os.path.join(data_folder, scenes_df.at[0, 'scene_folder'],scenes_df.at[0, 'input_dem'])
print(input_dem)

temp_dir = 'project/data/temp_dir'

if not os.path.exists(temp_dir):
    os.makedirs(temp_dir)
else:
    print(f'{temp_dir} already exists')

# fill depressions
# def fill_depressions(self, dem: Raster, fix_flats: bool = True, flat_increment: float = float('nan'), max_depth: float = float('inf')) -> Raster: ...


wbe.working_directory = temp_dir
print(wbe.working_directory)

# copy the dem to the directory
dem_copy = f'{temp_dir}/dem_copy.tif'
shutil.copyfile(input_dem, dem_copy)

input_dem_raster = wbe.read_raster(dem_copy)
print(input_dem_raster.file_name)

input_dem_raster = wbe.fill_depressions(input_dem_raster)  # leave default parameter, recommended by documetation

# create a hillshade for visualization
hs = wbe.multidirectional_hillshade(input_dem_raster)
hs.plot



