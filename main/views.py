from django.shortcuts import render

def post(request):
    return render(request, 'main/post.html', {})
