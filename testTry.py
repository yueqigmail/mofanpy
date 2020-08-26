try:
    file = open('try.txt','a')
except Exception as e:
    print(e)
    response = input('需要创建新文件吗？')
    if response == 'y':
        file = open('try.txt','w')

    else:
        pass

else:
    file.write('\n成功创建了新文件')
    file.close()

