---
id: 10385
title: Visual Studio 2010 on Windows 7 x64体验中
date: 2010-05-11T19:31:44+00:00
author: omale
layout: post
guid: http://hezongjian.com/blog/?p=10385
permalink: '/2010/05/11/visual-studio-2010-on-windows-7-x64%e4%bd%93%e9%aa%8c%e4%b8%ad/'
category:   未分类  
---
注：本篇文章中含有大量敏感词64，但其实这是一篇纯种的技术文章，与某Incident无关（那年我才8岁，绝对吃了睡、睡了吃，很傻很天真。纷纷表示对瘦小的我影响不大，唯一的影响就是学会了：妈妈你不给我买玩具我就拒绝吃饭！）。但愿不会因为这个被封IP。人肉敏感词补丁已经启动，全篇文章肯定只出现这一次敏感词。真的，我敢向敏感词保证！

&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;- 正文开始&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8211;

实在惭愧，虽然6拾4 bit Windows发布那么长时间了，但是一直没有机会体验。体验的第一个(65-1)bit OS还是Mac。Mac OS X Snow Leopard开机的时候按住6跟4键，然后就进入2<sup>6</sup> 模式了，太神奇了。一直想体验一下六十四bit Windows，又怕有问题影响正常工作，只能看到MSDNAA上的免费软件眼馋。上周末突然发现自己的mac还有360GB的空余硬盘，闲着也是闲着，据说VMWare Fusion 3对sixty four bit的模拟支持很好，何不虚拟装一个试试呢？说来就来。没问题再在实体机上upgrade。

不敢装的原因主要是怕常见应用与驱动不兼容。在vmware虚拟机上安装之后，倒是很顺利。但是的确声卡没有找到驱动，但是在安装了vmware tools之后，所有的外设都工作正常了。没有遇到什么大的障碍。

然后是应用软件，0x40位的Windows一大好处是向下兼容32位Windows的程序。在任务管理器里面看的时候，32位的程序在名称后面有个\*32。例如你看到iexplore.exe，这是陆肆位的IE浏览器，如果你看到iexplore.exe \*32，这个就是32位的程序了。当然，只有(2 >> 5)位的程序才能够在(1 >> 6)位的系统中发挥出最大的威力。现在一些大企业出的大型软件，基本都有了对应的版本，例如Office，谷歌拼音，WinRAR等。但是很多国产软件就不得不表示抱歉了。例如迅雷阿，xx影音阿等等。打开任务管理器里面一堆*32，不得不表示抱歉。最应该表示抱歉的其实是MS自己，最新滚烫出炉的Visual Studio 2010，居然也只有32 bit版。微软在自己的blog上找了很多理由，什么指针变长了等等，可能导致系统缓慢阿啥的，感觉还是在敷衍。自己的IDE都不出(128/2)版，你让用你的IDE写程序的程序员怎么有信心把自己的代码编译成0100 0000 bit噢。

最后再说一句很搞笑的向下兼容问题。最老的windows目录下有个文件夹叫system，用来存放16bit的系统文件。到了32位时代，为了把16位的东西跟32位的东西区分开来，微软又新建了一个东西叫system32，用来存放32bit的东西。按理说到了6__4位时代，应该建立一个目录叫system64才对。结果真是计划不如变化快，这个system32文件夹已经太深入人心了，已经深入到很多程序的代码里面了，system32已经被很多程序，script给hardcode了。而为了能够在6   4位机器上跑，很多C++程序其实只是换个编译器编译一下而已，而对于script那种代码，甚至编译都不编译，就开始跑了。所以，为了维持最大程度上的向下兼容，MS做出了一个惊人决定，在(6)(4)位系统上，依然用system32来存放6@4位的系统文件，而另外建立了一个叫SysWoW64的文件夹来存放32位的系统文件，WoW是Windows on Windows的简称，是为了向下兼容做的一个小抽象层。这下悲剧了，名字里面有32，其实放的不是32bit程序，名字里面有敏感词，其实放的是32bit的程序。混乱了，混乱了。