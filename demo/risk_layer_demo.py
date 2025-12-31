# 风控层 Demo
# 演示风控规则的设置和监控

from vnpy.trader.risk_manager import RiskManager

class CustomRiskManager(RiskManager):
    """自定义风险管理器"""

    def __init__(self):
        super().__init__()
        self.max_position = 100  # 最大持仓
        self.max_loss = 10000   # 最大亏损

    def check_risk(self, order):
        """检查订单风险"""
        # 检查持仓限制
        if abs(order.volume) > self.max_position:
            return False, "超过最大持仓限制"

        # 检查亏损限制
        # (需要实现亏损计算逻辑)

        return True, ""

# 初始化风控管理器
risk_manager = CustomRiskManager()

# 示例：检查订单
# order = OrderData(...)
# is_valid, msg = risk_manager.check_risk(order)
# if not is_valid:
#     print(f"风控拒绝: {msg}")

print("风控层 Demo: 自定义风险管理器已定义")