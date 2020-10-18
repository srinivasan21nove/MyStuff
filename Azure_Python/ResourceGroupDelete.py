# Author Srinivasan
# Date: 04/10/2020
# Used to delete resources groups in azure one by one
# Usage: Run the scripts in Azure Cloud Shell and provide yes to delete / any other to skip
# Language: Python 3
import os,json
stream = os.popen('az group list')
output = stream.read()
test=json.loads(output)
for i in test:
        print(i["name"])
        a=input("enter yes to delete")
        if(a=="yes"):
                tream=os.popen('az group delete --name '+i["name"]+' --yes --no-wait')
                print(stream.read())
