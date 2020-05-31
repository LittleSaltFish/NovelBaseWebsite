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
      - [user](#user)
      - [tag](#tag)
      - [fans](#fans)
      - [book(add)](#bookadd)
      - [novel](#novel)
  - [HTML MODEL DESIGN](#html-model-design)
  - [FUNCTION SHOW](#function-show)
    - [首页展示](#首页展示)
    - [查询展示](#查询展示)

<!-- /TOC -->

## PROGRESS

### 数据库端

- [ ] 数据库设计
- [ ] 语句设计

### 网页端

- [x] 搜索功能 @LittleSaltFish
- [x] 网页间跳转 @LittleSaltFish
- [ ] 弹出框操作
- [ ] 登录相关
- [x] 搜索防空跳转 @LittleSaltFish
- [ ] 防sql注入
- [ ] 图片自动调节大小
- [ ] 避免硬编码密码
- [ ] 网页外观设计
- [ ] 首页展示缓存
- [ ] 异步任务处理
- [ ] 富文本编辑器

## ABOUT

大概会做一个网络小说平台

使用Django+BootStrap+MySQL

## GROUP MEMBERS

| 吉祥物 |          数据库组          |               网页组               |
| :----: | :------------------------: | :--------------------------------: |
| 咸某人 | 高楠希<br>王汝婷<br>咸某人 | 钟旭鹏<br>吕奕航<br>吴漾<br>咸某人 |

~~我们的口号是：**将作大死进行到底！**~~ :+1:

## DATABASE STRUCTURE DESIGN

- *still in test now*

### Name : **novels**

### Tables

#### user

| Field | Type  | Null  |  Key  | Default | Extra |
| :---: | :---: | :---: | :---: | :-----: | :---: |
|       |       |       |       |         |       |

#### tag

| Field | Type  | Null  |  Key  | Default | Extra |
| :---: | :---: | :---: | :---: | :-----: | :---: |
|       |       |       |       |         |       |

#### fans

| Field | Type  | Null  |  Key  | Default | Extra |
| :---: | :---: | :---: | :---: | :-----: | :---: |
|       |       |       |       |         |       |

#### book(add)

| Field | Type  | Null  |  Key  | Default | Extra |
| :---: | :---: | :---: | :---: | :-----: | :---: |
|       |       |       |       |         |       |

#### novel

|  Field  |   Type   | Null  |  Key  | Default  |     Extra      |
| :-----: | :------: | :---: | :---: | :------: | :------------: |
|   id    |  int(8)  |  No   |  PRI  | \<null\> | auto_increment |
| img_url | char(50) |  No   |  \\   | \<null\> |       \\       |

## HTML MODEL DESIGN

- [x] home page
- [ ] user page (self/others)
- [ ] noval page
- [ ] write page
- [x] search page

## FUNCTION SHOW

### 首页展示

![gif1](https://github.com/LittleSaltFish/NovelBaseWebsite/blob/master/README/sample1.gif)

### 查询展示

![gif2](https://github.com/LittleSaltFish/NovelBaseWebsite/blob/master/README/sample2.gif)
