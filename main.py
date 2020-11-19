import irc, os, comms
os.system('clear')


channel = "#mk-comms"
server = "irc.freenode.net"
nickname = "mk-comms-agent00"

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
        else:
          client.send('fail ' + user + ' 0:RQST_NOT_RECOGNIZED')