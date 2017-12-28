import os
# import pandas as pd
from ftplib import FTP
from ftplib import all_errors
# from subprocess import call
from time import time as time_i
# import time
from datetime import datetime
# # import socket
import json
from shutil import copyfile
from pathlib import Path
import requests


def seconds_timestamp(seconds):
	m, s = divmod(seconds, 60)
	h, m = divmod(m, 60)
	restore_time = "%02d:%02d:%02d" % (h, m, s)
	# print ("Tardó:",restore_time)
	return(restore_time)

def ftp_download(item,conf):
	tiempo_inicial = time_i()
	ftp = FTP(conf["origin_ftp_server"]["host"])
	print(ftp.login(conf["origin_ftp_server"]["user"],conf["origin_ftp_server"]["pass"]))
	ftp.cwd(item["folder"])
	print("Descargando: "+item["clip"])
	try:
		ftp.retrbinary('RETR '+item["clip"], open(item["clip"], 'wb').write)
		download_success = True
	except all_errors as e:
		print(e)

	ftp.quit()
	tiempo_final = time_i()
	tiempo_ejecucion = tiempo_final - tiempo_inicial
	print("Tardó: " , tiempo_ejecucion,"s")
	print(seconds_timestamp(tiempo_ejecucion))
	return tiempo_ejecucion

def ftp_upload(item,conf):
	tiempo_inicial = time_i()
	ftp = FTP(conf["dest_ftp_server"]["host"])
	print(ftp.login(conf["dest_ftp_server"]["user"],conf["dest_ftp_server"]["pass"]))
	ftp.cwd(item["dest_folder"])

	print("Ingestando: "+item["clip"])
	ftp.storbinary('STOR '+item["clip"]+".mxf", open(item["clip"], 'rb'))
	ftp.quit()
	print( item["clip"] + " listo.")
	os.remove(item["clip"])
	tiempo_final = time_i()
	tiempo_ejecucion = tiempo_final - tiempo_inicial
	return tiempo_ejecucion

def insert_clip_istorage_db(item,conf):
	url = conf["istorage_api_store_clip"]
	has_pxy = 0
	if(item["metadata"]["proxy"] != ""):
	
		has_pxy = 1
	else:
	
		has_pxy = 0
	
	dic_test = {"name":item["clip"]
	,"created_date":item["metadata"]["Created Date"]
	,"modified_date":item["metadata"]["Modified Date"]
	,"duration":""
	,"path":item["dest_folder"]
	,"has_pxy":has_pxy
	,"archived_date":datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	,"archived_user":conf["user"]
	,"original_path":item["folder"]
	,"format":conf["origin_format"]
	,"origin":conf["origin_db_id"]
	,"storage":conf["dest_db_id"]
	}
	print(dic_test)
	data = json.dumps(dic_test)
	response = requests.post(url, data=data,headers={"Content-Type": "application/json"})
	print(response.json())
	return response.json()

# Open Configuration
json_data=open("conf.json").read()
conf = json.loads(json_data)
print(conf['user'])
print(conf["origin_ftp_server"]["host"])
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

	#Download files from List
	for item in backup_list:
		print(item["folder"]+"\\"+item["clip"])
		print("Descargando.")
		tiempo_inicial = time_i() 
		# ftp = FTP(conf["origin_ftp_server"]["host"])
		# print(ftp.login(conf["origin_ftp_server"]["user"],conf["origin_ftp_server"]["pass"]))
		# ftp.cwd(item["folder"])
		# print("Descargando: "+item["clip"])
		# try:
		# 	ftp.retrbinary('RETR '+item["clip"], open(item["clip"], 'wb').write)
		# 	download_success = True
		# except all_errors as e:
		# 	print(e)
		
		# ftp.quit()
		download_time = ftp_download(item,conf)
		print( item["clip"] + " listo para ingestar.")
		##Ingestar material
		upload_time = ftp_upload(item,conf)
		##Ingresar a DB de Istorage
		insert_clip_istorage_db(item,conf)


else:
	print("No se encuentra la lista de borrado: ",backup_list_path)

