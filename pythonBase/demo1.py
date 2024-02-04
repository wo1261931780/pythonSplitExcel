import pandas as pd


# 定义一个分列函数
def split_column(text):
	# 根据“代表性奖项”进行分列
	parts = text.split('代表性奖项', 1)
	return parts[0], parts[1] if len(parts) > 1 else ''


if __name__ == '__main__':
	# 读取xlsx文件
	df = pd.read_excel('./demo/demo.xlsx')
	
	# 对每一行应用分列函数
	df[['前半部分', '后半部分']] = df.apply(lambda row: split_column(row['html']), axis=1, result_type='expand')
	
	# 查看结果
	print(df)
	
	# 如果需要，可以将结果保存回xlsx文件
	df.to_excel('demo1.xlsx', index=False)
