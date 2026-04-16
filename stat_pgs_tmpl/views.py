from django.shortcuts import render

def home(request):
    return render(request, 'stat_pgs_tmpl/home.html')

def contact(request):
    return render(request, 'stat_pgs_tmpl/contact.html')