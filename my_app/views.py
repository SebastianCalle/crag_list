from django.shortcuts import render

# Create your views here.
def home(request):
    # View for home
    return render(request, 'base.html' )

def new_search(request):
    # View for new_search
    search = request.POST.get('search')
    context = {
        'search':search,
    }
    return render(request, 'my_app/new_search.html', context)
