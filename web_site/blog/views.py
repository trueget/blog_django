from django.shortcuts import render

# Create your views here.

def index_page(request):
    return render(request, 'blog/index.html')


# def about_page(request):
#     return render(request, 'about.html')
