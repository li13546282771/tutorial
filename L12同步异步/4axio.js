//https://github.com/axios/axios
// 前后端分离,前端框架发起的请求,需要用到前端的http库,其中流行的是axios库.基于js promise封装
var axios = require('axios');
axios.get("http://www.baidu.com",{
    params:{
        'wd':'学习'
    }
})
    .then(function (resp) {
        //成功回调
        console.log(resp)
    })
    .catch(function (resp) {
        //失败回调
    })
    .finally(function (resp) {
        //不管成功或失败都执行回调函数
    });
//终端运行方法  node xxx.js
// axios.post('http://www.baidu.com',{
//     arg1:'表单参数1'
// })
//     .then(function () {  })
//     .catch(function () {  });