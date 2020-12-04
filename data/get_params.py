from data import get_data
from common import get_path


class get_params:
    def getparams(self,api_id):
        path = get_path.get_api()
        casedate1 = get_data.excelshuju().openexl(path, 'Sheet2')
        casedate = []
        for index, value in enumerate(casedate1):
            # print(index,value)
            # print(value[1])
            if value[1] == api_id:
                casedate.append(value)
        return casedate


