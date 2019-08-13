css:编译后的产物,浏览器直接解析,缺点有些代码重复,便携效率一般

预编译语言:有变量有函数等类似后端语言的语法,优点:编写效率更高,缺点:浏览器无法直接识别.通常开发完需要转化为css

sass : 基于ruby中的一个包   bootstarp  compress 有些前端框架基于它开发
less   基于node.js中的一个包
stylus : 目前算比较新.没有大括号,分号,依赖缩进和空格表示键值对
相同点:变量  mixin(类似后端函数).函数(类似后端内置函数)
目前市场上sass less

##less
实例
编译xxx.less  书写一些less语法
安装less 编译器  npm install less -g
安装完成   lessc  -v   less compiler
编译   lessc xxx.less output.css

##vue-cli 单文件项目中
npm install -D less less-loader --save-dev
less 编译器  less-loader包时webpack生态的一个包,让webpack可以识别并调用less
单文件组件中编写.less样式代码,如果@import应用其他组件中less脚本中的变量
