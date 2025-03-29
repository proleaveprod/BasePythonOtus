from datetime import datetime



def parse_custom_datetime(datetime_str: str) -> datetime:
    """Парсит строку формата 'ГГГГ_ММ_ДД-ЧЧ_ММ_СС_микросекунды' в datetime."""
    return datetime.strptime(datetime_str, "%Y_%m_%d-%H_%M_%S_%f")





a = "2020_05_26-10_51_18_818800"
dt = parse_custom_datetime(a)

print(dt.ctime())