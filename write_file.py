text = '这是读取文件测试\n这是第二行\n这是最后一行'

my_file = open('my_file.txt','w')
my_file.write(text)
my_file.close()