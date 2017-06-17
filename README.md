# 基于Arduino和Raspberry Pi的智能家居控制系统 API SDK

## 设备列表:
### 0:控制器(Controller)
- (0,0): 继电器0

- (0,1): 继电器1

- (0,2): 空调电源

- (0,3): 空调模式

- (0,4): 空调温度

- (0,5): 空调风速

### 1:传感器(Sensor) 
- (1,0): 雨水

- (1,1): PM2.5

- (1,2): 温度

## 安装方法:
    pip install requests
    git clone https://github.com/myloft/API-SDK.git

## 使用方法：

    from api import get_status, patch_status, create_device, delete_device  # 调用SDK

### 获取设备状态:

    get_status(type_id, device_id)  # type_id:设备类型 device_id:设备id
    TMP = get_status(1, 2)  # 读取温度传感器状态
    print(TMP)  # 显示获取到的传感器温度
    
### 修改设备状态:

    patch_status(type_id, device_id, status)  # type_id:设备类型 device_id:设备id status:设备状态 返回值:HTTP状态码
    print(patch_status(1, 2, 26))  # 推送温度传感器状态并显示返回状态码 返回状态码200即修改成功

### 增加新设备:  

    create_device(type_id, "name", status)  # type_id:设备类型 name:设备名 status:设备初始状态 返回值:新创建设备ID
    ID = create_device(0, "test", 0)  # 创建新的控制器test 初始值为0
    print(ID)  # 显示新控制器test的ID 

### 删除设备:

    delete_device(type_id, device_id)  # 删除指定的设备 返回值:HTTP状态码
    delete_device(0, ID)  # 删除控制器test 返回值:204成功
    

