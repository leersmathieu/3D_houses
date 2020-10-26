### DONT LOOK THIS CODE IT'S JUST FOR DEV AND TESTING
### Take a look on the notebook file (.ipynb) for better reading

# import shapefile
import rasterio
from rasterio.plot import show


fp = r'./data/dtm/RELIEF_WALLONIE_MNS_2013_2014.tif'
dtm = rasterio.open(fp)


