# File: servsample2.py
#
# エコーサーバー 
# https://docs.python.org/ja/3/library/socket.html
#

import socket
import logging

#
# ログを取るための設定
#
logging.basicConfig(filename='servlog.log', encoding='utf-8',
			format='%(asctime)s [%(levelname)s] %(message)s',
			level=logging.INFO)

logging.info('Server Start')
HOST = '0.0.0.0'# すべてのIPアドレスからの接続を許す
PORT = 54321			# ポート番号 / ダイナミック・ポートの領域を利用
# with構文を使って処理を閉じる書き方
# ソケットでTCP/IPを開く
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST, PORT))	# ソケットをポートにバインド
	s.listen(1)			# 接続開始
	conn, addr = s.accept()		# 接続待ち
	with conn:
		logging.info('Connection ' + str(addr)) # 接続元情報をロギング
		while True:				# 無限ループ
			data = conn.recv(1024)
			if not data: break
			conn.sendall(data)

logging.info('Server Finish')

