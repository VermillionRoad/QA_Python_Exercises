#1. Create a python method that takes arguments int X and int Y,
#and updates DEPART and RETURN fields
#in test_payload1.xml:
#
#- DEPART gets set to X days in the future from the current date
#(whatever the current date is at the moment of executing the code)
#- RETURN gets set to Y days in the future from the current date
#
#Please write the modified XML to a new file.

import xml.etree.ElementTree as ET
import datetime

def parseXML(file):
	return ET.parse(file)

def writeXML(file, path):
	file.write(path)

def bumpDate(value):
	today = datetime.datetime.now()
	today += datetime.timedelta(days=value)
	return (f"{today.year}{today.month}{today.day}")

def updateField(file, field, value):
	for item in file.getroot().iter(field):
		item.text = str(bumpDate(value))
		print(item.text)
	
def updateDepartAndReturn(X, Y):
	file = parseXML('test_payload1.xml')
	
	updateField(file, 'DEPART', X)
	updateField(file, 'RETURN', Y)
		
	writeXML(file, 'modifiedTest_payload.xml')	
		
def main():
	updateDepartAndReturn(-2, 5)
	
if __name__ == "__main__":
	main()