# 数据库大作业

<!-- TOC -->

- [数据库大作业](#数据库大作业)
  - [PROGRESS](#progress)
    - [数据库端](#数据库端)
    - [网页端](#网页端)
  - [ABOUT](#about)
  - [GROUP MEMBERS](#group-members)
  - [DATABASE STRUCTURE DESIGN](#database-structure-design)
    - [Name : **novels**](#name--novels)
    - [Tables](#tables)
      - [user(each user has a table,name as userid)](#usereach-user-has-a-tablename-as-userid)
      - [tag](#tag)
      - [fans](#fans)
      - [book(each book has a table,name as bookid)](#bookeach-book-has-a-tablename-as-bookid)
      - [book_id](#book_id)
      - [novel(add about the commit)](#noveladd-about-the-commit)
  - [HTML MODEL DESIGN](#html-model-design)
  - [FUNCTION SHOW](#function-show)
    - [首页展示](#首页展示)
    - [查询展示](#查询展示)

<!-- /TOC -->

## PROGRESS

### 数据库端

- [ ] 数据库设计
- [ ] 语句设计
- [ ] 作为备份的触发器和表结构设计
- [ ] 密码加盐

### 网页端

- [x] 搜索功能 @LittleSaltFish
- [x] 网页间跳转 @LittleSaltFish
- [ ] 弹出框操作
- [ ] 登录相关
- [x] 搜索防空跳转 @LittleSaltFish
 - [ ] 防sql注入 <!-- NOTE 可以尝试更改结束符防注入/设计权限防止操作 -->
- [ ] 图片自动调节大小
- [ ] 避免硬编码密码
- [ ] 网页外观设计
- [ ] 首页展示缓存
- [ ] 异步任务处理
- [ ] 富文本编辑器
- [ ] 评论区预加载技术（强制要求文末按按钮打开评论）

## ABOUT

大概会做一个网络小说平台

使用Django+BootStrap+MySQL

## EXPAND USAGE

结合nlp、用户画像、推荐系统都是不错的出路

甚至可以考虑改为电商网站

## GROUP MEMBERS

| 吉祥物 |          数据库组          |               网页组               |
| :----: | :------------------------: | :--------------------------------: |
| 咸某人 | 高楠希<br>王汝婷<br>咸某人 | 钟旭鹏<br>吕奕航<br>吴漾<br>咸某人 |

~~我们的口号是：**将作大死进行到底！**~~ :+1:

## DATABASE STRUCTURE DESIGN

- *still in test now*

### Name : **novels**

### Tables

#### book_backup

(put all novels in one table to avoid mass)

|       Field       |   Type    | Null  |  Key  | Default |     Extra      |
| :---------------: | :-------: | :---: | :---: | :-----: | :------------: |
|     backup_id     |  int(10)  |       |  PRI  |         | auto_increment |
|   book_img_url    | char(50)  |       |       |         |                |
|  book_word_count  |  int(10)  |       |       |         |                |
|     book_name     | char(50)  |       |       |         |                |
|   refresh_flag    |  boolean  |       |       |  true   |                |
|    chapter_id     |  int(8)   |       |       |         |                |
|      user_id      |  int(8)   |       |       |   -1    |                |
|   book_hot_rate   |  int(10)  |       |       |         |                |
|    zip_tag_id     | int(1000) |       |       |         |                |
| book_introduction | char(500) |       |       |         |                |
|   chapter_count   |  int(10)  |       |       |         |                |

#### user_backup

(put all users in one table to avoid mass)

|       Field        |   Type    | Null  |  Key  | Default |     Extra      |
| :----------------: | :-------: | :---: | :---: | :-----: | :------------: |
|     backup_id      |  int(10)  |       |  PRI  |         | auto_increment |
|    user_img_url    | char(50)  |       |       |         |                |
|     user_name      | char(50)  |       |       |         |                |
|        key         | char(50)  |       |       | 1234567 |                |
|       gender       | char(50)  |       |       |         |                |
|       grade        |  int(1)   |       |       |         |                |
|       Email        | char(50)  |       |       |         |                |
| user_introduction  | char(50)  |       |       |         |                |
|      user_id       |  int(8)   |       |       |         |                |
|    zip_book_id     |  int(8)   |       |       |         |                |
|   zip_book_mark    |  int(8)   |       |       |         |                |
| zip_follow_user_id | char(800) |       |       |         |                |

#### user_message

(each user has a table , name as userid)

|       Field       |   Type   | Null  |  Key  | Default |     Extra      |
| :---------------: | :------: | :---: | :---: | :-----: | :------------: |
|      user_id      |  int(8)  |       |  PRI  |         | auto_increment |
|   user_img_url    | char(50) |       |       |         |                |
|     user_name     | char(50) |       |       |         |                |
|        key        | char(50) |       |       | 1234567 |                |
|      gender       | char(50) |       |       |    0    |                |
|       grade       |  int(1)  |       |       |         |                |
|       Email       | char(50) |       |       |         |                |
| user_introduction | char(50) |       |       |         |                |

#### follow

|    Field    |  Type  | Null  |  Key  | Default |     Extra      |
| :---------: | :----: | :---: | :---: | :-----: | :------------: |
|   fans_id   | int(8) |       |  PRI  |         | auto_increment |
|  user_id1   | int(8) |       |       |         |                |
| follow_flag | int(1) |       |       |         |                |
|  user_id2   | int(8) |       |       |         |                |

#### star

|   Field   |  Type  | Null  |  Key  | Default |     Extra      |
| :-------: | :----: | :---: | :---: | :-----: | :------------: |
|  star_id  | int(8) |       |  PRI  |         | auto_increment |
|  user_id  | int(1) |       |       |         |                |
|  book_id  | int(8) |       |       |         |                |
| book_mark | int(8) |       |       |         |                |

#### inform

|    Field    |  Type  | Null  |  Key  | Default |     Extra      |
| :---------: | :----: | :---: | :---: | :-----: | :------------: |
|  inform_id  | int(8) |       |  PRI  |         | auto_increment |
| inform_flag | int(1) |       |       |         |                |
|   root_id   | int(8) |       |       |         |                |
|   user_id   | int(8) |       |       |         |                |

#### book_massage

(each book has a table , name as bookid)

|        Field         |   Type    | Null  |  Key  | Default |     Extra      |
| :------------------: | :-------: | :---: | :---: | :-----: | :------------: |
|       book_id        |  int(8)   |       |  PRI  |         | auto_increment |
|     book_img_url     | char(50)  |       |       |  <-1>   |                |
|  book_introduction   | char(500) |       |       |         |                |
|    book_hot_rate     |  int(10)  |       |       |         |                |
|      book_name       | char(50)  |       |       |         |                |
|       user_id        |  int(8)   |       |       |  <-1>   |                |
|   book_word_count    |  int(10)  |       |       |         |                |

#### ~~novel~~chapter

(link book's detail with chapters)

|        Field         |   Type    | Null  |  Key  | Default |     Extra      |
| :------------------: | :-------: | :---: | :---: | :-----: | :------------: |
|      chapter_id      |  int(8)   |       |  PRI  |         | auto_increment |
|       book_id        |  int(8)   |       |       |         |                |
|   chapter_img_url    | char(50)  |       |       |  <-1>   |                |
| chapter_introduction | char(500) |       |       |         |                |
|   chapter_hot_rate   |  int(10)  |       |       |         |                |
|     chapter_name     | char(50)  |       |       |         |                |
|       user_id        |  int(8)   |       |       |  <-1>   |                |
|  chapter_word_count  |  int(10)  |       |       |         |                |

#### chapter_comment

|          Field          |   Type   | Null  |  Key  | Default |     Extra      |
| :---------------------: | :------: | :---: | :---: | :-----: | :------------: |
|       comment_id        |  int(8)  |       |  PRI  |         | auto_increment |
|       chapter_id        |  int(8)  |       |       |         |                |
| chapter_comment_img_url | char(50) |       |       |  <-1>   |                |
|         user_id         |  int(8)  |       |       |  <-1>   |                |

#### book_comment

|        Field         |   Type   | Null  |  Key  | Default |     Extra      |
| :------------------: | :------: | :---: | :---: | :-----: | :------------: |
|      comment_id      |  int(8)  |       |  PRI  |         | auto_increment |
|       book_id        |  int(8)  |       |       |         |                |
| book_comment_img_url | char(50) |       |       |  <-1>   |                |
|       user_id        |  int(8)  |       |       |  <-1>   |                |

#### tag

(each tag has a table , name as bookid)

|   Field    |  Type  | Null  |  Key  | Default | Extra |
| :--------: | :----: | :---: | :---: | :-----: | :---: |
|   tag_id   | int(8) |       |  PRI  |         |       |
|   tag_id   | int(8) |       |       |         |       |
| chapter_id | int(8) |       |       |         |       |

#### tag_massage

(link tag's detail with bookid)

|    Field     |   Type   | Null  |  Key  | Default |     Extra      |
| :----------: | :------: | :---: | :---: | :-----: | :------------: |
|    tag_id    |  int(8)  |       |  PRI  |         | auto_increment |
| tag_img_url  | char(50) |       |       |  <-1>   |                |
| tag_hot_rate |  int(8)  |       |       |         |                |
|   tag_name   | char(50) |       |       |         |     unique     |

## HTML MODEL DESIGN

- [x] home page
- [ ] user page (self/others)
- [ ] novel page
- [ ] write page
- [x] search page

## FUNCTION SHOW

### 首页展示

![gif1](https://github.com/LittleSaltFish/NovelBaseWebsite/blob/master/README/sample1.gif)

### 查询展示

![gif2](https://github.com/LittleSaltFish/NovelBaseWebsite/blob/master/README/sample2.gif)
