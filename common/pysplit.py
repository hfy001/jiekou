import re


class Get_Cookie:
    def cookie(self,login):
        array = re.split('[;]',login)
        return array[0]
