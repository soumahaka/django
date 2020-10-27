from django.shortcuts import render

# Create your views here.


""" Les vues qui manipulent la logique derriere les pages html """
def homepage(request):
    """ deux elements de dictionnaire quon a injecte dans ce fichier 
    html """
    homepageData={"key1": "hello world", "key2":200}
    return render(request, 'app5/homepage.html', homepageData)


def otherpage(request):
    return render(request, 'app5/otherpage.html')



def relativepage(request):
    return render(request, 'app5/relativepage.html')