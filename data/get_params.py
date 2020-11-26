from data import get_data


class get_params:
    def get_params(self,api_id):
        casedate1 = get_data.excelshuju().openexl('E:\pythonbijia\data\getapi.xlsx', 'Sheet2')
        casedate = []
        for index, value in enumerate(casedate1):
            # print(index,value)
            # print(value[1])
            if value[1] == 41:
                casedate.append(value)
        return casedate


