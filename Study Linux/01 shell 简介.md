# Shell
## 概念：Shell是一种特殊的程序
## 作用：是内核与用户的一种接口
### Shell命令解释器
- Shell一种解释型的语言（内部命令/外部命令）

		内部命令：系统自带的，随系统内核一起启动（56种） cd（改变路径）
		外部命令：就是一些额外的软件或者程序 ls（列出文件或者目录）
            sh （Borurne Shell）	csh		ksh
            *BASH 是rhel中默认的一种shell
	
            [root@localhost Desktop]#
                root：代表当前登录用户
                localhost：代表当前系统的主机名称
                Desktop：代表当前所在的位置
                #：代表当前登录用户是管理员用户
                    root：管理员 administrator（windows中的管理员账号）
                [root@192 ~]# su - student
	1.		su - username：切换当前登录				由root用户切换普通用户不需要密码
				有[-]：代表连同bash环境一起切换		由普通用户切换root用户需要密码
				没有[-]：代表仅切换用户，但bash环境不切换
            [student@192 ~]$ 
            $：代表当前登录用户是普通用户
		
	2.		exit：退出登录/退出终端
	3.		hostname：查看系统当前主机名
	4.		hostnamectl set-hostname ****	更换主机名为“****”
				切换完成后，bash界面内不会立即更新，使用“su -”命令，切换用户，“-”后什么都不跟意思是切换root用户
				
				[root@192 ~]# hostnamectl set-hostname rr
				[root@192 ~]# hostname
				rr
				[root@192 ~]# su -
				Last login: Mon Jan  7 16:26:27 CST 2019 on pts/0
				[root@rr ~]# 
    5.	    关机操作方法：
                poweroff
                init 0
                shutdown -h now现在关机（可以设置延时关机）
                halt
	6.	    重启操作方法：
                reboot
                shutdown -r now现在重启（可以设置延时重启）
                shutdown -r +15（15分钟后重启）
    7.	    data：查看当前系统时间
                [root@rr ~]# date
                Mon Jan  7 16:38:02 CST 2019
	8.	    cal：查看日历
                cal 年份		查看全年日历
                cal 月份 年份 	查看某年某月的日历
                    [root@rr ~]# cal
                        January 2019    
                    Su Mo Tu We Th Fr Sa
                           1  2  3  4  5
                     6  7  8  9 10 11 12
                    13 14 15 16 17 18 19
                    20 21 22 23 24 25 26
                    27 28 29 30 31
                    [root@rr ~]# cal 2019
                                                   2019                               
        
                           January               February                 March       
                    Su Mo Tu We Th Fr Sa   Su Mo Tu We Th Fr Sa   Su Mo Tu We Th Fr Sa
                           1  2  3  4  5                   1  2                   1  2
                     6  7  8  9 10 11 12    3  4  5  6  7  8  9    3  4  5  6  7  8  9
                    13 14 15 16 17 18 19   10 11 12 13 14 15 16   10 11 12 13 14 15 16
                    20 21 22 23 24 25 26   17 18 19 20 21 22 23   17 18 19 20 21 22 23
                    27 28 29 30 31         24 25 26 27 28         24 25 26 27 28 29 30
                                                                  31
                            April                   May                   June        
                    Su Mo Tu We Th Fr Sa   Su Mo Tu We Th Fr Sa   Su Mo Tu We Th Fr Sa
                        1  2  3  4  5  6             1  2  3  4                      1
                     7  8  9 10 11 12 13    5  6  7  8  9 10 11    2  3  4  5  6  7  8
                    14 15 16 17 18 19 20   12 13 14 15 16 17 18    9 10 11 12 13 14 15
                    21 22 23 24 25 26 27   19 20 21 22 23 24 25   16 17 18 19 20 21 22
                    28 29 30               26 27 28 29 30 31      23 24 25 26 27 28 29
                                                                  30
                            July                  August                September     
                    Su Mo Tu We Th Fr Sa   Su Mo Tu We Th Fr Sa   Su Mo Tu We Th Fr Sa
                        1  2  3  4  5  6                1  2  3    1  2  3  4  5  6  7
                     7  8  9 10 11 12 13    4  5  6  7  8  9 10    8  9 10 11 12 13 14
                    14 15 16 17 18 19 20   11 12 13 14 15 16 17   15 16 17 18 19 20 21
                    21 22 23 24 25 26 27   18 19 20 21 22 23 24   22 23 24 25 26 27 28
                    28 29 30 31            25 26 27 28 29 30 31   29 30
        
                           October               November               December      
                    Su Mo Tu We Th Fr Sa   Su Mo Tu We Th Fr Sa   Su Mo Tu We Th Fr Sa
                           1  2  3  4  5                   1  2    1  2  3  4  5  6  7
                     6  7  8  9 10 11 12    3  4  5  6  7  8  9    8  9 10 11 12 13 14
                    13 14 15 16 17 18 19   10 11 12 13 14 15 16   15 16 17 18 19 20 21
                    20 21 22 23 24 25 26   17 18 19 20 21 22 23   22 23 24 25 26 27 28
                    27 28 29 30 31         24 25 26 27 28 29 30   29 30 31
                    
                    [root@rr ~]# cal 8 2018
                         August 2018    
                    Su Mo Tu We Th Fr Sa
                              1  2  3  4
                     5  6  7  8  9 10 11
                    12 13 14 15 16 17 18
                    19 20 21 22 23 24 25
                    26 27 28 29 30 31


	
			
## 准确的shell命令规范
		命令字 【选项】	【参数】
		在Linux当中严格区分大小写
		在Linux当中一切皆文本
		
## 网络通讯的三种方法(有关于虚拟机VMWare的网络使用)
	    查看当前IP地址
        ifconfig：查看IP网络环境
            ping ***.***.***.***
            如果不设定次数，icm包会一直获取，按“ctrl+c”结束该指令
            ping ***.***.***.*** -c 4	执行4次，自动停止。
            测试网络连通性：
                ping 127.0.0.1
                ping 127.0.0.1 -c 4	#限制ping包次数(4次)
            ip addr show
		
            1.桥接
            2.NAT
                只可以访问外网，但外网不可以访问
            3.仅本地模式
	
## BASH常用快捷方式
            CTRL + C 	中断当前操作
            CTRL + L 	清屏
            "\"			换行
            CTRL + A	光标跳到行首
            CTRL + E	光标跳到行尾
            CTRL + U	清空到光标所在位置的前面所有内容
            CTRL + K	清空到光标所在位置的后面所有内容
            CTRL + SHIFT + '+'	放大字体
            CTRL + '-'	缩小字体
            命令:	history	查看历史命令,默认保留1000行
                    !(num)	调用某条历史命令
                    !41		调用历史第41行的命令
                    history -c 清除历史命令