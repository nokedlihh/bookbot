def count_words(text):
    words=text.split()
    counter=0
    for i in words:
        counter +=1
    return counter

def sorter(puszedli):
    return puszedli["num"]

def count_char(text):
    words=text.lower()
    dic = {}
    for i in words:
        if i in dic and str.isalpha(i) == True:
            dic[i]=dic[i]+1
        elif str.isalpha(i)==True:
            dic[i]=1
    cucc=[]
    for i in dic:
        value= dic[i]
        cucc.append({"char":i, "num":value},)
    cucc.sort(reverse=True, key=sorter)
    return cucc