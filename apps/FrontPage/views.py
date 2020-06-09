from django.shortcuts import render
from django.db import connection

# Create your views here.


def home(request):
    cursor = connection.cursor()
    # cursor.execute('insert into novels(img_url) values("testinsert2")')
    cursor.execute("select * from chapter")
    rows = cursor.fetchall()
    print(rows)
    form_rows = []
    for row in rows:
        rows_dic = {'chapter_id': row[0], 'text': row[1], 'book_id': row[2], 'chapter_img_url': row[3], 'chapter_introduction': row[4],
                    'chapter_hot_rate': row[5], 'chapter_name': row[6], 'user_id': row[7], 'chapter_word_count': row[8]}
        form_rows.append(rows_dic)
    return render(request, 'FrontPage.html', {"all_rows": form_rows})


def SearchResult(request):
    SearchInput = request.POST['SearchInput']
    print("获取输入值为"+SearchInput)
    cursor = connection.cursor()
    # cursor.execute('insert into novels(img_url) values("testinsert2")')
    cursor.execute("select * from chapter where chapter_id ="+str(SearchInput))
    # TODO 此处应防范SQL注入，后期添加限制项
    SearchResults = cursor.fetchall()
    print(SearchResults)
    form_rows = []
    for result in SearchResults:
        results_dic = {'chapter_id': result[0], 'text': result[1], 'book_id': result[2], 'chapter_img_url': result[3], 'chapter_introduction': result[4],
                       'chapter_hot_rate': result[5], 'chapter_name': result[6], 'user_id': result[7], 'chapter_word_count': result[8]}
        form_rows.append(results_dic)
    return render(request, 'SearchResult.html', {"search_rows": form_rows})
