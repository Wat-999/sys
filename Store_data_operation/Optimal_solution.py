#实现思路
#1梳理任务条件，转变成数学表达式
#2分别计算渠道和品类投放预算的最优解
#3计算各个品类在不同渠道投放预算的最优解
"""
做推广方案其实是运筹学中的求最优解问题，运用运筹学的知识可以制定出最佳的投放方案。
如果这个月老板给你1千万的推广预算，让你给分配到各个渠道和品类，要确认分配比例，可以让这1千万的效果最大化。

已知条件，该企业有4个主要渠道，分别是电商站、某音、某度和线下。
电商站不能少于1百万的投入，投入产出比（ROI）是1.5
某音不能高于3百万的投入，投入产出比是2
某度不能少于2百万的投入，投入产出比是0.7
线下不能低于1百万的投入，投入产出比是0.1

共有5个主要品类，分别为服装、家电、百货、美妆和餐饮具
服装不能少于100万的投入，ROI是1.2
家电不能高于300万的投入，ROI是2
百货不能少于100万的投入，ROI是1.4
美妆不能高于350万的投入，ROI是1.5
餐饮不能少于50万的投入，ROI是0.8

请把1千万的推广预算合理地分配到各个渠道和品类
要明确到某个品类要在某个渠道中投放多少预算。
"""

from scipy.optimize import linprog

"""
渠道投入分布
设X_1为电商站的广告投入，X_2为某音的广告投入，X_3为某度的广告投入，X_4为线下的广告投入，设z为总效益。
有以下公式：
①max z = 1.5X_1 + 2X_2 + 0.7X_3 + 0.1X_4
②X_1 + X_2 + X_3 + X_4 = 1000
③X_1 >= 100
④X_2 <= 300
⑤X_3 >= 200
⑥X_4 >= 100
"""
#linprog()函数用于求最小值，现在要求解最大值，只需要对目标函数取负，求解的最终值是取负后的目标函数的最小值，取负即为最大值。
#如果原方程中存在负数的系数，那么取负后是负负得正

#设置公式的系数，注意求解最大值时系数前要加负号
c1 = [-1.5, -2, -0.7, -0.1]  #①
A_eq1 = [[1, 1, 1, 1]]       #②
#各参数的限制条件
b_eq1 = [1000]
x1 = (100, 1000)
x2 = (0, 300)
x3 = (200, 1000)
x4 = (100, 1000)
res1 = linprog(c1, A_eq=A_eq1, b_eq=b_eq1, bounds=(x1, x2, x3, x4))
# 获取全部x的值
x = res1.get('x') #get中的x为linprog函数当前解向量，即此函数解的值，数据类型为一维数组 x为最优解
#get()函数是根据键获取键对应的值
#round()没有加第二个参数时，默认为本身数据进行四舍五入保留整数
# 渠道投产最大值
fu1 = abs(round(res1.get('fun'))) #get中的fun为linprog函数中目标函数的当前值即解，数据类型为浮点型；fun为目标函数的最大值
# 电商站投入份额
x_1 = round(x[0])
# 某音投入份额
x_2 = round(x[1])
# 某度投入份额
x_3 = round(x[2])
# 线下投入份额
x_4 = round(x[3])

print('品类投产最大值:', fu1)
print('电商站投入份额:', x_1)
print('某音投入份额:', x_2)
print('某度投入份额:', x_3)
print('线下投入份额:', x_4)
print('===================================================================')
"""
品类投入分布
设Y_1为服装的广告投入，Y_2为家电的广告投入，Y_3为百货的广告投入，Y_4为美妆的广告投入，Y_5为餐饮的广告投入，设z为总效益。
有以下公式：
①max z = 1.2Y_1 + 2Y_2 + 1.4Y_3 + 1.5Y_4 + 0.8Y_5
②Y_1 + Y_2 + Y_3 + Y_4 + Y_5 = 1000
②Y_1 >= 100
④Y_2 <= 300
⑤Y_3 >= 100
⑥Y_4 <= 350
⑦Y_5 >= 50
"""

c2 = [-1.2, -2, -1.4, -1.5, -0.8]
A_eq2 = [[1, 1, 1, 1, 1]]
b_eq2 = [1000]
y1 = (100, 1000)
y2 = (0, 300)
y3 = (100, 1000)
y4 = (0, 350)
y5 = (50, 1000)
res2 = linprog(c2, A_eq=A_eq2, b_eq=b_eq2, bounds=(y1, y2, y3, y4, y5))
# 获取全部y的值
y = res2.get('x')
# 品类投产最大值
fun2 = abs(round(res2.get('fun')))
# 服装投入份额
y_1 = round(y[0])
# 家电投入份额
y_2 = round(y[1])
# 百货投入份额
y_3 = round(y[2])
# 美妆投入份额
y_4 = round(y[3])
# 餐饮投入份额
y_5 = round(y[4])

print('品类投产最大值:', fun2)
print('服装投入份额:', y_1)
print('家电投入份额:', y_2)
print('百货投入份额:', y_3)
print('美妆投入份额:', y_4)
print('餐饮投入份额:', y_5)
print('===================================================================')
"""
    ======================================================
    =================计算各个品类在不同渠道的最优解==================
    ======================================================

"""
# 获取最小值
def least(num1, num2):
    lea = 0
    if num1 <= num2:
        lea = num1
    else:
        lea = num2
    return lea

"""
合并渠道和品类的投入份额
获取每个品类在各个渠道投入的份额
设a1为服装在电商站的广告投入，a2为服装在某音的广告投入，a3为服装在某度的广告投入，a4为服装在线下的广告投入,
设b1为家电在电商站的广告投入，b2为家电在某音的广告投入，b3为家电在某度的广告投入，b4为家电在线下的广告投入,
设c1为百货在电商站的广告投入，c2为百货在某音的广告投入，c3为百货在某度的广告投入，c4为百货在线下的广告投入,
设d1为美妆在电商站的广告投入，d2为美妆在某音的广告投入，d3为美妆在某度的广告投入，d4为美妆在线下的广告投入,
设e1为餐饮在电商站的广告投入，e2为餐饮在某音的广告投入，e3为餐饮在某度的广告投入，e4为餐饮在线下的广告投入,
设z为总效益。
有以下公式：
①Max z = 1.8a1 + 2a2 + 0.84a3 + 0.12a4
        + 3b1 + 4b2 + 1.4b3 + 0.2b4
        + 2.1c1 + 2.8c2 + 0.98c3 + 0.14c4
        + 2.25d1 + 3d2 + 1.05d3 + 0.15d4
        + 1.2e1 + 1.6e2 + 0.56e3 + 0.08e4
②a1 + a2 + a3 + a4 = 100
③b1 + b2 + b3 + b4 = 300
④c1 + c2 + c3 + c4 = 200
⑤d1 + d2 + d3 + d4 = 350
⑥e1 + e2 + e3 + e4 = 50
⑦a1 + b1 + c1 + d1 + e1 = 400
⑧a2 + b2 + c2 + d2 + e2 = 300
⑨a3 + b3 + c3 + d3 + e3 = 200
⑩a4 + b4 + c4 + d4 + e4 = 100
"""
#设置公式①的系数，注意求解最大值时系数前要加负号
c = [-1.8, -2, -0.84, -0.12, -3, -4, -1.4, -0.2, -2.1, -2.8, -0.98, -0.14, -2.25, -3, -1.05, -0.15, -1.2, -1.6, -0.56, -0.08]
cc = [1.8, 2, 0.84, 0.12, 3, 4, 1.4, 0.2, 2.1, 2.8, 0.98, 0.14, 2.25, 3, 1.05, 0.15, 1.2, 1.6, 0.56, 0.08] #原公式①的系数
#设置公式②～⑩的系数(注意：要对应在公式①的位置上，填写自身的系数)
A = [
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1]
     ]
b = [y_1, y_2, y_3, y_4, y_5, x_1, x_2, x_3, x_4]

a1 = (0, least(x_1, y_1))
a2 = (0, least(x_2, y_1))
a3 = (0, least(x_3, y_1))
a4 = (0, least(x_4, y_1))
b1 = (0, least(x_1, y_2))
b2 = (0, least(x_2, y_2))
b3 = (0, least(x_3, y_2))
b4 = (0, least(x_4, y_2))
c1 = (0, least(x_1, y_3))
c2 = (0, least(x_2, y_3))
c3 = (0, least(x_3, y_3))
c4 = (0, least(x_4, y_3))
d1 = (0, least(x_1, y_4))
d2 = (0, least(x_2, y_4))
d3 = (0, least(x_3, y_4))
d4 = (0, least(x_4, y_4))
e1 = (0, least(x_1, y_5))
e2 = (0, least(x_2, y_5))
e3 = (0, least(x_3, y_5))
e4 = (0, least(x_4, y_5))
res = linprog(c, A_eq=A, b_eq=b, bounds=(a1, a2, a3, a4, b1, b2, b3, b4, c1, c2, c3, c4, d1, d2, d3, d4, e1, e2, e3, e4))
z = res.get('x')
# 个品类在各个渠道投入的份额的投产最大值
fun = abs(round(res.get('fun')))
# 服装电商站投入份额
a_1 = round(z[0])
# 服装某音投入份额
a_2 = round(z[1])
# 服装某度投入份额
a_3 = round(z[2])
# 服装线下投入份额
a_4 = round(z[3])
# 家电电商站投入份额
b_1 = round(z[4])
# 家电某音投入份额
b_2 = round(z[5])
# 家电某度投入份额
b_3 = round(z[6])
# 家电线下投入份额
b_4 = round(z[7])
# 百货电商站投入份额
c_1 = round(z[8])
# 百货某音投入份额
c_2 = round(z[9])
# 百货某度投入份额
c_3 = round(z[10])
# 百货线下投入份额
c_4 = round(z[11])
# 美妆电商站投入份额
d_1 = round(z[12])
# 美妆某音投入份额
d_2 = round(z[13])
# 美妆某度投入份额
d_3 = round(z[14])
# 美妆线下投入份额
d_4 = round(z[15])
# 餐饮电商站投入份额
e_1 = round(z[16])
# 餐饮某音投入份额
e_2 = round(z[17])
# 餐饮某度投入份额
e_3 = round(z[18])
# 餐饮线下投入份额
e_4 = round(z[19])

print('每个品类在各个渠道投入的份额的投产最大值为:',fun)
print('服装投入份额渠道分布')
print('电商站投入份额:', a_1, '某音投入份额:', a_2, '某度投入份额:', a_3, '线下投入份额:', a_4)
print('家电投入份额渠道分布')
print('电商站投入份额:', b_1, '某音投入份额:', b_2, '某度投入份额:', b_3, '线下投入份额:', b_4)
print('百货投入份额渠道分布')
print('电商站投入份额:', c_1, '某音投入份额:', c_2, '某度投入份额:', c_3, '线下投入份额:', c_4)
print('美妆投入份额渠道分布')
print('电商站投入份额:', d_1, '某音投入份额:', d_2, '某度投入份额:', d_3, '线下投入份额:', d_4)
print('餐饮投入份额渠道分布')
print('电商站投入份额:', e_1, '某音投入份额:', e_2, '某度投入份额:', e_3, '线下投入份额:', e_4)