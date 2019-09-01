
# import random
#
# menu= """"
# (0)石头
# (1)剪刀
# (2)布
# (q)游戏结束
# """
# all_list =["石头","剪刀","布"]
# y =input(menu)
# c = random.choice(all_list)
#
# if y in ["0","1","2","q"]:
#     if y == "q":
#         print("游戏结束！")
#     else:
#         you =all_list[int(y)]
#         if you == c:
#             print("平局")
#         elif (you=="石头"and c=="剪刀") or (you == "剪刀"and c=="布")or (you == "布"and c=="剪刀"):
#             print("你赢了")
#         else:
#              print("电脑赢了")
# else:
#     print("输入错误")

# import random
#
# menu="""
# (0)石头
# (1)剪刀
# (2)布
# (q)q
# """
# all_list = ["石头","剪刀","布"]
# c = random.choice(all_list)
# y = input(menu)
# win_list = [["石头","剪刀"],["剪刀","布"],["布","石头"]]
# if y in ["0","1","2","q"]:
#     if y == "q" :
#         print("游戏结束")
#     else:
#         you = all_list[int(y)]
#         if you == c:
#             print("平局")
#         elif [you,c] in win_list:
#             print("你赢")
#         else:
#             print("电脑赢")
# else:
#     print("输入无效")
# all_list = ["石头","剪刀","布"]
# c= random.choice(all_list)
# y =input(menu)
# win_list = [["石头","剪刀"],["剪刀","布"],["布","石头"]]
# if y in ["0","1","2","q"]:
#     if y== "q":
#         print("退出")
#     else :
#         you=all_list[int(y)]
#         if you==c:
#             print("平局")
#         elif [you, c] in win_list:
#             print("你赢")
#         else:
#             print("电脑赢")
# else:
#     print("输入无效")

# import random　　　引入模块
# str = "0123456789abcdefghigklmnopqrstuvwxyz_"   字符串集合
# n=int(input("请输入密码位数"))　　　定义ｎ输出“提示性字符串‘
# i=1　　　　　　　　　　　　　　　　　　　定义ｉ值变量
# pwd = ''　　　　　　　　　　　　　　　　　定义密码为空　　原始密码
# while i <= n:　　　　　　　　　　　　　　　　　执行ｗｈｉｌｅ　循环　　　
#     a=random.choice(str)　　　　　　　　　　　在集合中随机寻去一位数　　ｒａｎｄｏｍ.choice()
#     pwd=pwd + a                          定义新的密码赋值数字的拼接
#     i+=1　　　　　　　　　　　　　　　　　　　ｉ进行ｉ＋１操作
# print(pwd)　　　　　　　　　　　　　　　　　　　打印

#
# i=1
# n=int(input("输入数："))
# su=range(1,n+1)
# while i <= n:
#     i=i+1
#     su=su+1
#     print(su)

#
# i=1
# n=int(input("输入一个整数ｎ"))　　　　　　　输出１——你　　除去　　３的倍数
# while i <= 10:
#     if i % 3 == 0:　　　　　　　
#         i+=1
#         continue           contiue 语句　　返回执行ｗｈｉｌｅ　不执行下面的代码　　和ｉｆ语法一起使用  不执行
# 　　　　　　　　　　　　　　　　　ｐｒｉｎｔ的代码　　就是　ｃｏｎｔｉｎｕｅ的意思
#     print(i)
#     i=i+1


# i=1
# n=int(input("输入一个整数"))
# while i < n :
#     i+=1           定义ｉ＋１
#     if i % 3 == 0 :　　求余数
#         continue　　　语法　返回ｗｈｉｌｅ　　不执行   ｐｒｉｎｔ
#     print(i)

count=0
str=input("输入一个字符串")
for i in str:
    if i == " ":
        count+=1
print(count)









    



