#PIL  C\C++知名图形库  python不擅长图形,直接调用PIL库,封装后叫pillow库
from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random

def random_char():
    '''生成随机字母'''
    # ord('a') 根据ascill编码规则，字母-对应二进制十进制表示
    #chr('120)  ord逆运算
    return chr(random.randint(65,90))


def random_num():
    '''生成随机数'''
    return random.randint(0,9)   # 随机生成0到9


def random_color():
    '''随机颜色 较浅颜色rgb()'''
    return (random.randint(150,255),random.randint(150,255),random.randint(150,255))
def random_color2():
    '''随机颜色  较深rgb()'''
    return (random.randint(30,120),random.randint(30,120),random.randint(30,120))


#  生成白色画布
width = 240
height = 60
image = Image.new('RGB',size=(width,height),color=(255,255,255))
# 生成绘制对象
draw = ImageDraw.Draw(image)
# 设置字体
font = ImageFont.truetype('ARLRDBD.TTF',36)
# 根据像素点（x,y）填充颜色
for x in range(0,241):
    for y in range(0,60):
        draw.point(xy=(x,y),fill=random_color2())
# 生成文字
for t in range(0,4):
    draw.text((60*t+20,10),random_char(),font= font,fill =random_color())
# 加模糊滤镜
# image = image.filter(ImageFilter.BLUR)
for i in range(100):  # 加噪点
        draw.point([random.randint(0, width), random.randint(0, height)], fill=random_color())
for i in range(5):  # 加干扰线,这里通过添加多组横纵坐标实现
    x1 = random.randint(0, width)
    y1 = random.randint(0, height)
    x2 = random.randint(0, width)
    y2 = random.randint(0, height)
    x3 = random.randint(0, width)
    y3 = random.randint(0, height)

    draw.line((x1, y1, x2, y2, x3, y3), fill=random_color())

# 保存到本地
image.save('7test.jpg','jpeg')


# 追加需求(选做);加横线,噪点
# 登陆 django返回登陆页之前生成验证码图片,存到static文件夹下,保存验证码到表(用户名,随机数字)
# form  <img scr= '/static/xxx.jpg'
# 3.用户提交,后端比对用户传过来的验证码跟后端存的是否一致