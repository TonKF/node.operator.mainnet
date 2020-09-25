import telegram
import subprocess
import psutil
import time
from time import sleep
my_token = '1106924426:AAGC1XlEMcuEGRivP7OkJHisk45MRL3VrS4'
bot = telegram.Bot(token = my_token)

VALIDATION=subprocess.check_output("cat ~/node.operator/logs/election.log | grep -oP '(?<=VALIDATION_STATUS: )[0-9]'",shell=True);
ELECTION=subprocess.check_output("cat ~/node.operator/logs/election.log | grep -oP '(?<=ELECTION_STATUS: )[0-9]'",shell=True);

if float(VALIDATION) == "1"
  print "validating"
