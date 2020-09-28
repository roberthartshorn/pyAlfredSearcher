import subprocess as sp
import ntpath 
import json 
import sys

print("hello")
folder = '/Volumes/MidstateDocs'
query = '110868'
bashCmd = "mdfind 'kMDItemFSName = " + query + "*.pdf" + "' -onlyin " + folder

proc = sp.check_output(bashCmd, shell=True)
result = proc.decode("UTF-8").splitlines()

resultDict = {"items": []}
resultLst = []
for line in result:
   resultLst.append({"title": query, "subtitle": line, "arg": line}
        )

resultDict["items"] = resultLst
resultJSON = json.dumps(resultDict)

print(resultJSON)
#sys.stdout.write(resultJSON)



