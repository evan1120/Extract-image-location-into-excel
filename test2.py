import os
import exifread
import openpyxl
#import Workbook

#import pandas as pd

dirPath = 'F:\武穴现场调研 - 副本'
#img="F:\武穴现场调研 - 副本\\1 (1).jpg"
for img in os.listdir(dirPath):
    img_path = dirPath + '\\' + img


def get_single_gps(img_path):
    file_path = open(img_path, 'rb')
    print(img)
    contents = exifread.process_file(file_path)
    for key in contents:
        if key == "GPS GPSLongitude":
            longitude = contents["GPS GPSLongitude"].values
            #print("lon =", contents[key], contents['GPS GPSLatitudeRef'])
        elif key == "GPS GPSLatitude":
            latitude = contents["GPS GPSLatitude"].values
            #print("lat =", contents[key], contents['GPS GPSLongitudeRef'])

    # 度分秒转换成十进制数据
    longitude_f = longitude[0].num / longitude[0].den + (longitude[1].num / longitude[1].den / 60) + (
                    longitude[2].num / longitude[2].den / 3600)
    latitude_f = latitude[0].num / latitude[0].den + (latitude[1].num / latitude[1].den / 60) + (
                    latitude[2].num / latitude[2].den / 3600)
    print(longitude_f, latitude_f)

    # 打开工作簿（如果不存在，则创建一个新的）
    workbook = openpyxl.Workbook()
    worksheet = workbook.active

    # 将数据1输入到单元格A1
    worksheet['A1'] = data1

        # 数据2
    data2 = 'Hello, world!'

        # 将数据2输入到单元格B1
    worksheet['B1'] = data2

        # 数据3
    data3 = [1, 2, 3, 4, 5]

        # 将数据3输入到单元格C1到C5
    for i in range(len(data3)):
        cell = worksheet.cell(row=i + 1, column=3)
        cell.value = data3[i]

    # 保存工作簿
#workbook.save('example.xlsx')

#
# if __name__ == '__main__':
#     filepath = r'F:\PYTHON\Extract_img_location\img_location.xls'  # 文件路径
#     #xls_file = xlrd.open_workbook(filepath)
#     #xls_sheet = xls_file.sheet_by_name("Sheet1")  # Excel里的sheet名
#     arr=[]
#     for i in range(1, xls_sheet.nrows):
#         img_name = str[get_single_gps(img_name)[i]]
#         lon = float[get_single_gps(lon)[i]]
#         lat = float[get_single_gps(lat)[i]]
#     pf_target = pd.DataFrame(arr, columns=["img_name", "lon", "lat"])
