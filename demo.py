"""API SDK Demo"""
# coding:utf-8
from api import get_status, patch_status, create_device, delete_device


# 0:controller 控制器 (0,0):继电器0 (0,1):继电器1 (0,2):空调电源 (0,3):空调模式 (0,4):空调温度 (0,5):空调风速
# 1:sensor 传感器 (1,0):雨水传感器 (1,1):PM2.5传感器 (1,2):温度传感器
# 访问 http://api.iloft.xyz/admin 查看设备最新列表或手动管理设备

patch_status(1, 2, 29)  # 推送温度传感器状态并返回状态码 返回200成功

TMP = get_status(1, 2)  # 读取温度传感器状态

print(TMP)  # 显示获取到的温度

ID = create_device(0, "test", 0)  # 创建新的控制器test 初始值为0 返回设备id

print(ID)  # 显示新创建的设备id

delete_device(0, ID)  # 删除刚创建的设备 返回204成功
