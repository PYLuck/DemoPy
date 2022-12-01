# 计算模型 推理时间  2种方法
"""
# 注意：在pytorch里面，程序的执行都是异步的。
torch.cuda.synchronize()
start = time.time()
result = model(input)
torch.cuda.synchronize()
end = time.time()
print('推理时间{}ms',end-start)     # 单位：秒

"""
import time

import torch
from torchvision.models.resnet import resnet18

device = torch.device("cuda:0")


# 测试方法1--time.time()秒：
def use_timeInfer(random_input, model,iters):
    _time = torch.zeros(iters)  # 存储每轮iteration的时间
    with torch.no_grad():
        for i in range(iters):
            torch.cuda.synchronize()
            start = time.time()
            _ = model(random_input)  # 推理
            torch.cuda.synchronize()
            end = time.time()

            _curr_time = end - start  # 计算时间
            _time[i] = _curr_time

    mean_time = _time.mean().item()
    print('推理时间： {:.4f} 毫秒'.format(mean_time*1000))  # time单位：s *1000 -> ms


# 测速方法2--torch.cuda.Event毫秒
def use_torchEventInfer(random_input, model, iters):
    starter, ender = torch.cuda.Event(enable_timing=True), torch.cuda.Event(enable_timing=True)

    _times = torch.zeros(iters)  # 存储每轮iteration的时间
    with torch.no_grad():
        for iter in range(iters):
            starter.record()
            _ = model(random_input)
            ender.record()
            torch.cuda.synchronize()  # torch是异步计算，需要同步GPU时间

            curr_time = starter.elapsed_time(ender)  # 计算时间
            _times[iter] = curr_time

    mean_time = _times.mean().item()
    print("Inference time: {:.4f} 毫秒, FPS: {} ".format(mean_time, 1000 / mean_time))


if __name__ == '__main__':

    model = resnet18()
    model.to(device)

    random_input = torch.randn(1, 3, 224, 224).to(device)

    # =================== GPU预热 =================================================
    starter, ender = torch.cuda.Event(enable_timing=True), torch.cuda.Event(enable_timing=True)
    starter.record()
    for _ in range(50):
        _ = model(random_input)
    ender.record()

    torch.cuda.synchronize()  # 同步GPU时间
    warm_up_time = starter.elapsed_time(ender)
    print("GPU warm up time:{:.2f}毫秒".format(warm_up_time))  # starter.elapsed_time单位：ms

    # ===========两种测速方法可选 =====================================
    iterations = 1000       # 重复计算的轮次,求平均
    # way1
    use_timeInfer(random_input, model, iterations)
    # way2
    use_torchEventInfer(random_input, model, iterations)
