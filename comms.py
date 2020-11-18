def parsecmd(msg):
  cmd = None
  spl = msg.split(' ')
  if spl[1] == 'PRIVMSG':
    cmd = spl[3][1:]
  
  return cmd