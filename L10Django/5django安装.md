官网 https://www.djangoproject.com/download/
版本选择：
1.3 上古版本
1.8 三五年前项目
1.11  第一带版本的最后一个中版本，最后一个支持python2的版本。
2.0以后  更完善的功能，仅支持python3
(LTS)long-term support 长期维护版，公司开发选用，更稳定 




目前2.2.3 （推荐）
安装  
`pip install Django`
`pip install Django==2.2.3` 特定版本


报错：网不好会报无合适版本或重试最大次数错误。

## 创建项目
安装django后会一并安装django-admin.exe的命令行工具。
1. cd 到放项目的目录下
2. django-admin startproject [project name]

基本项目结构介绍：
manage.py   命令行工具，负责运行、创建子模块等功能，跟django-admin 。
mysite 跟项目同名的子包
mysite/settings.py   工程项目设置文件。数据库、时区、语言等，方便其它地方调用。
mysite/urls.py   url路由，指向不同的视图函数。
mysite/wsgi     通用网关接口。部署时用到。

## 运行测试服务器
测试服务器性能低，不负责高并发，仅供单人开发访问用。
cd 到项目文件夹下
`python manage.py runserver`   
与平时python xxx.py 不同，manage.py被第三方工具封装成了CLI命令行工具，
后面runserver是一个参数。
`python manage.py runserver 0.0.0.0:8000`  自定义访问者ip和开放端口

manage.py的源码理解，把settings路径作为系统环境变量注入，sys.arv搜集命令行参数，最终交给cmdline函数运行。

## 创建app
` python manage.py startapp [appname]`
project VS apps ,django项目里的app并不是我们平时所说的应用。一个项目、一个应用在project，django框架中的app是一个更小级别的划分，代表一个大模块。
比如大型项目教育网站，权限、学生、教室、后台，每个大模块下有几十个页面功能。都写在一起脚本太大不好维护，所以django小项目可以一个模块，大项目可以按逻辑分为多个app（子应用）。

目录：
app/migrations： 数据库迁移桥本
admin.py        自带的后台配置文件，快捷实现表CRUD
models.py       定义数据库表结构
tests.py        单元测试
views.py        功能逻辑，渲染页面。

修改文件自动重启，django debug开发模式自动重启服务。

## 整体流程
客户端发起请求
全局urls（项目同名包下的） 查询指向视图或子app下url 
app下子url继续匹配，成功匹配指向视图函数
视图函数进行业务逻辑处理，返回http响应信息(html源代码)
浏览器加载响应html代码，看到结果

http://127.0.0.1:8000/polls/index/
-----ip和端口-------*全局url*子url*

## 报错
1. 启动服务 unicodeDecodeError：utf-8 can not 
原因 源代码gethostaddr() ，windows默认编码gbk，计算机名为中文会导致报错。 解决，我的电脑右键属性修改计算机名为英文。
2. 404,url找不到
原因url配置错误。
分析，观察报错url规则，看目录层级，url正斜杠。
浏览器请求的url如果最后没有正斜杠，django会自动补充。
一般情况，url配置文件里的匹配规则正斜杠结尾。
3. 套接字无权限操作
原因，某些软件占用了8000端口。
解决，结束软件或更改服务端口。

## 配置settings.py
mysql连用户名 密码。项目大型后会有很多配置，如果写在每一个py脚本中将会产生重复代码。解决方案是在 py  .json 配置文件声明键值对变量。其它各个py脚本引用变量。
配置变量习惯上全大写字母命名。  

数据库配置
`
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
`
默认sqlite,其它mysql，postgresql



其它，详见settings.py注释


## ORM
文档位置  模型层-supported database ，http://d.u753.com/ref/databases.html
配置settings-database http://d.u753.com/ref/settings.html#std:setting-NAME
mysql:
1. 官方推荐驱动mysqlclient
`pip install mysqlclient`
2. 确认字符集为utf-8
登录mysql客户端 `show variables like 'character%';`
主要看server database两个变量的值。
3. settings
`
# 'default': {
    #     'ENGINE': 'mysql.connector.django',   # 对应驱动 mysql connector/python .exe安装包
    #     # 'ENGINE': 'django.db.backends.mysql',   # 对应 mysqlclient ，django2.2暂时不支持mysql8.0版本
    #     'NAME': 'django_test',  # database/schema 名
    #     'USER': 'root',
    #     'PASSWORD': '56tyghbn',
    #     'HOST': '127.0.0.1',
    #     'PORT': '3306',
    #     'OPTIONS': {
    #         # 'read_default_file': '/path/to/my.cnf',
    #     },
    # }`


### 迁移
1. model.py 用类的方式定义表结构。
2. 想要使用和生成表结构的app需要先加入到settings中的installed_apps
3. 生成sql  `python manage.py  makemigrations  [app_name]`   ，生成的迁移脚本在migrations文件夹下。
3. （可选）`python manage.py sqlmigrate [appname] [sqlNo]` 看sql语句。
3. 执行sql `python manage.py migrate`
4. 成功后会在数据库中看到生成的表。django_migrations表记录迁移的过程。

可能的报错：db.sqlite3 后缀无所谓，本质都是数据库，但跟txt不同，有自己的规则，必须由驱动生成，不能直接在pycharm中new。django 初始migrate迁移内置app时会初始化。
### django shell
类似python交互式命令行。会加载django源代码，项目根目录，环境变量，数据库库驱动。在django shell中可以执行各种跟django项目有关的语法。
##数据库对象查询语法
Question.objects.all()  object 定义表的类具有默认属性=== 等价cursor.exe(select * from Question)  cursor.fetchall()
 Question.objects.filter(id=1,text='吃饭了吗')
 sql:select * from question where id=1 and text=""
 
 表连接 join
 sql:
 (1)select id from question;select * from choice where question_id=%s;
 (2)select * from question as q join choice c on q.id = c.question_id
 orm:
 (1)Question.objects.get(test='今天') id = q.id Choice.objects.filter(question_id=id)
 (2)q.choice_set.all()
 
  插入: insert into table values (%s,%s) ; 
q=Question(question_test='今天吃饭了吗',pub_date=timezone.now())


修改
q = Question.object.get(id=1)
q.text ='新值;
q.save()
相当于sql =update table set text='新值'where id= 1;


删除:
q=Question.objects.get(id=1)
q.delete()

#django中的时间坑
数据库中存的都是UTC标准时间,而中国是+8时区,py内置包datatime不含时区属性


#一对多  多对多
一对多,一个班级有多个学生.学生表里有外键存班级id
多对多,一个学生会有多个老师,一个老师也会带多个学生
sid  sname t_id
1    大名    1
2    大红    2
3    
tid  tname
1   小明
2   小红

##管理后台
几乎所有管理类项目都有后台功能
需求:对标数据进行增删改查,但是普通用户不会sql.
程序员需要做后台管理功能,但这个功能代码重复和无聊,所以django自带了管理后台功能,只需要进行一些配置

1.创建django自带后台的管理员    python manage.py createsuperuser
2.访问/admin 路由登陆
观察权限表的设计思想
3.在app.admin.py下注册要管理的model

虽然很快捷,但实际工作需求千变万化,django自带后台需要查文档进行各种配置才能个性化,公司往往自己开发后台

orm:object reference Mapping  类到关系型数据表的映射
django 自带orm框架,其他比较知名SQLAlchemy 重  peewee包 轻量
##MVC框架 
M :model  模型层,  数据库表结构
V:view    视图   平时看到的网页HTML前端,业务逻辑
C ;control 控制  路由转发,在M层和V层交互

##前端模板语言
前端路径     django2.2
loader.get_template('polls/index.html')   
参数写那个app下的那个html文件
1.app下templates,自动收集
2.首先查找项目根目录下的templates,不会自动收集,必须把路径添加到setting-templates-dirs才会扫描到

服务启动时会把所有html文件收集起来放到一起 ,    所有html收集起来, get_template("index.html")
polls/index.html 表示匹配 project/app/templates/app/index.html
#参数写那个app下的那个html文件,框架会自动到app下的templates文件夹下找,templates文件夹名不能随便改变



{% if latest_question_list %}
   {% endif %}
为了避免跟html混淆,{%    %}
写简单的python表达式,控制语句(没法写冒号和缺点,所以语句块相关的语法都有闭标签)

渲染模板开发模式,优点,后端懂点前端基础,就可以开发出一个项目,只需要一个框架
缺点:前后端代码耦合度高,维护,前后端开发来说需要会对方的一些知识.