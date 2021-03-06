import gspread
import subprocess
from datetime import datetime
from oauth2client.service_account import ServiceAccountCredentials
import psutil
from random import randint
import time
from time import sleep
import socket

HOSTNAME = (socket.gethostname())

scope = [
'https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive',
]
json_file_name = '/home/username/node.operator/configs/spread.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
gc = gspread.authorize(credentials)
spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1Rcmlw0lcUHQj2UKeibFFKbAcGdXy4tr7boOkNisikQc/edit#gid=188383744'
doc = gc.open_by_url(spreadsheet_url)
worksheet = doc.worksheet('sheet1') 

tot_before = psutil.net_io_counters()
DISKB=psutil.disk_io_counters(perdisk=False, nowrap=True)
time.sleep(1)
tot_after = psutil.net_io_counters()
DISKA=psutil.disk_io_counters(perdisk=False, nowrap=True)
DISKR=DISKA.read_bytes-DISKB.read_bytes
DISKW=DISKA.write_bytes-DISKB.write_bytes
NETSENT=(tot_after.bytes_sent-tot_before.bytes_sent)
NETREC=(tot_after.bytes_recv-tot_before.bytes_recv)
CPU=psutil.cpu_percent(interval=None, percpu=False)
TIME=datetime.now().strftime('%d %H:%M')
SYNC=subprocess.check_output("~/*.ton.dev/scripts//check_node_sync_status.sh | grep TIME_DIFF | awk '{print $4}' | tr '[:upper:]' '[:lower:]'",shell=True)
RAM=psutil.virtual_memory()
LOG=subprocess.check_output("tail -n 1 ~/node.operator/logs/master.log | tr -d ';'  | tr -d ':'",shell=True)
ELECTION=subprocess.check_output("tail -n 1 ~/node.operator/logs/election.log | tr -d ';'  | tr -d ':'",shell=True)
sleep (randint(1,10))

ADD = "1"
CELLNO = int(ADD)+ int(HOSTNAME)
CELL = 'B'+str(CELLNO)

worksheet.update_acell(CELL,'TIME'+TIME+' SYNC'+SYNC+' CPU'+str(CPU)+' RAM'+str(RAM.percent)+' NETSENT'+str((NETSENT)/131072)+ ' NETREC'+str((NETREC)/131072)+ ' DISKREAD'+str((DISKR)/131072)+' DISKWRITE'+str((DISKW)/131072)+ str(LOG) + str(ELECTION))
