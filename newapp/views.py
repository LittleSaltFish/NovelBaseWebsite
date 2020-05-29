from django.shortcuts import render_to_response
import MySQLdb


# Create your views here.

def img_url_lists(request):
    db = MySQLdb.connect(user='root', db='novals', passwd='2.718281828', host='localhost')
    
    return render_to_response('home.html', {"img_urls":urls})
