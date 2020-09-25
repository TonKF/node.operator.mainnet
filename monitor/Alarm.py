import socket
import telegram
import subprocess
import psutil
import time
from time import sleep
my_token = '1106924426:AAGC1XlEMcuEGRivP7OkJHisk45MRL3VrS4'
bot = telegram.Bot(token = my_token)

HOSTNAME = socket.gethostname()
VALIDATION = subprocess.check_output("cat ~/node.operator/logs/election.log | grep -oP '(?<=VALIDATION_STATUS: )[0-9]'",shell=True);
ELECTION = subprocess.check_output("cat ~/node.operator/logs/election.log | grep -oP '(?<=ELECTION_STATUS: )[0-9]'",shell=True);
SYNC=subprocess.check_output("~/net.ton.dev/scripts/check_node_sync_status.sh | grep TIME_DIFF | awk '{print $4}' | tr '[:upper:]' '[:lower:]'",shell=True);

SYNCalarm = "-100"
SYNCalarm1 = 0

print VALIDATION
print ELECTION
print HOSTNAME
if int(VALIDATION) == 1:
  bot.sendMessage(chat_id='-1001416401295', "Server "+text=str(HOSTNAME)+" Validating");
if int(ELECTION) == 1:
  bot.sendMessage(chat_id='-1001416401295', "Server "+text=str(HOSTNAME)+" in Election");
if int(SYNC) < int(SYNCalarm):
  bot.sendMessage(chat_id='-1001416401295', "server "+text=str(HOSTNAME)+" SYNC off, SYNC:"+str(SYNC));
if int(SYNC) > int(SYNCalarm1):
  bot.sendMessage(chat_id='-1001416401295', "server "+text=str(HOSTNAME)+" SYNC off, SYNC:"+str(SYNC));
