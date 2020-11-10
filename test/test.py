
#第一个注释
#print ("Hello  Python!")

# !/usr/bin/python3

#input("\n\n按下 enter 键后退出。")


# !/usr/bin/python3

#import sys;

"""x = 'runoob';
sys.stdout.write(x + '\n')"""

# !/usr/bin/python3

#x = "a"
#y = "b"
# 换行输出
#print(x)
#print(y)

#print('---------')
# 不换行输出
#print(x, end=" ")
#print(y)

#print('---------')
#!/usr/bin/python3

#str = 'Runoob'

#print (str)          # 输出字符串
#print (str[0:-1])    # 输出第一个到倒数第二个的所有字符
#print (str[0])       # 输出字符串第一个字符
#print (str[2:5])     # 输出从第三个开始到第五个的字符
#print (str[2:])      # 输出从第三个开始的后的所有字符
#print (str * 2)      # 输出字符串两次，也可以写成 print (2 * str)
#print (str + "TEST") # 连接字符串

# print('---------')
#
# def reverseWords(input):
#     # 通过空格将字符串分隔符，把各个单词分隔为列表
#     inputWords = input.split(" ")

    # 翻转字符串
    # 假设列表 list = [1,2,3,4],
    # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
    # inputWords[-1::-1] 有三个参数
    # 第一个参数 -1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1 表示逆向
#     inputWords = inputWords[-1::-1]
#
#     # 重新组合字符串
#     output = ' '.join(inputWords)
#
#     return output
#
#
# if __name__ == "__main__":
#     input = 'I like runoob'
#     rw = reverseWords(input)
#     print(rw)
#
# print('---------')
#
# #!/usr/bin/python3
#
# tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )
# tinytuple = (123, 'runoob')
#
# print (tuple)             # 输出完整元组
# print (tuple[0])          # 输出元组的第一个元素
# print (tuple[1:3])        # 输出从第二个元素开始到第三个元素
# print (tuple[2:])         # 输出从第三个元素开始的所有元素
# print (tinytuple * 2)     # 输出两次元组
# print (tuple + tinytuple) # 连接元组

# print(3+2)
# print("我喜欢用Python")
# print('@@@')
# print( "Hello Python" )
# print("Hello IMOOC")

#用一行代码输出来慕课网学习python跳槽加薪必备，并分三行
# print("来慕课网\n学习python\n跳槽加薪必备")

# my_name="liuwei"
# my_age=18
# my_sex=True
# print("My name is",my_name,"My age is",my_age,"My sex is",my_sex)
#
# print(type(my_name),type(my_age),type(my_sex))

# m=10
# n=5
# m+=3
# n+=5
# #求m和n的平均值
# averageResult=(m+n)/2
# #求m的平方乘以n的平方
# productresult=m**2+n**2
# print("平均值：",averageResult,"平方乘积：",productresult)

# name=input("请输入你的姓名：")
# CID=input("请输入身份证号：")
# id =int(CID)
# print(type(CID),CID, name)
# print(type(id),id, name)

# strText="Hello"
# strInt=2020
# resultstr=strText+str(strInt)
# print(resultstr)
#
#
# date = input("请输入日期")
# str1=" Welcom to imooc"
# str2=" Imooc's URL is https://www.imooc.com/"
# #定义变量str3拼接date、str1、str2
# str3 = date +str1+str2
# print(str3)

# art="bmw"
# print(art.upper())

#print("{}{}you".format("I","love"))


# name="小明"
# age=25
# height=180.5
#
# str1="我叫{}，今年{}，身高{}".format(name,age,height)
# print(str1)
#
# str2="我叫{0},身高{1}，今年{2}".format(name,age,height)
# print(str2)
#
# str3="我叫{p1},身高{p2}，今年{p3}".format(p1=name,p3=age,p2=height)
# print(str3)

#
# print(format(123.4537,'0.2f'))
#
# print(format(1234567,','))

# print("姓名\t性别\t年级\n赵四\t男\t三年级")

# str1="   imooc  "
# lenstr=len(str1)
# print("字符串：",str1,"长度：",lenstr)
# str2=str1.strip()
# lenstr2=len(str2)
# print("字符串：",str2,"长度：",lenstr2)

# str="imooc"
# print(str.find("o"))
# str1=str.replace("o","i",1)
# print(str1)

# year=input("请输入正确的年份：")
# if(int(year)%4==0 and (int(year)%100)!=0 and int(year)%400==0):
#     print("{y}年是闰年".format(y=year))
# else:
#     print("{y}年不是闰年".format(y=year))

# num=int(input("请输入一个三位数："))
# bw=num//100
# sw=(num%100)//10
# gw=num%10
# total=bw**3+sw**3+gw**3
#
# if total == num:
#     print("yes")
# else:
#     print("no")

# if 1!=1:
#     print("1等于1")
# else:
#     print("1不等于1")
#
# b=1==1
#
# print(b)
# print(1==1.0)

# num=input("请输入一个数字：")
# print(type(num))
# print(num%2==0)
# print(num%2!=0)
# if num%2==0:
#     print("这是一个整数")
# elif num%2!=0:
#     print("不是整数")
# else:
#     print("请输入正确的数字！")

#综合训练，血压评估
# high=input("请输入您测量的高亚值：")
# low=input("请输入您测量的低压值：")
# high=int(high)
# low=int(low)
# '''
# if(low>60 and low <90) and(high>90 and high<140):
#     print("您的血压正常，请继续保持健康的生活习惯！")
# else:
#     print("您的血压出现异常，请尽快就医")
# '''