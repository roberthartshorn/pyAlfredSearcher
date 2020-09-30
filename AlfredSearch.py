import os
import sys
import subprocess as sp
import ntpath 
import json 

#These env setters are for development purposes and will be received by the Alfred workflow in production.
os.environ["query"] = sys.argv[1]
os.environ["searchFolder"] = sys.argv[2]

#Get upstream environment variables from the Alfred workflow
searchFolder = os.getenv("searchFolder")
query = os.getenv("query")

#Mdfind is a leaner version 
bashCmd = "mdfind 'kMDItemFSName = " + query + "*.pdf" + "' -onlyin " + '"' + searchFolder + '"'
print(bashCmd)
proc = sp.check_output(bashCmd, shell=True)
result = proc.decode("UTF-8").splitlines()

resultDict = {"items": []}
resultLst = []

for line in result:
   resultLst.append({"title": query, "subtitle": line, "arg": line})

resultDict["items"] = resultLst
resultJSON = json.dumps(resultDict)
sys.stdout.write(resultJSON)



