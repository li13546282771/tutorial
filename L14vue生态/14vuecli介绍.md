vueCLI介绍
===
cli 命令行工具,之前在终端使用python  mysql,django-admin是命令行工具,而qq 是图形化界面
vue-cli  继承了vue.js  vue-loader vue-router webpack 等vue生态的包   vuejs是一个小而核心的库,人们开发大型项目怎么组织是比较自由的,但初学者不容易搭建项目架子,每个人写的项目组织不一样不利于互相学习,vue-cli  根据webpack自动创建项目组织(类似django-admin)
webpack:最终产品index html,在一个html文件中开发组件容易混淆,把index.html打散成一个个功能组件(类似django项目组织),方便开发,开发完再合并
安装vue-cli3.x   `npm install -g @vue/cli`     -g表示全局   安装完后使用vue   @vue表示大仓库大文件夹下的一个小包cli
验证  `vue-V`


##npm补充(了解)
疑似nodejs老版本目录
C:\Users\asus\AppData\Roaming\npm\node_modules\@vue\cli
C:\Users\asus\AppData\Roaming\npm 全局安装的npm包路径已经被配置到全局变量中
~\AppData\Roaming\npm\node_modules\@vue\cli
~\AppData\Roaming\npm-cache  最近安装npm包的缓存,注意因为网络问题包不完整,但install是用的是残缺的包,虽然现实安装成功但是代码报错不能运行.
新10.15版本C:\program files\nodejs\modules下.  
新旧版本环境变量会有冲突

解决办法:
npm uninstall 包名 ,
npm cache clean清楚缓存
再进行安装

~代表C:\Users\asus用户文件夹
AppData是隐藏文件夹,放置安装程序和配置文件

 
#创建项目
3.x   vue create [project name]  或  vue ui  在图形化界面创建(不建议)
2.x   vue init [template name,default:webpack] [project name]
向导,键盘上下切换选项,回车确定:
1.选择  Manual 手动设置
2.
babel  es6语法转es3 es5,开发快并且让浏览器兼容代码
typeScript  js语法封装,类似jquery
PWA   谷歌带头的新技术,浏览器增强技术,离线缓存,系统通知,内置数据库
vue-Router  路由系统,类似django中的urls.py
Vuex  组件状态管理器.父子组件传值为了避免混淆.变量专门的控制工具(类似sap pi),好像是前后端两个项目中间又加了中介.
CSS pre-processors css预处理器.开发者使用sass less语言书写样式,开发完成后会通过sass/less-loader编译为css
linter   语法风格检查.不像python语法风格严格.js语法风格灵活,例如 ; 可以不写.语句块{}可以分行也可以写成一行,等号左右是否有空格
Unit Testing E2E  单元测试相关
选择:babel\router(中型项目)\vueX(大项目)\css预处理器(看开发者)\linter(初学建议不开,否则总报语法不规范无法运行项目)\Testing(不用开启)\PWA(不用开)\TypeScript(不用开)
3.babel\eslint等工具的配置文件单独dedicate放还是放到package.json中,选择"单独放"
4.是否保存现在的选择默认供以后项目使用,选"N"
5.自动安装项目依赖.  而vue-cli 2.x  手动选择自动安装或初始化项目后手动npm install 安装   问题:安装依赖卡住,自动走npm可以梯子或手机网络  重新create [project name],提示是否覆盖overwrite或合并merge 选择merge接着之前进度进行安装

以后的项目可以把node_modules文件夹和package.json package-lock.json

#打开项目和项目组织
webstorm
如果卡死进程管理器结束再打开,node_modules文件夹右键-make directory as -not excluded,这样ide就不会索引这个文件夹卡死了
项目结构:
modules  依赖包
package.json  描述依赖包配置文件,类似python中的pip freeze requirements.text
   name  version关于项目信息
   script 是npm run [cmd name]  真正执行的命令.npm run的本质是node xx.js
   vuecli3.x大版本中`npm run server`  2.x  `npm run dev`
   dependencies  生产依赖,开发和放服务器上都需要的依赖包,例如vue.js
   devDependencies  开发依赖  开发时需要,部署到服务器不需要,例如babel,放到服务器是编译后的js
   随着开发发觉需要安装更多的包, npm install xxx 后再手动修改package.json,如果想自动修改 npm i xxx --save 写道生产依赖中缩写为 npm i xxx -S; npm i xxx --save-dev/npm i xxx -D 写到开发依赖中
为了避免package.json描述文件开发中修改与node_models安装不一致,所以新增lock文件来描述真正安装的包

.git   git代码版本控制
.gitignore   排除git不想跟踪的代码,例如node_modules,太大了,用户可以自行安装
README.md    项目介绍文件
.browserlistrc  浏览器兼容性描述文件,影响到babel转码
babel.config.js  babel配置文件
postcss 是一个自动补充css的工具 -webkit前缀
上面的配置文件package.json经常修改,其他一般不动
public/index.html 首页,但是主题内容将被vue实例替换掉,只有js加载不成功才会显示报错.<% 类似{{}},
src  source源代码 ,核心业务逻辑
    scr/assets  静态资源,类似django中的static,例如logo 图标 字体
    (2.x)src/static   侧重用户上传的文件夹,用户上传头像.文件.类似django中的upload文件夹
    [入口]src/main.js   项目入口
        import Vue from 'vue'  类似py from 包 import 类  
        from搜索路径意识node_models二是项目本身
        import App from './App.vue'  注意相对路径同一文件夹下要写成./
        包含子组件  1.先引用  子组件.vue 2.父组件局部注册子组件 3.父组件html引用子组件
    scr/components  各种子组件
##运行
cd 项目根目录 
`npm run serve`
报错1:
如果报错找不到xxx模块,解决1 npm install xxx;
解决2:删除node_modules文件夹,重新安装npm install
报错2:
webstorm卡死,任务管理器结束进程

编译`npm run build`把散着的各文件.es6转化,sass转化
最终生成dist目录(distribution 分发),里面带有编号(防止浏览器缓存)的index.html(单页文件),js,css
最终产物 纯静态文件 不依赖后端服务器可以浏览器直接解析