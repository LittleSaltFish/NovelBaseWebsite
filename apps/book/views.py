from django.shortcuts import render
from django.db import connection
from django.views.generic import View

# Create your views here.


def home(request):
    cursor = connection.cursor()
    # cursor.execute('insert into novels(img_url) values("testinsert2")')
    cursor.execute("select * from book")
    rows = cursor.fetchall()
    print(rows)
    form_rows = []
    for row in rows:
        rows_dic = {'createtime': row[0],
                    'updatetime': row[1],
                    'is_delete': row[2],
                    'book_id': row[3],
                    'book_img_url': row[4],
                    'book_introduction': row[5],
                    'book_hot_rate': row[6],
                    'book_name': row[7],
                    'book_word_count': row[8],
                    'user_id': row[9], }
        form_rows.append(rows_dic)
    return render(request, 'FrontPage.html', {"all_rows": form_rows})


def SearchResult(request):
    SearchInput = request.POST['SearchInput']
    print("获取输入值为"+SearchInput)
    cursor = connection.cursor()
    # cursor.execute('insert into novels(img_url) values("testinsert2")')
    cursor.execute("select * from book where book_id = "+str(SearchInput))
    # TODO 此处应防范SQL注入，后期添加限制项
    SearchResults = cursor.fetchall()
    print(SearchResults)
    form_rows = []
    for result in SearchResults:
        results_dic = {'createtime': result[0],
                       'updatetime': result[1],
                       'is_delete': result[2],
                       'book_id': result[3],
                       'book_img_url': result[4],
                       'book_introduction': result[5],
                       'book_hot_rate': result[6],
                       'book_name': result[7],
                       'book_word_count': result[8],
                       'user_id': result[9], }
        form_rows.append(results_dic)
    return render(request, 'SearchResult.html', {"search_rows": form_rows})

