from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request , 'index.html')

def count(request):

    ######## to get the words HTML #########
    textarea = request.GET['textarea']

    ######## count Words ###########
    countwords = len(textarea.split())

    ######### count Characters ##########
    countChar = 0
    for xx in textarea:
        if xx == ' ' :
            continue
        countChar += 1

    ######## for order the words ########
    #ordd = sorted(dic.items() , key=lambda item: item[1] , reverse=True)
    dic = dict()
    splword = textarea.split()
    for word in splword :
        if word == '--' :
            continue
        dic[word] = dic.get(word , 0 ) + 1
    orderr = sorted(dic.items() , key=lambda x: x[1] , reverse =True)





    return render(request , 'count.html' , {'stringtextarea' : countwords ,'thirdd' : countChar , 'yourtext' : textarea , 'dic' : orderr })

#    return render(request , 'count.html' , {'stringtextarea' : count ,'thirdd' : countt , 'yourtext' : textarea })
#
#    def count(request):
#        textarea = request.GET['textarea']
#
#        count = 0
#        countt = 0
#
#        textt = textarea.split()
#        for x in textt :
#            count += 1
#
#        for xx in textarea:
#            if xx == ' ' :
#                continue
#            countt += 1
#
#
#
#
#    return render(request , 'count.html' , {'stringtextarea' : count ,'thirdd' : countt , 'yourtext' : textarea })

def about(request):
    return render(request , 'about.html')
