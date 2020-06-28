from django.shortcuts import render, redirect
from django.urls import reverse
from django.db import connection
from django.views.generic import View
from chapter.models import Chapter

# Create your views here.


def get_chapter_by_chapter_id(id):
    cursor = connection.cursor()
    cursor.execute("select * from chapter where chapter_id=" + str(id))
    rows = cursor.fetchall()
    format_chapter_rows = format_chapter(rows)
    return format_chapter_rows


def format_chapter(rows):
    form_rows = []
    for row in rows:
        content=row[4].replace("script","sc ri pt")
        # NOTE 防xss攻击
        rows_dic = {'create_time': row[0],
                    'update_time': row[1],
                    'is_delete': row[2],
                    'chapter_id': row[3],
                    # 'text': row[4],
                    'text':content,
                    'chapter_img_url': row[5],
                    'chapter_introduction': row[6],
                    'chapter_hot_rate': row[7],
                    'chapter_name': row[8],
                    'chapter_word_count': row[9],
                    'book_id_id': row[10],
                    'user_id_id': row[11]}
        form_rows.append(rows_dic)
    return form_rows


class ChapterDetailView(View):
    def get(self, request,book_id_id, chapter_id):
        try:
            # 查是否有这本书，没有则返回首页
            chapter = Chapter.objects.get(chapter_id=chapter_id)
        except Chapter.DoesNotExist:
            # BUG 这边抓不住异常，但是可跳过去
            return redirect(reverse('home'))
        # 获取书籍信息
        # TODO 后期尝试不用raw写
        # cursor = connection.cursor()
        # cursor.execute("select * from chapter where chapter_id=" +
        #                str(chapter.chapter_id))
        # rows = cursor.fetchall()
        # form_rows = format_chapter(rows)
        format_chapter_rows = get_chapter_by_chapter_id(chapter.chapter_id)
        return render(request, 'ChapterContent.html', {"all_rows": format_chapter_rows})


def SearchResult(request):
    SearchInput = request.POST['SearchInput']
    print("获取输入值为"+SearchInput)
    # # TODO 此处应防范SQL注入，后期添加限制项
    # cursor = connection.cursor()
    # cursor.execute("select * from chapter where chapter_id ="+str(SearchInput))
    # SearchResults = cursor.fetchall()
    # form_rows = format_chapter(SearchResults)
    format_chapter_rows = get_chapter_by_chapter_id(SearchInput)
    return render(request, 'SearchResult.html', {"search_rows": format_chapter_rows})


# def contentresult(request):
#     cursor = connection.cursor()
#     # cursor.execute('insert into novels(img_url) values("testinsert2")')
#     cursor.execute("select * from chapter")
#     rows = cursor.fetchall()
#     print(rows)
#     form_rows = []
#     for row in rows:
#         rows_dic = {'createtime': row[0],
#                     'updatetime': row[1],
#                     'isdelete': row[2],
#                     'chapter_id': row[3],
#                     'chapter_img_url': row[4],
#                     'chapter_introduction': row[5],
#                     'chapter_hot_rate': row[6],
#                     'chapter_name': row[7],
#                     'chapter_word_count': row[8],
#                     'user_id': row[9], }
#         form_rows.append(rows_dic)
#     return render(request, 'FrontPage.html', {"all_rows": form_rows})

# def SelectChapterResult(request):
#     cursor = connection.cursor()
#     # cursor.execute('insert into novels(img_url) values("testinsert2")')
#     cursor.execute("select * from chapter")
#     rows = cursor.fetchall()
#     print(rows)
#     form_rows = []
#     for row in rows:
#         rows_dic = {'createtime': row[0],
#                     'updatetime': row[1],
#                     'isdelete': row[2],
#                     'chapter_id': row[3],
#                     'text':row[4],
#                     'chapter_img_url': row[5],
#                     'chapter_introduction': row[6],
#                     'chapter_hot_rate': row[7],
#                     'chapter_name': row[8],
#                     'chapter_word_count': row[9],
#                     'book_id':row[10],
#                     'user_id': row[11], }
#         form_rows.append(rows_dic)
#     return render(request, 'Content.html', {"all_rows": form_rows})
