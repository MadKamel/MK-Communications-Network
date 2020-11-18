import irc, os, comms
os.system('clear')

channel = "#mk-comms"
server = "irc.freenode.net"
nickname = "mk-comms-agent00"

client = irc.IRC()
client.connect(server, channel, nickname)


while True:
  cmd, user = comms.parsecmd(client.get_text())
  if not cmd == None:
    if cmd == 'ping':
      client.send(channel, 'pong')
      print('ping from ' + user + ' ponged.')
    
    elif cmd == 'pong':
      print('pong from ' + user + ' recieved.')

    elif cmd[:4] == 'send':
      print(cmd)