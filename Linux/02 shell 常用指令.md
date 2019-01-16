#shell命令详解与Linux目录结构(重点)
- Linux精髓在于命令行
##Linux命令的通用命令格式
		命令字	[选项]	[参数]
			选项：
				作用：用于调节命令的具体功能
					"-"引导短格式选项(单个字符)		EX："-1"
					"--"引导长格式选项(多个字符)	EX："--color"
					
					-a -z -l -x	-->	-alzx	多个短格式选项可以写在一起
				参数：
					命令操作的对象，有文件，目录等
				
				EX：ls -l /home
				
##Linux目录结构
		boot：存放系统引导文件和内核文件（删了之后系统起不来了）
		bin：存放可执行文件（二进制文件）（ls、cat、mkdir）
		sbin：root用户执行命令
		home：存放普通用户的家目录
		root：root用户的家目录
		dev：放置所有设备文件（外设）	/dev/md*	/dev/sd*	/dev/hd*
		etc：放置所有配置文件（服务）
		lib/lib64：lib（普通用户）lib64（管理员）动态链接库文件（共享库）类似于.dll文件
		media：媒体库文件
		opt：文件安装目录，安装软件就在opt目录下
		mnt：挂载点目录 mount * *（用mount命令挂载）
		var：存放一些需要改变数据的文件	日志、某些大文件的溢出区
		proc：放的是内存的一个映射
			   cat /proc/cpuinfo	#查看CPU运行状态
			   cat /proc/meminfo	#查看内存运行状态
			   cat /proc/version	#查看系统版本
			   uname -m				#查看CPU架构
			   uname -r				#查看内核版本
		usr：最大的目录 只要用到的目录或者文件都在这	/usr/sbin 	/usr/doclinx
		tmp：共享文件夹，临时目录
		lost+found：平时为空，只有系统在非正常关机时才会有，保存意外掉电中内存的数据
	
##Linux常用命令：
- 目录操作命令：
    - ls：列出当前目录下的所有文件	#在Linux中,以"."开头的文件是隐藏文件
            
            格式：ls【选项】【目录或文件名】
            选项：
                -l	以长格式显示
                -a	显示所有文件目录信息,包括隐藏文件
                -d	显示目录本身的属性
                -h	显示详细信息,变换了统计单位
                --color	以颜色区分不同类型的文件（默认显示的时候已经以颜色区分）
                ll = ls -l
                
    - cd：切换工作目录
    
            cd 【目录位置】	输入路径的时候“tab”2次会把当前目录内容显示出来
                绝对路径：cd/home/student
                相对路径：
                        cd ..返回上级目录	
                        cd - 返回前一次工作目录
                        cd ../../ 返回上一级目录的上一级目录（最多返回到根目录）
                        cd ~返回到用户的家目录
                        
    - pwd：查看当前所在的工作目录（告诉你自己在哪）
        
    - mkdir：创建一个新目录
    
            格式：mkdir	【选项（-p）】【路径】（可加可不加，不加路径是当前目录）	目录名
                -p 递归创建多级目录
                mkdir	-p	b/c/d/e/f/g
                
    - rmdir：删除一个空目录（该命令用的很少）
    
            格式：rmdir【选项】【目录或文件名】	
                rmdir -p b/c/e/f/g
    
- 文件操作命令：
        
    - touch：创建一个空文件，更新文件时间标记
    
            格式：touch Filename
            在Linux中，不以后缀区分文件
        
    - echo：打印某个文件里的内容
           
            [root@rr aa]# echo "hello world" > a.txt	#重定向写

    - cp：复制文件或者目录
    
            格式：cp【选项】	源文件/目录	目标文件/目录
                -r 递归复制整个目录树
                
    - rm：删除文件或目录
            
            格式：rm【选项】	文件或者目录
                -r 递归删除整个目录树
                -f 强制删除不给任何提示（慎用！！）
            rm -rf * 当前目录下所有文件全部删除（尤其清理日志的时候，慎用！！）
            
    - mv：移动文件或者目录
           
            格式：mv【选项】	源文件/目录	目标文件/目录
            EX：	[root@localhost text]# ls
                    a.txt b.txt
                    [root@localhost text]# mv b.txt /root/text-2/
            用法2：若移动目标位置与原位置相同（当前目录下操作），则此操作相当于重命名（改名）
            EX：	[root@localhost ~]# mv text text-1
            
    - find：用于查找文件或者目录
           
            格式：find 【查找范围】	【查找条件】
                查找条件：
                    -name 	按文件名查找
                                [root@rr ~]# find / -name initial-setup-ks.cfg 
                                /root/initial-setup-ks.cfg
                                [root@rr ~]# find / -name initial		#不搜索全文件名找不到东西,要加*号通配符
                                [root@rr ~]# find / -name initial*
                                /root/initial-setup-ks.cfg
                    -type	按文件类型查找
                            f	普通文件
                            d	目录
                            b	块设备文件
                            c	字符设备文件
                    -user	按文件属主查找（这个文件是谁的）
                                [root@rr ~]# find / -user student -type f -name abc.test
                                /home/student/abc.test
                    -size	按文件大小进行查找
                                [root@rr ~]# find / -user student -type f -name abc.test
                            在var目录下，查找大于10K小于15K的文件
                                [root@rr ~]# find /var/ -size +10k -type f -size -15k -type f
                                
                    -a	逻辑与
                    -o	逻辑或
                    !	逻辑非
                                [root@rr ~]# find / !  -name temp -type f  查找不是temp的文件
                            
    - alias：
        别名：为使用频率较高的命令，设置昵称，默认情况下，别名只在当前bash下可用，如果想要永久生效，需要额外设置
            
            查看当前用户所有别名
                [root@rr ~]# alias
                alias cp='cp -i'
                alias egrep='egrep --color=auto'
                alias fgrep='fgrep --color=auto'
                alias grep='grep --color=auto'
                alias l.='ls -d .* --color=auto'
                alias ll='ls -l --color=auto'
                alias ls='ls --color=auto'
                alias mv='mv -i'
                alias rm='rm -i'
                alias which='alias | /usr/bin/which --tty-only --read-alias --show-dot --show-tilde'

            设置别名
                alias 别名=“实际执行的命令”
                    alias aa=head -n -5 anaconda-ks.cfg     （aa就是后面那条命令的别名）
            取消别名
                unalias 别名
                    unalias aa 
                    unalias -a  （取消所有别名）
            让别名永久生效
                将别名设置在~/.bashrc文件中
                    gedit .bashrc   输入命令后在其他别名中间输入也可以，在末尾输入也行
                    
                        # .bashrc
    
                        # User specific aliases and functions
                        
                        alias rm='rm -i'
                        alias cp='cp -i'
                        alias mv='mv -i'
                        # alias aa=head -n -5 anaconda-ks.cfg（在此输入）
                        
                        # Source global definitions
                        if [ -f /etc/bashrc ]; then
                            . /etc/bashrc
                        fi
                        # alias aa=head -n -5 anaconda-ks.cfg（在此输入）
                
- 文件内容操作命令：
	
	- cat：文件内容产看，显示出文件的全部内容
	        
	        格式：cat filename
	
	- less/more：全屏方式分页显示文件内容（使用more命令时，下方会显示阅读百分比）
	        
	        格式：less/more filename
	        
	        按回车Enter逐行滚动
	        按空格键向下翻页
	        按B键向上翻页
	        按Q键退出
	        more用法与less一致，只是多了一个百分比显示
	        
	- head：显示文件头部若干行，默认十行
    - tail：显示文件尾部若干行，默认十行
            
            格式：head/tail 【选项】 filename
            head -n 5 initial-setup-ks.cfg      查看文件前5行，行数输入正，表示正数到第几行，如果是负，就是遍历到倒数第几行为止
            tail -n -5 initial-setup-ks.cfg     查看文件尾5行，行数输入正，表示倒数到第几行，如果是负，就是遍历到正数第几行为止
	        
	        注意：符号的使用 + - 代表意思不同
	        
	- wc：默认情况下统计文件内容的：行数 词数 字节数 文件名
	       
	        格式：wc 【选项】 filename
	        [root@rr ~]# wc anaconda-ks.cfg 
            64  148 1694 anaconda-ks.cfg
	        
	        选项：
	            -w 统计字数 一个字被定义为由空白，跳格，换行以这些为分割字符串
	            -l 统计行数
	            -c 统计字节数（-m 和 -c 不能同时使用）
	            -m 统计字符数（-m 和 -c 不能同时使用）
	            -L 打印最长行的长度
	            man wc
	            wc --help
	            wc --version
	            
	- grep：检索，在文件中查找并显示包含指定字符串的行，相当于正则表达式
	        
	        格式：grep 【选项】 查找条件 目标文件
	        [root@rr ~]# grep 'boot' anaconda-ks.cfg 
            
            选项：
	            -c 显示匹配行数
	            -i 查找时，不区分大小写
	            -v 反转查找（显示不包含查找字符串的行）
	            -cv 显示不包含指定字符串的行数

            查找条件设置：
                1.查找条件用引号引起来
                2.“^...”表示以...开头
                3.“...$”表示以...结尾
                [root@rr ~]# grep '^$' anaconda-ks.cfg -c       查找空行数量
                [root@rr ~]# grep '^$' anaconda-ks.cfg -cv      查找不包含空行的数量
                [root@rr ~]# grep '^#' anaconda-ks.cfg          查找以#号开头的行
	            
- 归档以及压缩命令：

	- tar：压缩与解压缩    制作归档文件和释放归档文件
	        压缩文件有2种格式：
	                格式1：    .gz
	                格式2：    .bz2
	                bz格式比gz格式压缩率更高，但是压缩时间更长。
	        格式：
	            制作归档文件：
	                tar 【选项】 【目录】/归档文件名  源文件或者目录
	            释放归档文件：
	                tar 【选项】 归档文件 【-c 目标文件】
	        
	        命令：
	            压缩：
	                tar -czvf 【存放路径】 归档文件名.tar.gz 源文件或者目录
	                tar -cjvf 【存放路径】 归档文件名.tar.bz2 源文件或者目录
	                
	                -c  压缩
	                -z  .gz格式
	                -j  .bz2格式
	                -vf 显示详细信息  
	                
	                tar -czvf /root/var.tar.gz /var/    压缩gz格式
	                tar -cjvf /root/var.tar.bz2 /var/   压缩bz2格式
	                tar -czvf a.tar.gz text-1 text-2    同时压缩2个文件
	                
	            解压：
	                tar -xzvf 【存放路径】 归档文件名.tar.gz [-c 解压目录(不写表示为当前目录)]
	                tar -xjvf 【存放路径】 归档文件名.tar.bz2 [-c 解压目录(不写表示为当前目录)]
	                
	                -x  解压
	                -z  .gz格式
	                -j  .bz2格式
	                -vf 显示详细信息
	                
	                tar -xzvf var.tar.gz
	                tar -xjvf var.tar.bz2 -c text-1/
	                
- 链接命令：
    
    - ln：---->  link    链接
        
            链接有两种：
                软连接 ln -s 源文件 目标文件
                    类似于创建快捷方式，权限对所有人开放，删除源文件后，快捷方式不可打开
                硬链接 ln 源文件 目标文件（类似于 cp -p +同步更新 权限也一模一样）
	                类似于 （cp -p +同步更新），权限与源文件一样，删除源文件后，硬链接就只是一个备份，依旧可以使用，但是重新创建新的文件和原来的链接文件同名，不会再次形成链接
			
##Linux中如何获得命令帮助：
		1.	help（内部命令）cd，kill	56条
				EX：help cd
			--help（适用于大多数外部命令查找）
			    EX：ls --help
			
		2.	使用man手册进行命令查看（man：命令阅读手册）
				man 命令字
				上下键滚动文本
				Page down & Page up上下翻页
				空格也支持翻页,回车走一行
				输入/,可以查找
				
		3.	info也可以进行命令帮助查找（使用与man接近）
			
		4.	pinfo 命令名称
				以浏览器的形式查看详细的GUN信息
			/usr/share/doc #所有已安装软件的说明文件
				firefox file:///usr/share/doc

## 重定向与管道符
- 重定向
    - 作用：将命令的执行结果输出到指定的文件中，而不是直接显示在屏幕上
    
        0   标准输入    键盘  stdin   仅读取
        1   标准输出    终端  stdout  仅写入
        2   标准错误    终端  stderr  仅写入
        
        
        3+  filename    其他文件    读/写
        
        在Linux中构建了一个带有编号标记的通道（文件描述符）的进程结构来管理打开文件通过进程链接到文件，进行文件数据的操作。
        
        类型              操作符                             用途                                  
        重定向标准输出     (1)>     将命令的执行结果输出到指定文件中，而不是显示在屏幕上，覆盖写      history > history.txt
                           (1)>>    与上一条命令使用结果相近，不过是追加写，不覆盖源文件内容          history >> history.txt
        
        重定向标准错误      2>      将标准错误信息保存到指定文件中，进行覆盖写                        find / -user student 2> error.txt
                           2>>      将标准错误信息保存到指定文件中，进行追加写                        find / -user student 2>> error.txt  
        分别重定向标准输出和标准错误          find / -user student > true.txt 2> false.text
        重定向标准输出和标准错误    &>      将标准输出和标准错误全部保存到另一个文件中，覆盖写
                                    &>>     将标准输出和标准错误全部保存到另一个文件中，追加写       find / -user student >>true.txt 2>/dev/null(/dev/null文件是一个特殊的文件，黑洞文件，所有不想要的内容都可以往里面扔，然后就没有了)

- 管道
    - 作用：传送， 将管道前面输出的结果作为后面语句的条件执行
        - 标识符号  ->  "|"
            
                语句1 | 语句2 | 语句3 |......|语句n
                