# 哈希：hash
# 场景：
# 1.编程语言数据结构的基础，例如字典 {'name': '小明'}    # 《图解算法》
# 2.密码加密。正推（加密）容易反推（解密）难。
# 3.不管明文短或长，摘要（加密后）信息长度一致长度,离散程度大。 下载软件MD5确保软件下载的是原版；爬虫去重；快速判断两个文件是否一样；
# 大概原理： 参考https://blog.csdn.net/jingcheng345413/article/details/54969292   。  把原字节信息经过算法处理，按照规则分散取出固定个数的字节作为最终的字节、字符串。
# 常见的哈希算法： md5简单快速  sha1 sha128 sha256加密更消耗资源但更安全

import hashlib

md5 = hashlib.md5()
md5.update('6541964'.encode('utf-8'))      # 16字节
print(md5.hexdigest())      # 5f4dcc3b5aa765d61d8327deb882cf99   e10adc3949ba59abbe56e057f20f883e  f1887d3f9e6ee7a32fe5e76f4ab80d63

# 比对文件是否内容一样 ，例如图片或电影.跟文件名无关。场景：url去重；文件去重；七牛云、百度云盘。
# with open('xxx.jpg', mode='rb') as file:
#     img_bytes = file.read()
#     md5 = hashlib.md5()
#     md5.update('123457'.encode('utf-8'))


## 成熟网站的密码通常sha算法加密
# goNlHGsh9xWr$eVB7QNie81HPvWWofZ9VyMkkked2is+dpfPmP62j+dA=
# 但可能仍然不安全，因为穷举攻击可破解。
# 穷举攻击原理： 找弱密码字典, .txt弱密码文件中有很多的简单密码（123456 qew123 password admin ）（假设10万条），读取到列表中，开始循环，计算md5或sha加密后的字符串， 存入数据库（20w条）。黑客获取到某公司用户表，跟自己穷举跑出的表对比加密后的字符串有没有一样的，如果有就知道用户的明文，这种攻击方式叫“撞库”。
# 所以平时设置密码不应该太简单；不要把所有网站密码设置为一样。
# 解决：
# 1. 原始明文 加上 一段随机信息（俗称加盐），组成新字符串之后再加密。解密时由加密字符串解密再减去加上的信息得到原始信息。黑客不知道加的盐的什么，从而导致穷举攻击成本大大提高。
# 2. 多次加密(了解)

# raw_content = '123456'
# salt = 'hello'
# content = raw_content + salt
# sha256 = hashlib.sha256
# # sha256.update(content.encode())
# # sha256.hexdigest()
#
#
# md5 = hashlib.md5()
# md5.update('123457'.encode('utf-8'))
# str1 = md5.hexdigest()
# md5.update(str1.encode('utf-8'))
# str2 = md5.hexdigest()
# md5.update(str2.encode('utf-8'))
# str3 = md5.hexdigest()


# 例如django中， pbkdf2_sha256$150000$goNlHGsh9xWr$eVB7QNie81HPvWWofZ9VyMkkked2is+dpfPmP62j+dA=







