import logging

# Задаем вам подходящий формат времени
time_format = '%H:%M:%s,%03d'

# Определяем настройки логгера
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()

# Описываем формат вывода сообщений
formatter = logging.Formatter('%(asctime)s.%(msecs)03d    %(funcName)-15s %(levelname)-7s -> %(message)s', '%H:%M:%S')
handler.setFormatter(formatter)
logger.addHandler(handler)
