
# File: simplelog.py
#
# ログのとり方
# https://docs.python.org/ja/3.13/howto/logging.html#logging-basic-tutorial
#

import logging

logging.basicConfig(filename='simplelog.log', encoding='utf-8',
			format='%(asctime)s [%(levelname)s] %(message)s',
			level=logging.DEBUG)

logging.debug('デバッグメッセージ')
logging.info('インフォメーション')
logging.warning('警告')
logging.error('エラー')


