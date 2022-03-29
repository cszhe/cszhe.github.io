---
id: 9846
title: Windows Mobile 5手机使用经历——两天三刷
date: 2007-06-12T02:32:00+00:00
author: omale
layout: post
guid: http://hezongjian.com/blog/?p=9846
permalink: '/2007/06/12/windows-mobile-5%e6%89%8b%e6%9c%ba%e4%bd%bf%e7%94%a8%e7%bb%8f%e5%8e%86-%e4%b8%a4%e5%a4%a9%e4%b8%89%e5%88%b7/'
category:   嵌入式  
tags:   Windows CE
  - 嵌入式
  - 软件
---
<div>
  <div>
    看了标题不用吃惊。你搞Windows CE的人，怎么才用了两月Windows Mobile？别着急，慢慢道来。这篇文章不是技术贴，只是自己的一些故事。权当休闲看。
  </div>
  
  <div>
     
  </div>
  
  <div>
    其实呢，我用基于Windows CE的手机用的是很早的。我2003年的时候就买了基于Windows CE 4.2的smartphone多普达515，当时花了将近4000大洋。多普达515是国内能找到的第一款smartphone手机了，现在早就停产了。所以自己也算是中国第一批吃螃蟹的人了。正是应了嵌入式系统的一大特性——更新换代慢——我的多普达515安然无恙的运行了4年（期间还经历了一次手机掉到厕所里，寒；还有一次充电器线掉到水里短路烧掉，还好有备用）。终于，4月15号彻底不工作了。现象是每次系统boot起来进入主界面之后大概10秒钟之后，键盘就不再响应任何操作了，只能拔电池。怀疑是GWES挂了。经过了一次恢复出厂设置，问题依然存在。后来经过我反复拔电池reboot，终于导致手机彻底歇菜。连boot都boot不起来了。肯定是硬件的损害。虽然对偶的515还有深深的感情，但是现在的smartphone早就步入了6.0时代，我还在使用4.2时代的产品，实在落伍。干脆一咬牙，换！
  </div>
  
  <div>
     
  </div>
  
  <div>
    其实自己心里早就有了心仪的对象，水货577w，因为不但支持WM 5.0，而且还带wifi。说道这个wifi，上次在南方周末上看了一篇文章，说这个叫“技术爱国主义”。因为国内的规定，同一款设备上，有wifi就不能有电话模块，有电话模块就不能有wifi。原因是：1，国内前几年在推与WiFi竞争的标准WiMax，现在WiMax已经基本挂了，wimax挂了，也不能给wifi好眼色看。2，担心大家都用wifi打网络电话，导致运营商少赚钱，或者遭到国外运营商的竞争。所以国外手机从正规渠道进入国内市场，都必须先把wifi阉割掉。这反而给了水货可乘之机，这样一来，水货不但价格便宜，而且功能还比行货好，哎。
  </div>
  
  <div>
     
  </div>
  
  <div>
    4月16号冒雨去了火车站附近的不夜城，那里是上海水货手机的总集散地。只能用一个字形容——乱。场地的布置乱，交易的流程乱，卖的东西乱，来往的人也乱，全都是怎一个乱字形容。在一派混乱之中，我随便找了一家，花了1900大洋，买了577w，走人。
  </div>
  
  <div>
     
  </div>
  
  <div>
    没想到回去之后的两天之内，就刷了三次机。
  </div>
  
  <div>
     
  </div>
  
  <div>
    所谓刷机，其实只不过是使用loader更新flash中的OS映像。没什么技术含量，只要按照网上的教程一步步走，绝对不会有错。真正的技术含量都在loader里。（如果说刷机，其实当年在老板那里开发Elastos手机的时候，哪天不得刷机几十次……只不过那个手机只是个裸板。这个可是自己花了将近2000大洋买来的。）刷机使用的工具叫ROM Update Utility，在网上很好找。
  </div>
  
  <div>
     
  </div>
  
  <div>
    <img height=358 src="http://images.blogcn.com/2007/6/12/2/omale,20070612023211143.JPG" width=560 border=0>
  </div>
  
  <div>
     
  </div>
  
  <div>
    第一次刷机：为了尝鲜，把默认的老旧ROM换掉，装了个微软雅黑字体的ROM，雅黑是Vista里面才有的字体，号称超级漂亮。结果尝鲜之后，感觉虽然比宋体舒服不少，但是占系统空间太厉害。这个时候我还没有mini SD卡呢，所有东西都要装在本机flash上，所以为了那可怜的空间，换宋体。
  </div>
  
  <div>
     
  </div>
  
  <div>
    第二次刷机：就是刷宋体ROM，刷完之后，果然发现机器本身的存储宽裕了不少。恩，欣慰。结果又是为了尝鲜，装了某些好事者从刚发布的Windows Mobile 6模拟器ROM里面提取出来的Windows Live Messenger软件（哎，不得不佩服这些家伙了，人家发布一个nk.bin，居然可以写个工具，从bin里面提文件出来。而且还把提出来的东西自己再打包成新的bin，就有了到处流传的xxx版ROM）。这次，实在不知道微软怎么想的，居然Windows Live Mobile登录的时候，会把你MSN里的联系人一古脑给添加到手机通讯录里。可怜我的MSN联系人从来不清理，累积了几百个不认识的人。一下子就搞得我的通讯录暴涨，速度变得很慢。一个个删除是不可能的，没有提供回滚方法。只好走到了下一步。
  </div>
  
  <div>
     
  </div>
  
  <div>
    第三次刷机：其实这次只是为了把Windows Live Mobile私自添加的联系人除掉。本来不要刷机，只要恢复出厂设置就好，只不过我被气的抓狂了，不分青红皂白就刷了。目的也打到了。那些碍眼的联系人终于没了。
  </div>
  
  <div>
     
  </div>
  
  <div>
    就这样，相安无事的使用了一段时间。又有一些感想：
  </div>
  
  <div>
    Wifi超级耗电。不过速度比GPRS快很多，在参加无聊会议的时候，用wifi上网解闷也不错。
  </div>
  
  <div>
    QVGA的屏幕导致好多老版本SP下设计不精良的软件使用起来别扭，无法全屏。哈哈，偶在上课的时候一直强调UI分辨率的设计的。:-)
  </div>
  
  <div>
    第三方厂商和爱好者自编的软件越来越多了，质量也不断提高。想当年Smartphone刚出炉的时候，偶写个连连看游戏都可以骗下载量的日子一去不复返了。这就是平台标准化和开放化的恐怖。
  </div>
  
  <div>
     
  </div>
  
  <div>
     
  </div>
</div>