from django.shortcuts import render, redirect
from django.urls import reverse
from django.db import connection
from django.views.generic import View
from book.models import Book
from chapter.views import format_chapter, get_chapter_by_chapter_id, get_all_chapters

# Create your views here.


def get_all_chapters_by_book_id(id):
    cursor = connection.cursor()
    cursor.execute(
        "select * from chapter where book_id_id="+str(id))
    chapter_rows = cursor.fetchall()
    format_chapter_rows = format_chapter(chapter_rows)
    return format_chapter_rows


def get_book_by_book_id(id):
    # TODO 此处应防范SQL注入 
    cursor=connection.cursor()
    # id=id.replace("'","\'")
    # id = "{}{}{}".format("%", id, "%")
    # NOTE 此处不可模糊匹配，否则索引失效且无意义
    # BUG 百分号被转义
    # print(str(id))
    # cursor.execute(
    #     "select * from book where book_id = "+str(id))
    cursor.execute(
        "select * from book where book_id = %s ",[id]
        )
    book_rows=cursor.fetchall()
    format_book_rows=format_book(book_rows)
    return format_book_rows


def get_book_by_book_name(name):
    # TODO 此处应防范SQL注入
    name = "{}{}{}".format("%%", name, "%%")
    # BUG 百分号被转义，引号被转义，不可上线
    cursor=connection.cursor()
    cursor.execute(
        "select * from book where book_name = %s ;",[name]
        )
    book_rows=cursor.fetchall()
    format_book_rows=format_book(book_rows)
    return format_book_rows


def get_all_books():
    cursor=connection.cursor()
    cursor.execute("select * from book")
    rows=cursor.fetchall()
    format_all_book_rows=format_book(rows)
    return format_all_book_rows


def format_book(rows):
    form_rows=[]
    for row in rows:
        rows_dic={'createtime': row[0],
                    'updatetime': row[1],
                    'is_delete': row[2],
                    'book_id': row[3],
                    'book_img_url': row[4],
                    'book_introduction': row[5],
                    'book_hot_rate': row[6],
                    'book_name': row[7],
                    'book_word_count': row[8],
                    'user_id': row[9],
                    'book_statue':row[10],
                    }
        form_rows.append(rows_dic)
    return form_rows


class BookDetailView(View):
    def get(self, request, book_id):
        try:
            # 查是否有这本书，没有则返回首页
            book = Book.objects.get(book_id=book_id)
        except Book.DoesNotExist:
            return redirect(reverse('home'))
        # 获取书籍信息
        # TODO 后期尝试不用raw写
        format_chapter_rows = get_all_chapters_by_book_id(book.book_id)
        # 获取对应章节信息
        # TODO 后期尝试不用raw写
        format_book_rows = get_book_by_book_id(book.book_id)

        return render(request, 'info_for_book.html', {"form_chapter_rows": format_chapter_rows, "form_book_rows": format_book_rows})


def home(request):
    # cursor = connection.cursor()
    # cursor.execute("select * from book")
    # rows = cursor.fetchall()
    # form_rows = format_book(rows)
    format_all_book_rows = get_all_books()
    format_all_chapter_rows = get_all_chapters()
    return render(request, 'theFrontPage.html', {"all_book_rows": format_all_book_rows, "all_chapter_rows": format_all_chapter_rows})


def SearchResult(request):
    SearchInput = request.POST['SearchInput']
    print("获取输入值为"+SearchInput)
    # cursor = connection.cursor()
    # cursor.execute("select * from book where book_id = "+str(SearchInput))
    # SearchResults = cursor.fetchall()
    # form_rows = format_book(SearchResults)
    format_book_rows_id = get_book_by_book_id(SearchInput)
    format_book_rows_name = get_book_by_book_name(SearchInput)
    format_book_rows=format_book_rows_id+format_book_rows_name
    # BUG 合并id和name的查询结果
    format_chapter_rows_id = get_chapter_by_chapter_id(SearchInput)
    return render(request, 'SearchResult.html', {"search_book_rows": format_book_rows, "search_chapter_rows": format_chapter_rows_id})
