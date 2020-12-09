import json
from data import  get_api
from page_request.pagerequest import Apimethod
from common import get_path


path=get_path.get_api()



def pretty(r):
    print(json.dumps(r.json(), indent=4, ensure_ascii=False))

#  购物车


casedate1 = get_api.excelshuju().openexl(path, 'Sheet2')

a=casedate1[29][2]
b=eval(a)
bb=b['data_info']




print(b)
print(type(b))
print(bb)
print(type(bb))

c=json.loads(bb)
print(c)
print(type(c))

parms = {'data_info': {}}
print(type(parms['data_info']))