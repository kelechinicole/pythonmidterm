import csv


streetsCSV = r"C:\Users\kelei\PycharmProjects\JupyterProject\data\streets.csv"

def listheadernames(csvfilepath):
    with open(csvfilepath, 'r') as csvFile:
        reader = csv.reader(csvFile)
        headers = reader.__next__()
        headerlist = []
        for header in headers:
            headerlist.append(header)# Ge
        csvFile.close()# t the first row as headers
        return headerlist
with open(streetsCSV, 'r') as csvFile:
    reader = csv.reader(csvFile)
    print(reader)
    headers = reader.__next__()

headernames = listheadernames(streetsCSV)
print(headernames)



