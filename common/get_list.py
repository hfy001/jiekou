from data import get_data

casedate1 = get_data.excelshuju().openexl('E:\pythonbijia\data\getapi.xlsx', 'Sheet2')
case=eval(casedate1[0][2])
# print(case)
print([casedate1[40]])
print(len(casedate1))


# for case in casedate1:
#     for ca in case:
#         if ca[1]==33:
#             return ca

casedate=[]
for index, value in enumerate(casedate1):
    # print(index,value)
    # print(value[1])
    if value[1]==41:
        casedate.append(value)
        print(casedate)
