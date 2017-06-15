"""TEST API"""
# coding:utf-8
from api import get_status, patch_status


# 0:emitter 红外发射器 (0,1):温度 (0,2):模式 (0,3):风速 (0,4):电源
# 1:relay 继电器 (1,1):继电器1状态 (1,2):继电器2状态
# 2:sensor 传感器 (2,1):雨水状态 (2,2):红外状态 (2,3):门磁状态 (2,4):PM2.5状态 (2,5):温度状态
# 访问 http://api.iloft.xyz/admin 手动添加删除设备

print(patch_status(2, 5, 29))  # 推送温度传感器状态并返回状态码 状态码200即成功

TMP = get_status(2, 5)  # 读取温度传感器状态

print(TMP)  # 显示获取到的温度
