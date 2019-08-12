var factorial=function(n){
    var r=1;
    for (var i=1;i<=n;i++) {
        r=r*i
    }
    return r
};

// var n=math.floor(math.random()*100);
module.exports=factorial;

// 函数导出时,导出得失标识符,传递引用(址传递,值传递)
//变量名都是全局的,变量名不要冲突
// 模块化优势,封装,重用