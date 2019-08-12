var axios = require('axios');
axios.get('http://api.map.baidu.com/direction/v2/transit',{params:
        {"origin":"40.056878,116.30815",
    'destination':'31.222965,121.505821',
    "ak":'nazZGPjoTnQQLm7uW8VTXr6muI5n5hIr'}
}).then(function (resp) {
        //成功回调
        console.log(resp)
    })
    .catch(function (resp) {
        //失败回调
    })
    .finally(function (resp) {
        //不管成功或失败都执行回调函数
    });