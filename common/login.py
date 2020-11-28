import requests
from data import canshu1
from common import get_path


path=get_path.get_login()
casedate=canshu1.excelshuju1().openexl(path,'Sheet2')
print(casedate)

class login1():
    def get_ssid(self):
        response = requests.get(url=casedate[0][1] + casedate[0][2], headers=casedate[0][3], params=eval(casedate[0][4]))
        print(response.text)
        rescookid = response.headers['Set-Cookie']
        print(rescookid)
        return rescookid

    def get_accountid(self):
        response = requests.get(url=casedate[0][1] + casedate[0][2], headers=casedate[0][3], params=eval(casedate[0][4]))
        accountid=response.json()['result']['id']
        print(accountid)
        return accountid


