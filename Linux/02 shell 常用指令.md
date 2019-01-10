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
        
        ls：列出当前目录下的所有文件	#在Linux中,以"."开头的文件是隐藏文件
            格式：ls【选项】【目录或文件名】
            选项：
                -l	以长格式显示
                -a	显示所有文件目录信息,包括隐藏文件
                -d	显示目录本身的属性
                -h	显示详细信息,变换了统计单位
                --color	以颜色区分不同类型的文件（默认显示的时候已经以颜色区分）
                ll = ls -l
                
        cd：切换工作目录
            cd 【目录位置】	输入路径的时候“tab”2次会把当前目录内容显示出来
                绝对路径：cd/home/student
                相对路径：
                        cd ..返回上级目录	
                        cd - 返回前一次工作目录
                        cd ../../ 返回上一级目录的上一级目录（最多返回到根目录）
                        cd ~返回到用户的家目录
                        
        pwd：查看当前所在的工作目录（告诉你自己在哪）
        
        mkdir：创建一个新目录
            格式：mkdir	【选项（-p）】【路径】（可加可不加，不加路径是当前目录）	目录名
                -p 递归创建多级目录
                mkdir	-p	b/c/d/e/f/g
                
        rmdir：删除一个空目录（该命令用的很少）
            格式：rmdir【选项】【目录或文件名】	
                rmdir -p b/c/e/f/g
    
- 文件操作命令：
        
        touch：创建一个空文件，更新文件时间标记
            格式：touch Filename
            在Linux中，不以后缀区分文件
        echo：打印某个文件里的内容
            [root@rr aa]# echo "hello world" > a.txt	#重定向写

        cp：复制文件或者目录
            格式：cp【选项】	源文件/目录	目标文件/目录
                -r 递归复制整个目录树
                
        rm：删除文件或目录
            格式：rm【选项】	文件或者目录
                -r 递归删除整个目录树
                -f 强制删除不给任何提示（慎用！！）
            rm -rf * 当前目录下所有文件全部删除（尤其清理日志的时候，慎用！！）
            
        mv：移动文件或者目录
            格式：mv【选项】	源文件/目录	目标文件/目录
            EX：	[root@localhost text]# ls
                    a.txt b.txt
                    [root@localhost text]# mv b.txt /root/text-2/
            用法2：若移动目标位置与原位置相同（当前目录下操作），则此操作相当于重命名（改名）
            EX：	[root@localhost ~]# mv text text-1
            
        find：用于查找文件或者目录
            格式：find 【查找范围】	【查找条件】
                查找条件：
                    -name 	按文件名查找
                    -type	按文件类型查找
                            f	普通文件
                            d	目录
                            b	块设备文件
                            c	字符设备文件
                    -user	按文件属主查找（这个文件是谁的）
                    -size	按文件大小进行查找
                    -a	逻辑与
                    -o	逻辑或
                    !	逻辑非
                [root@rr ~]# find / -name initial-setup-ks.cfg 
                /root/initial-setup-ks.cfg
                [root@rr ~]# find / -name initial		#不搜索全文件名找不到东西,要加*号通配符
                [root@rr ~]# find / -name initial*
                /root/initial-setup-ks.cfg

- 文件内容操作命令：
			cat：
			less：
			head：
			tail：
			grep：
		归档以及压缩命令：
			tar：
			
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