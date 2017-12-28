import os
# import pandas as pd
# from ftplib import FTP
# from ftplib import all_errors
# from subprocess import call
# from time import time as time_i
# import time
from datetime import datetime
# # import socket
import json
from shutil import copyfile
from pathlib import Path

# Open Configuration
json_data=open("conf.json").read()
conf = json.loads(json_data)
print(conf['user'])

backup_list_path = "backup_list.json"
if(os.path.exists(backup_list_path)):
	print("lista de backup ok.")
	backup_list_name = Path(os.path.basename(backup_list_path)).stem

	# Open DownloadList
	json_data=open(backup_list_path).read()
	backup_list = json.loads(json_data)
	# print(backup_list[0])
	
	#Save DownloadList in history

	##Get Last DownloadList from history
	last_history_file_path = conf['history_path']+"last_history_file.txt"
	last_history_file = ""
	if(os.path.exists(last_history_file_path)):
		with open(last_history_file_path) as f:
			last_history_file = f.read()
		print("última lista de recuperación:",last_history_file)
	else:
		print("Es la primer ejecución...")

	##Save Current DownloadList to history
	history_file = conf['history_path']+backup_list_name+datetime.now().strftime("%d-%m-%Y_%H_%M_%S")+".json"
	copyfile(backup_list_path, history_file)
	with open(last_history_file_path,"w") as l_h_f:
		l_h_f.write(history_file)

	# print(datetime.now().strftime("%d-%m-%Y_%H_%M_%S"))

else:
	print("No se encuentra la lista de borrado: ",backup_list_path)

