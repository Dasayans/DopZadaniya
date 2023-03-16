l= []
with open('synonyms.txt', 'r+') as file:
    for line in file:
        if line!="\n":
            l.append([i.lower().strip().replace(';', '') for i in line.split() if i!='-'])
    # for i in l:
    #     print(i)
    d = {}
    for a in l:
        for b in a:
            d[b] = set([c for c in a if c!=b])
    # for i in d:
    #     print(i,d.get(i));
    # print(d.get('предвзятый'))
    s=input('Введите слово для поиска синонима: ').lower().strip()
    if d.get(s) == None:
        print("Такого слова нет в словаре!")
    else:
        print('Синонимы подходящие под ваше слово: ', d.get(s))
        c = input("Вас устраивает работа программы? (Y = да / N = нет)\n")
        if c == "N":
            newword = input("Введите слово, которое считаете более подходящим: ")
            # print(newword)
            nw = d.get(s)
            nw.add(s)
            nw.add(newword)
            print('Теперь набор подходящих синонимов выглядит вот так: ',nw)
            for i in nw:
                d[i] =  set([c for c in nw if c!=i])
            file.write("\n" + ' '.join(list(nw)))


print('Cпасибо что воспользовались этой программой!')