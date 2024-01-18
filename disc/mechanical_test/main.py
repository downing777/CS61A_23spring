import argparse
import torch
torch.cuda.is_available()
torch.cuda.set_device(-1)
parser = argparse.ArgumentParser()
parser.add_argument("--local_rank", default=1, type=int)
FLAGS = parser.parse_args()
local_rank = FLAGS.local_rank

torch.cuda.set_device(local_rank)

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
