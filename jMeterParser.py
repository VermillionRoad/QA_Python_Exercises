#3. Create a python script that parses jmeter log files in CSV format,
#and in the case if there are any non-successful endpoint responses recorded in the log,
#prints out the label, response code, response message, failure message,
#and the time of non-200 response in human-readable format in PST timezone
#(e.g. 2021-02-09 06:02:55 PST).
#
#Please use Jmeter_log1.jtl, Jmeter_log2.jtl as input files for testing out your script
#(the files have .jtl extension but the format is  CSV).

import csv
import datetime

def parseJTL(file, fields, entries):
	with open(file) as jtlfile:
		jtlreader = csv.reader(jtlfile)
		fields = next(jtlreader)
		entries = list(jtlreader)
	return fields, entries

def findField(fields, field):
	return fields.index(field)
	
def findErrors(fields, entries):
	column = findField(fields, "success")
	for entry in entries:
		if entry[column] != "true":
			printError(entry, fields)
	
def printTime(time):
	date = datetime.datetime.fromtimestamp(time / 1000, datetime.timezone.utc) - datetime.timedelta(hours=8)
	date = date.strftime("%m/%d/%Y, %H:%M:%S")
	return date
	
def printError(entry, fields):
	print("Error:")
	print("Label:", entry[findField(fields,"label")])
	print("Response Code:", entry[findField(fields,"responseCode")])
	print("Response Message:", entry[findField(fields,"responseMessage")])
	print("Failure Message:", entry[findField(fields,"failureMessage")])
	print("Time:", printTime(int(entry[findField(fields,"timeStamp")])), "PST")
	print()
	
def parseJTLErrors(file):
	fields = []
	entries = []
	
	print("Parsing errors from ", file)
	
	fields, entries = parseJTL(file, fields, entries)
	findErrors(fields, entries)
	
	print("Finished!\n")
		
def main():
	parseJTLErrors("Jmeter_log1.jtl")
	parseJTLErrors("Jmeter_log2.jtl")
	
if __name__ == "__main__":
	main()