# 公平席位分配函数
# 文档链接 https://www.cnblogs.com/zpfbuaa/p/5864594.html
# http://www.docin.com/p-1960382087.html?docfrom=rrela
import math

n = 4  # 总席位
a = 0.5
b = 0.39
c = 0.11
d = [a, b, c]  # 人员比例
f = []  # 分配席位
# 计算每个种类按照比例分成的向下取整值
for x in d:
    f.append(math.floor(x / sum(d) * n))
print('比例分配整数席位：            ', f)

# 分配资格
# 判断是否有未分到席位的种类
count = 0  # 判断次数
while 0 in f:
    # 当有未分到席位的种类时利用 D值法判断
    # 计算D值，最大D值类别增加一个席位，直到无没有席位的种类，或没有可分配席位
    count = count + 1  # 计算次数计数
    p1 = []  # D值公平系数存放
    for x in range(0, len(d)):  # 循环计算d值
        dz = d[x] / (f[x] + 1)
        p1.append(dz)  # 每次的d值
        p1_index = p1.index(max(p1))  # 最大值的索引
    f[p1_index] = f[p1_index] + 1  # 对应席位加一
    print('D值法第', count, '次剩余席位分配结果：', f, 'D值为：', p1)
    if sum(f) == n:  # 总数分配完，结束分配
        break

# 剩余席位分配
# 利用
count2 = 0
while sum(f) < n:  # 分配不完全时运行
    count2 = count2 + 1  # 计算次数计数
    p2 = []  # Q值公平系数
    for x in range(0, len(d)):  # 循环计算d值
        qz = d[x]**2 / (f[x] + 1) / f[x]
        p2.append(qz)  # 每次的d值
        p2_index = p2.index(max(p2))  # 最大值的索引
    f[p2_index] = f[p2_index] + 1  # 对应席位加一
    print('Q值法第', count2, '次剩余席位分配结果：', f, 'D值为：', p2)
    if sum(f) == n:  # 总数分配完，结束分配
        break

# 结果展示
renshu = []
xiwei = []
for x in range(0, len(d)):
    renshu.append(round(d[x] / sum(d), 2))
    xiwei.append(round(f[x] / sum(f), 2))
print('最终分配席位', f, '人数比例', renshu, '席位比例', xiwei)
