from socket import *
from time import ctime
import threading
import sys
import os

HOST = '127.0.0.1'
PORT = 6666
# ADDR = (HOST, PORT)

BUFSIZE = 1024

# tcpCliSock = socket(AF_INET, SOCK_STREAM)
# tcpCliSock.connect(ADDR)

def send(tcpCliSock, blank):
	suportTxt = "输入指令 “--list” 可查看当前服务器下所有用户名单； “--init0” 退出； “--help” 查看此帮助；\
	 “To:用户名” 与目标用户建立连接"
	print(suportTxt)
	while True:
		data = input()
		if data == '--help':
			print(suportTxt)
			continue
		tcpCliSock.send(bytes(data, 'utf-8'))
		if data == '--init0':
			break

def recv(tcpCliSock, blank):
	while True:
		data = tcpCliSock.recv(BUFSIZE).decode()
		if data == '--init0':
			break
		print("		", data)

if __name__ == '__main__':
	if input("请输入服务器地址，按回车跳过且使用默认本地地址\nhost: "):
		HOST = _
		PORT = input("请输入对应端口号\nport: ")
	ADDR = (HOST, PORT)
	tcpCliSock = socket(AF_INET, SOCK_STREAM)
	tcpCliSock.connect(ADDR)
	while True:
		name = input("请输入您的用户名: ")
		if not name:
			print("不能为空")
			continue
		tcpCliSock.send(bytes(name, 'utf-8'))
		name = tcpCliSock.recv(BUFSIZE).decode()
		if name ==  "sdf9321cPLf;2;":
			print("此名字已被使用")
			continue
		else: 
			print("用户注册成功")
			break
	# tcpCliSock.send(bytes(name, 'utf-8'))
	sendMessageThread = threading.Thread(target=send, args=(tcpCliSock, None))
	recvMessageThread = threading.Thread(target=recv, args=(tcpCliSock, None))

	sendMessageThread.start()
	recvMessageThread.start()
	sendMessageThread.join()
	recvMessageThread.join()
