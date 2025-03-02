"""
Query URL:
    https://waterservices.usgs.gov/nwis/iv/?format=json&stateCd=ky&startDT=2025-02-01T00:00&endDT=2025-03-01T00:00&siteStatus=active&siteType=ST

"""

# Import NWIS Module from USGS
import dataretrieval.nwis as nwis

stateCD = 'ky'
start = '2025-02-01T00:00'
end = '2025-02-28T00:00'
service = 'iv'

url = f'https://waterservices.usgs.gov/nwis/iv/?format=json&stateCd=ky&startDT={start}&endDT={end}&siteStatus=active&siteType=ST'

df = nwis._read_json(url)
print(df.head)