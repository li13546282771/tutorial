//引入mysql模块
var mysql = require('mysql');
var connection = mysql.createConnection({
    host     : 'localhost',
    user     : 'root',
    // password : '123456',
    database : 'job51'
});
connection.connect();


// 增加数据
// var addsql='insert into lianxi(id,name)values(9,?)';
// var addsqlparams = ['小李'];
// connection.query(addsql,addsqlparams,function(err,result){
//     if (err){
//         console.log('[insert error]-',err.message);
//         return;
//     }
//     console.log('insert id:',result.insertId);
//     console.log('insert id:',result)
// });

//删除数据
// var delsql='delete from lianxi where id=6';
// connection.query(delsql,function(err,result){
//     if (err){
//         console.log('[delete error]-',err.message);
//         return;
//     } console.log('delete affectedRows',result.rowsAffected)
// });

//更改
var upsql='update lianxi set name="小白" where id="8"';
connection.query(upsql);

//查询数据
var sql='select * from lianxi';
connection.query(sql,function (err,result) {
    if(err){
        console.log('error');
        return
    }
    console.log(result)
});















