rest 风格接口
===
##引提
很多招聘需求会要求写RESTful风格接口

##传统接口存在的问题
假设开发一个前后端分离的电商网站后台
1.商品列表
2.单个商品
3.单个商品评论

单说"商品列表"接口
127.0.0.1:8000/goods/
127.0.0.1:8000/goods/list
127.0.0.1:8000/goods/get_goods_list
127.0.0.1:8000/goods/goods_list
127.0.0.1:8000/goods/api_goods_list
127.0.0.1:8000/goods/getFoodsList
"单个商品"接口
127.0.0.1:8000/goods/10001/
127.0.0.1:8000/goods/10001/get_info
127.0.0.1:8000/goods/get_single_goods/?good_id=10001


一种功能,大家起名的习惯不一样,长得各种各样.有的取数据,有的写数据,有的查询参数?有的url传参数
项目大型后非常容易混乱

##restful
一位程序员在论文中提出的理论.提倡:
1.看到url就回到要访问的资源是什么
2.http请求类型GET POST  UPDATE  DELETE就知道对资源增加还是删除
如果rest风格表示上面的需求
1.商品列表       GET 127.0.0.1:8000/goods/
2.查询单个商品   GET 127.0.0.1:8000/goods/1001/   商品id是个主要的属性并且能表示资源,放到url中匹配
3.查询单个商品   GET  127.0.0.1:8000/goods/1001/?price=30&color=write&page_size=10&page_no=1跟商品有关的各种细节维度社和放到查询参数.如果写成127.0.0.1:8000/goods/1001/30/write/就没有逻辑性和可读性
4.修改单个商品 UPDATE 127.0.0.1:8000/goods/1001/
5.删除单个商品 DELETE 127.0.0.1:8000/goods/1001/
6.每个大版本程序的api接口编一个版本可以在url中看出  http://github.com/api/v3/goods/1001/

所以restful并不是一个新知识,而是一种风格
现状,人们提倡rest 但是但多数人还是习惯get post.没有完全跟理论保持一致.所以平时写项目注意保持风格即可

## (了解)graphsql 和jsonapi
restful风格也有缺点:
假设""首页商品列表"接口
{
    'banner':'http://xxx.jpg'
     'goods_id':1001,
    'sku':ER1001W,
    'color':
    'price':
    'user_comments':[
    {
    'content':'这个商品不错',
    }
    ]
}
另外还需'商品列表接口'程序员开发时发现逻辑重复.
解决方案:1 "首页商品列表接口"根据业务拆分成三个接口banner,goods,commits.缺点 视图函数中sql数量增加.消耗服务器资源.前端活加重

graphsql应运而生  github v3(restful风格)  v4 (graphSQL)
graphSQL风格,数据库表结构,python字典列表,json这几种格式表达的实际意义非常相似,但由于语言不通不能直接转化,我们想能不能从前端直接从数据库取数据,中间交给代码做自动转换
使用:安装好对应框架的插件,前端语法语法类似json和sql
sql  
    name

现状:行业新闻上graphSQL是下一代api风格,会取代rest,但它也有自己缺点,目前还是rest多