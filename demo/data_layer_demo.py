# 数据层 Demo
# 演示如何使用 vnpy 基于 XtQuant 获取和处理市场数据

from datetime import datetime
from xtquant import xtdata
from vnpy.trader.datafeed import get_datafeed
from vnpy.trader.constant import Exchange, Interval
from vnpy.trader.object import HistoryRequest

# ================================
# 方式一：使用 xtquant 直接获取数据
# ================================

def get_data_with_xtquant():
    """使用 xtquant 直接获取市场数据"""
    print("=== 方式一：使用 xtquant 直接获取数据 ===")
    
    # 1. 下载历史数据
    stock_code = "600000.SH"  # 浦发银行
    start_time = "20240101"
    end_time = "20241231"
    
    # 下载日线数据
    print(f"下载 {stock_code} 的历史数据...")
    xtdata.download_history_data(stock_code, period="1d", start_time=start_time, end_time=end_time)
    
    # 2. 获取K线数据
    bars = xtdata.get_market_data(
        stock_list=[stock_code],
        period="1d",
        start_time=start_time,
        end_time=end_time,
        field_list=["open", "high", "low", "close", "volume"]
    )
    print(f"获取到 {len(bars)} 条K线数据")
    print(bars.head())
    
    # 3. 订阅实时行情（回调函数方式）
    def on_tick(data):
        """实时行情回调"""
        print(f"收到实时行情: {data}")
    
    # xtdata.subscribe_quote(stock_code, period="tick", callback=on_tick)
    # print(f"已订阅 {stock_code} 的实时行情")


# ================================
# 方式二：使用 vnpy datafeed 获取数据
# ================================

def get_data_with_vnpy_datafeed():
    """使用 vnpy datafeed 接口获取数据"""
    print("\n=== 方式二：使用 vnpy datafeed 获取数据 ===")
    
    # 1. 初始化数据服务
    datafeed = get_datafeed()
    datafeed.init()
    print("数据服务初始化完成")
    
    # 2. 创建历史数据请求
    req = HistoryRequest(
        symbol="600000",
        exchange=Exchange.SSE,
        start=datetime(2024, 1, 1),
        end=datetime(2024, 12, 31),
        interval=Interval.DAILY
    )
    
    # 3. 查询历史数据
    bars = datafeed.query_bar_history(req)
    print(f"查询到 {len(bars)} 条K线数据")
    if bars:
        print(f"第一条数据: {bars[0]}")


# ================================
# 方式三：下载指数成分股数据
# ================================

def download_index_components():
    """下载指数成分股数据"""
    print("\n=== 方式三：下载指数成分股数据 ===")
    
    # 1. 下载行业板块数据
    xtdata.download_sector_data()
    print("行业板块数据下载完成")
    
    # 2. 获取沪深300成分股
    index_code = "000300.SH"
    date = "20241231"
    
    stocks = xtdata.get_stock_list_in_sector(index_code, date)
    print(f"沪深300成分股数量: {len(stocks)}")
    print(f"前10只股票: {stocks[:10]}")
    
    # 3. 批量下载成分股数据
    print("批量下载成分股数据...")
    for stock in stocks[:5]:  # 仅下载前5只作为示例
        xtdata.download_history_data(stock, period="1d", start_time="20240101", end_time="20241231")
        print(f"  {stock} 数据下载完成")


# ================================
# 主函数
# ================================

if __name__ == "__main__":
    print("数据层 Demo: 基于 XtQuant 在 vnpy 中获取数据\n")
    
    # 运行示例（取消注释以运行）
    # get_data_with_xtquant()
    # get_data_with_vnpy_datafeed()
    # download_index_components()
    
    print("\n提示：请根据需要取消注释相应函数以运行示例")
    print("注意：需要先安装 xtquant 和 vnpy_xt: pip install xtquant vnpy_xt")