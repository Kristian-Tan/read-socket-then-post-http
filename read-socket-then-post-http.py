#!/usr/bin/env python3

import socket
import requests
import sys
import json

if len(sys.argv) != 6:
	print("Usage: "+sys.argv[0]+" (socket-host) (socket-port) (socket-buffer-size) (http-endpoint) (http-headers-json)", file=sys.stderr)
	exit()

arg_socket_host			= sys.argv[1]
arg_socket_port			= sys.argv[2]
arg_socket_buffer_size	= sys.argv[3]
arg_http_endpoint		= sys.argv[4]
arg_http_headers		= sys.argv[5]

try:
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((arg_socket_host, int(arg_socket_port)))
except Exception as e:
	print("cannot connect to TCP "+arg_socket_host+":"+arg_socket_port, file=sys.stderr)
	exit()

try:
	buffer = int(arg_socket_buffer_size)
except Exception as e:
	buffer = 4092

try:
	http_headers = json.loads(arg_http_headers)
except Exception as e:
	http_headers = {}

while True:
	try:
		message = sock.recv(buffer).decode()
	except Exception as e:
		print("cannot read from socket", file=sys.stderr)
		exit()

	try:
		response = requests.post(arg_http_endpoint, data=message, headers=http_headers)
	except Exception as e:
		print("cannot create http request", file=sys.stderr)
		exit()

	print(response.status_code, file=sys.stdout)
	print(response.text, file=sys.stdout)
