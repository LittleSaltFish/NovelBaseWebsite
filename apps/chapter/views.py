from django.shortcuts import render, redirect
from django.urls import reverse
from django.db import connection
from django.views.generic import View
from chapter.models import Chapter

# Create your views here.


def get_chapter(rows):
    form_rows = []
    for row in rows:
        rows_dic = {'create_time': row[0],
                    'update_time': row[1],
                    'is_delete': row[2],
                    'chapter_id': row[3],
                    'text': row[4],
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
    def get(self, request, chapter_id):
        try:
            # 查是否有这本书，没有则返回首页
            chapter = Chapter.objects.get(chapter_id=chapter_id)
        except Chapter.DoesNotExist:
            # BUG 这边抓不住异常，但是可跳过去
            return redirect(reverse('home'))
        cursor = connection.cursor()
        # 获取书籍信息
        # TODO 后期尝试不用raw写
        # DONE 三块代码有点冗余，可以往一个函数里修正
        cursor.execute("select * from chapter where chapter_id=" +
                       str(chapter.chapter_id))
        rows = cursor.fetchall()
        form_rows = get_chapter(rows)
        return render(request, 'Content.html', {"all_rows": form_rows})


def SearchResult(request):
    SearchInput = request.POST['SearchInput']
    print("获取输入值为"+SearchInput)
    cursor = connection.cursor()
    # cursor.execute('insert into novels(img_url) values("testinsert2")')
    cursor.execute("select * from chapter where chapter_id ="+str(SearchInput))
    # TODO 此处应防范SQL注入，后期添加限制项
    SearchResults = cursor.fetchall()
    form_rows = get_chapter(SearchResults)
    return render(request, 'SearchResult.html', {"search_rows": form_rows})


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
