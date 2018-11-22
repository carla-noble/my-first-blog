from django.shortcuts import render

# Create
def post_list(request):
    return render(request, 'blog/post_list.html', {})
