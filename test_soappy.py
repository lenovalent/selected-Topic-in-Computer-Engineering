from SOAPpy import SOAPServer
import xml.etree.ElementTree as ET
import sys, time
from SOAPpy import WSDL
class webservice:
    def return_xml():
        tree = ET.parse('MovieAll_SPN.xml')
        root = tree.getroot()
        return ET.tostring(root,encoding="us-ascii", method="xml")
    def movieNameFromeType(self,type):
        list_ = [] 
        tree = ET.parse('MovieAll_SPN.xml')
        root = tree.getroot()
        for movie in root.findall('movie'):
            for type_ in movie.find('types'):
                if type_.text == type:
                    list_.append(movie.find('name').text)
        return list_
    def update_xml(self,name,type,name_actor,Director,day,month,year):
        tree = ET.parse('MovieAll_SPN.xml')
        root = tree.getroot()
        new_tag = ET.Element('movie')
        name_tag = ET.Element('name')
        name_tag.text = name
        types_tag = ET.Element('types')
        for t in type:
            type_tag = ET.Element('type')
            type_tag.text = t
            types_tag.append(type_tag)
        stars_tag = ET.Element('stars')
        for star in name_actor:
            actor_tag = ET.Element('name_actor')
            actor_tag.text = star
            stars_tag.append(actor_tag)
        director_tag = ET.Element('director_actor')
        director_tag.text = Director
        date_tag = ET.Element('date')
        day_tag = ET.Element('day')
        day_tag.text = day
        month_tag = ET.Element('month')
        month_tag.text = month
        year_tag = ET.Element('year')
        year_tag.text = year
        date_tag.append(day_tag)
        date_tag.append(month_tag)
        date_tag.append(year_tag)
        new_tag.append(name_tag)
        new_tag.append(types_tag)
        new_tag.append(stars_tag)
        new_tag.append(director_tag)
        new_tag.append(date_tag)
        root.insert(0,new_tag)
        tree.write('MovieAll_SPN.xml')
    def removeMovie(self,name):
        tree = ET.parse('MovieAll_SPN.xml')
        root = tree.getroot()
        for movie in root.findall('movie'):
            #print movie.find('name').text
            if movie.find('name').text == name:
                #root = movie.getparent()
                root.remove(movie)
                tree.write('MovieAll_SPN.xml')
        return name + " removed"
    def addInitResolution(self,res):
        tree = ET.parse('MovieAll_SPN.xml')
        root = tree.getroot()
        for movie in root.findall('movie'):
            res_tag = ET.Element('resolution')
            res_tag.text = res
            movie.append(res_tag)
        tree.write('MovieAll_SPN.xml')
        return "resolution added"

    def editResolution(self,name,res):
        tree = ET.parse('MovieAll_SPN.xml')
        root = tree.getroot()
        for movie in root.findall('movie'):
            res_tag = ET.Element('resolution')
            res_tag.text = res
            movie.append(res_tag)
        tree.write('MovieAll_SPN.xml')
        return "resolution added"
    
    def addInitLength(self,length):
        tree = ET.parse('MovieAll_SPN.xml')
        root = tree.getroot()
        for movie in root.findall('movie'):
            len_tag = ET.Element('length')
            len_tag.text = length
            movie.append(len_tag)
        tree.write('MovieAll_SPN.xml')
        return "movie length added"
            
print "start"
server = SOAPServer(("172.31.23.46", 8081))
server.registerObject(webservice(), "xml")
server.serve_forever()




