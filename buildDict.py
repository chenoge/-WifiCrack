import itertools

# 如需要，可加入大写字母及其他符号
words = '0123456789abcdefghijklmnopqrstuvwxyz'
fileIndex = 1  # 当前字典文件编号
index = 0 # 当前字典文件中，正在生成的密码编码
# 长度为8~10位数
for digit in range(8, 9):
	f = open('dict/' + str(digit) + '_' + str(fileIndex) + '.txt', 'w')
	keys = itertools.product(words, repeat = digit)
	for key in keys:
		f.write(''.join(key) + '\n')
		index = (index + 1) % 200000
		if not index :
			f.close()
			fileIndex = fileIndex + 1
			f = open('dict/' + str(digit) + '_' + str(fileIndex) + '.txt', 'w')
	index = 0
	fileIndex = fileIndex + 1