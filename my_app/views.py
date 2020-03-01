from django.shortcuts import render
import requests
from requests.compat import quote_plus
from bs4 import BeautifulSoup
from . import models
import re

url = 'https://losangeles.craigslist.org/search/sss?query={}'

def home(request):
    # View for home
    return render(request, 'base.html' )

def new_search(request):
    # View for new_search
    search = request.POST.get('search')
    models.Search.objects.create(search=search)
    final_url = url.format(quote_plus(search))
    res = requests.get(final_url)
    data = res.text
    soup = BeautifulSoup(data, features='html.parser')
    search_list = soup.find_all('li', {'class': 'result-row'})

    final_postings = []
    for post in search_list:
        post_title = post.find(class_='result-title').text
        post_url = post.find('a').get('href')
        post_img = post.find(class_='result-image').get('data-ids')
        post_price = post.find(class_='result-price').text
        if not post_img :
            post_img = "peace,None"
        img_id = re.split(',|:',post_img)
        src_img = "https://images.craigslist.org/{}_300x300.jpg".format(img_id[1])
        final_postings.append((post_title, post_url, post_price, src_img))


    context = {
        'search':search,
        'final_postings': final_postings,
    }
    return render(request, 'my_app/new_search.html', context)
