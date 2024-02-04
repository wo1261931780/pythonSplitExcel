
import pandas as pd

if __name__ == '__main__':
	# 加载Excel文件，指定openpyxl作为引擎
	df = pd.read_excel("./demo/teacherInfo.xlsx", engine='openpyxl')
	
	# 假设我们要分列的列名为'TextColumn'，并且文本用逗号分隔
	df_split = df['html'].str.split('研究方向', expand=True)
	
	# 将分列后的数据赋回原始的DataFrame
	df[df_split.columns] = df_split
	
	# 保存回Excel文件，如果是非常大的文件，可以考虑保存为CSV格式
	df.to_excel('path_to_your_modified_excel_file.xlsx', index=False)
