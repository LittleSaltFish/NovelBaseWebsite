from django.shortcuts import render
from django.db import connection

# Create your views here.
def home(request):
    cursor = connection.cursor()
    # cursor.execute('insert into novels(img_url) values("testinsert2")')
    cursor.execute("select * from novels")
    rows=cursor.fetchall()
    print(rows)
    form_rows=[]
    for row in rows:
        rows_dic={'id':row[0],'url':row[1]}
        form_rows.append(rows_dic)
    return render(request,'FrontPage.html',{"contents":form_rows})

def SearchResult(request):
    SearchInput=request.POST['SearchInput']
    print("获取输入值为"+SearchInput)
    cursor = connection.cursor()
    # cursor.execute('insert into novels(img_url) values("testinsert2")')
    cursor.execute("select * from novels where id ="+str(SearchInput))
    #此处应防范SQL注入，后期添加限制项
    SearchResults=cursor.fetchall()
    print(SearchResults)
    form_rows=[]
    for result in SearchResults:
        results_dic={'id':result[0],'url':result[1]}
        form_rows.append(results_dic)
    return render(request,'SearchResult.html',{"contents":form_rows})

