# 读写csv 、excel场景：文件读到变量，插入数据库；写，数据库信息导出。
# pip install pyexcel pyexcel-xls pyexcel-xlsx
#
from pyexcel_io import save_data
from pyexcel_io import get_data
from collections import OrderedDict

# 读
excel = get_data('6test.xlsx')
print(type(excel))
sheet1 = excel['Sheet1']
print(sheet1)   # [['id', 'name', 'password', 'role'], [1, '小明', 1111, '普通用户'], [2, 'admin', 'admin', '管理员']]
for index, row in enumerate(sheet1):
    if index == 0:  # 如果表头，注意隔过。如果有列合并，以第一列下标取值
        continue
    print(row)

# 写
sheet2 = [
    ['id', 'name', 'password', 'role'],
    [1, '小明', 1111, '普通用户'],
    [2, 'admin', 'admin', '管理员']
]
save_data(data=sheet2, afile='6write.xlsx')


# OrderedDict 有序字典。列表有下标有序，字典本身无序，但有些业务场景要求有序会用到orderDict
# {
#     'stu2': {}
#     'stu3': {}
#     'stu1'
# }