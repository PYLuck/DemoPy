# 读取Excel[csv/xls]文件内容，并重写成json，数据以字典嵌套形式存放
"""
需求[COCO目标检测datasets标注]：
json文件包含以下Key：info、licenses、images、annotations
    images，表示标注文件中图像信息列表，每个元素是一张图像的信息。
"""


import json
import xlrd  # 需要1.2.0版本的，2.0以上的版本只能读取.xls类型的文件
import csv
import imagesize        # 用于获取图片宽＆高



# 1.读取文件(.xlsx .xls .csv) 返回[字典]数据
def ReadFile(filePath):         # return data
    try:
        fileType = filePath.split(".")[-1]
        print("读入数据[xls/csv]:", f'{filePath}\t{fileType}')

        if fileType == 'xlsx' or fileType == 'xls':     # 此部分未调试
            res = []
            wb = xlrd.open_workbook(filePath)
            sh = wb.sheet_by_index(0)
            title = []
            for item in sh.row_values(0):
                title.append(item)
            data = []
            # 实现第一行为key，剩下的为value 转为字典了
            var = [[data.append({title[index]: transfer(sh.row_values(it)[index]) for index in range(0, len(title))})]
                   for it
                   in range(1, sh.nrows)]
            return data
        elif fileType == "csv":
            data = []
            with open(filePath) as csvfile:
                rows = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件
                title = next(rows)  # 读取第一行,每一列的标题
                # 以title为键，按行写入字典
                val = [[data.append({title[index]: transfer(it[index]) for index in range(0, len(title))})] for it in rows]
                # print("data__", data[0]);   print("data__1", data[1]['gtbboxid'])
            return data
        else:
            return -1

    except EOFError:
        print("转化过程出错！")
        print(EOFError)
        return -1

# 字符串输入，转成相应的类型
def transfer(string):
    try:
        if float(string) == float(int(float(string))):
            return int(string)
        else:
            return float(string)
    except:
        pass
    return True if string.lower() == 'true' else (False if string.lower() == 'false' else string)



# 2.[dict{info}]转Json
def Convert2Json(data, Img_Path, json_file):
    # 初始化
    json_dict = {"images": [],  "type": "instances",  "annotations": [],  "categories": []}
    bnd_id = 1
    # 解析CSV_list:
    for index, line in enumerate(data):
        # print("Processing %s"%(line))
        # 查询Images信息
        image_id = line['imageid']              # int—获取图片编号==图片名
        filename = str(image_id) + '.jpg'       # str
        # Get图片の宽和高
        width, height = imagesize.get(Img_Path + filename)      # width, height = 2448, 3264
        # images写入字典
        image = {'file_name': filename, 'height': height, 'width': width, 'id': image_id}
        json_dict['images'].append(image)


        #  用于图像分割中的类型选择[ignore]
        segmented = None;   assert segmented is None
        # 当前标注框的类别:0~1222
        category_id = line['classid']
        # 标注框[lx,ty, weigh, height]
        o_width = abs(line['rx'] - line['lx'])
        o_height = abs(line['by'] - line['ty'])
        # annotations写入JSON:
        ann = {'area': o_width * o_height, 'image_id': image_id,
               'bbox': [line['lx'], line['ty'], o_width, o_height],
               'category_id': category_id, 'id': bnd_id, 'ignore': 0,
               'segmentation': None, 'iscrowd': None}
        json_dict['annotations'].append(ann)
        bnd_id = bnd_id + 1

    with open(json_file, mode='w', encoding='utf-8') as fp:
        json_str = json.dumps(json_dict)        # dumps：将python对象编码成Json字符串
        fp.write(json_str)

    print("------------create {} done--------------".format(json_file))




if __name__ == '__main__':
    Path = r'DataLoad/GroziImg/grozi.csv'  # 示例文件
    img_path = r'./DataLoad/GroziImg/ImageSets/'      # 图片数据文件夹的地址，for获取图片宽高
    # 生成的_json文件
    save_json_train = './DataLoad/GroziImg/instances_train2017.json'
    save_json_val = './DataLoad/GroziImg/instances_val2017.json'

    # 1. 读入CSV数据标注
    CSV_list = ReadFile(filePath=Path)         # return data->CSVdata

    # 2.传入CSV_list=[dict], 写入json_file
    Convert2Json(data=CSV_list, Img_Path=img_path, json_file=save_json_val)





