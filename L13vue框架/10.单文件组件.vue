<template>
    <div>
<!--        .vue 单文件组件,搭配打包工具webpack ,nodejs,npm,vue.js运行-->
<!--        template特殊标签下写的是.vue中html部分.注意有且只有一个顶级元素-->

        <p>{{greeting}}world</p>
    </div>
</template>
<script>
    //.vue单文件其实并不是一个文件,上面的template跟下面data内容并没有直接联系,html,css,js三个文件放到一个盒子里面,一个项目有很多组件.webpack打包工具最终把每一个单文件组件的html抽出来拼合成一个完整的html网页
    //这样做的原因,单文件组件非常独立化,易于复用,开发时把精力放下单文件组件的业务逻辑上,最终通过打包工具,生成最终静态网页,思想,把一个完整产品分割多个独立部分,做完之后在整合
    module.exports = {
        //需要写成nodejs模块导出形式,打包工具最终会把这些信息合并到vue实例中
        data:function () {
            return {greeting:'hello'}
        }
    }
</script>
<style scoped>
/*    scoped这段css只作用于单文件组件中的html不会作用于全局,优点:作用域可控,不会影响到其他组件的html
原理:打包工具会自动给这个组件编id,class名 css选择器  编上id*/
    p{font-size: 50px;}
</style>