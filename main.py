import irc, os, comms
os.system('clear')

channel = "#mk-comms"
server = "irc.freenode.net"
nickname = "mk-comms-agent00"

client = irc.IRC()
client.connect(server, channel, nickname)


while True:
  cmd = comms.parsecmd(client.get_text())
  if not cmd == None:
    if cmd == 'test':
      print('Message recieved.')
    pass
    # run command