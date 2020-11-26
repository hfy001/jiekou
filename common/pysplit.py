import re

class get_cookie:
    def cookie(self,login):
        array = re.split('[;]',login)
        return array[0]
