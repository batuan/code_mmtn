from socket import *
import base64
msg = "\ri love computer network!"
endmsg  = "\r\n . \r\n"

# mail server 
mailserver = 'smtp.gmail.com'
mailPort = 25
#create socket called clientSocket and establist TCP connection with mail server
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, mailPort))
recv = clientSocket.recv(1024)
print recv
if recv[:3] != '220':
    print '220 reply not received from server.'

#say hello
helloCommand = 'ehlo Alice \r\n'
clientSocket.send(helloCommand)
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
    print '250 reply not received from server.'

#send starttls command
print "Sending auth Command"
clientSocket.send("STARTTLS auth login\r\n")
recv2 = clientSocket.recv(1024)
print recv2

# send auth login command
clientSocket.send("AUTH LOGIN\r\n")
recv3 = clientSocket.recv(1024)
print base64.b64decode(recv3[4:])

#send gmail user
user = raw_input("input your gmail: ")
user_encode =  base64.b64encode(user)
user_encode = user_encode + '\r\n'
clientSocket.send(user_encode)
recv4 = clientSocket.recv(1024)
print base64.b64decode(recv4[4:])

#send password user
PassWord = base64.b64encode(raw_input("input your PassWord: "))
PassWord  = PassWord + '\r\n'
clientSocket.send(PassWord)
recv5 = clientSocket.recv(1024)
print recv5

# begin send mail
# fist: enter set mail from commad
print 'set your gmail is ' + user
Mail_From = 'mail from:<'+user+'>\r\n'
clientSocket.send(Mail_From)
recv6 = clientSocket.recv(1024)
print recv6
#second: set mail receive command

Mail_Recive = raw_input("Input your recive adress:")

Mail_Recive_command = 'rcpt to:<'+Mail_Recive+'>\r\n'

clientSocket.send(Mail_Recive_command)
recv7 = clientSocket.recv(1024)
print recv7

#third: enter mail

clientSocket.send('DATA\r\n')
recv8 = clientSocket.recv(1024)

subject = raw_input("input your subject: ")
message = raw_input("input your messages: ")

data = 'from:'+user+'\r\n'+'To:'+Mail_Recive+'\r\n'+'Subject:'+subject+'\r\n'+message+'\r\n'+'.\r\n'

print 'your messages is: \r\n' + data

clientSocket.send(data)
recv9 = clientSocket.recv(1024)
print recv9

print 'ban da gui thanh cong email toi dia chi: '+ Mail_Recive


