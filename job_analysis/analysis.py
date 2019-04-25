# 曲线图
import matplotlib.pyplot as plt
import pandas

data = pandas.read_csv('./results/zhi_lian.csv', encoding='utf-8', lineterminator='\r')
salary = data['salary']
condition1 = salary != '薪资面议'
condition2 = pandas.notnull(salary)
condition3 = condition1 & condition2
data = data[condition3]['salary']
print(data.index)
data.loc[data['Y'] == 'T']
for x in data.index:

    print(data[x].split('-')[0])
d = data[0:12]

# 指定横坐标和纵坐标数据(多次指定绘制多条线)
# plt.plot(d['work_year'], d['salary'], c="red", )
#
# # 横坐标说明
# plt.xlabel('year')
# # 纵坐标说明
# plt.ylabel('salary')
# # 标题
# plt.title('-------')
# # 绘制
# plt.show()

plt.show()
