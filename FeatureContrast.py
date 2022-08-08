# 图像相似度比较:模型-图像特征提取，比对数据
"""
参考人脸识别方法:
 Ref: https://blog.csdn.net/m0_38106923/article/details/83862334; http://dlib.net/; https://pypi.org/simple/dlib/
 dlib库：C++工具箱，包含机器学习算法和工具；For Win系统: 新版Dlib库下载后需要在本地编译。编译要用到软件CMake，CMake编译CPP源代码还需要C++编译器。
    对于Windows系统，C++编译器在Visual Studio里面集成，所以需要安装Visual Studio并配置C++编译环境。
    ubuntun环境：pip3 install cmake； dlib可用源码安装 Python setup.py install
    python3.6环境: pip install dlib==19.7.0

"""



import torch
import torchvision

from PIL import Image
from torchvision import transforms
from tqdm import tqdm

# class FaceVsimilarity():
#
#     def __init__(self, detector_path, face_rec_model_path, faces_folder_path, TestImg):
#         # 人脸关键点检测器
#         self.predictor_path = detector_path
#         # 人脸识别模型、提取特征值
#         self.face_rec_model_path = face_rec_model_path
#         # 训练图像文件夹
#         self.faces_folder_path = faces_folder_path
#
#         # 测试数据
#         self.TestImg = TestImg
#
#     def run(self):
#         # 加载模型
#         # detector = dlib.get_frontal_face_detector()
#         # sp = dlib.shape_predictor(self.predictor_path)
#         facerec = dlib.face_recognition_model_v1(self.face_rec_model_path)
#
#         candidate = []  # 存放训练集人物名字
#         descriptors = []  # 存放训练集图片特征列表
#
#         for f in glob.glob(os.path.join(self.faces_folder_path, "*.jpg")):
#             print("正在处理: {}".format(f))
#             img = io.imread(f)
#             candidate.append(f.split('\\')[-1].split('.')[0])
#             # 人脸检测
#             # dets = detector(img, 1)
#             for k, d in enumerate(dets):
#                 # shape = sp(img, d)
#                 # 提取特征
#                 face_descriptor = facerec.compute_face_descriptor(img, shape)
#                 v = numpy.array(face_descriptor)
#                 descriptors.append(v)
#
#         print('计算图片特征，并放到一个列表里面:识别训练完毕！')
#
#         try:
#             # test_path=input('请输入要检测的图片的路径（记得加后缀哦）:')
#             img = io.imread(self.TestImg)
#             dets = detector(img, 1)
#         except:
#             print('输入路径有误，请检查！')
#
#         dist = []
#         global Range;   Range = 0  # 测试人脸与训练数据之间的欧式距离
#         for k, d in enumerate(dets):
#             shape = sp(img, d)
#             face_descriptor = facerec.compute_face_descriptor(img, shape)
#             d_test = numpy.array(face_descriptor)
#
#
#             for i in descriptors:  # 计算距离
#                 dist_ = numpy.linalg.norm(i - d_test)
#                 dist.append(dist_)
#                 Range += dist_
#
#         print("测试图与训练数据的平均相似度",1-(Range/len(dist)))
#
#         # 训练集人物和距离组成一个字典
#         c_d = dict(zip(candidate, dist))
#         cd_sorted = sorted(c_d.items(), key=lambda d:d[1])
#
#         print("识别到的相似度最高的人物:{} ,相似度为{}".format(cd_sorted[0][0], 1-cd_sorted[0][1]))
#         print(cd_sorted)    # 距离值越小，相似度越高


class FeatureMatch:
    def __init__(self, model_path, path_to_data, path_to_query):
        # 识别模型、提取特征值
        self.rec_model_path = model_path
        # 上游图像文件：os2d—detected_Img
        self.path_to_data = path_to_data
        # 底库数据
        self.path_to_query = path_to_query
        # args:
        self.threshold = 0.5  # pick out if the cosine similarity > threshold.

    def _Run(self):
        # load model
        model = torchvision.models.detection.maskrcnn_resnet50_fpn(pretrained=False, pretrained_backbone=False)
        model.load_state_dict(
              torch.load(self.rec_model_path), strict=False)
        model.eval()

        # build dataloader
        preprocess = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])
        test_data = torchvision.datasets.ImageFolder(self.path_to_data, preprocess)
        image_names = test_data.samples
        data_loader = torch.utils.data.DataLoader(test_data, batch_size=1)

        # load model to GPU
        model.to('cuda')
        BATCH_SIZE = 1
        count = 0
        result = []

        # test and query
        with torch.no_grad():

            # load query image
            input_image = Image.open(self.path_to_query).convert('RGB')  # 底库图片
            input_tensor = preprocess(input_image)              # 预处理
            input_batch = input_tensor.unsqueeze(0)             # create a mini-batch as expected by the model
            input_batch = input_batch.to('cuda')

            # build feature extractor
            resnet50_feature_extractor = model
            resnet50_feature_extractor.fc = torch.nn.Linear(2048, 2048)  # 512,512 2048,1024 ...
            # the size varies for different models. Refer to official implementations for the size of feature maps

            # ---初始化fc：---
            torch.nn.init.eye_(resnet50_feature_extractor.fc.weight)        # 将二维tensor初始化为单位矩阵
            torch.nn.init.zeros_(resnet50_feature_extractor.fc.bias)
            for param in resnet50_feature_extractor.parameters():
                param.requires_grad = False  # 冻结R50参数
            # ---------------------

            # use_model提取特征————
            resnet50_feature_extractor = resnet50_feature_extractor.cuda()
            q_feature = resnet50_feature_extractor(input_batch)

            # use DataLoader———load os2detected—images
            for (x, y) in tqdm(data_loader, desc="Evaluating", leave=False):
                x = x.to('cuda')
                y = y.to('cuda')

                # extract fature
                output = resnet50_feature_extractor(x)
                print(output[0]['boxes'].shape)

                # 计算余弦相似度，计算哪个维度上的相似度？？
                similarity = torch.cosine_similarity(q_feature[0]['boxes'], output[0]['boxes'], dim=0)

                for index in range(output[0]['boxes'].shape):
                    if similarity[index] > self.threshold:
                        result.append(image_names[count * BATCH_SIZE + index][0])
                count += 1

        # print the results
        for r in result:
            print(r)


        similarity = 0
        return similarity, result


    # from shutil import copyfile
    # import os
    # os.makedirs(target_dir, exist_ok=True)
    # for r in result:
    #     copyfile(r, target_dir+'/'+r.split('/')[-1])




if __name__ == '__main__':
    # 识别模型、模型权重:  https://download.pytorch.org/models/resnet50-0676ba61.pth
    model_path = "/home/xk/下载/resnet50.pth"
    # 已检测图像文件夹
    path_to_data = "/home/xk/下载/detected_folder/"
    # 底库图片
    path2Query = "/home/xk/下载/my.png"

    Func = FeatureMatch(model_path, path_to_data, path2Query)
    Func._Run()


