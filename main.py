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
    print(fullmsg)
    if cmd[:4] == 'ping':
      client.send(channel, 'pong')
      print('ping from ' + user + ' ponged.')
    
    elif cmd[:4] == 'pong':
      print('pong from ' + user + ' recieved.')