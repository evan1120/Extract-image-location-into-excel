import gmplot
import os
import exifread


dirPath = 'E:/202208湖北武穴老城区旧改/03-过程文件/202203现场调研\武穴现场调研 - 副本'

# # 遍历目录下的所有图片文件
# for i, img in enumerate(os.listdir(dirPath)):
#     img_path = os.path.join(dirPath, img)
#     #print(img)
#
#     # 获取GPS数据
#     file_path = open(img_path, 'rb')
#     contents = exifread.process_file(file_path)
#     for key in contents:
#         if key == "GPS GPSLongitude":
#             longitude = contents["GPS GPSLongitude"].values
#         elif key == "GPS GPSLatitude":
#             latitude = contents["GPS GPSLatitude"].values
#
#     # 度分秒转换成十进制数据
#     longitude_f = longitude[0].num / longitude[0].den + (longitude[1].num / longitude[1].den / 60) + (
#                     longitude[2].num / longitude[2].den / 3600)
#     latitude_f = latitude[0].num / latitude[0].den + (latitude[1].num / latitude[1].den / 60) + (
#                     latitude[2].num / latitude[2].den / 3600)
#
# create a list of coordinates
lats, lons, img_links = [], [], []
for img in os.listdir(dirPath):
    img_path = os.path.join(dirPath, img)
    file_path = open(img_path, 'rb')
    contents = exifread.process_file(file_path)
    for key in contents:
        if key == "GPS GPSLongitude":
            longitude = contents["GPS GPSLongitude"].values
        elif key == "GPS GPSLatitude":
            latitude = contents["GPS GPSLatitude"].values

    # convert from degrees, minutes, seconds to decimal format
    longitude_f = longitude[0].num / longitude[0].den + (longitude[1].num / longitude[1].den / 60) + (longitude[2].num / longitude[2].den / 3600)
    latitude_f = latitude[0].num / latitude[0].den + (latitude[1].num / latitude[1].den / 60) + (latitude[2].num / latitude[2].den / 3600)

    # add to list of coordinates and image links
    lats.append(latitude_f)
    lons.append(longitude_f)
    img_links.append(f'<a href="file://{img_path}">{img}</a>')

# create a new map object
gmap = gmplot.GoogleMapPlotter.from_geocode("Wuxue, China")

# plot the coordinates on the map
gmap.scatter(lats, lons, 'red', size=10, marker=False)

# add image links as markers on the map
for lat, lon, img_link in zip(lats, lons, img_links):
    gmap.marker(lat, lon, title=img_link)

# draw the map
gmap.draw("map.html")
