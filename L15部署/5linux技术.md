#用户组  用户  设置  登录
默认最高权限root  但直接用root 操作错误有风险 
添加新用户  useradd  用户名    普通用户能操作跟自己账户相关内容,但不能操作其他用户或系统关键设置
修改密码  passwd  用户名  
注意第一次进入到ubuntu系统时,sudo passwd root  设置新的unix密码

权限:
root 用户#开头  普通用户$开头
su :switch user  ..   su  用户
sudu : super user do  ..   以root权限还行命令


密钥对登录
ssh配置文件  /etc/ssh/ssh1-config/  PermitRootlogin yes

## linux目录
linux目录跟windows  C.D盘不一样
/根目录
/bin  /sbin   跟系统有关的命令(ls mkdir mount),已配置到环境变量path下 ,可以在任何目录使用命令
/dev device 设备.   linux一切皆文件,硬件也可以用文件代指
/etc   放各种软件配置文件
/home  用户文件夹,类似windows C:/user/  添加一个用户时,会在home下成成同名文件夹
linux 是同时登陆多用户的系统
/lib library 各种开发软件,解释器,工具,框架
/media
/mnt  mount  移动硬盘 U盘  传感器,插入到电脑,手动挂载指定设备目录,才能访问.windows上这个过程是自动化的
/opt
/proc
/root   root用户的用户目录.跟home类似
/run  文件形式表示程序进程
/sys  linux系统核心文件
/tmp  临时缓存
/usr  安装的软件  /usr/lib python nodejs软件  /usr/bin  命令
/var 用户自己的文件

常用命令:
1.cd change directory 相对/绝对路径   
 cd/    cd/home  cd../
2. ls ,list查看当前文件夹下所有文件
3.mkdir  mack directory 创建文件夹

##文件权限
root权限最高,普通用户 /home/用户名  和/bin目录下权限,其他目录下不能创建文件和读取文件
1.whoami  查看当前用户
提升权限1.sudo  2.su root 3.group把普通用户放到管理员用户组  4.chmod修改文件权限.
2.查看文件权限  ls      ls -a显示隐藏文件   ls -l 详细信息
3.复制  剪切  mv  /home/lixiang/aaa.txt  
drwxr-xr-x  2 root root 4096 Aug 14 15:59 lixiang
权限           创建者 用户组  大小  时间     文件名
drwxr-xr-x
第一位d表示文件类型d文件夹   -文件  l软连接(快捷方式)
后面9位分三组表示权限,当前用户,用户组,其他用户  r read读 w 写  x执行权限 九位可以用二进制01转成十进制的结果表示
修改权限  chmod+wx 文件名

##软件安装
没有图形化界面,依靠包管理器安装,debian系  apt  centos系 yum类似pip.npm
软件源:维护软件下载列表的配置,默认是国外,速度慢 ,建议更换为国内阿里源
更新源:本地源配置文件不一定最新,安装软件最好更新源
搜索软件  apt search  软件名
安装软件  apt-get install 软件名
卸载软件  apt uninstall  软件名  部分软件无法卸载

## 文本处理
cat xxx.xx   查看文件里面的文本信息
vi : 强大的历史悠久的命令行文本编译器,可定制性强,插件
ecma:另一款强大的编译器
nano:比较简单,类似windows文本编辑器.可能需要安装.apt install nano
vim:vi加插件封装而成,相对vi更加易用.linux自带
     打开 vim /xxx.txt
     正常状态   只能看不能编辑
     编辑状态   按insert键进入 屏幕下方有提示---insert---,按esc键退出
     命令状态   正常状态下  shift+;  进入命令模式,下方显示冒号:  w保存  q退出 !q强制退出
     众多快捷键和插件详见网上