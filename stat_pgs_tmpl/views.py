from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    ctx = {
        'name': "Tony",
        'age': 25,
        'gains': 2344.322211
    }
    return render(request, 'stat_pgs_tmpl/home.html', ctx)

def contact(request):
    return render(request, 'stat_pgs_tmpl/contact.html')

@login_required
def p1(request):
    body = {
        'user2': "John",
        'login': True,
        'password_length': 16
    }
    return render(request, 'stat_pgs_tmpl/page1.html', body)

@login_required
def p2(request):
    content2 = {
        'list1': [1, 2, 100, 200],
        'dict1': {"A": 1, "B": 2, "C": 3, "D": 4, "E": 3}
    }
    return render(request, 'stat_pgs_tmpl/page2.html', content2)
