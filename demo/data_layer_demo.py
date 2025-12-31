# 数据层 Demo
# 演示如何使用 vnpy 获取和处理市场数据

from vnpy.trader.engine import MainEngine
from vnpy.app.data_recorder import DataRecorderApp

# 初始化主引擎
engine = MainEngine()

# 添加数据录制应用
data_recorder = DataRecorderApp()
engine.add_app(data_recorder)

# 连接数据源 (示例：CTP 接口)
# engine.connect("CTP", {})

# 启动数据录制
# data_recorder.start_recording("IF888", "1m")

print("数据层 Demo: 数据录制已启动")