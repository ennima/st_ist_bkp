import os
import json
from ftplib import FTP

dirs = os.listdir("V:\\media")
carpetas = []
for item in dirs:
	if("." in item):
		pass
	else:
		carpetas.append(item)
content = json.dumps(carpetas)
with open('carpetas_to_array.json','w') as fb:
	fb.write(content)
