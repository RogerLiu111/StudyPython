# Linux中的软件安装
    在windows下，安装软件".exe"双击运行即可。
    Linux中，软件包封装类型多样

- 常见的软件包封装类型：
    - rpm软件包 扩展名为  .rpm
    - deb软件包 扩展名为  .deb
    - 源代码软件包    一般为.tar.gz或者.tar.bz2格式的压缩包，包含程序源代码 README
    - 提供安装程序的软件包    install.sh、setup、.bin、agent
    
- RPM软件包
    - 由Redhat公司提出，建立统一的数据库文件，详细记录软件包安装，卸载等变化信息，能自动分析软件包依赖关系
        推荐网站：http://rpmfind.net/
        
    - rpm软件包格式：bash-4.2-9.1.i586.rpm
            
            bash            -4.2            -9.1            .i586          .rpm 
            软件名称        版本号          发布次数        硬件平台        扩展 名 
                                                        (noarch)不区分硬件架构
                                                        
    - YUM源软件管理方式
            
            1.YUM仓库集中化管理，管理RPM包
            2.很好的解决了软件包之间的依赖关系
            
        - YUM配置文件
                    
                    例：
                    [root@rr ~]# cd /etc/yum.repos.d/           # 此处为YUM配置文件路径
                    [root@rr yum.repos.d]# ls                   # 以下为YUM配置文件的示例文件
                    CentOS-Base.repo  CentOS-Debuginfo.repo  CentOS-Media.repo    CentOS-Vault.repo
                    CentOS-CR.repo    CentOS-fasttrack.repo  CentOS-Sources.repo
                    
                    注：yum配置文件必须以 .repo结尾
                    
        - YUM配置文件内容
                    
                    例：
                    [c7-media]                                  # yum标识(带方括号，以为这个这个是yum文件)
                    name=CentOS-$releasever - Media             # yum名称
                    baseurl=file:///media/CentOS/               # yum源路径
                    gpgcheck=1                                  # 是否校验软件包的签名信息  1 校验    0 不校验
                    enabled=0                                   # 是否开机自启    1 自启    0 不自启

        - YUM源管理软件的步骤
            1.配置yum配置文件
            2.清空yum源的缓存
            3.软件安装
        
            - 挂载命令：
                mount 源文件 挂载文件
            - 卸载命令：    
                umount 源文件or挂载文件
                
        - 实际在VM虚拟机中的操作
                
                1.虚拟机挂载光盘信息
                2.创建yum源路径             mkdir /mnt/cdrom
                3.挂载光盘到yum路径下       mount /dev/cdrom /mnt/cdrom
                4.修改yum配置文件
                    路径：/etc/yum.repos.d/
                    文件：vim dvd.repo
                    文件内容：
                        [dvd]                               # yum标识
                        name = Linux_GG                     # yum名称
                        baseurl = file:///mnt/cdrom         # yum路径
                        gpgcheck = 0                        # 不校验yum软件包的签名信息
                        enabled = 1                         # 是否自动开机
                5.yum repolist all          查看所有yum状态信息
                6.yum list all              列出所有的yum软件包
                7.yum clean all             清除yum缓存
                8.yum install 软件包名 -y   安装yum软件包
                
        - 常用yum命令
           
                yum remove "packagename"                # 删除软件包
                yum info "packagename"                  # 查看软件包详细信息
                yum search "packagename"                # 查找软件包
                yum update "packagename"                # 更新软件包
                
                yum安装软件包组
                    yum grouplist                       # 列出所有可用组
                    yum groupinfo                       # 查看组的信息
                    yum groupinstall                    # 安装软件包组
                    yum grouperase                      # 删除软件包组
                    yum groupupdate                     # 更新软件包组
                    
                使用yum安装本地rpm包
                    yum localsinstall **.rpm
                    
    - RPM软件包安装
        查看已安装的RPM包信息
            
            rpm 【选项】 【软件名】
            rpm -qa                                     # 查看系统中所有已安装的RPM包
            rpm -qa '****'                              # 查看'****'软件包
            rpm -qf                                     # 查看文件或目录属于哪个rpm软件
            
        安装/升级RPM软件包
            rpm 【选项】 软件包文件
            
            rpm -ivh 软件包文件
                -i  安装
                -v  显示安装过程的详细信息  
                -h  显示安装进度，以#显示
                
                -U  （大写）升级某个rpm软件，若没有安装，则进行安装
                -F  更新某个RPM软件，若没有安装， 则放弃安装
                
        卸载指定的rpm软件包
            rpm -e 软件名                              # erase剔除
                    
- 源码安装
    把程序的源码，执行就可以了，看README
        
        1.检查源代码所处的编译环境
        2.编译
        3.安装
        
        example：
            1.安装vmware tools
            2.NTFS-3g
    

            
            