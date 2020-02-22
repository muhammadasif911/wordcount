from django.shortcuts import render
import operator

def homepage(request):
    return render(request,'home.html')


def aboutus(request):
    return render(request,'about_us.html')


def count(request):
    fulltext = request.GET['fulltext']
    word_list = fulltext.split()

    word_dict = {}
    for word in word_list:
        if word in word_dict:
            word_dict[word]+=1
        else:
            word_dict[word] = 1

    sorted_word = sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True)
    return render(request,'count.html',{'fulltext':fulltext, 'count':len(word_list),'sorted_word':sorted_word})