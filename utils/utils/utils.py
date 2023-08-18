from datetime import datetime

def converter_data_string_para_datetime(data_string: str):
    data = data_string.split('-')
    return datetime.datetime(year=int(data[0]), month=int(data[1]), day=int(data[2]))