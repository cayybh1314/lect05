"""
    作者：赵钦超
    功能：52周存钱挑战
    版本: 1.0
    日期: 20/04/2019
"""

def main():
    """
        主函数
    """
    money_per_week = 10   #每周存入的金额
    i = 1                 #记录周数
    increase_money = 10   #递增的金额
    total_week = 52       #总的周数
    saving = 0            #账户累计

    while i <= total_week:
        #存钱操作
        #saving = saving + money_per_week
        saving += money_per_week

        #输出每周存钱数额
        print("第{}周，存储账户{}块钱，账户累计{}块钱".format(i,money_per_week,saving))

        #更新下周存钱数额
        #money_per_week = money_per_week + increase_money
        money_per_week += increase_money
        i += 1


if __name__ == '__main__':
    main()