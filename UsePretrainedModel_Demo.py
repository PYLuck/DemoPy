# torchvison中已有的预训练模型

import torchvision.models as models
import torch



def Load_models(model_list=None, model_path=None):
    if model_list is None:
        model_list = ['squeezenet1_0', 'shufflenetv2_x1', 'inception_v3']
    squeezenet1_0 = models.squeezenet1_0(pretrained=False)
    shufflenetv2_x1 = models.shufflenet_v2_x1_0(pretrained=False)
    inception_v3 = models.inception_v3(pretrained=False)

    all_names = {}
    for model_name in model_list:
        model = eval(model_name)
        model.load_state_dict(torch.load(model_path + model_name+'.pth'), strict=True)
        model.eval().to('cuda')

        with torch.no_grad():
            model.fc = torch.nn.Linear(2048, 2048)
            torch.nn.init.eye_(model.fc.weight)
            torch.nn.init.zeros_(model.fc.bias)
            for param in model.parameters():
                param.requires_grad = False

            all_names[model_name] = model

    return all_names




if __name__ == '__main__':
    save_path = '/data/sda1/Download_sda1/'
    myModel_dict = Load_models(model_list=['squeezenet1_0', 'shufflenetv2_x1', 'inception_v3'], model_path=save_path)
    print(myModel_dict.keys())
    # 取值: 按字典中对应的模型名 取 model
    print(myModel_dict['squeezenet1_0'])

