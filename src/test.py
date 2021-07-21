from pathlib import Path
import math
from osgeo import gdal

gdal.AllRegister()
print(gdal.GetDriverCount())
name = 'p0_01a.ntf'
input = 'test_data/' + name
path = Path(input)
bytes = path.stat().st_size
targetBytes = 5 * 1024 * 1024
if targetBytes < bytes:
    factor = bytes/targetBytes
    percent = 1 / math.sqrt(factor)
    nitf = gdal.Open(input)
    gdal.Translate('test_data/output.jpeg', nitf, format='JPEG', heightPct=percent, widthPct=percent);

print(nitf.GetMetadata())
nitf = None
