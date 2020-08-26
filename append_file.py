append_text = '\n这是追加的一句话'

my_file = open('my_file.text','a')
my_file.write(append_text)
my_file.close()