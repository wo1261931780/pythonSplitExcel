import pandas as pd


# 分割文本的函数
def split_by_keywords(text, keywords):
	# 初始化分割结果字典
	split_results = {keyword: "" for keyword in keywords}
	start_pos = 0
	for keyword in keywords:
		# 查找关键词位置
		found_pos = text.find(keyword, start_pos)
		if found_pos != -1:
			# 截取前一个关键词到当前关键词之间的文本
			split_results[keyword] = text[start_pos:found_pos].strip()
			start_pos = found_pos
		else:
			break  # 如果关键词没有找到，停止处理
	
	# 截取最后一个关键词之后的所有文本
	split_results[keywords[-1]] = text[start_pos:].strip()
	
	return pd.Series(split_results)


if __name__ == '__main__':
	# 读取xlsx文件
	df = pd.read_excel('./demo/demo.xlsx')
	
	# 关键词列表
	keywords = [
		"/正文", "研究方向", "主要经历", "教育", "工作", "兼职",
		"教学", "开设课程", "教学项目", "科研成果", "学术论文", "会议论文",
		"媒体随笔", "学术编著", "科研项目", "主持", "参与", "奖项", "联系方式"
	]
	# 应用分割函数到每一行
	split_df = df['html'].apply(split_by_keywords, keywords=keywords)
	
	# 将分割后的新DataFrame与原始DataFrame合并
	result_df = pd.concat([df, split_df], axis=1)
	
	# 查看结果
	print(result_df)
	
	# 保存到一个新的xlsx文件
	result_df.to_excel('demo1.xlsx', index=False)
