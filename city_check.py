from pandas import DataFrame as df
from openpyxl import Workbook
import datetime as dt


team_id_dict = {
    '10000': '北京',
    '10002': '沈阳',
}


class Makelog:

    def write_log_to_excel(self, work_sheet, data: dict):
        work_sheet.append([str(dt.datetime.now()), data['business'], data['city'], data['err']])

    def open_excel(self):
        file_xlsx = Workbook()
        work_sheet = file_xlsx.active
        work_sheet.append(['时间', '业务', '城市', '错误描述'])
        return work_sheet, file_xlsx

    def save_log(self, file_xlsx, path):
        """
        :param file_xlsx: open_excel方法返回的file_xlsx
        :param path: 日志想保存的路径
        :return: 保存日志，执行完成后保存。否则保存后再打开原有日志内容将被覆盖。
        """
        file_xlsx.save(path)


class MakingSamples:

    def __init__(self, city_name):
        self.city_name = city_name

    def check_team_city(self, _df, _df_59, team_id_type='团队ID', order_id_type='订单号'):
        """

        :param _df: 57的df
        :param _df_59: 59的df
        :param team_id_type: 团队ID 字段的名称
        :return: _df, _df_59
        """
        team_id = list(set(_df[team_id_type].to_list()))
        check = CheckCity(team_id_dict)
        if check.team_id_cheek(team_id, self.city_name):
            _df['下载城市'] = self.city_name
            order_id = _df_59[order_id_type].to_list()
            id_poll = _df[order_id_type].to_list()
            if check.order_id_check(order_id, id_poll):
                _df_59['下载城市'] = self.city_name
                return _df, _df_59
            else:
                return _df, None
        else:
            return None, None


class CheckCity:

    def __init__(self, team_dict):
        self.team_dict = team_dict

    def team_id_cheek(self, team_ids: list, city_name):
        team_ids.append('end')
        for _id in team_ids:
            _city = self.team_dict.get(_id)
            if _city:
                if _city == city_name:
                    return True
                elif _city == 'end':
                    return False
                else:
                    return False

    def order_id_check(self, order_id: list, id_poll: list):
        _inter = set(order_id).intersection(set(id_poll))
        if _inter:
            return True
        else:
            return False


def print_test(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')

# a = CheckCity(team_id_dict)
# print(a.team_id_cheek(['101010', '100001', '100001'], '北京'))
# print(a.order_id_check(['1', '2', '3'], ['1', '5', '6', '2', '3']))

# l = ['%s' % i for i in range(1000000)]
# l.append('10000')
#
# d57 = df({'团队ID': l,
#           '订单号': l})
# d59 = df({'订单号': ['10', '22', '1', '56']})
# b = MakingSamples('北京')
# s = dt.datetime.now()
# for i in range(100):
#     print(i)
#     b.check_team_city(d57, d59)
# e = dt.datetime.now()
# print(e - s)
