# 短信,支付类接口
# 自己公司没有设备,依赖第三方平台,
# 支付类:阿里云,腾讯云上有支付接口,注意只对公司开放(营业执照),申请接口app,沙箱测试开发,正式.规则比普通接口复杂一点..个人想做需要找第三方提供的接口
# 短信:阿里云,腾讯云  注意只对公司开放.  第三方公司知名和允许个人接入的是  云片网.
# callback_url:回调url  如果公司项目比较大,项目a负责发短信,项目b专门级联发送历史结果,项目a发送完短信后再请求b项目，但如果b项目路由发生了变更，a项目内源码也需要修改，不好维护。所以可以项目a请求接口时，像云片网传递callback_url 参数,让第三方网站代替你发送

# SMS:send message 发送短信接口
# sdk:suit develop kit 一套开发工具.官方提供封装好的包.根据官方示例就可以调用接口而不需要根据API文档开发,更加简单傻瓜化,但实际由于可能没有开发小众语言版本或版本更新不及时sdk有bug,和封装程度高报错不易排错.建议根据API开发

# 作业(选做):注册/登陆功能使用短信接口
# 1.注册,防止注册机批量注册,添加手机验证.用户名密码字段添加后,添加文本框(填写手机号),按钮(发送短信)没法直接请求django路由否则表单页面会刷新 js发请求,文本框(请填写收到的验证码)
# 2.
import requests,random,json
# random_code = ''
# for i in range(4):
#     random_code += str(random.randint)
# print(random_code)
random_code = '0123'
data = {
    'apikey':'7a795f6e7e13d8ec121d69befa25222c',
    "mobile":'17635497546',
    'text':'【李想测试】您的假期余额已不足,好好享受假期'
}

resp = requests.post(url='https://sms.yunpian.com/v2/sms/single_send.json',data=data)
print(resp.status_code)
print(resp.text)
# resp_dict = json.loads(resp.text)