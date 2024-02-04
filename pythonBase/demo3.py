import json
import xlsxwriter

with open('./demo/demo.json', 'rb') as f:
	content = f.read()
	
	# content = content.decode('gbk')
	
	data = json.loads(content)
	contents = []
	for item in data:
		contents.append(item['html'])
		text = "\n".join(contents)

if __name__ == '__main__':
	workbook = xlsxwriter.Workbook('data.xlsx')
	worksheet = workbook.add_worksheet()
	
	worksheet.write(0, 0, text)
	
	workbook.close()
