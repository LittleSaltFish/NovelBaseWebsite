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
