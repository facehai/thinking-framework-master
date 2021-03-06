'''
1. C/S架构
    C/S: Client客户端--------基于网络----------Server服务端
         你  ---------------     电商     ---------- 商家
        有一个地址不固定                       有一个地址固定
        多个                                    只有一个（稳定）
                                                多并发（外卖小哥送你的快餐的同时也在送其他人的）
2. 服务端需要遵循的原则:
    1. 服务端与客户端都需要有唯一的地址,但是服务端的地址必须固定/绑定
    2. 对外一直提供服务,稳定运行（代码保证，操作系统稳定，计算机也稳定）
    因为服务端代码运行在操作系统之上，操作系统运行在硬件之上（这就是运维的工作）
    3. 服务端应该支持并发（客服端同时接收服务）
3. 什么是网络
    客户端计算机和服务端计算机通信
    网络建立的目的是为数据交互(通信)
    如何实现通信:
        1. 建立好底层的物理连接介质
        2. 有一套统一的通信标准,称之为互联网协议
4. 互联网协议:就是计算机界的英语（一个标准）
    世界标准组织：OSI七层协议
    应用层
        http协议
            超文本传输协议  超文本   ‘超级文本’   ‘带超链接文本’
            通过这个带超链接文本可以从网站的一个地方到达另一个地方，这就是超文本的含义
            那么带超链接的文本也是一个富文本的表现形式，可以有图片，视频，文章
            本质上来讲web服务就是提供这样的服务，我们对网站的浏览就是对网站内容的浏览
            那么内容都有一个地址
            地址
            https://ke.qq.com/course/list/python?tuin=b695991e
            https，是协议
            ke.qq.com  是服务器  域名等价于ip地址和端口
            http 80，https 443是服务器上的默认端口号
            course/list/python?tuin=b695991e 是查询。
            ke.qq.com  DNS服务器解析域名 DNCP服务器自动配置ip
    传输层  *****
        传输层的由来：网络层的ip帮我们区分子网，以太网层的mac帮我们找到主机，
                然后大家使用的都是应用程序，你的电脑上可能同时开启qq，
                暴风影音，等多个应用程序，
                那么我们通过ip和mac找到了一台特定的主机，如何标识这台主机
                上的应用程序，答案就是端口，端口即应用程序与网卡关联的编号。
                传输层功能：建立端口到端口的通信
                补充：端口范围0-65535，0-1023为系统占用端口
        tcp 可靠传输
        TCP（传输控制协议）
        是面向连接的，面向流的，提供高可靠性服务。tcp是基于数据流。
             tcp 三次握手
                syn：
                    建立连接  非常小的一种数据包。
                ack
                    确认建立连接
                seq
                    是序号   （暗号）
            tcp 四次挥手
                fin
                    断开连接
            utp 不可靠传输
                UDP（用户数据报协议）
                是无连接的，面向消息的，提供高效率服务。udp是基于数据报。
    网络层
        ip协议 网络直接互联的协议
        规定网络地址的协议叫ip协议
        它定义的地址称之为ip地址，广泛采用的v4版本即ipv4，
         它规定网络地址由32位2进制表示
        范围0.0.0.0-255.255.255.255   0 是八个 00000000   255  八个 11111111
        一个ip地址通常写成四段十进制数，例：172.16.10.3
            172.16.10.3
            10101100.00010000.00001010.000000011
        找到唯一的局域网
        arp协议    计算机自带的
        arp协议  地址解析协议  专门把ip地址解析成mac地址
    不需要上层    有了物理连接介质和互联网协议
    数据链路层        局域网比喻成一个教学楼
        数据链路层由来：单纯的电信号0和1没有任何意义，必须规定电信号多少位一组，每组什么意思
        数据链路层的功能：定义了电信号的分组方式
        以太网协议：
         以太网采用最原始的方式，广播的方式进行通信，即计算机通信基本靠吼
        所以它只能在局域网内使用
        以太网数据包 （了解）
        1.一组电信号构成一个数据包，叫做‘帧’
        每一数据帧分成2部分：报头head（相当于快递单）和数据data（快递本身）两部分
                                head	                       data
        2.数据报：
            head包含：(固定18个字节) 为了描述数据
                发送者／源地址，6个字节
                接收者／目标地址，6个字节
                数据类型，6个字节
            data包含：(最短46字节，最长1500字节)
                数据包的具体内容
            head长度＋data长度＝最短64字节，最长1518字节，超过最大限制就分片发送
        3.ethernet规定接入internet的设备都必须具备网卡
            发送端（源mac地址）和接收端（目标mac地址）的地址便是指网卡的地址，即mac地址
        mac地址：
            每块网卡出厂时都被烧制上一个世界唯一的mac地址，
            通常由12位16进制数表示
            14-18-C3-73-3A-F6
            前六位是网络硬件制造商的编号
            后六位代表该制造商所制造的某个网络产品的系列号
            也称为局域网位置
    物理层
        0101010111

    目标mac地址怎么获取？
    了解
        1.先知道ip地址 自己的和对方的ip
        # arp协议
        2.一：首先通过ip地址和子网掩码区分出自己所处的子网
            一个完整的ip地址的标识方式
                ip地址        172.16.10.1
                子网掩码      255.255.255.0
            标识方式二
                172.16.10.1/24   24代表有24个连续的1
            子网地址
                    ip地址和子网掩码地址 按位与运算 得到子网地址
            网关作用:
                就是跨子网的,一个局域网只能mac通信，所以就有来跨局域网
            # arp协议
            场景	数据包地址
                同一子网	     目标主机mac，目标主机ip
                不同子网	     网关mac，    目标主机ip
            在同一个局域网内
                二：分析172.16.10.10/24与172.16.10.11/24处于同一网络
                获取目标mac的方式
                发送端主机
                        源mac	    目标mac	                 源ip	            目标ip	             数据部分
                        发送端mac	FF:FF:FF:FF:FF:FF	     172.16.10.10/24	172.16.10.11/24	     数据
                                    (相当于一个暗号告诉对方我需要你的mac地址)
                三：这个包会以广播的方式在发送端所处的子网内传输，
                所有主机接收后拆开包，发现目标ip为自己的，就响应，返回自己的mac
            不同局域网内
                arp先获取的是网关的mac
                1.ip1   192.168.1.2/24      ip2    192.168.2.2/24
                    1.由于ip1和ip1的网关在同一个子网内
                    ip1先获取ip1的网关在的mac地址
                        源mac	目标mac	                  源ip  ip1的ip地址	    目标ip   ip1的网关	 数据部分
                    发送端mac	FF:FF:FF:FF:FF:FF	     192.168.1.2/24 	    192.168.1.1/24 	     数据
                                (相当于一个暗号告诉对方我需要你的mac地址)
                    2.ip1 的子网的网关通过路由协议获取到ip2的子网的网关mac地址
                    3.ip2的子网的网关获取ip2的mac地址
                    源mac	   目标mac	                 源ip  ip2的子网地址 目标ip   ip2的ip地址	 数据部分
                    发送端mac	FF:FF:FF:FF:FF:FF	     192.168.2.0/24 	192.168.2.2/24 	     数据
                                (相当于一个暗号告诉对方我需要你的mac地址)



    ip+mac可以标识全世界范围内独一无二的一台计算机的位置

    port可以标识一台计算机之上唯一的一个基于网络通信的应用软件
    C/S: Client客户端软件--------基于网络----------Server服务端软件
    ip+mac+port:可以标识全世界范围内独一无二的一个应用软件(基于网络通信)
    ip找到局域网
    mac找到局域网所在的计算机
    port找到计算机上的具体的软件
    C/S: Client客户端软件有ip+mac+port--------基于网络----------Server服务端软件ip+mac+port
                                                                需要绑定固定的ip+port
                                                                不需要绑定mac
                                                                arp协议地址解析协议
                                                                专门把ip地址解析成mac地址

'''