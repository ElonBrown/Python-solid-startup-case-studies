"""
    作者：ElonBrown
    功能：汇率兑换
    版本：2.0
    日期：2017/10/3
    2.0 新增功能：根据输入判断是人民币还是美元
"""
# 汇率
USD_VS_RMB = 6.77

# 带单位的货币金额输入
currency_str_value = input('请输入带单位的货币金额：')

# 获取货币单位
unit = currency_str_value[-3:]

if unit == 'CNY':
    # 人民币转换美元
    rmb_str_value = currency_str_value[:-3]
    # 字符串转换为数字
    rmb_value = eval(rmb_str_value)
    # 输出结果
    print('美元金额是：', rmb_value / USD_VS_RMB)

elif unit == 'USD':
    # 美元转换人民币
    usd_str_value = currency_str_value[:-3]
    # 字符串转换为数字
    usd_value = eval(usd_str_value)
    # 输出结果
    print('人民币金额是：', usd_value * USD_VS_RMB)

else:
    # 其他情况
    print('本版本尚不支持')
