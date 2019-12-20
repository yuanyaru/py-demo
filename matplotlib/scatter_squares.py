# -*- encoding:utf-8 -*-

import matplotlib.pyplot as plt

# 绘制单个点
# plt.scatter(2, 4, s=200)

# 绘制一系列点
# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]

# 自动计算数据
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
# 默认为蓝色点，黑色轮廓。此处删除数据点的轮廓
# plt.scatter(x_values, y_values, c='red', edgecolor='none', s=40)
# RGB颜色模式自定义颜色，元组内3各小数值分别代表红、绿、蓝分量
# plt.scatter(x_values, y_values, c=(0, 0, 0.8), edgecolor='none', s=40)
# 使用颜色映射
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=40)

# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

# plt.show()
# 自动保存图表
plt.savefig('squares_plot.png', bbox_inches='tight')
