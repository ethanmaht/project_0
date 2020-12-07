from openpyxl import Workbook
import datetime as dt


class Makelog:

    def open_excel(self):
        file_xlsx = Workbook()
        work_sheet = file_xlsx.active
        work_sheet.append(['时间', '业务', '城市', '错误描述'])
        self.work_sheet = work_sheet
        self.file_xlsx = file_xlsx

    def write_log_to_excel(self, data: dict):
        work_sheet = self.work_sheet
        work_sheet.append([str(dt.datetime.now()), data['business'], data['city'], data['err']])

    def save_log(self, path):
        self.file_xlsx.save(path)


class MakingSamples:

    def __init__(self, city_name):
        self.city_name = city_name

    """
    def check_team_city(self, _df, _df_59, team_id_type='团队ID', order_id_type='订单号'):
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
    """

    def check_team_city_57(self, _df, team_id_dict, team_id_type='团队ID'):
        """
        :param _df: 57的df
        :param team_id_type: 团队ID 字段的名称
        """
        team_id = list(set(_df[team_id_type].to_list()))
        check = CheckCity()
        if check.team_id_cheek(team_id, self.city_name, team_id_dict):
            _df['下载城市'] = self.city_name
            return _df
        else:
            return None

    def check_team_city_59(self, _df, _df_59, order_id_type='订单号'):
        """
        :param _df: 57的df
        :param _df_59: 59的df
        :param team_id_type: 团队ID 字段的名称
        :return: _df, _df_59
        """
        check = CheckCity()
        order_id = _df_59[order_id_type].to_list()
        id_poll = _df[order_id_type].to_list()
        if check.order_id_check(order_id, id_poll):
            _df_59['下载城市'] = self.city_name
            return _df_59
        else:
            return None


class CheckCity:

    def team_id_cheek(self, team_ids: list, city_name, team_id_dict):
        team_ids.append('end')
        for _id in team_ids:
            _city = team_id_dict.get(_id)
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
