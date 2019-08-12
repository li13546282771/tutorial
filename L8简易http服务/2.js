/**
 * Created by asus on 2019/7/3.
 */
// nodejs开启web服务
var http=require('http');

var app=http.createServer(function (req,res) {
    res.end('<h1>hello,world</h1>')
});
app.listen(8000,function () {
    console.log('服务已开启')
});
