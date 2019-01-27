# 传统RAID技术
## RAID的基本概念和实现方式
- RAID：redundant array of independent disk，独立硬盘冗余阵列，也被称为RAID
    - 高效的数据组织：
        - 条带化：
            - 条带(strip)：硬盘中单个或者多个连续的扇区构成一个条带，他是一块硬盘上进一次数据读写的最小单元。 它是组成分条的元素。
            - 分条(stipe)：同一硬盘阵列中的多个硬盘驱动器上的相同“位置”（或者说是相同编号）的条带。
            - 分条宽度：指在一个分条中，数据成员盘的个数
            - 分条深度：指一个条带的容量大小

        - 并行访问
        
    - 数据保护：
        - 奇偶校验：奇偶校验算法（XOR异或）。异或算法，可逆运算算出结果，所以可以用来校验。
            - XOR运算广泛地使用在数字电子和计算机科学中。
            - XOR校验的算法——相同为假，相异为真：
                
                    0⊕0= 0； 0⊕1= 1； 1⊕0= 1； 1⊕1= 0；
        - 热备用：时刻有一块磁盘，更替下故障的RAID组中故障的那块磁盘。
        - 在另一块冗余的硬盘上保存数据的副本。
            
    - 实现方法：
        - 硬件RAID
        - 软件RAID

## RAID状态
- RAID组被创建-->RAID组正常工作-->RAID组降级-->RAID组失效

                       创建成功               成员盘掉线或故障        故障盘数超过冗余盘数     
        RAID组被创建  -------->  RAID组正常工作  ---------->  RAID组降级  ----------> RAID组失效
        
                                                 <---------
                                                  重构成功           


## 常用RAID级别与分类标准
- RAID技术将多个单独的物理硬盘以不同的方式组合成一个逻辑盘：
    - 提高了硬盘的读写性能和数据安全性
    - 根据不同的组合方式可以分为不同的RAID级别
- RAID级别
    - RAID0：无差错校验的分条RAID，又叫条带化RAID。一般使用在图形化工作站，对硬盘读写数据有一定要求。
        - 至少2块磁盘组成：
            - 容量、性能、转速等指标，尽可能一样
        - 数据下发的时候以分条下发
        - 不提供数据保护
            - 无差错校验
            - 任意一块磁盘损坏，整套数据就会丢失
            - 同样的数据分开存放，提高了数据读写的性能
        - 磁盘利用率为100%
    - RAID1：镜像结构的阵列
        - 至少2块磁盘组成：
            - 容量、性能、转速等指标，尽可能一样
        - 提供数据保护
            - 完全镜像拷贝
            - 其中一块磁盘损坏，其他磁盘有完全相同的镜像备份
        - 磁盘利用率为1/n
    - RAID3：带奇偶校验的分条RAID
        - 至少3块磁盘组成，校验信息只存放于同一块磁盘
            - 其中1块磁盘作为校验盘，所有数据校验信息都会存放在此磁盘上，对磁盘损伤交大
            - 除了校验盘，其他的数据盘，在写入过程中，写入数据均匀分布，对磁盘的损伤较小 
            - 磁盘数据读取过程中，只提取数据盘内容，与校验盘无关
        - 当写入数据较少时，存在“写惩罚”问题
            - 一次写，多次读：一次有效写入，导致多次读取。
        - 提供数据保护
            - 存在异或校验机制，允许其中一块磁盘损坏，及时更换可修复数据
        - 磁盘利用率为(n-1)/n   
    - RAID5：分布式奇偶校验的独立硬盘结构
         - 至少3块磁盘组成，校验信息分布式存储在多块磁盘上
            - 校验信息分布在多块磁盘上，每块磁盘的工作压力比较平均
                - 减少了RAID3中的热盘(工作压力较大的磁盘)的存在
            - 磁盘数据读取过程中，只提取数据盘内容，与校验信息无关
        - 提供数据保护
            - 存在异或校验机制，允许其中一块磁盘损坏，及时更换可修复数据
        - 磁盘利用率为(n-1)/n
    - RAID6：具有两种校验算法的RAID类型
        - 需要至少N+2(N>2)个(4个)硬盘来构成阵列，一般用在数据可靠性、可用性要求极高的应用场合 。
        - 常用的RAID 6技术有：
            - RAID6 P＋Q(Huawei)：P＋Q需要计算出两个校验数据P和Q，当有两个数据丢失时，根据P和Q恢复出丢失的数据。
                - P = D0 ⊕ D1 ⊕ D2… (常规异或校验)        
                - Q = (α ⊕ D0) ⊕ (β ⊕ D1) ⊕ (γ ⊕ D2)… GF变换得到校验信息(芦苇码)，其中α、β、γ..是常量，已经存在于cpu内核中
            - RAID6 DP(NetApp)：DP－Double Parity，就是在RAID4所使用的一个行XOR校验硬盘的基础上又增加了一个硬盘用于存放斜向的XOR校验信息
                
                        横向校验盘中P0—P3为各个数据盘中横向数据的校验信息
                        例：P0=D0⊕D1⊕D2⊕D3
                        斜向校验盘中DP0—DP3为各个数据盘及横向校验盘的斜向数据校验信息      
                        例：DP0=D0⊕D5⊕D10⊕D15
        - 提供数据保护
            - 存在两种校验机制，允许其中两块磁盘同时损坏，及时更换可修复数据
        - 磁盘利用率为(n-2)/n
    - RAID10：RAID10是将镜像和条带进行组合的RAID级别，先进行RAID1镜像然后再做RAID0。RAID10也是一种应用比较广泛的RAID级别。
        - 至少需要4块磁盘组成
        - 允许两块磁盘损坏，但是这两块磁盘不允许同时是RAID1的同侧磁盘
    - RAID50：RAID50是将RAID5和RAID0进行两级组合的RAID级别，第一级是RAID5，第二级为RAID0。
        - 至少需要6块磁盘组成
        - 允许两块磁盘损坏，但是这两块磁盘不允许同时是RAID1的同侧磁盘

- 常见RAID级别的对比
        
        RAID级别	RAID 0   RAID 1     RAID 3      ☆RAID 5 	☆RAID6	    ☆RAID 10   RAID 50
        容错性	    无       有         有          有	        有	        有	        有
        冗余类型	无       复制       奇偶校验    奇偶校验	奇偶校验	复制	    奇偶检验
        热备盘选项	无       有         有          有	        有	        有	        有
        读性能	    高       低	        高          高	        高	        一般	    高
        随机写性能	高       低	        最低        低	        低	        一般	    低
        连续写性能	高       低	        低          低	        低	        一般	    低
        最小硬盘数	2块      2块	    3块         3块	        ４块	    4块	        6块
        磁盘利用率	N        (1/N)	    (N -1)	    (N -1) 	    (N -2)	    (N /2)	    (N -2)

- RAID的典型应用场景

        RAID 级别	应用场景
        RAID 0	    迅速读写，安全性要求不高，如图形工作站等
        RAID 1	    随机数据写入，安全性要求高，如服务器、数据库存储领域
        RAID 5	    连续数据传输，安全性要求高，如视频编辑、大型数据库等
        RAID 6	    随机数据传输，安全性要求高，如邮件服务器，文件服务器等
        RAID 10	    数据量大，安全性要求高，如银行、金融等领域
        RAID 50	    随机数据传输，安全性要求高，并发能力要求高，如邮件服务器，www服务器等
        
- 热备盘
    - 热备（Hot Spare）：当RAID组中某个硬盘失效时，在不干扰当前RAID系统正常使用的情况下，用该RAID组外一个正常的备用硬盘顶替失效硬盘。
    - 热备通过配置热备盘实现，热备盘分为全局热备盘和局部热备盘。

- 预拷贝：系统通过监控发现RAID组中某成员盘即将故障时，将即将故障成员盘中的数据提前拷贝到热备盘中，有效降低数据丢失风险。
    - 依赖磁盘的SmartIO功能来实现
    
- 重构：当RAID组中某个硬盘故障时，根据RAID算法和其它正常的成员盘，重新计算生成发送故障的硬盘上的所有数据（用户数据和校验数据），并将这些数据写到热备盘或者替换的新硬盘上的过程。

## Linux下通过mdadm命令实现软件RAID配置
1. 配置yum源，/etc/yum.repos.d
2. yum install mdadm
3. man mdadm

- mdadm常用模式：
    - Assemble：装配模式，将原来属于一个阵列的每个块设备(一般指磁盘)组装为阵列
    - Bulid：创建一个不需要元数据的阵列(超级块)，每个设备没有元数据块
    - Create：创建一个新的阵列，每个设备都有超级块
    
            --create == -C              创建一个新的阵列 
            --level == -l               设置RAID组级别
            --raid-devices == -n        设置设备活动个数
            --spare-devices == -x       设置备用盘的个数
            --chunk == -c               chunk默认64K
    - Monitor：监控模式，监控RAID状态，可以实现全局热备
            
            --follow == -F              选择监控模式
            --syslog == -y              事件日志记录
            --delay == -d               设置raid轮循，默认时间60秒
            --test == -t                生成警告信息
    - Grow：修改阵列属性(阵列磁盘个数，使用容量)
            
            --grow == -G                修改阵列大小或设备数量
            --raid-devices == -n        活动设备个数
            --chunk == -c               设置chunk大小
            --level == -l               设置等级
            --name == -N                设置阵列名称
    - Incremental Assembly：添加一个设备到阵列中
    - Misc：报告或者修改阵列中相关设备信息
            
            --query == -Q               查询一个RAID或者RAID组件设备信息
            --detail == -D              查看RAID组详细信息
            --stop == -S                停止RAID组
    - Auto-detect：要求在Linux内核启动时，自动检测阵列 

### RAID 0实现过程
1. 进行软件安装及更新
    
        yum install mdadm
2. 准备两块raid 0的成员盘并进行分区
        
        fdisk /dev/sdb
        Command (m for help): t
        Selected partition 1
        Hex code (type L to list all codes): fd                                 # 改变分区类型为'Linux raid autodetect'
        Changed type of partition 'Linux' to 'Linux raid autodetect'            # 并且改变成功

        Command (m for help): p

        Disk /dev/sdc: 21.5 GB, 21474836480 bytes, 41943040 sectors
        Units = sectors of 1 * 512 = 512 bytes
        Sector size (logical/physical): 512 bytes / 512 bytes
        I/O size (minimum/optimal): 512 bytes / 512 bytes
        Disk label type: dos
        Disk identifier: 0xe2b54778

           Device Boot      Start         End      Blocks   Id  System
        /dev/sdc1            2048    41943039    20970496   fd  Linux raid autodetect

        Command (m for help): w
        The partition table has been altered!
			
        fdisk /dev/sdc  同上
3. 准备完磁盘后，检查磁盘是否正确定义RAID
        
        [root@localhost ~]# mdadm --examine /dev/sd[b-c]            # 检查磁盘是否完成RAID格式化与是否已经存在RAID
		/dev/sdb:
		   MBR Magic : aa55
		Partition[0] :     41940992 sectors at         2048 (type fd)
		/dev/sdc:   
		   MBR Magic : aa55
		Partition[0] :     41940992 sectors at         2048 (type fd)
		[root@localhost ~]# mdadm --examine /dev/sd[b-c]1           # 检查磁盘分区内是否有超级块
		mdadm: No md superblock detected on /dev/sdb1.
		mdadm: No md superblock detected on /dev/sdc1.
4. 创建RAID(/dev/md0)：RAID组通常的就是md开头的
        
        mdadm -C /dev/md0 -l raid0 -n 2 /dev/sdb1 /dev/sdc1
        mdadm -C /dev/md0 -l raid0 -n 2 /dev/sd[b-c]1
5. 查看RAID组的状态信息：
       
        [root@rr ~]# cat /proc/mdstat
        Personalities : [raid0] 
        md0 : active raid0 sdc1[1] sdb1[0]
              10473472 blocks super 1.2 512k chunks
              
        unused devices: <none>
6. 查看RAID组的级别：
        
        [root@rr ~]# mdadm -E /dev/sd[b,c]1
        /dev/sdb1:
                  Magic : a92b4efc
                Version : 1.2
            Feature Map : 0x0
             Array UUID : 1e3e90de:65fb24e6:277114e6:5ffb94e1
                   Name : rr:0  (local to host rr)
          Creation Time : Sun Jan 27 16:50:03 2019
             Raid Level : raid0
           Raid Devices : 2
        
         Avail Dev Size : 10473472 (4.99 GiB 5.36 GB)
            Data Offset : 10240 sectors
           Super Offset : 8 sectors
           Unused Space : before=10160 sectors, after=0 sectors
                  State : clean
            Device UUID : 6b1f438a:472ae555:6d879fe8:8a6f0f99
        
            Update Time : Sun Jan 27 16:50:03 2019
          Bad Block Log : 512 entries available at offset 8 sectors
               Checksum : 80df8630 - correct
                 Events : 0
        
             Chunk Size : 512K
        
           Device Role : Active device 0
           Array State : AA ('A' == active, '.' == missing, 'R' == replacing)
        /dev/sdc1:
                  Magic : a92b4efc
                Version : 1.2
            Feature Map : 0x0
             Array UUID : 1e3e90de:65fb24e6:277114e6:5ffb94e1
                   Name : rr:0  (local to host rr)
          Creation Time : Sun Jan 27 16:50:03 2019
             Raid Level : raid0
           Raid Devices : 2
        
         Avail Dev Size : 10473472 (4.99 GiB 5.36 GB)
            Data Offset : 10240 sectors
           Super Offset : 8 sectors
           Unused Space : before=10160 sectors, after=0 sectors
                  State : clean
            Device UUID : 2eaa7dcd:528178bb:48ed9d17:8cdc4ac5
        
            Update Time : Sun Jan 27 16:50:03 2019
          Bad Block Log : 512 entries available at offset 8 sectors
               Checksum : 84e73adc - correct
                 Events : 0
        
             Chunk Size : 512K
        
           Device Role : Active device 1
           Array State : AA ('A' == active, '.' == missing, 'R' == replacing)
7. 查看RADI组设备
            
            [root@rr ~]# mdadm --detail /dev/md0
            /dev/md0:
                       Version : 1.2
                 Creation Time : Sun Jan 27 16:50:03 2019
                    Raid Level : raid0
                    Array Size : 10473472 (9.99 GiB 10.72 GB)
                  Raid Devices : 2
                 Total Devices : 2
                   Persistence : Superblock is persistent
            
                   Update Time : Sun Jan 27 16:50:03 2019
                         State : clean 
                Active Devices : 2
               Working Devices : 2
                Failed Devices : 0
                 Spare Devices : 0
            
                    Chunk Size : 512K
            
            Consistency Policy : none
            
                          Name : rr:0  (local to host rr)
                          UUID : 1e3e90de:65fb24e6:277114e6:5ffb94e1
                        Events : 0
            
                Number   Major   Minor   RaidDevice State
                   0       8       17        0      active sync   /dev/sdb1
                   1       8       33        1      active sync   /dev/sdc1
8. 针对RAID组进行创建文件系统
    
            mkfs -t ext4 /dev/md0
           
9. 创建挂载目录并进行永久挂载
            
            mkdir /mnt/raid0
            一次性挂载：
            mount /dev/md0 /mnt/raid0
            永久挂载：
            [root@rr ~]# vim /etc/fstab
            [root@rr ~]# cat /etc/fstab
            
            #
            # /etc/fstab
            # Created by anaconda on Sun Jan  6 23:25:37 2019
            #
            # Accessible filesystems, by reference, are maintained under '/dev/disk'
            # See man pages fstab(5), findfs(8), mount(8) and/or blkid(8) for more info
            #
            /dev/mapper/centos-root /                       xfs     defaults        0 0
            UUID=fa6d401c-1bd2-4397-bd88-363cf44b7e1c /boot                   xfs     defaults        0 0
            /dev/mapper/centos-swap swap                    swap    defaults        0 0
            /dev/md0 /mnt/raid0 ext4	defaults	0 0
            
            [root@rr ~]# mount -a                   # 重新挂载，顺便检查挂载文件是否有错误，如果有错误，下次启动系统会失败
10. 保存RAID组配置文件(必不可少!!!)
    
            [root@rr ~]# mdadm --detail --scan --verbose >> /etc/mdadm.conf
            [root@rr ~]# cat /etc/mdadm.conf
            ARRAY /dev/md0 level=raid0 num-devices=2 metadata=1.2 name=rr:0 UUID=1e3e90de:65fb24e6:277114e6:5ffb94e1
               devices=/dev/sdb1,/dev/sdc1
11. 使用RAID组：
            
            echo"这是一个RAID0阵列测试文件" > /mnt/raid0/test.txt
            
