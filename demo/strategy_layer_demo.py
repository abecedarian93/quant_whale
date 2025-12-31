# 策略层 Demo
# 演示一个简单的均线交叉策略

from vnpy.app.cta_strategy import CtaStrategy
from vnpy.trader.object import BarData, TickData

class MaCrossStrategy(CtaStrategy):
    """均线交叉策略"""

    # 参数
    fast_window = 10
    slow_window = 20

    def __init__(self, cta_engine, strategy_name, vt_symbol, setting):
        super().__init__(cta_engine, strategy_name, vt_symbol, setting)

        # 变量
        self.fast_ma = 0
        self.slow_ma = 0

    def on_init(self):
        """策略初始化"""
        self.load_bar(10)

    def on_bar(self, bar: BarData):
        """K线数据更新"""
        # 计算均线
        fast_ma = bar.close_price.rolling(self.fast_window).mean()
        slow_ma = bar.close_price.rolling(self.slow_window).mean()

        if fast_ma > slow_ma:
            self.buy(bar.close_price, 1)
        elif fast_ma < slow_ma:
            self.sell(bar.close_price, 1)

# 使用示例
# strategy = MaCrossStrategy(cta_engine, "ma_cross", "IF888.CFFEX", {})
# cta_engine.add_strategy(strategy)

print("策略层 Demo: 均线交叉策略已定义")