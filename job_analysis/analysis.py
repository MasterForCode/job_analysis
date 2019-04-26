# 曲线图
import matplotlib.pyplot as plt
import pandas

original_data = pandas.read_csv('./results/zhi_lian.csv', encoding='utf-8', lineterminator='\r')
salary = original_data['salary']
condition1 = salary != '薪资面议'
condition2 = pandas.notnull(salary)
condition3 = condition1 & condition2
valid_salary = salary[condition3]
valid_data = original_data[condition3]
# print(valid_data['salary'])
cleaned_salary = []
for x in valid_salary:
    cleaned_salary.append(x.split('-')[0])
valid_data.drop(labels=['salary'], axis=1)
cleaned_data = pandas.concat([valid_data, pandas.DataFrame({'salary': cleaned_salary})])
print(cleaned_data)
# 指定横坐标和纵坐标数据(多次指定绘制多条线)
plt.plot(cleaned_data['work_year'], cleaned_data['salary'], c="red", )
#
# # 横坐标说明
plt.xlabel('year')
# # 纵坐标说明
plt.ylabel('salary')
# # 标题
plt.title('-------')
# 保存结果图片
plt.savefig('test.png')
# # 绘制
plt.show()

