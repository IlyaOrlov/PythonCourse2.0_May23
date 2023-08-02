# Больше примеров здесь: https://webdevblog.ru/logging-v-python/
import logging

s_handler = logging.StreamHandler()
f_handler = logging.FileHandler('file.log')
logging.basicConfig(format='%(asctime)s-%(levelname)s-%(message)s',
                    level=logging.INFO,
                    handlers=(s_handler, f_handler))
logging.info('Полезная информация')