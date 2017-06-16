# 基于Arduino和Raspberry Pi的智能家居控制系统 API SDK

## 设备列表:
### 0:红外发射器(Emitter)
- (0,1): 温度

- (0,2): 模式

- (0,3): 风速

- (0,4): 电源

### 1:继电器(Relay) 
- (1,1): 继电器1状态

- (1,2): 继电器2状态

### 2:传感器(Sensor) 
- (2,1): 雨水

- (2,2): 红外

- (2,3): 门磁

- (2,4): PM2.5

- (2,5): 温度

## 使用方法：

    from api import get_status, patch_status, create_emitter, create_relay, create_sensor, delete_device  # 调用SDK

### 获取设备状态:

    get_status(type_id, device_id)  # type_id:设备类型 device_id:设备id
    TMP = get_status(2, 5)  # 读取温度传感器状态
    print(TMP)  # 显示获取到的传感器温度
### 修改设备状态:

    patch_status(type_id, device_id, data)  # type_id:设备类型 device_id:设备id data:设备数据 返回值为HTTP状态码
    print(patch_status(2, 5, 29))  # 推送温度传感器状态并显示返回状态码 返回状态码200即修改成功
### 增加新设备:  


    ID = create_emitter("Function", data)  # fucntion:发射器功能描述 data:设备初始状态 返回新创建设备ID
    create_relay(data)  # data:继电器初始状态
    create_sensor("name", data)  # name:传感器描述 data:传感器初始状态
### 删除设备:
    delete_device(type_id, device_id)  # 删除指定的设备
    
    

