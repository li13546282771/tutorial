# base64编码
# 原因：早期服务器只支持ascii编码，不支持其它编码。 url如果有中文，需要先转换成只包含ascii编码的字符串。
# base64编码， https://baike.baidu.com/item/base64/8545775?fr=aladdin  。 二进制每三个字节32位，每6位+补2位0组成四个字节，64种可能，通过编码规则表对应成常见英文字母和符号。 对称加密。
# 场景：base64优点 简单，缺点 加密简单容易被破解、文件增加三分之一。
# 1. url有中文  https://www.1owo.com/%E6%95%99%E6%A1%88/
# 2. 以字符串的方式传递图片。
# 3. 信息简单加密。   v2ex上留手机微信号的又怕爬虫外行 NzU2NDY1MTg1QHFxLmNvbQ==

import base64

content = '我的电话是13733170000'
bytes_content = content.encode(encoding='utf-8')
print(content.encode(encoding='utf-8'))     # b'\x32\x3e'   00001010  1111110   # base64 把原信息的三个字节转成四个字节，再decode(encoding='ascii')
b64_content_bytes = base64.b64encode(bytes_content)
b64_content_str = b64_content_bytes.decode()
print(b64_content_str)   # 5oiR55qE55S16K+d5pivMTM3MzMxNzAwMDA=  5oiR55qE55S16K+d5pivMTM3MzMxNzAwMDE=

# b'\xe6\x88\x91\xe7\x9a\x84\xe7\x94\xb5\xe8\xaf\x9d\xe6\x98\xaf13733170000'    # 二进制的0101太长了，一个字节两个16进制表示。
# b'5oiR55qE55S16K+d5pivMTM3MzMxNzAwMDA='   # 没有\x分隔，但类型是bytes,字节数经过编码后增加三分之一。本质是 000001111 二进制，ide自动解码所以我们看到的是比较自然的。
# b'5oiR55qE55S16K+d5pivMTM3MzMxNzAwMDA='.decode()   #  字节解码为str '5oiR55qE55S16K+d5pivMTM3MzMxNzAwMDA='

content2_base64_str = 'NzU2NDY1MTg1QHFxLmNvbQ=='
content2_raw_bytes = base64.b64decode(content2_base64_str)
content2_raw_str = content2_raw_bytes.decode()
print(content2_raw_bytes)
print(content2_raw_str)
