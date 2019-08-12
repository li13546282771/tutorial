/**
 * Created by asus on 2019/7/1.
 */
var str4='我是4.js中的字符串';
var num=1;
var obj={
    name:'张三',
    age:20
};
// 1.导出单个变量
// module.exports = str4;

// 2.导出多个变量
// module.exports= [str4,obj,num];导出数组可以用索引
// module.exports= {str4,obj,num};会导出键值对

// 3.导出对象(推荐)
module.exports = {
    'str4':str4,
    'num':num
};