"""
    作者：ElonBrown
    功能：汇率兑换
    版本：1.0
    日期：2017/10/3
"""
# 汇率
USD_VS_RMB = 6.77

# 人民币的输入
rmb_str_value = input('请输入人民币金额：')
# 字符串转换为数字
rmb_value = eval(rmb_str_value)

#输出结果
print('美元金额是：', rmb_value / USD_VS_RMB)
