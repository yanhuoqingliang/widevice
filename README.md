# widevice

*****说明：该工具可并发同时安装ios、Android安装包，简化安装复杂过程*****

【前提】
1. 已安装python环境，并配置环境变量

【iOS安装步骤】
1. 第一步：下载iTools4或者爱思助手并安装成功
2. 第二步：安装tidevice，打开cmd窗口输入命令pip3 install -U "tidevice[openssl]" 
3. 第三步：把需要安装的ipa文件复制到和widevice.exe同目录下
4. 第四步：手机连接到电脑（可连接多台ios手机）
5. 第五步：点击widevice.exe，等待安装完毕

【Android安装步骤】
1. 第一步：下载Android sdk 并配置环境变量
2. 第二步：把需要安装的apk文件复制到和widevice.exe同目录下
3. 第三步：点击widevice.exe，等待安装完毕

【并发同时安装】
Android、iOS手机连接到电脑，将Android、iOS安装包一起放到和widevice.exe同目录下，直接点击widevice.exe，即可同时安装
