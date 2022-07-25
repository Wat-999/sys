import pandas as pd

#2客户基本数据分析处理、缺失值填补

F1_1 = pd.read_csv('workeddata/F1_1.csv')
#读取列
F1_2_1 = F1_1[['ID', 'F1.1', 'F1.2', 'F1.4', 'F1.5', 'F1.9', 'F1.15', 'F1.23', 'F1.24', 'F1.27', 'F1.35', 'F1.38', 'F1.39']]
#空值替换为0
F1_2_1 = F1_2_1.fillna(0)
#读取列
F1_2_2 = F1_1[['label', 'ID']]
#设置所需列的空值替换为均值
title = ['F1.3', 'F1.6', 'F1.7', 'F1.8', 'F1.10', 'F1.11', 'F1.12', 'F1.13', 'F1.14', 'F1.16', 'F1.17', 'F1.18', 'F1.19',
         'F1.20', 'F1.21', 'F1.22', 'F1.25', 'F1.26', 'F1.28', 'F1.29', 'F1.30', 'F1.31', 'F1.32', 'F1.33', 'F1.34', 'F1.36',
         'F1.37']
for t in title:
    #获取每一列的均值
    mean = F1_1[[t]].mean().values[0]
    #获取列
    null = F1_1[['ID', t]]
    #空值替换为均值
    null = null.fillna(mean)
    #根据用户ID合并特征
    F1_2_2 = F1_2_2.join(null.set_index('ID'), on='ID')
#根据用户ID合并表格
F1_2 = F1_2_1.join(F1_2_2.set_index('ID'), on='ID')
#计算所需列值除以该列的均值，结果替换该列的值
for t in list(F1_2):
    #跳过以下几列
    if t == 'ID' or t == 'label' or t == 'F1.38' or t == 'F1.39':
        continue #跳出循环，执行后面的
    mean = F1_2[[t]].mean().values[0]
    #列值/均值，然后赋值到原有列
    F1_2[t] = F1_2[t]/mean

F1_2 = F1_2[['label', 'ID', 'F1.1', 'F1.2', 'F1.3', 'F1.4', 'F1.5', 'F1.6', 'F1.7', 'F1.8', 'F1.9', 'F1.10',
             'F1.11', 'F1.12', 'F1.13', 'F1.14', 'F1.15', 'F1.16', 'F1.17', 'F1.18', 'F1.19', 'F1.20', 'F1.21',
             'F1.22', 'F1.23', 'F1.24', 'F1.25', 'F1.26', 'F1.27', 'F1.28', 'F1.29', 'F1.30', 'F1.31', 'F1.32',
             'F1.33', 'F1.34', 'F1.35', 'F1.36', 'F1.37', 'F1.38', 'F1.39']]
#为相对路径
F1_2.to_csv('workeddata/F1_2.csv', index=False, encoding="utf_8_sig")
#print(F1_2)