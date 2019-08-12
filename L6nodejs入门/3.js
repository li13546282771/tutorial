/**
 * Created by asus on 2019/7/1.
 */
//模块化
// js跟其他语言例如python,当项目较大时,有多个脚本文件,可以互相引用,或者导入第三方包
// python : from  xx import xxx
// node.js 跟其它语言不一样的地方:先导出,在引用.而其他语言不用显示到处


// node.js
// 导入require('xxx');  注意 相对路径同一级不能写4.js,要写成严谨的./4.js// 导出 module.exports   module是每个node.js脚本默认的特殊全局变量,包含模块化的属性,把想要导出的变量.方法.对象放到module.exports中.其他js文件就可以通过require引用导出的东西
// 处于底层原理和设计严谨考虑:一个脚本很多全局变量,都导出容易冲突,模块化抽象封装
//js文件通过接口与外界沟通信息(导入和导出)





var aaa=require('./4.js');
console.log(aaa);