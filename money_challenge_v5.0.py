"""
    作者：赵钦超
    功能：52周存钱挑战
    版本: 1.0
    日期: 20/04/2019
    2.0新增功能: 记录每周的存款数
    3.0新增功能：使用循环直接计数
    3.0新增功能：使用循环直接计数
    4.0增加功能：灵活设置每周的存款数，增加的存款数及存款周数
    5.0增加功能：根据用户输入的日期，判断是一年中的第几周，然后输出相应的存款金额
"""

import math
import datetime

#函数外的变量是全局变量，
saving = 0

def save_money_in_n_week(money_per_week,increase_money,total_week):
    """
        计算n周的存款金额
    """

    #函数内调用全局变量，需要用global关键字声明一下
    global  saving

    money_list = []  # 记录每周存款数的列表，   [] 代表空列表
    saved_money_list = [] #记录每周账户累计


    # while i <= total_week:
    # 使用for 替代 while 做循环，  for循环会遍历 in 后面的一个集合，天然的带有次数限定，while如果没有表达式判断相当于无限循环
    for i in range(total_week):
        # 存钱操作
        # saving = saving + money_per_week
        # saving += money_per_week

        money_list.append(money_per_week)
        saving = math.fsum(money_list)
        # saving计算完毕后每周会更新一个结果，使用append方法，吧新产生的结果追加到列表里。
        saved_money_list.append(saving)

        # 输出每周存钱数额
        #print("第{}周，存储账户{}块钱，账户累计{}块钱".format(i + 1, money_per_week, saving))

        # 更新下周存钱数额
        # money_per_week = money_per_week + increase_money
        money_per_week += increase_money
        # i += 1
    #return saving
    return saved_money_list

def main():
    """
        主函数
    """
    money_per_week = float(input("请输入每周存入的金额："))   #每周存入的金额
    #i = 1                 #记录周数
    increase_money = float(input("请输入递增的金额："))   #递增的金额
    total_week = int(input("请输入总的周数："))       #总的周数

    #week_num = int(input("请输入第几周："))


    input_date_str = input("请输入日期(yyyy/mm/dd)：")

    input_date = datetime.datetime.strptime(input_date_str,'%Y/%m/%d')

    week_num = input_date.isocalendar()[1]



    global saving #已经声明了变量属于全局变量
    # 函数内的变量，属于局部变量
    saving = 0            #账户累计

    #调用函数
    saved_money_list =  save_money_in_n_week(money_per_week,increase_money,total_week)
    #print("存款总额为：",saving)
    print("第{}周的存款:{}元".format(week_num,saved_money_list[week_num - 1]))


if __name__ == '__main__':
    main()