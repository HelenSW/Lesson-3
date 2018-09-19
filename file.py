with open('referat.txt', 'r', encoding='utf-8') as f:
    content=f.read()
    print(len(content))
    #эта часть нужна только для подсчета количества слов
    #content=content.split()
    #print(len(content))
    content=content.replace('.','!')
    print(content)
    with open('referat2.txt', 'w', encoding='utf-8') as f:
        f.write(content)