from common import get_cwd
import os


def get_login():
    path = get_cwd.get_cwd()
    excel_path1 = os.path.join(path, 'data/case.xlsx')
    return excel_path1


def get_api():
    path = get_cwd.get_cwd()
    api_path1 = os.path.join(path, 'data/getapi.xlsx')
    return api_path1


def get_bijia():
    path = get_cwd.get_cwd()
    bijia_path1 = os.path.join(path, 'data/canshu1.xlsx')
    return bijia_path1
