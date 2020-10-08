###DONT LOOK THIS CODE IT'S JUST FOR DEV AND TESTING
### Take a look on the notebook file (.ypnd) for better reading

import shapefile
from PIL import Image


print("Hello World")

shp = shapefile.Reader("data/shp/DHMVII_vdc_k01.shp")
shp_object = open("data/shp/DHMVII_vdc_k01.shp", "rb")

dbf = shapefile.Reader("data/shp/DHMVII_vdc_k01.dbf")
dbf_object = open("data/shp/DHMVII_vdc_k01.dbf", "rb")

im = Image.open('a_image.tif')
im.show()

print(shp)
print(dbf)
s = shp.shape(1)

print(shp.shape(0))
print(shp.shapeType)  # 5 = polygon
print(shp.bbox)

shapes = shp.shapes()
print(len(shapes), shapes)


