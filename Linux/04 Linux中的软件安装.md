# Linux中的软件安装
    在windows下，安装软件".exe"双击运行即可。
    Linux中，软件包封装类型多样

- 常见的软件包封装类型：
    - rpm软件包 扩展名为  .rpm
    - deb软件包 扩展名为  .deb
    - 源代码软件包    一般为.tar.gz或者.tar.bz2格式的压缩包，包含程序源代码 README
    - 提供安装程序的软件包    install.sh、setup、.bin
    
- RPM软件包
    - 由Redhat公司提出，建立统一的数据库文件，详细记录软件包安装，卸载等变化信息，能自动分析软件包依赖关系
        推荐网站：http://rpmfind.net/
        
    - rpm软件包格式：bash-4.2-9.1.i586.rpm
            
            bash            -4.2            -9.1            .i586          .rpm 
            软件名称        版本号          发布次数        硬件平台        扩展名 
                                                        (noarch)不区分硬件架构
                                                        
    - YUM源软件管理方式
            
            1.YUM仓库集中化管理，管理RPM包
            2.很好的解决了软件包之间的依赖关系
            
    - YUM配置文件
                    
                    [root@rr ~]# cd /etc/yum.repos.d/           # 此处为YUM配置文件路径
                    [root@rr yum.repos.d]# ls                   # 以下为YUM配置文件的示例文件
                    CentOS-Base.repo  CentOS-Debuginfo.repo  CentOS-Media.repo    CentOS-Vault.repo
                    CentOS-CR.repo    CentOS-fasttrack.repo  CentOS-Sources.repo
                    
                    注：yum配置文件必须以 .repo结尾
                    
    - YUM配置文件内容
                
                    [c7-media]                                  # yum标识(带方括号，以为这个这个是yum文件)
                    name=CentOS-$releasever - Media             # yum名称
                    baseurl=file:///media/CentOS/               # yum源路径
                    gpgcheck=1                                  # 是否校验软件包的签名信息  1 校验    0 不校验
                    enabled=0                                   # 是否开机自启    1 自启    0 不自启


            
            