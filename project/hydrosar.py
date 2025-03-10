import subprocess
import pandas as pd
import requests
import os
from zipfile import ZipFile
import multiprocessing
from concurrent.futures import ThreadPoolExecutor

box_data = {
    'zipfile': ['S1A_IW_20250205T233956_DVP_RTC10_G_gduned_DD97.zip',
                'S1A_IW_20250217T233955_DVR_RTC10_G_gduned_0491.zip'],
    'link': ['https://ky.box.com/shared/static/2w2x6sj97x2trg0gv9az6k16o0v9zgbl.zip', 
             'https://ky.box.com/shared/static/w3zruxeczm2zpl9mepixbpp6nxszxzg1.zip']
    }

df = pd.DataFrame(data=box_data)

# for row_index, row in df.iterrows():
#     out_folder = "project/data/"  # relative path from root
#     out_file = row['zipfile']
#     url = row['link']
#     out_file_path = os.path.join(out_folder, out_file)

#     if not os.path.exists(out_folder):
#         out_folder = os.path.join(out_folder)
#     else:
#         print(f'{out_folder} directory already exists.')
    

#     # download file
#     try:
#         response = requests.get(url, stream=True)
#         print(f'Status Code: {response.status_code}\n')
#         if response.status_code == 200:
#             with open(out_file_path, 'wb') as file:
#                 for chunk in response.iter_content(chunk_size=8192):  # download in chunks for efficiency
#                     file.write(response.content)
#             print(f'Downloaded: {out_file_path}.\n')
#     except Exception as e:
#         print(e)

# def box_download(df):
#     for row_index, row in df.iterrows():
#         out_dir = "project/data/"  # relative path from root
#         url = row['link']

#         if not os.path.exists(out_dir):
#             out_dir = os.makedirs(out_dir)
#         else:
#             print(f'{out_dir} directory already exists.')
        
#         # download file
#         try:
#             response = requests.get(url, stream=True)
#             print(f'Status Code: {response.status_code}\n')
            
#             if response.status_code == 200:
#                 with open(out_file, 'wb') as file:
#                     for chunk in response.iter_content(chunk_size=8192):  # download in chunks for efficiency
#                         file.write(response.content)
#                         print(f'Downloaded: {out_file}.\n')
#             else:
#                 print(f'{os.path.basename(out_file)} already downloaded.\n')
                    
#         except Exception as e:
#             print(e)

def box_download(df):
    out_folder = "project/data"
    
    for row_index, row in df.iterrows():
        link = row['link']
        unzipped_folder = os.path.splitext(row['zipfile'])[0]
        cmd = f"cd project/data && curl -L -o file.zip {link} && unzip file.zip && rm file.zip && cd ../../"

        if not os.path.exists(os.path.join(out_folder, unzipped_folder)):
            subprocess.run(cmd, shell=True, check=True)


logical_cores = multiprocessing.cpu_count()
# determine number of threads to use for multiprocessing
num_workers = int(logical_cores * 0.75)  # rounds down in case not a whole number
print(f'Number of threads to use: {num_workers}\n')

with ThreadPoolExecutor(max_workers=num_workers) as executor:
    executor.map(box_download(df))