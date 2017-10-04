"""
    作者：ElonBrown
    功能：汇率兑换
    版本：4.0
    日期：2017/10/3
    2.0 新增功能：根据输入判断是人民币还是美元
    3.0 新增功能：程序一直运行，直到用户选择退出
    4.0 新增功能：将汇率兑换功能封装到函数中
"""


def convert_currency(im, er):
    # 汇率兑换函数
    out = im * er
    return out

# 汇率
USD_VS_RMB = 6.77

# 带单位的货币金额输入
currency_str_value = input('请输入带单位的货币金额(退出请输入Q)：')

# 获取货币单位
unit = currency_str_value[-3:]

if unit == 'CNY':
    # 人民币转换美元
    exchange_rate = 1 / USD_VS_RMB

elif unit == 'USD':
    # 美元转换人民币
    exchange_rate = USD_VS_RMB

else:
    # 其他情况
    exchange_rate = -1

if exchange_rate != -1:
    in_money = eval(currency_str_value[:-3])
    out_money = convert_currency(in_money, exchange_rate)
    print('兑换后的金额：',out_money)
else:
    print('本版本尚不支持')
