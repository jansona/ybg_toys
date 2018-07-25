#coding:utf-8

from socket import *
from time import ctime
import threading
import re

# 建立服务器
HOST = ''
PORT = 6666
ADDR = (HOST, PORT)

BUFSIZE = 1024

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)

tcpSerSock.listen(5)

# 建立用于存储用户及连接关系的字典
name2sock = {}
send2recv = {}

# 服务器重要工作是不断接受各个客户端发送的消息并进行解析，判断输入合法性，
# 创建新用户、建立新联系或递送消息
def messageParser(senderSock, senderName):
	'服务器接收并处理来自已注册的客户端的消息'
	while True:
		data = senderSock.recv(BUFSIZE).decode()
		if data == '--init0':
			senderSock.send(bytes('--init0', 'utf-8'))
			if senderSock in send2recv.keys():
				senderSock.send(bytes("对方登出", 'utf-8'))
				del send2recv[send2recv[senderSock]]
				del send2recv[senderSock]
			del name2sock[senderName]
			senderSock.close()
			# print('wtf')
			print("The member in the chat room update:")
			for name in name2sock.keys():
				print(name, end='\t')
			print('')
			break

		if data == '--list':
			l = []
			for name in name2sock.keys():
				l.append(name)
			senderSock.send(bytes(str(l), 'utf-8'))
			continue

		# if senderName in name2sock.keys():
		# 	if senderSock in send2recv.keys():
		# 		send2recv[senderSock].send('%s' % data)
		# 	elif re.match('^To:.+', data) is not None:
		# 		data = data[3:]
		# 		if name2sock[data] in send2recv.keys():
		# 			print('he has already had a partner')
		# 			continue
		# 		send2recv[senderSock] = name2sock[data]
		# 		send2recv[name2sock[data]] = senderSock
		# 		print('connection between %s and %s completed' % (senderName, data))
		# 	elif data == 'init0':
		# 		shutoffServer()
		# 	else:
		# 		print("don't understand")
		# elif data == 'init0':
		# 	shutoffServer()
		# else:

		if re.match('^To:.+', data) is not None:
			data = data[3:]
			if data in name2sock.keys():
				if data == senderName:
					senderSock.send(bytes("禁止与自己建立联系", 'utf-8'))
				if name2sock[data] not in send2recv.keys():
					if senderSock in send2recv.keys():
						del send2recv[send2recv[senderSock]]
						del send2recv[senderSock]
						print("为建立新连接，已将旧连接移除")
					send2recv[senderSock] = name2sock[data]
					send2recv[name2sock[data]] = senderSock
					senderSock.send(bytes("与 %s 的连接建立" % (data), 'utf-8'))
					name2sock[data].send(bytes("与 %s 建立连接" % senderName, 'utf-8'))
					print('match complete')
				else:
					print("There's already been a connection")
					senderSock.send(bytes('有第三者呼叫你', 'utf-8'))
			else:
				senderSock.send(bytes('查无此用户，键入指令 “--list” 可查看当前所有用户', 'utf-8'))
				print("There's no such a person")
		elif senderSock in send2recv.keys():
			send2recv[senderSock].send(bytes("[%s @ %s] %s" % (senderName, ctime(), data), 'utf-8'))
			# print('transform')
		else:
			senderSock.send(bytes("尚未与任何人建立联系", 'utf-8'))
			print('message useless')

def connectThreat(tcpCliSock, blank):
	while True:
		name = tcpCliSock.recv(BUFSIZE).decode()
		if name in name2sock.keys():
			tcpCliSock.send(bytes("sdf9321cPLf;2;", 'utf-8')) # 防止偶然，用乱码验证
		else:
			name2sock[name] = tcpCliSock
			tcpCliSock.send(bytes(name, 'utf-8'))
			break

	print("The member in the chat room update:")
	for name in name2sock.keys():
		print(name, end='\t')
	print('')

	messageParser(tcpCliSock, name)

if __name__ == '__main__':
	while True:
		print('waiting for conection...')
		tcpCliSock, addr = tcpSerSock.accept()
		print('connection from ', addr)
		chatThread = threading.Thread(target=connectThreat, args=(tcpCliSock, None))
		chatThread.start()
