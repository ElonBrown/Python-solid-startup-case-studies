"""
    作者：ElonBrown
    功能：模拟掷骰子
    日期：2017/10/5
    版本：3.0
    2.0新增功能：模拟投掷两个骰子
    3.0新增功能：可视化投掷两个骰子的结果
"""
import random
import matplotlib.pyplot as plt


def roll_dice():
    """
        模拟掷骰子
    """
    roll = random.randint(1, 6)
    return roll


def main():
    """
        主函数
    """
    total_times = 100

    # 初始化列表 [0, 0, 0, 0, 0, 0]
    result_list = [0] * 11

    # 初始化点数列表
    roll_list = list(range(2, 13))
    roll_dict = dict(zip(roll_list, result_list))

    # 记录骰子的结果
    roll1_list = []
    roll2_list = []

    for i in range(total_times):
        roll1 = roll_dice()
        roll2 = roll_dice()

        roll1_list.append(roll1)
        roll2_list.append(roll2)

        for j in range(2, 13):
            if (roll1 + roll2) == j:
                roll_dict[j] += 1

    for i, result in roll_dict.items():
        print('点数{}的次数：{}，频率：{}'.format(i, result, result / total_times))

    # 数据可视化
    x = range(1, total_times + 1)
    plt.scatter(x, roll1_list, c='red', alpha=0.5)
    plt.scatter(x, roll2_list, c='green', alpha=0.5)
    plt.show()


if __name__ == '__main__':
    main()
