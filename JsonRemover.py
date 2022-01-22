#2. Create a python method that takes a json element
#as an argument, and removes that element from test_payload.json.
#
#Please verify that the method can remove either nested or non-nested elements
#(try removing "outParams" and "appdate").
#
#Please write the modified json to a new file.
import json

def parseJSON(path):
	return json.load(open(path))

def writeJSON(data, path):
	file = open(path, "w")
	json.dump(data, file, indent=2)
	file.close()
	
def removeElement(json, element):
	if (json.get(element, 0) != 0):
		json.pop(element, None)
	else:
		for key,value in json.items():
			if isinstance(value, dict):
				removeElement(value,element)
	
def removeJSONElement(element):
	json = parseJSON('test_payload.json')
	
	removeElement(json, element)
	
	writeJSON(json, 'modifiedTest_payload.json')	
		
def main():
	removeJSONElement("retdt")
	
if __name__ == "__main__":
	main()