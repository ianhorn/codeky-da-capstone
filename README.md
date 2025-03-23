# Creating Near-Real-Time Flood Data with Satellite Imagery

### Project Overview

1. Objective
    - Use Sythetic Aperture Radar (SAR) date from the European Space Agency (ESA) Sentinel-1 satellite.

2. Data sources
 - Imagery
    - Acquisition
        - European Space Agency
    - Preprocessing
        - Alaska Satellite Facility [ASF Vertex](https://search.asf.alaska.edu/#/?maxResults=250) Data Search Tool
 - Water Data
    - USGS [Stream Gages](https://opengisdata.ky.gov/maps/44a956e2d58a48cfb2e01b0c127acdec/explore?location=37.827060%2C-85.702407%2C7.15) for Kentucky
 - Python
    - [asf-tools](https://github.com/ASFHyP3/asf-tools/)


     

3. References for background information
    - podaac [cheatsheets & guides](https://podaac.github.io/tutorials/quarto_text/cheatsheet.html#workflow-cheatsheet-terminology)
    - ASF Python [API](https://hyp3-docs.asf.alaska.edu/tools/asf_tools_api/)
    - [HydroSAR](https://github.com/HydroSAR/HydroSAR/tree/develop)


### Data Collection and Loading

Create a virtual environment

Initialize repo
```git
git clone https://github.com/ianhorn/codeky-da-capstone.git 
cd codeky-da-capstone
```

Create a virtuel environment
```bash
python3 -m venv venv
source venv/bin/activate   # linux/mac
venv/Scripts/Activate.ps1  # windows
```
---
### Data Acquisition

My original plan was to use a STAC API to query for data by location and date.  However, obtaining raw satellite data and processing into a usable geo-referenced is very complex.  Fortunately, the [Alaska Satellite Facility](https://asf.alaska.edu/), a NASA Distributed Active Archive Center ([DAAC](https://asf.alaska.edu/asfsardaac/) provides search tool called [Vertex](https://search.asf.alaska.edu/#/?maxResults=250).  This tool allows a user to easily filter data easily.

For this project, I picked to images.  The first images dates February 5<sup>th</sup> while the second image is from February 17<sup>th</sup>.  According to stream gage data, these dates show stream levels are low and high marks for this time during during the Kentucky 2025 Floods in February 2025.

Using the Vertex interface, I selected the two scenes I wanted to submit to the queue for Radiometrically Terrain Corrected (RTC) processing.  [RTC](https://hyp3-docs.asf.alaska.edu/guides/rtc_product_guide/) corrects geometric and radiometric distortions inherent in SAR data because of side-looking instrumentation on the satellite.  By providing this service free of charge to subscribed users at 10,000 credits a month, analysts like myself can bypass intense computational process and use a GIS-ready product.  One could process between 166 to 2000 scences a month depending on final product resolution.

Below is an example of the options I used to order two ESA Sentinel-1 scenes from NASA's Alaska Satellite Facility.

<br>
<p align="center">
  <img src="media/vertex_queue.jpg" alt="Vertex On Demand" width="550"/>
</p><br>

By applying DEM matching, this aligns the scene with the digital elevation model, which provides a ground value for the data.  By applying a speckle filter, the On-Demand processing removes noise.  The end product is a ground range detected (GRD) product at decibel scale.  I chose the decibel scale (not power or amplitude) because it is most suited for detecting water.  

 - Load Data
 - Initial Check
 - Selection Options

### Exploratory Data Analysis

Once we've download the scenes, or granules, for the project area,  We can create a map to make sure we really have the data we need.  A quick and dirty way to do is just to read in the delivered shapefile and load into the map.

For the images themselves, it would take some processing to display on a map.  Since Kentucky has a distinct shape and the images cover a large area, it should be obvious if it is Kentucky.  We can just display a geotiff with an ipywidget image widget or use [titiler](https://developmentseed.org/titiler) to create a tiled image that can be loaded to a map.  

### Data Cleaning and Preparation

Before we can start extracting flood data, we need to process the download Digital Elevation Model (*\*_dem.tif\**) downloaded with our granules create a Height Above Natural Drainage (*HAND*) Model.  To do this, we will use the Whitebox Workflows for Pyhton from [Whitebox Geospatial Inc](https://www.whiteboxgeo.com/).








### Analysis and Insights

 - Findings
 - Supporting Data

### Conclusion and Recommendations

 - Summarize
 - Recommendations

### Optional Advanced Section (Bonus)

 - Advanced EDA (elevation layer?)
 - Dashboards



---
Using Hydrosar to create a few products needed for extracting water data

```cmd
cd project
git clone notebooks/notebook_archives/hydrosar.ipynb
cd hydrosar
```
---