from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n NYU Tandon"
    endmsg = "\r\n.\r\n"



    # TCP connection with mailserver

    # Fill in start
    #gmailAddress = "smtp.hotmail.com"
    #mailServerAddress = "127.0.0.1"
    #port = 1025
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    # Fill in end
    # NYU Tandon
    recv = clientSocket.recv(1024).decode()
    #print(recv) #You can use these print statement to validate return codes from the server.
    #if recv[:3] != '220':
    #    print('220 reply not received from server.')

    # Send HELO command and print server response.
    helloCommand = 'HELlO NYU Tandon \r\n'
    clientSocket.send(helloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    #if recv1[:3] != '250':
    #    print('250 reply not received from server.')

    # Send MAIL FROM command.
    # Fill in start
    mailfromCmd = 'MAIL FROM:<ram@zingzing.com>\r\n'
    clientSocket.send(mailfromCmd.encode())
    recv2=clientSocket.recv(1024).decode()
    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
    rcpttomCmd = 'RCPT TO:<ram1@blingbling.org>\r\n'
    clientSocket.send(rcpttomCmd.encode())
    recv3=clientSocket.recv(1024).decode()
    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start
    dataCMD = 'DATA\r\n'
    clientSocket.send(dataCMD.encode())
    recv4=clientSocket.recv(1024).decode() #354
    # Fill in end

    # Send message data.
    # Fill in start
    clientSocket.send(msg.encode())
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    clientSocket.send(endmsg.encode())
    recv5=clientSocket.recv(1024).decode() #250
    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    quitCmd = "QUIT\r\n"
    clientSocket.send(quitCmd.encode())
    recv6=clientSocket.recv(1024).decode()
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')