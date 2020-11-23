import irc, os, comms
os.system('clear')


channel = "#mk-comms"
server = "irc.freenode.net"
nickname = "mcsys-host"

client = irc.IRC()
client.connect(server, channel, nickname, "MK-COMMS Test Service")


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
        print('recieved request from ' + user + ' to ' + rqst_data + '.')
        
        if rqst_data == 'ack':
          client.send('give ' + user + ' ack')
        elif rqst_data.split(' ')[0] == 'get':
          try:
            client.send('give ' + user + ' file ' + rqst_data.split(' ')[1] + ' ' + comms.encode_file('public/' + rqst_data.split(' ')[1]))
          except:
            client.send('fail ' + user + ' 1:OBJECT_NOT_RECOGNIZED')
         
        else:
          client.send('fail ' + user + ' 0:RQST_NOT_RECOGNIZED')