from django.shortcuts import render

def home(request):
    ctx = {
        'name': "Tony",
        'age': 25,
        'gains': 2344.322211
    }
    return render(request, 'stat_pgs_tmpl/home.html', ctx)

def contact(request):
    return render(request, 'stat_pgs_tmpl/contact.html')
