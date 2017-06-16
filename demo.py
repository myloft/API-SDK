"""TEST API"""
# coding:utf-8
from api import get_status, patch_status, create_emitter, create_relay, create_sensor, delete_device


# 0:emitter 红外发射器 (0,1):温度 (0,2):模式 (0,3):风速 (0,4):电源
# 1:relay 继电器 (1,1):继电器1状态 (1,2):继电器2状态
# 2:sensor 传感器 (2,1):雨水状态 (2,2):红外状态 (2,3):门磁状态 (2,4):PM2.5状态 (2,5):温度状态
# 访问 http://api.iloft.xyz/admin 具体查看设备列表

print(patch_status(2, 5, 29))  # 推送温度传感器状态并返回状态码 返回200成功

TMP = get_status(2, 5)  # 读取温度传感器状态

print(TMP)  # 显示获取到的温度

ID = create_emitter("test", 0)  # 创建新的红外发射功能test 初始值为0 返回设备device_id

print(ID)  # 显示创建的设备device_id

print(delete_device(0, ID))  # 删除刚创建的设备 返回204成功
