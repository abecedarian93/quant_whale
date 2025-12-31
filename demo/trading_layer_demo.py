# 交易层 Demo
# 演示订单提交和执行

from vnpy.trader.engine import MainEngine
from vnpy.trader.object import OrderData, Direction, Offset

# 初始化主引擎
engine = MainEngine()

# 连接交易网关 (示例：CTP)
# engine.connect("CTP", {})

# 提交订单
def submit_order(symbol, direction, offset, price, volume):
    """提交订单"""
    order = OrderData(
        symbol=symbol,
        direction=direction,
        offset=offset,
        price=price,
        volume=volume
    )
    engine.send_order(order)
    return order

# 示例：买入开仓
# order = submit_order("IF888", Direction.LONG, Offset.OPEN, 4000, 1)
# print(f"订单已提交: {order.vt_orderid}")

print("交易层 Demo: 订单提交函数已定义")