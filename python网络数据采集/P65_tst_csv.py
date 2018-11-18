import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://en.wikipedia.org/wiki/Comparison_of_text_editors')
bsobj = BeautifulSoup(html,'html.parser')
table = bsobj.findAll('table',{'class':'wikitable'})[0]
rows = table.findAll('tr')

csv_file = open('../files/edit.csv','wt',newline="",encoding='utf-8')
writer = csv.writer(csv_file)
try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td','th']):
            csvRow.append(cell.get_text())
            writer.writerow(csvRow)
finally:
    csv_file.close()
