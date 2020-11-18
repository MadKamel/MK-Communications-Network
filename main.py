import irc, os
os.system('clear')

channel = "#mk-comms"
server = "irc.freenode.net"
nickname = "mk-comms-agent00"

client = irc.IRC()
client.connect(server, channel, nickname)


while True:
  text = client.get_text()
  print(text)

  