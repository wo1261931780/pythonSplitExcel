import json
import xlsxwriter

with open('./demo/demo.json', 'rb') as f:
	content = f.read()
	data = json.loads(content)

contents = []
for item in data:
	contents.append(item['html'])

text = "\n".join(contents)

cols = []
for html in text.split("\n"):
	if html == "/正文":
		cols.append([html])
	else:
		cols[-1].append(html)

workbook = xlsxwriter.Workbook('data.xlsx')
worksheet = workbook.add_worksheet()

for i, col in enumerate(cols):
	for j, cell in enumerate(col):
		worksheet.write(j, i, cell)

workbook.close()
