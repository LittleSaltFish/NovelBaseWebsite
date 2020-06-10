from django.shortcuts import render, redirect
from django.urls import reverse
from django.db import connection
from django.views.generic import View
from book.models import Book

# Create your views here.


class BookDetailView(View):
    def get(self, request, book_id):
        try:  # 查是否有这本书，没有则返回首页
            book = Book.objects.get(book_id=book_id)
        except Book.DoesNotExist:
            # BUG 这边抓不住异常，但是可跳过去
            return redirect(reverse('home'))
        cursor = connection.cursor()  # 获取书籍信息
        cursor.execute("select * from book where book_id="+str(book.book_id))
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
        return render(request, 'BookDetail.html')


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
