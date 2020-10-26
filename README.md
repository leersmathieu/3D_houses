# 3D_houses
Type of Challenge: Learning &amp; Consolidation

[Link](https://github.com/leersmathieu/CRL-Turing-4.22/tree/master/Projects/3.3D_houses_numpy) to the descriptive challenge 

## The Mission

> We are LIDAR PLANES , active in the Geospatial industy. We would like to use our data to launch a new branch in the insurrance business.  So, we need you to build a solution with our data to model a house in 3D with only a home address.

## Steps to realise

### 1. Data
Comprendre les données pour pouvoir les utiliser

- Appréhender les dossiers DSM & DTM
- Appréhender LIDAR
- Apprendre à utiliser les fichier geoTIFF

Nettoyer les données


**Piste :**

- Fichier de formes ([shapefiles](https://desktop.arcgis.com/fr/arcmap/10.3/manage-data/shapefiles/what-is-a-shapefile.htm))
- Lidar

```
What is LIDAR ?

LIDAR is a method to measure distance using light. The device will illuminate a target with a laser light and a sensor will measure the reflection. Differences in wavelength and return times will be used to get 3D representations of an area.
Here is a LIDAR segmentation :
```

![Lidar Segmentation](lidar_seg.png)

- Format de fichier  [geoTIFF](https://www.commentcamarche.net/contents/1205-tiff-format-tif)

### 2. Manipulation

Manipuler les données ainsi que les outils nécessaires à la réalisation de la mission

- 3D-Plot