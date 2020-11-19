import irc, os, comms
os.system('clear')


channel = "#mk-comms"
server = "irc.freenode.net"
nickname = "microsystems_host"

client = irc.IRC()
client.connect(server, channel, nickname)


while True:
  cmd, user, fullmsg = comms.parsecmd(client.get_text())
  if not cmd == None:
    if cmd == 'ping':
      client.send('pong')
      print('ping from ' + user + ' ponged.')
    
    elif cmd == 'pong':
      print('pong from ' + user + ' recieved.')

    elif cmd == 'send':
      if fullmsg.split(' ')[1] == nickname:
        sent_command = ' '.join(fullmsg.split(' ')[2:])
        print('sending message from ' + user + ' to logs.')
        print(sent_command)
    
    elif cmd == 'rqst':
      if fullmsg.split(' ')[1] == nickname:
        rqst_data = ' '.join(fullmsg.split(' ')[2:])
        print('recieved request from ' + user + ' for ' + rqst_data + '.')
        
        if rqst_data == 'ack':
          client.send('give ' + user + ' ack')
        elif rqst_data == 'get':
          try:
            client.send('give ' + user + ' ' + fullmsg.split(' ')[3] + ' ' + comms.encode_file('public/' + fullmsg.split(' ')[1]))
          except:
            client.send('fail ' + user + ' 1:OBJECT_NOT_RECOGNIZED')
         
        else:
          client.send('fail ' + user + ' 0:RQST_NOT_RECOGNIZED')