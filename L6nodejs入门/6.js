var aaa=require('./5.js');
// var aaa=require('./5.js');
// 第一次引用一个文件,会加载哪个文件,存到缓存中,第二次或其他文件引用时加载更快
console.log(aaa(5));