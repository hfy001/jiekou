import pytest
from src.person  import person
from data import  get_data
import allure
from common import get_path
from common.id_number import IdNumber

path=get_path.get_api()
casedate1 = get_data.ExcelData().openexl(path, 'Sheet2')
list=casedate1[37]
case=list[2]
a=eval(case)
b=a['data']
print(b)
print(type(b))