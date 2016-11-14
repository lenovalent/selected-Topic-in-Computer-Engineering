import sys
from SOAPpy import SOAPProxy
import xml.etree.ElementTree as ET

serverUrl="54.169.207.52:8081"
namespace='xml'
server = SOAPProxy(serverUrl, namespace)
server.config.dumpSOAPOut = 1
server.config.dumpSOAPIn = 1
#response = server.movieNameFromeType("Adventure")
#response = server.editResolution("The Last Airbender","720p")
response = server.editLength("Letters To Juliet","90")

#response = server.removeMovie("Always")
#response = server.addInitResolution("1080p")
#response = server.addInitLength("120") #in min

#response = server.update_xml("aaa",["bb","cc"],["ee","ff"],"gg","1","oct","1234")
print response
