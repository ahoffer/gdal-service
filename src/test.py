from osgeo import gdal

gdal.AllRegister()
print(gdal.GetDriverCount())
nitf = gdal.Open("test_data/p0_01a.ntf")
gdal.Translate('test_data/ouput.jpeg', nitf)
print(nitf.GetMetadata())