# quant_whale

![量化框架](./images/量化框架.png)

## 项目设计方案

本项目是一个基于 XtQuant + vn.py + miniQMT 的多人协作量化平台，旨在提供高效、灵活的量化交易解决方案。

## 一、整体架构设计

采用模块化微服务架构，分为数据层、策略层、交易层、风控层。以下结合 vnpy 框架详细说明各个模块：

### 数据层

**功能描述**：负责市场数据的获取、存储、处理和分发。支持实时数据流和历史数据回测。

**vnpy 对应模块**：
- `vnpy/trader/engine.py`：数据引擎 (DataEngine)
- `vnpy/app/data_recorder`：数据录制应用
- `vnpy/api`：各种数据接口 (如 Tushare, RQData 等)

### 策略层

**功能描述**：策略的开发、测试和执行。支持多种策略类型，如 CTA、期权等。

**vnpy 对应模块**：
- `vnpy/trader/strategy.py`：策略基类
- `vnpy/app/cta_strategy`：CTA 策略应用
- `vnpy/app/cta_backtester`：策略回测引擎

### 交易层

**功能描述**：订单生成、执行和监控。集成 XtQuant 和 miniQMT 接口。

**vnpy 对应模块**：
- `vnpy/trader/engine.py`：交易引擎 (MainEngine)
- `vnpy/gateway`：交易网关 (如 CTP, XTP 等)
- `vnpy/api/xtp`：XtQuant 接口 (如果支持)

### 风控层

**功能描述**：实时监控交易风险，包括仓位控制、止损等。

**vnpy 对应模块**：
- `vnpy/trader/risk_manager.py`：风险管理器
- `vnpy/app/risk_manager`：风险管理应用

## vnpy 集成

本项目集成了 [vnpy](https://github.com/vnpy/vnpy) 框架。vnpy 是一个基于 Python 的开源量化交易平台开发框架，由国内社区驱动，支持多种交易接口和策略开发。