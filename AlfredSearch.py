import os
import sys
import subprocess as sp 
import json 

#Set mode for development 
#os.environ['mode'] = ""

#Get upstream environment variables
mode = os.getenv('mode')
query = sys.argv[1]
searchFolder = os.getenv('searchFolder') if mode == "Production" else sys.argv[2]
limit = os.getenv('limit') if mode == "Production" else sys.argv[3]

#Mdfind is a native Mac OS X command to search a Spotlight index.
bashCmd = "mdfind 'kMDItemFSName = " + '"' + query + '*"' + "c"  + "' -onlyin " + '"' + searchFolder + '"' + " | head -n " + limit
proc = sp.check_output(bashCmd, shell=True)
result = proc.decode("UTF-8").splitlines()

resultDict = {"items": []}
resultLst = []
for line in result:
   resultLst.append({"title": os.path.basename(line), "subtitle": line, "arg": line})
resultDict["items"] = resultLst
resultJSON = json.dumps(resultDict)

sys.stdout.write(resultJSON)


