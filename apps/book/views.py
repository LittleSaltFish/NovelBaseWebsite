from django.shortcuts import render, redirect
from django.urls import reverse
from django.db import connection
from django.views.generic import View
from book.models import Book
from chapter.views import get_chapter

# Create your views here.


def get_book(rows):
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
    return form_rows


class BookDetailView(View):
    def get(self, request, book_id):
        try:
            # 查是否有这本书，没有则返回首页
            book = Book.objects.get(book_id=book_id)
        except Book.DoesNotExist:
            # BUG 这边抓不住异常，但是可跳过去
            return redirect(reverse('home'))
        cursor = connection.cursor()
        # 获取书籍信息
        # TODO 后期尝试不用raw写
        cursor.execute("select * from chapter where book_id_id="+str(book.book_id))
        rows = cursor.fetchall()
        form_rows=get_chapter(rows)
        return render(request, 'BookDetail.html', {"all_rows": form_rows})


def home(request):
    cursor = connection.cursor()
    # cursor.execute('insert into novels(img_url) values("testinsert2")')
    cursor.execute("select * from book")
    rows = cursor.fetchall()
    form_rows = get_book(rows)
    return render(request, 'FrontPage.html', {"all_rows": form_rows})


def SearchResult(request):
    SearchInput = request.POST['SearchInput']
    print("获取输入值为"+SearchInput)
    cursor = connection.cursor()
    # cursor.execute('insert into novels(img_url) values("testinsert2")')
    cursor.execute("select * from book where book_id = "+str(SearchInput))
    # TODO 此处应防范SQL注入，后期添加限制项
    SearchResults = cursor.fetchall()
    form_rows = get_book(SearchResults)
    return render(request, 'SearchResult.html', {"search_rows": form_rows})
