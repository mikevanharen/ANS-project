import socket
import time

host = 'local host'
port = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', port))

# receive message
msg = s.recv(1024)

result = []
begin = time.time()
decoded = ""

# as long as the server does not send "end" keep receiving the message
# meanwhile extract the bits encoded in the timing channel
while decoded != "end":
    decoded = msg.decode()
    print('Received:' + decoded)
    msg = s.recv(1024)
    end = time.time()
    between = end - begin
    print(between)
    if between > 0.05:
        result.append("1")
    else:
        result.append("0")
    begin = time.time()

message = ''.join(result)

# convert the byte array to a message
i = 0
test_list = []
while i < len(message):  # Convert the byte string to a string of characters
    letter = chr(int(message[i:i + 8], 2))
    if int(message[i:i + 8], 2) == 0:
        break
    test_list.append(letter)
    i += 8
    print(letter, end="")

# disconnect the client
s.close()
