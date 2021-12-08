import socket
import time

# setup connection
host = 'local host'
port = 5000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', port))
s.listen(1)
c, address = s.accept()

print("CONNECTION FROM:", str(address))

message = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et " \
          "dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip " \
          "ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu " \
          "fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt " \
          "mollit anim id est laborum. Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium " \
          "doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto " \
          "beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut " \
          "fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro " \
          "quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam " \
          "eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima " \
          "veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi " \
          "consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae " \
          "consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?"

# split the message into an array
split_message = message.split(" ")

secret = "Hello, World"
bin_secret_list = []

# convert secret string to byte string
for letter in secret:
    ASCII = ord(letter)
    bin_secret_list.append(format(ASCII, '08b'))
bin_secret = ''.join(bin_secret_list)
bin_secret += "00000000"

bit_string = "".join(bin_secret_list)

# insert the timing and send the message in parts
x = 0
for bit in bit_string:
    c.send(split_message[x].encode())
    if bit == "1":
        time.sleep(0.05)
    else:
        time.sleep(0.01)
    x += 1
c.send(b"end")
  
# disconnect the server
c.close()
