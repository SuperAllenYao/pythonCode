#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 导入模块
from lxml import etree

html_data = """
<html lang="zh-CN"><head><script src="//pingjs.qq.com/h5/stats.js?v2.0.2" name="MTAH5" sid="500460529"></script>
  <title>腾讯首页</title>
  <meta charset="gb2312">
  <meta http-equiv="X-UA-Compatible" content="IE=Edge">
  <meta name="baidu-site-verification" content="cNitg6enc2">
  <meta name="theme-color" content="#FFF">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="format-detection" content="telephone=no">
  <script src="//js.aq.qq.com/js/aq_common.js"></script>
  <script type="text/javascript">
try {
  if (location.search.indexOf('?pc') !== 0 && /Android|Windows Phone|iPhone|iPod/i.test(navigator.userAgent)) {
    window.location.href = 'https://xw.qq.com?f=qqcom';
  }
} catch (e) {}
</script><!--[if !IE]>|xGv00|2d5210e6c1b95e3bf4b8983f9cb00ab3<![endif]-->
  <meta content="资讯,新闻,财经,房产,视频,NBA,科技,腾讯网,腾讯,QQ,Tencent" name="Keywords">
  <meta name="description" content="腾讯网从2003年创立至今，已经成为集新闻信息，区域垂直生活服务、社会化媒体资讯和产品为一体的互联网媒体平台。腾讯网下设新闻、科技、财经、娱乐、体育、汽车、时尚等多个频道，充分满足用户对不同类型资讯的需求。同时专注不同领域内容，打造精品栏目，并顺应技术发展趋势，推出网络直播等创新形式，改变了用户获取资讯的方式和习惯。">
  <link rel="shortcut icon" href="//mat1.gtimg.com/www/icon/favicon2.ico">
  <link rel="stylesheet" href="//mat1.gtimg.com/pingjs/ext2020/qqindex2018/dist/css/qq_eefda19a.css" charset="utf-8">
<script id="_gdt_loader_0.08364318710508245" data-name="1648225091" type="text/javascript" charset="utf-8" src="https://qzonestyle.gtimg.cn/qzone/biz/ac/comm/qbscomm.20150907.js"></script><script id="_gdt_loader_0.6518717861667793" data-name="1001645319" type="text/javascript" charset="utf-8" src="https://qzonestyle.gtimg.cn/qzone/biz/ac/comm/gdtlib.20181219.js"></script><script id="_gdt_loader_0.6620049847759459" data-name="1513054522" type="text/javascript" charset="utf-8" src="https://qzonestyle.gtimg.cn/qzone/biz/ac/comm/ver.20170622.js"></script><style></style><script src="//l.qq.com/lview?c=www&amp;loc=NEW_QQCOM_N_Width1,NEW_QQCOM_N_Width2,NEW_QQCOM_N_button1,NEW_QQCOM_N_Width3,NEW_QQCOM_N_button2,NEW_QQCOM_N_Width4,NEW_WWW_RM_RightMove1,NEW_QQ_Couplet&amp;callback=crystal.callbackarea&amp;rot=1&amp;ri=l.&amp;chl=www&amp;page_type=1&amp;k=&amp;t=%E8%85%BE%E8%AE%AF%E9%A6%96%E9%A1%B5&amp;r=&amp;s=" charset="gbk"></script><link rel="stylesheet" type="text/css" href="//vm.gtimg.cn/tencentvideo/txp/style/txp_desktop.css?_=1564051875449"><script async="" src="//vm.gtimg.cn/c/=/tencentvideo/txpv5/creative/plugins/txp-creative-player.1.0.141.js,/tencentvideo/txp/js/plugins/htmlframe.50adbc.js,v4hdplayer.12e55c.js,uishadow.dbb436.js,hdadadapter.3098df.js,uiposter.c4db0a.js,v4h5report.5c3009.js,v4hdplayerreport.50720c.js,uiloading.15fe25.js,uiloadingwithad.e5afd0.js,hdplayerhistory.fb9c37.js,hlshelper.cedfbe.js,v4hdplayercontrol.658637.js,downloadmonitor.438f48.js,v4uierror.543c06.js,uitips.966cb8.js,uicontrol.52391c.js,uiprogress.174747.js,v4uicontrolplay.b0f651.js,uiplaynext.223a63.js?max_age=604800&amp;_ts=1564051875449" charset="utf-8"></script><script async="" src="//vm.gtimg.cn/c/=/tencentvideo/txp/js/plugins/uiloopplay.7d87cb.js,uishowtime.efe8a4.js,uiduration.1c3197.js,uibarragebtn.9c828a.js,v4uidefinition.72c9b7.js,uispeed.c02463.js,v4uivolume.028862.js,uipreview.4b99c0.js,uipreviewlist.09c56f.js,uipreviewad.bbe4e7.js,uiwindowfullscreen.494cb1.js,uilogo.ca9bc2.js,videointeractive.5851ec.js,uititle.9a4570.js,hdhotkey.afb6e0.js,uiscreenpercent.c62e91.js,uitrbtngroup.073444.js,uipip.c38ffc.js,uioverlayplay.d47f65.js,uiclock.2673c9.js?max_age=604800&amp;_ts=1564051875449" charset="utf-8"></script><script async="" src="//vm.gtimg.cn/c/=/tencentvideo/txp/js/plugins/uiconsole.55d961.js,uiwatermark.769ec3.js,uiwatermarkaction.1ca706.js,uirightclickmenu.233e7e.js,uiunofficialendtip.f7be9c.js,uiopenclientbubble.3be267.js?max_age=604800&amp;_ts=1564051875449" charset="utf-8"></script><link rel="stylesheet" type="text/css" href="//vm.gtimg.cn/c/=/tencentvideo/txp/style/txp_barrage.css?_=1564051875449"><script src="https://ra.gtimg.com/web/default_fodders/defaultFodder.js"></script><script src="//dp3.qq.com/dynamic?get_type=cm&amp;ch=www&amp;callback=crystal.cookieMapping"></script></head>

<body>

  <div class="global">

    <!-- 大皮肤 -->
    <div id="big-skin" class="layout qq-skin" style=""></div>
    <!-- /大皮肤 -->

    <!-- 头部 -->
    <div class="layout qq-top cf" bossexpo="bg_top">

      <h1 class="top-logo fl">
        <a href="/" target="_blank" bosszone="top_logo">
          <img width="100%" src="//mat1.gtimg.com/pingjs/ext2020/qqindex2018/dist/img/qq_logo_2x.png" alt="腾讯网">
        </a>
      </h1>

      <!-- 小皮肤 -->
      <div id="small-skin" class="skin-min fl"></div>
      <!-- /小皮肤 -->

      <!-- 搜索 -->
      <div class="top-search fl" id="sosobar" role="search" bosszone="top_search">
        <form id="searchForm" method="get" name="soso_search_box" action="https://www.sogou.com/tx?hdq=sogou-wsse-3f7bcd0b3ea82268&amp;ie=utf-8&amp;query=" target="_blank">
          <div id="searchTxt" class="searchTxt">
            <input type="hidden" value="w.q.in.sb.web" name="cid">
            <div class="searchMenu fl">
              <div class="searchSelected" id="searchSelected">网页</div>
              <div class="searchTab" id="searchTab" style="display: none;">
                <ul></ul>
              <ul><li class="selected">网页</li><li>图片</li><li>视频</li><li>音乐</li><li>地图</li><li>问问</li><li>百科</li><li>新闻</li><li>购物</li></ul></div>
            </div>
            <input id="sougouTxt" type="text" value="" name="w" aria-label="请输入搜索文字" autocomplete="off">
            <div class="searchSmart" id="searchSmart" style="display: none; visibility: hidden;">
              <ul></ul>
            </div>
            <div class="fr">
              <button id="searchBtn" class="searchBtn" type="submit">搜狗搜索</button>
            </div>
          </div>
        <input type="hidden" name="hidden"></form>
      </div>
      <script type="text/javascript">
        function sogouShow() {}
        function sosoShow() {}
      </script>
      <!-- /搜索 -->

      <!-- 登录 -->
      <div id="top-login" class="top-login fr">
        <div class="item item-qzone fl">
          <a href="https://qzone.qq.com" class="q-icons l-qzone" target="_blank" bosszone="top_qzone">Qzone</a>
          <div class="pop">
            <i class="arr-icon"></i>
            <a class="txt" href="https://qzone.qq.com" target="_blank" bosszone="top_qzone">点击查看QQ空间</a>
          </div>
        </div>
        <div class="item item-qmail fl">
          <a href="https://mail.qq.com" class="q-icons l-qmail" target="_blank" bosszone="top_mail">Qmail</a>
          <div class="pop">
            <i class="arr-icon"></i>
            <a class="txt" href="https://mail.qq.com/cgi-bin/loginpage" target="_blank" bosszone="top_mail">点击查看QQ邮箱</a>
          </div>
        </div>
        <div class="item item-login fl">
          <a class="l-login" href="javascript:;" onclick="userLogin()" bosszone="top_login">登录</a>
          <div class="pop">
            <i class="arr-icon"></i>
            <div class="nick">你好，</div>
            <a class="loginout" href="javascript:;" onclick="login.loginOut()" bosszone="top_login">[退出登录]</a>
          </div>
        </div>
      </div>
      <!-- /登录 --><!--515e8a9b2bd0d8267501d39b452aab86--><!--[if !IE]>|xGv00|5a4447b21df6aecffe06d861a91af412<![endif]-->

    </div>
    <!-- /头部 -->

    <!-- 导航 -->
    <div class="layout qq-nav">
      <div class="nav-mod cf">
        <ul class="nav-main fl" bossexpo="bg_dh_1">
    <li class="nav-item">
    <a href="http://news.qq.com" target="_blank" bosszone="dh_1">新闻</a>
  </li>
    <li class="nav-item">
    <a href="http://v.qq.com" target="_blank" bosszone="dh_2">视频</a>
  </li>
    <li class="nav-item">
    <a href="http://new.qq.com/ch/photo/" target="_blank" bosszone="dh_3">图片</a>
  </li>
    <li class="nav-item">
    <a href="https://new.qq.com/ch/milite/" target="_blank" bosszone="dh_4">军事</a>
  </li>
    <li class="nav-item">
    <a href="http://sports.qq.com/" target="_blank" bosszone="dh_5">体育</a>
  </li>
    <li class="nav-item">
    <a href="http://sports.qq.com/nba/" target="_blank" bosszone="dh_6">NBA</a>
  </li>
    <li class="nav-item">
    <a href="https://new.qq.com/ch/ent/" target="_blank" bosszone="dh_7">娱乐</a>
  </li>
    <li class="nav-item">
    <a href="http://finance.qq.com" target="_blank" bosszone="dh_8">财经</a>
  </li>
    <li class="nav-item">
    <a href="https://new.qq.com/ch/tech/" target="_blank" bosszone="dh_9">科技</a>
  </li>
    <li class="nav-item">
    <a href="https://new.qq.com/ch/fashion/" target="_blank" bosszone="dh_10">时尚</a>
  </li>
    <li class="nav-item">
    <a href="http://auto.qq.com/" target="_blank" bosszone="dh_11">汽车</a>
  </li>
    <li class="nav-item">
    <a href="http://house.qq.com/" target="_blank" bosszone="dh_12">房产</a>
  </li>
    <li class="nav-item">
    <a href="https://new.qq.com/ch/edu/" target="_blank" bosszone="dh_13">教育</a>
  </li>
    <li class="nav-item">
    <a href="https://new.qq.com/ch/cul/" target="_blank" bosszone="dh_14">文化</a>
  </li>
    <li class="nav-item">
    <a href="https://new.qq.com/ch/games/" target="_blank" bosszone="dh_15">游戏</a>
  </li>
    <li class="nav-item">
    <a href="http://astro.fashion.qq.com/" target="_blank" bosszone="dh_16">星座</a>
  </li>
  </ul><!--2cd95688b05ed9807ddf0f2089839f67--><!--[if !IE]>|xGv00|4aafa5db9f486a66b732bd13e91146b3<![endif]-->
        <div class="nav-more fl">
  <div class="more-txt" bosszone="dh_more">更多</div>
  <div class="nav-sub" bossexpo="bg_dh_2">
    <ul class="sub-list cf">
            <li class="nav-item">
          <a href="https://new.qq.com/ch/ori/" target="_blank" bosszone="dh_1_2">独家</a>
      </li>
            <li class="nav-item">
          <a href="https://v.qq.com/tv/" target="_blank" bosszone="dh_2_2">热剧</a>
      </li>
            <li class="nav-item">
          <a href="http://gy.qq.com/" target="_blank" bosszone="dh_3_2">谷雨</a>
      </li>
            <li class="nav-item">
          <a href="http://new.qq.com/ch/history/" target="_blank" bosszone="dh_4_2">历史</a>
      </li>
            <li class="nav-item">
          <a href="http://sports.qq.com/premierleague/" target="_blank" bosszone="dh_5_2">英超</a>
      </li>
            <li class="nav-item">
          <a href="http://sports.qq.com/cba/" target="_blank" bosszone="dh_6_2">CBA</a>
      </li>
            <li class="nav-item">
          <a href="https://new.qq.com/ch2/star" target="_blank" bosszone="dh_7_2">明星</a>
      </li>
            <li class="nav-item">
          <a href="http://money.qq.com/" target="_blank" bosszone="dh_8_2">理财</a>
      </li>
            <li class="nav-item">
          <a href="http://digi.tech.qq.com/" target="_blank" bosszone="dh_9_2">数码</a>
      </li>
            <li class="nav-item">
          <a href="http://health.qq.com/" target="_blank" bosszone="dh_10_2">健康</a>
      </li>
            <li class="nav-item">
          <a href="http://auto.qq.com/" target="_blank" bosszone="dh_11_2">车型</a>
      </li>
            <li class="nav-item">
          <a href="http://www.jia360.com/" target="_blank" bosszone="dh_12_2">家居</a>
      </li>
            <li class="nav-item">
          <a href="http://class.qq.com/" target="_blank" bosszone="dh_13_2">课程</a>
      </li>
            <li class="nav-item">
          <a href="http://dajia.qq.com/" target="_blank" bosszone="dh_14_2">大家</a>
      </li>
            <li class="nav-item">
          <a href="https://new.qq.com/ch/comic/" target="_blank" bosszone="dh_15_2">动漫</a>
      </li>
            <li class="nav-item">
          <a href="http://gongyi.qq.com/" target="_blank" bosszone="dh_16_2">公益</a>
      </li>
            <li class="nav-item">
          <a href="http://tianqi.qq.com/index.htm" target="_blank" bosszone="dh_17_2">天气</a>
      </li>
            <li class="nav-item">
          <a href="https://new.qq.com/ch/politics/" target="_blank" bosszone="dh_18_2">政务</a>
      </li>
            <li class="nav-item">
          <a href="https://v.qq.com/channel/variety" target="_blank" bosszone="dh_19_2">综艺</a>
      </li>
            <li class="nav-item">
          <a href="http://news.qq.com/photon/photoex.htm" target="_blank" bosszone="dh_20_2">影展</a>
      </li>
            <li class="nav-item">
          <a href="https://new.qq.com/ch/world/" target="_blank" bosszone="dh_21_2">国际</a>
      </li>
            <li class="nav-item">
          <a href="http://sports.qq.com/csocce/csl/" target="_blank" bosszone="dh_22_2">中超</a>
      </li>
            <li class="nav-item">
          <a href="http://fans.sports.qq.com/#/" target="_blank" bosszone="dh_23_2">社区</a>
      </li>
            <li class="nav-item">
          <a href="http://v.qq.com/movie/" target="_blank" bosszone="dh_24_2">电影</a>
      </li>
            <li class="nav-item">
          <a href="http://stock.qq.com/" target="_blank" bosszone="dh_25_2">证券</a>
      </li>
            <li class="nav-item">
          <a href="https://new.qq.com/ch2/phone" target="_blank" bosszone="dh_26_2">手机</a>
      </li>
            <li class="nav-item">
          <a href="https://new.qq.com/ch/baby/" target="_blank" bosszone="dh_27_2">育儿</a>
      </li>
            <li class="nav-item">
          <a href="https://new.qq.com/ch/visit/" target="_blank" bosszone="dh_28_2">旅游</a>
      </li>
            <li class="nav-item">
          <a href="https://new.qq.com/ch/life/" target="_blank" bosszone="dh_29_2">生活</a>
      </li>
            <li class="nav-item">
          <a href="http://kid.qq.com/" target="_blank" bosszone="dh_30_2">儿童</a>
      </li>
            <li class="nav-item">
          <a href="http://book.qq.com/" target="_blank" bosszone="dh_31_2">文学</a>
      </li>
            <li class="nav-item">
          <a href="https://new.qq.com/omv/" target="_blank" bosszone="dh_32_2">享看</a>
      </li>
            <li class="nav-item">
          <a href="https://new.qq.com/ch/cul_ru" target="_blank" bosszone="dh_33_2">新国风</a>
      </li>
            <li class="nav-item">
          <a href="http://www.qq.com/map/" target="_blank" bosszone="dh_34_2">全部</a>
      </li>
          </ul>
  </div>
</div><!--6af4cd883164c06e94a55109d9285180--><!--[if !IE]>|xGv00|6d3c48df3e25771911fda6430fe7456d<![endif]-->
      </div>
    </div>
    <!-- /导航 -->

    <!-- 广告1 -->
    <div class="layout qq-gg gg-1 cf">
      <div class="col-1 fl">
        <!--NEW_QQCOM_N_Width1_div AD begin...."l=NEW_QQCOM_N_Width1&log=off"--><div id="NEW_QQCOM_N_Width1" style="width: 920px; height: 75px; display: block; position: relative; zoom: 1;" class="l_qq_com" adconfig_lview="l.qq.com" adconfig_charset="gbk" adconfig_lview_template="//l.qq.com/lview?c=www&amp;loc={loc}" oid="5056842" btoid="0" display="banner"><a href="https://c.l.qq.com/lclick?oid=5056842&amp;cid=3430580&amp;loc=NEW_QQCOM_N_Width1&amp;soid=m1vEkgAAXUjvJQDmkQHYjncRAZLm&amp;click_data=dXNlcl9pbmZvPW9BRGptenc4RUI0PSZwYWdlX3R5cGU9MSZzc3A9MSZ1cF92ZXJzaW9uPVMxMDB8TDg2NiZzaT0xNTM0NTQ3Njk=&amp;index=1&amp;chl=478" target="_blank" style="display:block;cursor:pointer;width:920px;height:75px;background-image:url(//wa.gtimg.com/website/201908/C2_NQNW_20190805114629569839.jpg);background-size:920px 75px;background-position:50% 50%;filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(src='//wa.gtimg.com/website/201908/C2_NQNW_20190805114629569839.jpg',sizingMethod='scale');"></a><a class="absolute a_cover" href="https://c.l.qq.com/lclick?oid=5056842&amp;cid=3430580&amp;loc=NEW_QQCOM_N_Width1&amp;soid=m1vEkgAAXUjvJQDmkQHYjncRAZLm&amp;click_data=dXNlcl9pbmZvPW9BRGptenc4RUI0PSZwYWdlX3R5cGU9MSZzc3A9MSZ1cF92ZXJzaW9uPVMxMDB8TDg2NiZzaT0xNTM0NTQ3Njk=&amp;index=1&amp;chl=478&amp;k=&amp;t=%E8%85%BE%E8%AE%AF%E9%A6%96%E9%A1%B5&amp;r=&amp;s=" target="_blank" rel="nofollow" style="position:absolute;width:920px;height:75px;left:0px;top:0px;cursor:pointer;z-index:10;background-color:#fff;filter:alpha(opacity=0);opacity:0;"></a><div style="position: absolute; left: 0px; bottom: 0px; width: 26px; height: 16px; z-index: 12; background-image: url(&quot;https://ra.gtimg.com/web/res/icon/leftbottom_new.png&quot;); background-position: right top; background-repeat: no-repeat no-repeat;"></div></div><!--NEW_QQCOM_N_Width1 AD end --><!--[if !IE]>|xGv00|5aeb88a89c01e5641c5589dce242c026<![endif]-->
      </div>
      <div class="col-2 fr">
        <div id="gg-focus1" class="gg-focus">
  <ul class="list">
    <li class="item" style="display: none;">
      <a href="http://www.qq.com/jubaoxuzhi.htm" target="_blank">
        <img src="//mat1.gtimg.com/pingjs/ext2020/test2017/netwatch.png" alt="网络监控">
      </a>
    </li>
    <li class="item" style="display: list-item;">
      <a href="https://110.qq.com/" target="_blank">
        <img src="//img1.gtimg.com/ninja/2/2018/10/ninja153907290259802.png" alt="腾讯网110">
      </a>
    </li>
    <li class="item" style="display: none;">
      <a href="http://report.12377.cn:13225/toreportinputNormal_anis.do" target="_blank">
        <img src="//img1.gtimg.com/ninja/2/2018/10/ninja153907291410277.png" alt="网上有害信息举报">
      </a>
    </li>
  </ul>
  <div class="dot"><span class=""></span><span class="active"></span><span class=""></span></div>
</div><!--d5b2246199483af4ee72144a8b27e37e--><!--[if !IE]>|xGv00|ee64106218efcd265762f083de1d2631<![endif]-->
      </div>
    </div>
    <!-- /广告1 -->

    <!-- 要闻 -->
    <div class="layout qq-main cf">
      <div class="col col-1 fl">

        <div id="main-news" class="mod m-news">

          <div class="hd cf">
            <h2 class="tit active fl"><a href="//news.qq.com" target="_blank" bosszone="yw_logo">要闻</a></h2>
            <span class="tit-line fl"></span>
            <h2 class="tit fl"></h2>
            <div id="m-weather" class="m-weather f14 fr">
              <a id="weaher-info" href="https://tianqi.qq.com/" target="_blank">
                <div id="ipWeather" class="w-city fl"></div>
                <div id="weatherIcon" class="w-icon fl"></div>
                <div id="weatherTemperature" class="w-du fl"></div>
              </a>

              <div id="weatherMore" class="weather-more">

                <!-- 天气详情 -->
                <div class="face front">
                  <div class="weatherMoreTitle cf">
                    <div class="weather-info fl">
                      <a id="weatherMoreLink" href="https://tianqi.qq.com/" target="_blank">
                        <span id="weatherMoreCity"></span>
                        <span id="weatherMoreTxt"></span>
                        <span id="weatherMoreTem"></span>
                      </a>
                    </div>
                    <div class="weatherMoreSet fr" id="weatherMoreSet">
                      <a href="javascript:void(0);">更换城市</a>
                    </div>
                  </div>
                  <div class="weatherMoreAir">
                    <a id="weatherMoreAirLink" href="https://tianqi.qq.com/" target="_blank">
                      空气质量：<span id="weatherMoreAirTxt" style="padding-right:20px;"></span>
                      PM2.5：<span id="weatherMoreAirPmTxt"></span>
                    </a>
                  </div>
                  <a id="weatherMoreFuture" class="weatherMoreFuture cf" href="https://tianqi.qq.com/" target="_blank">
                    <div class="weatherMoreFutureCon">
                      <div class="weatherMoreIcon w-icon" id="weatherMoreTodayIcon"></div>
                      <p><strong>今天</strong></p>
                      <p>
                        <span id="weatherMoreTodayHighest" class="weatherMoreMath">-</span>℃ -
                        <span id="weatherMoreTodayLowest" class="weatherMoreMathLow">-</span>
                        <span class="weatherMoreSign">℃</span>
                      </p>
                    </div>
                    <div class="weatherMoreFutureCon">
                      <div class="weatherMoreIcon w-icon" id="weatherMoreTomorrowIcon"></div>
                      <p><strong>明天</strong></p>
                      <p>
                        <span id="weatherMoreTomorrowHighest" class="weatherMoreMath">-</span>℃ -
                        <span id="weatherMoreTomorrowLowest" class="weatherMoreMathLow">-</span>
                        <span class="weatherMoreSign">℃</span></p>
                    </div>
                    <div class="weatherMoreFutureCon">
                      <div class="weatherMoreIcon w-icon" id="weatherMoreAfterTomorrowIcon"></div>
                      <p><strong>后天</strong></p>
                      <p>
                        <span id="weatherMoreAfterTomorrowHighest" class="weatherMoreMath">-</span>℃ -
                        <span id="weatherMoreAfterTomorrowLowest" class="weatherMoreMathLow">-</span>
                        <span class="weatherMoreSign">℃</span>
                      </p>
                    </div>
                  </a>
                </div>
                <!-- /天气详情 -->

                <!-- 城市设置 -->
                <div class="face back">
                  <div class="weatherMoreTitle cf">
                    <div class="fl">
                      <span>设置城市</span>
                    </div>
                    <a href="javascript:void(0);" id="weatherMoreReset" class="weatherMoreReset">恢复默认城市</a>
                  </div>
                  <div class="weatherMoreSelectLayout cf">
                    <div class="weatherMoreProviceLayout fl">
                      <div class="weatherMoreProviceDefault" id="ipSetProvince">北京市</div>
                      <div class="weatherMoreProviceSelect" id="weatherMoreProviceSelect">
                        <ul>
                          <li><a href="javascript:void(0);">北京市</a></li>
                          <li><a href="javascript:void(0);">上海市</a></li>
                          <li><a href="javascript:void(0);">天津市</a></li>
                          <li><a href="javascript:void(0);">重庆市</a></li>
                          <li><a href="javascript:void(0);">河北省</a></li>
                          <li><a href="javascript:void(0);">山西省</a></li>
                          <li><a href="javascript:void(0);">内蒙古</a></li>
                          <li><a href="javascript:void(0);">江苏省</a></li>
                          <li><a href="javascript:void(0);">安徽省</a></li>
                          <li><a href="javascript:void(0);">山东省</a></li>
                          <li><a href="javascript:void(0);">辽宁省</a></li>
                          <li><a href="javascript:void(0);">吉林省</a></li>
                          <li><a href="javascript:void(0);">黑龙江省</a></li>
                          <li><a href="javascript:void(0);">浙江省</a></li>
                          <li><a href="javascript:void(0);">江西省</a></li>
                          <li><a href="javascript:void(0);">福建省</a></li>
                          <li><a href="javascript:void(0);">湖北省</a></li>
                          <li><a href="javascript:void(0);">湖南省</a></li>
                          <li><a href="javascript:void(0);">河南省</a></li>
                          <li><a href="javascript:void(0);">广东省</a></li>
                          <li><a href="javascript:void(0);">广西</a></li>
                          <li><a href="javascript:void(0);">海南省</a></li>
                          <li><a href="javascript:void(0);">四川省</a></li>
                          <li><a href="javascript:void(0);">贵州省</a></li>
                          <li><a href="javascript:void(0);">云南省</a></li>
                          <li><a href="javascript:void(0);">西藏</a></li>
                          <li><a href="javascript:void(0);">陕西省</a></li>
                          <li><a href="javascript:void(0);">甘肃省</a></li>
                          <li><a href="javascript:void(0);">宁夏</a></li>
                          <li><a href="javascript:void(0);">青海省</a></li>
                          <li><a href="javascript:void(0);">新疆</a></li>
                          <li><a href="javascript:void(0);">香港</a></li>
                          <li><a href="javascript:void(0);">澳门</a></li>
                          <li><a href="javascript:void(0);">台湾省</a></li>
                        </ul>
                      </div>
                    </div>
                    <div class="weatherMoreCityLayout fl">
                      <div class="weatherMoreCityDefault" id="ipSetCity">北京市</div>
                      <div class="weatherMoreCitySelect" id="weatherMoreCitySelect">
                        <ul id="weatherMoreCitySelectUl">
                          <li><a href="javascript:void(0);">北京市</a></li>
                        </ul>
                      </div>
                    </div>
                  </div>
                  <div class="weatherMoreNews">
                    <div id="weatherMoreNewsCheckbox" class="weatherMoreNewsCheckbox weatherMoreNewsYes">同时更新资讯所属地</div>
                  </div>
                  <div class="weatherMoreBtn">
                    <input type="button" value="确定" id="weatherMoreSubmit" class="weatherMoreSubmit">
                    <input type="button" value="取消" id="weatherMoreCancel" class="weatherMoreCancel">
                  </div>
                </div>
                <!-- /城市设置 -->

              </div>
            </div><!--87dd1c20ecef276c7c41a49ad09c3aa9--><!--[if !IE]>|xGv00|649f4a5728d5a2f0ee5e39c7f629214a<![endif]-->
          </div>
          <div class="bd">

            <!-- 要闻 -->
            <div id="tab-news-01" class="tab-news" bossexpo="bg_yw">
              <style>
    .bgcolor1 {
        background: #f56300;
        color: #FFF;
        padding: 1px 3px;
        border-radius: 3px;
    }

    .bgcolor1:hover {
        color: #FFF;
    }
</style>
<ul class="yw-list" bosszone="yw_1">
    
    <li class="news-top">
                <a class=" bold" href="https://new.qq.com/omn/20190805/20190805A0RNTO00.html" target="_blank" newsexpo="yw1_1">点滴之间见初心——习近平与一封群众来信的故事</a>
            </li>

    
    <li class="">
                <a class="" href="https://new.qq.com/omn/20190806/20190806A02CZP00.html" target="_blank" newsexpo="yw2_1">彩云长在有新天 ——书写中国外交新华章之文明交流互鉴篇</a>
            </li>

    
    <li class="">
                <a class="" href="https://new.qq.com/omn/20190806/20190806A0395100.html" target="_blank" newsexpo="yw3_1">人民日报国际论坛：不能没有的公平</a>
            </li>

    
    <li class="">
                        <a class="" href="https://new.qq.com/omn/20190806/20190806A02CY200.html" target="_blank" data-icon="no-icon" newsexpo="yw4_1">推动社会主义文化繁荣兴盛</a>                <a class="" href="https://yslp.qq.com/gaoguang.htm" target="_blank" data-icon="no-icon" newsexpo="yw4_2">国力全开</a>                <a class="" href="http://news.qq.com/zt_http/bwcx.htm" target="_blank" data-icon="no-icon" newsexpo="yw4_3">不忘初心</a>                    </li>

    
    <li class="">
                        <a class="" href="https://new.qq.com/omn/20190805/20190805V0LO0H00.html" target="_blank" data-icon="no-icon" newsexpo="yw5_1">中国“夜经济”新图景</a>                <a class="" href="https://new.qq.com/omn/20190805/20190805A0IC8E00.html" target="_blank" data-icon="no-icon" newsexpo="yw5_2">他们远在边疆，却冲锋在科学报国前线</a>                    </li>

    
    <li class="">
                        <a class="" href="https://new.qq.com/omn/20190805/20190805A0GVQV00.html" target="_blank" data-icon="no-icon" newsexpo="yw6_1">实施就业优先政策</a>                <a class="" href="https://new.qq.com/omn/20190806/20190806A0388P00.html" target="_blank" data-icon="no-icon" newsexpo="yw6_2">为潜力巨大的消费市场培育强大新动能</a>                    </li>

    
    <li class="">
                        <a class="" href="https://new.qq.com/omn/20190806/20190806A036BN00.html" target="_blank" data-icon="no-icon" newsexpo="yw7_1">“破7”影响有限 汇率稳定可期</a>                <a class="" href="https://new.qq.com/omn/20190805/20190805A09RJ500.html" target="_blank" data-icon="no-icon" newsexpo="yw7_2">5G赋能雄安新区</a>                <a class="" href="http://www.qstheory.cn/zt2019/llxjj/index.htm" target="_blank" data-icon="no-icon" newsexpo="yw7_3">理上网来</a>                    </li>

    
    <li class="">
                        <a class="" href="https://new.qq.com/omn/PEG20190/PEG2019080500454000.html" target="_blank" data-icon="no-icon" newsexpo="yw8_1">闽晋冀发给县级以下文件减少30%—50%</a>                <a class="" href="https://new.qq.com/omn/20190805/20190805A09RFE00.html" target="_blank" data-icon="no-icon" newsexpo="yw8_2">麻城追忆红军干娘</a>                    </li>

    </ul><!--5576b49883a19144d703cad7313875b0--><!--[if !IE]>|xGv00|fccc60c6c66601a6ffca20589f59a4ed<![endif]-->
              <style type="text/css">
.news_color_3{color:#0c82ff!important;}
.news_color_4{color:#df5147!important;}
</style>

<ul class="yw-list" bosszone="yw_2">
          <li class="news-pic-txt cf">
      <div class="pic fl">
        <a href="https://new.qq.com/omn/20190806/20190806A028DC00.html" target="_blank" newsexpo="yw9_1">
          <img src="//img1.gtimg.com/ninja/2/2019/08/ninja156504331095391.jpg" alt="美国退出《中导条约》 普京：或将被迫研发中程导弹">
        </a>
      </div>
      <div class="txt fl">
        <a href="https://new.qq.com/omn/20190806/20190806A028DC00.html" target="_blank" newsexpo="yw9_1">美国退出《中导条约》 普京：或将被迫研发中程导弹</a>
        <div class="info">
          <a href="https://new.qq.com/omn/20190806/20190806A028DC00.html" target="_blank">
            
          </a>
        </div>
      </div>
    </li>
        <li>
              <a class="" href="https://new.qq.com/omn/20190806/20190806A01MIG00.html" target="_blank" newsexpo="yw10_1">新华时评：言而无信害人害己 暂停农产品采购责任在美方</a>
          </li>
        <li>
              <a class="" href="https://new.qq.com/omn/20190806/20190806A02X3D00.html" target="_blank" newsexpo="yw11_1">印度取消克什米尔自治引巴方担忧 印媒：局势像站在刀尖上</a>
          </li>
        <li>
              <a class="" href="https://new.qq.com/omn/TWF20190/TWF2019080501025200.html" target="_blank" newsexpo="yw12_1">董建华：支持正义市民 对妄想摧毁香港的害群之马说“不”</a>
          </li>
        <li>
              <a class="" href="https://new.qq.com/omn/20190806/20190806A011TM00.html" target="_blank" newsexpo="yw13_1">港府凌晨声明谴责暴力示威：正将香港推向极为危险的边缘</a>
          </li>
        <li>
              <a class="" href="https://new.qq.com/omn/20190806/20190806A02XJ800.html" target="_blank" newsexpo="yw14_1">韩方：朝鲜今晨再次发射两枚不明飞行器</a>
          </li>
        <li>
              <a class="" href="https://new.qq.com/omn/20190805/20190805A0Q2E900.html" target="_blank" newsexpo="yw15_1">新疆兵团一些党员干部认为不存在黑恶势力 被督导组点名</a>
          </li>
                    </ul><ul class="yw-list" bosszone="yw_3">
        <li class="news-pic-txt cf">
      <div class="pic fl">
        <a href="https://new.qq.com/omn/WLD20190/WLD2019080600013100.html" target="_blank" newsexpo="yw16_1">
          <img src="//img1.gtimg.com/ninja/2/2019/08/ninja156504395737994.jpg" alt="美国得州沃尔玛枪击案死亡人数上升至22人">
        </a>
      </div>
      <div class="txt fl">
        <a href="https://new.qq.com/omn/WLD20190/WLD2019080600013100.html" target="_blank" newsexpo="yw16_1">美国得州沃尔玛枪击案死亡人数上升至22人</a>
        <div class="info">
          <a href="https://new.qq.com/omn/WLD20190/WLD2019080600013100.html" target="_blank">
            
          </a>
        </div>
      </div>
    </li>
        <li>
              <a class="" href="https://new.qq.com/omn/20190805/20190805A0MY6800.html" target="_blank" newsexpo="yw17_1">趁美国新防长要来 韩美不顾朝方警告如期启动军演</a>
          </li>
        <li>
              <a class="" href="https://new.qq.com/omn/20190805/20190805V0NT4J00.html" target="_blank" newsexpo="yw18_1">法院庭长写保证书不与5女子往来 本人称不实 官方介入调查</a>
          </li>
        <li>
              <a class="" href="https://new.qq.com/omn/20190805/20190805A0QY4700.html" target="_blank" newsexpo="yw19_1">广东加强外籍教师管理，要求培训机构主动公示外教信息</a>
          </li>
        <li>
              <a class="" href="https://new.qq.com/omn/20190805/20190805V0RQ4700.html" target="_blank" newsexpo="yw20_1">南昌舰航拍画面曝光 多艘052D火力全开霸气“露腹肌”</a>
          </li>
        <li>
              <a class="" href="https://new.qq.com/omn/20190805/20190805V0Q3RK00.html" target="_blank" newsexpo="yw21_1">男子偶遇并辱骂15年前老师 弟弟当街追打被拘</a>
          </li>
  </ul><!--7c69c5c3f846e317ad6522f72abd51bc--><!--[if !IE]>|xGv00|76b03c83ff8a9facd3fb878fc18778f4<![endif]-->
            </div>
            <!-- /要闻 -->

            <!-- 地方新闻 -->
            <div id="tab-news-02" class="tab-news undis" bossexpo="bg_dfz">
              <ul class="yw-list" bosszone="dfz_1">
        <li class="news-top"><a href="https://new.qq.com/omn/20190806A0335D00" target="_blank">今明两天北京仍有雷阵雨，山区易生地质灾害</a></li>
          <li><a href="https://new.qq.com/omn/20190805A0DT8Y00" target="_blank">平谷醉酒女乘客殴打公交司机，法院判了</a></li>
          <li><a href="https://new.qq.com/omn/20190805A0CHJU00" target="_blank">北京将通过立法规范市民文明行为 </a></li>
          <li><a href="https://new.qq.com/omn/20190805A034FF00" target="_blank">北京7月二手房成交量同比降15％ </a></li>
          <li><a href="https://new.qq.com/omn/BJC2019080500373400" target="_blank">游客注意！北京105家景区受降雨影响临时关闭</a></li>
          <li><a href="https://new.qq.com/omn/20190805A07R1I00" target="_blank">北京石景山区八宝山街道一出纳贪污225万 获刑4年</a></li>
          <li><a href="https://new.qq.com/omn/20190805A07TLW00" target="_blank">北京大兴消防员帮被困居民开锁 </a></li>
          <li><a href="https://new.qq.com/omn/20190805A0E2QP00" target="_blank">北京东城宝华里百岁老人告别20余年蜗居</a></li>
                  </ul><ul class="yw-list" bosszone="dfz_2">
    <li class="news-pic-txt cf">
      <div class="pic fl">
        <a href="https://new.qq.com/omn/20190805A0AHN000" target="_blank">
          <img src="//inews.gtimg.com/newsapp_ls/0/9933794694_640330/0" alt="北京市因雨已转移211户299位市民">
        </a>
      </div>
      <div class="txt fl">
        <a href="https://new.qq.com/omn/20190805A0AHN000" target="_blank">北京市因雨已转移211户299位市民</a>
        <div class="info">
          <a href="https://new.qq.com/omn/20190805A0AHN000" target="_blank">
            北京日报客户端
          </a>
        </div>
      </div>
    </li>
                <li><a href="http://bj.jjj.qq.com/a/20190806/001571.htm" target="_blank">首店进首钢 新业态激活老园区</a></li>
                <li><a href="http://bj.jjj.qq.com/a/20190806/001636.htm" target="_blank">北京入汛以来降水量较去年同期少三成</a></li>
                <li><a href="http://bj.jjj.qq.com/a/20190806/001595.htm" target="_blank">通州北运河大堤路 一路林荫一路花</a></li>
                <li><a href="http://bj.jjj.qq.com/a/20190806/001617.htm" target="_blank">朝阳推“月老银行”婚恋服务</a></li>
                <li><a href="http://bj.jjj.qq.com/a/20190806/001620.htm" target="_blank">北京：11批次食品抽检不合格</a></li>
                <li><a href="http://bj.jjj.qq.com/a/20190806/001589.htm" target="_blank">北安河车辆段上盖将融入西山风景</a></li>
                        </ul><ul class="yw-list" bosszone="dfz_3">
    <li class="news-pic-txt cf">
      <div class="pic fl">
        <a href="https://new.qq.com/omn/20190805A0IA0600" target="_blank">
          <img src="//inews.gtimg.com/newsapp_ls/0/9935854559_640330/0" alt="贴心！地铁2号线、13号线试行强冷、弱冷车厢">
        </a>
      </div>
      <div class="txt fl">
        <a href="https://new.qq.com/omn/20190805A0IA0600" target="_blank">贴心！地铁2号线、13号线试行强冷、弱冷车厢</a>
        <div class="info">
          <a href="https://new.qq.com/omn/20190805A0IA0600" target="_blank">
            北京日报客户端
          </a>
        </div>
      </div>
    </li>
                <li><a href="https://new.qq.com/omn/20190805A07WQW00" target="_blank">大雨过后朝阳一小区16层楼的墙皮掉了，砸坏楼下车辆</a></li>
                <li><a href="https://new.qq.com/omn/20190805A0BJZV00" target="_blank">怀柔普降中到大雨 中高路西树行桥桥面下沉</a></li>
                <li><a href="https://new.qq.com/omn/20190805A0DP4M00" target="_blank">北京这些图书馆目前都开设了夜间时段</a></li>
                <li><a href="https://new.qq.com/omn/20190805A0FE5600" target="_blank">“夜京城”不光是吃吃喝喝 大有文章可做</a></li>
                <li><a href="https://new.qq.com/omn/20190805A0FZSO00" target="_blank">盈盈一水间，大运河畔话七夕</a></li>
  </ul><!--44262d6e9400fcfe05f230fb68db8595--><!--[if !IE]>|xGv00|51a41834cff4f2ec29bf10c460a4d127<![endif]-->
            </div>
            <!-- /地方新闻 -->

          </div>
        </div>
      </div>
      <div class="col col-2 fl">

        <!-- 今日话题 -->
        <div class="mod m-topic" bossexpo="bg_jrht">
  <div class="hd cf">
    <h2 class="tit active"><a href="https://new.qq.com/omn/author/41" target="_blank" bosszone="jrht_logo">今日话题</a></h2>
  </div>
  <div class="bd">
    <ul class="news-list">
                  <li class="news-top" bosszone="jrht_1">
          <a href="https://new.qq.com/omn/20190806/20190806A00G3F00.html" target="_blank">侠客岛：人民币破7，意味着什么？</a>
        </li>
                        <li bosszone="jrht_2">
                                                    <a class="cate" href="https://new.qq.com/omn/author/5093138" target="_blank">剥洋葱</a><span class="line">|</span>
                                                        <a href="https://new.qq.com/omn/20190805/20190805A0NM5D00.html" target="_blank">绝笔信女教师罗生门：学校、信访局、本人各执一词</a>
                                            </li>
                        <li bosszone="jrht_3">
                                                    <a class="cate" href="https://new.qq.com/omn/author/5413195" target="_blank">人民日报评论</a><span class="line">|</span>
                                                        <a href="https://new.qq.com/omn/20190805/20190805A0R55F00.html" target="_blank">被摘牌的“5A级景区”，如何进取？</a>
                                            </li>
                        <li bosszone="jrht_4">
                                                    <a class="cate" href="https://new.qq.com/omn/author/1795" target="_blank">半月谈网</a><span class="line">|</span>
                                                        <a href="https://new.qq.com/rain/a/20190806A03F4600" target="_blank">远离“假学生证” 珍惜个人诚信</a>
                                            </li>
                        <li bosszone="jrht_5">
                                                    <a class="cate" href="https://new.qq.com/omn/author/1209" target="_blank">瞭望</a><span class="line">|</span>
                                                        <a href="https://new.qq.com/omn/20190805/20190805A06KGI00.html" target="_blank">1个月成立超8000家相关企业，垃圾分类生意不容易</a>
                                            </li>
                        <li bosszone="jrht_6">
                                                    <a class="cate" href="https://new.qq.com/ch/history/" target="_blank">短史记</a><span class="line">|</span>
                                                        <a href="https://new.qq.com/omn/20190806/20190806A032PL00.html" target="_blank">三国谋士中真正最聪明的人，永远不说废话</a>
                                            </li>
                        <li bosszone="jrht_7">
                                                    <a class="cate" href="https://new.qq.com/omn/author/5107513" target="_blank">较真</a><span class="line">|</span>
                                                        <a href="https://new.qq.com/omn/20190805/20190805A06ALN00.html" target="_blank">年轻人晚睡会导致不长个？生长激素可不背这个锅</a>
                                            </li>
              </ul>
  </div>
</div><!--f5c63af8bbd0b653e04a5240bde256a4--><!--[if !IE]>|xGv00|558b5294e116d1d83070fba854945c68<![endif]-->
        <!-- /今日话题 -->

        <!-- 原创 十三邀 -->
        <div class="mod m-yao13" bossexpo="bg_ycsp">
  <div class="hd-2 cf">
    <h2 class="tit active">
                        <a href="http://v.qq.com/detail/8/83743.html" target="_blank" bosszone="ycsp_logo">
            <img src="//img1.gtimg.com/ninja/2/2019/07/ninja156393380829631.png" alt="1068魂考">
          </a>
                                                                                                      </h2>
  </div>
  <div class="bd">
    <ul class="news-list">
                                        <li class="news-pic-txt cf" bosszone="ycsp_2">
            <div class="pic video-box click-drag-play fl" bossvv="vv_ycsp">
              <img src="//img1.gtimg.com/orignal/pics/hv1/15/240/2313/150464040.jpg" alt="郭麒麟自述儿时遭性侵经历  呼吁性教育别忽视男童">
              <i class="q-icons icon-play2"></i>
              <div class="txt undis">郭麒麟自述儿时遭性侵经历  呼吁性教育别忽视男童</div>
              <div class="desc undis">f00310xr14l</div>
              <div id="mod-player4" class="mod-player" data-vid="f00310xr14l" data-url="https://v.qq.com/x/cover/khl3pkdjym7jfck/f00310xr14l.html" style="display: none;"></div>
              <div class="click-layer"></div>
            </div>
            <div class="txt fl">
              <a href="https://v.qq.com/x/cover/khl3pkdjym7jfck/f00310xr14l.html" target="_blank">郭麒麟自述儿时遭性侵经历  呼吁性教育别忽视男童</a>
              <div class="info">

              </div>
            </div>
          </li>
                                          <li bosszone="ycsp_3">
                                        <a href="https://v.qq.com/x/cover/khl3pkdjym7jfck/v0031nr5z6v.html" target="_blank">[爆猛料]郝景芳自述童年曾遭熟人性侵 不敢告诉父母  </a>
                      </li>
                                          <li bosszone="ycsp_4">
                                        <a href="https://v.qq.com/x/cover/khl3pkdjym7jfck/e00311zwv2y.html" target="_blank">[你咋看] 姜思达：我可以和任何人拥抱 但不知如何抱母亲</a>
                      </li>
                                          <li bosszone="ycsp_5">
                                                                            <a class="cate q-icons icon-video" href="https://v.qq.com/x/cover/16ujegdnltfio83/u0906pt0ckm.html" target="_blank">再见前任</a><span class="line">|</span>
                                                                <a href="https://v.qq.com/x/cover/16ujegdnltfio83/v00316s5se1.html" target="_blank">认识10天就恋爱 女生：他冒雨帮我买卫生巾</a>
                                                    </li>
                                          <li bosszone="ycsp_6">
                                                                            <a class="cate q-icons icon-video" href="https://v.qq.com/x/page/v09044q4x34.html" target="_blank">有话请亮牌</a><span class="line">|</span>
                                                                <a href="https://v.qq.com/x/cover/29jwlm37ex12ant/k00313cam8j.html" target="_blank">姜文参演大片《星球大战》 全因儿子一句话</a>
                                                    </li>
                                          <li bosszone="ycsp_7">
                                                                            <a class="cate q-icons icon-video" href="https://v.qq.com/detail/8/84253.html" target="_blank">创战到底</a><span class="line">|</span>
                                                                <a href="https://v.qq.com/x/cover/duw6b652w1eydxn/e0031q0lwzp.html" target="_blank">马薇薇称一线城市聪明人更多 因此选择来北京</a>
                                                    </li>
                      </ul>
  </div>
</div><!--92b69435d3934e23f5af9cc0bd4a43c8--><!--[if !IE]>|xGv00|dc2823c59e9a434c7ec47c0daa4fa25c<![endif]-->
        <!-- /原创 十三邀 -->

        <!-- 图话 -->
        <div class="mod m-picture" bossexpo="bg_th">
          <div class="hd-2 cf">
            <h2 class="tit active">
              <a href="https://new.qq.com/ch/photo" target="_blank" bosszone="th_logo">图话</a>
            </h2>
          </div>
          <div class="bd">
            <ul class="news-list">
                    <li class="v-item news-pic-txt cf" bosszone="th_1">
      <div class="pic fl">
        <a href="https://new.qq.com/rain/a/20190805A099N700" target="_blank">
          <img src="//inews.gtimg.com/newsapp_ls/0/9940773823_640330/0" alt="银行职员从北京到贵州当第一书记 先学苗语和吃辣椒">
        </a>
      </div>
      <div class="txt fl">
        <a href="https://new.qq.com/rain/a/20190805A099N700" target="_blank">银行职员从北京到贵州当第一书记 先学苗语和吃辣椒</a>
        <div class="info">
          <a href="https://new.qq.com/rain/a/20190805A099N700" target="_blank">
            中国人的一天 第3511期
          </a>
        </div>
      </div>
    </li>
        <li class="v-item" bosszone="th_2">
                                                <a class="cate q-icons icon-pic" href="https://new.qq.com/omn/author/5825141" target="_blank">萤火体验</a><span class="line">|</span>
                                        <a href="https://new.qq.com/omn/20190801/20190805A0A0RX00.html" target="_blank">凯叔：我和一个6岁脑瘫孩子一起背声律启蒙</a>
                            </li>
  <!--90424db1d5a89e335b736cdc9f7c59ba--><!--[if !IE]>|xGv00|3b42bce940f5bcce148c9f9b3073b562<![endif]-->
                    <li class="v-item" bosszone="th_2">
                                                <a class="cate q-icons icon-pic" href="http://news.qq.com/guyu/huizong/hz_report.htm" target="_blank">谷雨</a><span class="line">|</span>
                                        <a href="https://new.qq.com/omn/20190802/20190802A0H0K200.html" target="_blank">对话谢梦遥：在罗永浩身上，我看见时代与自己</a>
                            </li>
  <!--951b4b640e73cc62886a2f66075106bb--><!--[if !IE]>|xGv00|99abc0c1a455b6991e22a8dc6135d991<![endif]-->
                    <li class="v-item" bosszone="th_3">
                                                <a class="cate q-icons icon-pic" href="http://sports.qq.com/photo/" target="_blank">体坛</a><span class="line">|</span>
                                        <a href="http://sports.qq.com/a/20190806/000712.htm" target="_blank">美国男篮集训猛将玩背扣 主帅波波维奇一脸严肃</a>
                            </li>
  <!--0f74d8c85b93def2df600e81682eb3e4--><!--[if !IE]>|xGv00|858694bee36edc8c4377bb4e11da2eb5<![endif]-->
                    <li class="v-item" bosszone="th_4">
                                                <a class="cate q-icons icon-pic" href="https://new.qq.com/omn/author/6853487" target="_blank">认真映画</a><span class="line">|</span>
                                        <a href="https://new.qq.com/omn/20190805A0RX0V00" target="_blank">直肠子真性情！那英怒怼无理记者</a>
                            </li>
  <!--3ef433783514f6657774c620cb143743--><!--[if !IE]>|xGv00|8b3fec3c541e33f4d2ebf47d0ab52ddf<![endif]-->
                    <li class="v-item" bosszone="th_5">
                                                <a class="cate q-icons icon-pic" href="https://new.qq.com/ch/fashion/" target="_blank">时尚圈</a><span class="line">|</span>
                                        <a href="https://new.qq.com/omn/20190723/20190723A08HSW00.html" target="_blank">要想在人群中出挑，就要找祖母的衣服来穿</a>
                            </li>
  <!--978dc49246baebee755884c474ddb5aa--><!--[if !IE]>|xGv00|a72ee1aaf8e8de1f7553913d34c1bbc7<![endif]-->
            </ul>
          </div>
        </div>
        <!-- /图话 -->

      </div>
      <div class="col col-3 fr">

        <!-- 产品 -->
        <div id="m-product" class="m-product">
  <ul class="list f14">
                                                                                <li class="q-icons prod-1">
                                                <a href="http://news.qq.com/mobile/" target="_blank" bosszone="cp_1_1_1">新闻APP</a>
                                  <a href="http://sports.qq.com/kbsweb/" target="_blank" bosszone="cp_1_1_2">体育APP</a>
                                  <a href="https://om.qq.com/userAuth/index" target="_blank" bosszone="cp_1_1_3">企鹅号</a>
                                  <a href="http://kuaibao.qq.com/" target="_blank" bosszone="cp_1_1_4">快报</a>
                                  <a href="http://v.qq.com/download.html#pc" target="_blank" bosszone="cp_1_1_5">视频</a>
                                  <a href="https://browser.qq.com/" target="_blank" bosszone="cp_1_1_6">浏览器</a>
                                  <a href="http://www.weishi.com/" target="_blank" bosszone="cp_1_1_7">微视</a>
                                        </li>
                                <li class="q-icons prod-2">
                                                <a href="http://weixin.qq.com/" target="_blank" bosszone="cp_1_2_1">微信</a>
                                  <a href="https://im.qq.com/index.shtml" target="_blank" bosszone="cp_1_2_2">QQ</a>
                                  <a href="https://qzone.qq.com/" target="_blank" bosszone="cp_1_2_3">空间</a>
                                  <a href="https://work.weixin.qq.com/wework_admin/register_wx?from=regopt_tlogo_wxcbar_tengxunwang" target="_blank" bosszone="cp_1_2_4">企业微信</a>
                                  <a href="https://mail.qq.com/cgi-bin/loginpage" target="_blank" bosszone="cp_1_2_5">邮箱</a>
                                  <a href="https://cloud.tencent.com/?fromSource=gwzcw.756432.756432.756432" target="_blank" bosszone="cp_1_2_6">腾讯云</a>
                                  <a href="https://guanjia.qq.com/?ADTAG=news.qqcom" target="_blank" bosszone="cp_1_2_7">电脑管家</a>
                                  <a href="https://vip.qq.com/" target="_blank" bosszone="cp_1_2_8">会员</a>
                                        </li>
                                <li class="q-icons prod-3">
                                                <a href="http://lol.qq.com/index.shtml?ADTAG=media.innerenter.qqcom.index_navigation" target="_blank" bosszone="cp_1_3_1">LOL</a>
                                  <a href="http://dnf.qq.com/?ADTAG=media.innerenter.qqcom.index_navigation" target="_blank" bosszone="cp_1_3_2">DNF</a>
                                  <a href="http://cf.qq.com/?ADTAG=media.innerenter.qqcom.index_navigation" target="_blank" bosszone="cp_1_3_3">CF</a>
                                  <a href="http://pvp.qq.com/?ADTAG=media.innerenter.qqcom.index_navigation" target="_blank" bosszone="cp_1_3_4">王者</a>
                                  <a href="https://gouhuo.qq.com/?ADTAG=QQHOME" target="_blank" bosszone="cp_1_3_5">单机游戏</a>
                                  <a href="http://huoying.qq.com/act/a20141009landingpage/index.htm?via=45&amp;ADTAG=ied.neiguang&amp;ADTAG=media.innerenter.qqcom.index_navigation" target="_blank" bosszone="cp_1_3_6">火影OL</a>
                                  <a href="http://wuxia.qq.com/?ADTAG=media.innerenter.qqcom.index_navigation" target="_blank" bosszone="cp_1_3_7">天刀</a>
                                  <a href="http://iwan.qq.com/index.htm?ADTAG=media.innerenter.qqcom.indexnavigation" target="_blank" bosszone="cp_1_3_8">爱玩</a>
                                  <a href="http://nz.qq.com/main.shtml?ADTAG=media.innerenter.qqcom.index_navigation" target="_blank" bosszone="cp_1_3_9">逆战</a>
                                        </li>
                                <li class="q-icons prod-4">
                                                <a href="https://pc.qq.com/" target="_blank" bosszone="cp_1_4_1">软件</a>
                                  <a href="https://pay.qq.com/" target="_blank" bosszone="cp_1_4_2">Q币</a>
                                  <a href="https://www.jd.com/?utm_source=qq.com&amp;utm_medium=cpc&amp;utm_campaign=dmp_77&amp;utm_term=dmp_77_11727_d604816f27c2b5e98ae51fd59de8b1c43abfdac_1538472240" target="_blank" bosszone="cp_1_4_3">京东</a>
                                  <a href="https://map.qq.com/#city=%D6%D0%B9%FA&amp;wd=%D6%D0%B9%FA" target="_blank" bosszone="cp_1_4_4">腾讯地图</a>
                                  <a href="https://docs.qq.com/" target="_blank" bosszone="cp_1_4_5">腾讯文档</a>
                                  <a href="https://qian.qq.com/?stat_data=oth87ppcsy00222&amp;ADTAG=SCQD.BD.PC.TXDH1" target="_blank" bosszone="cp_1_4_6">理财通</a>
                                  <a href="http://www.qq.com/map/" class="more" target="_blank" bosszone="cp_1_4_7">全部</a>
                                        </li>
                </ul>
  <div id="prod-more" class="prod-more">
    <div class="prod-more-btn">
      <div class="q-icons btn-icon">展开</div>
    </div>
    <ul class="list f14">
                        <li class="prod-1">
                                                <a href="https://new.qq.com/omv" target="_blank" bosszone="cp_2_1_6">享看</a>
                                  <a href="http://qq.pinyin.cn/" target="_blank" bosszone="cp_2_1_5">QQ拼音</a>
                                  <a href="http://player.qq.com/" target="_blank" bosszone="cp_2_1_4">QQ影音</a>
                                  <a href="https://pc.qq.com/detail/15/detail_755.html" target="_blank" bosszone="cp_2_1_3">QQ影像</a>
                                  <a href="http://www.weiyun.com/index.html" target="_blank" bosszone="cp_2_1_2">微云</a>
                                  <a href="https://fm.qq.com/" target="_blank" bosszone="cp_2_1_1">企鹅FM</a>
                                        </li>
                                <li class="prod-2">
                                                <a href="http://book.qq.com/?g_f=70085" target="_blank" bosszone="cp_2_2_5">QQ阅读</a>
                                  <a href="https://y.qq.com/" target="_blank" bosszone="cp_2_2_4">QQ音乐</a>
                                  <a href="http://kg.qq.com/" target="_blank" bosszone="cp_2_2_3">全民K歌</a>
                                  <a href="http://z.qzone.com/" target="_blank" bosszone="cp_2_2_2">手机空间</a>
                                  <a href="https://im.qq.com/mobileqq/" target="_blank" bosszone="cp_2_2_1">手机QQ</a>
                                        </li>
                                <li class="prod-3">
                                                <a href="http://speed.qq.com/main.shtml?ADTAG=media.innerenter.qqcom.index_navigation" target="_blank" bosszone="cp_2_3_7">QQ飞车</a>
                                  <a href="http://yxwd.qq.com/?ADTAG=media.innerenter.qqcom.index_navigation" target="_blank" bosszone="cp_2_3_6">英雄</a>
                                  <a href="http://dn.qq.com/cp/a20180904ysjj/index.htm" target="_blank" bosszone="cp_2_3_5">龙之谷</a>
                                  <a href="http://eafifa.qq.com/?ADTAG=media.innerenter.qqcom.index_navigation" target="_blank" bosszone="cp_2_3_4">FIFA</a>
                                  <a href="http://hdl.qq.com/index.shtml?ADTAG=media.innerenter.qqcom.index_navigation" target="_blank" bosszone="cp_2_3_3">魂斗罗</a>
                                  <a href="http://cfm.qq.com/cp/a20180927vacation/index.html" target="_blank" bosszone="cp_2_3_2">CF手游</a>
                                  <a href="http://tlbb.qq.com/main.shtml?ADTAG=media.innerenter.qqcom.index_navigation" target="_blank" bosszone="cp_2_3_1">天龙手游</a>
                                        </li>
                                <li class="prod-4">
                                                <a href="http://xing.qq.com/" target="_blank" bosszone="cp_2_4_7">星钻</a>
                                  <a href="https://888.qq.com/?bc_tag=10161.1.1" target="_blank" bosszone="cp_2_4_6">QQ彩票</a>
                                  <a href="http://cb.qq.com/?attach=200_1000_10090&amp;QQ_from=200_1000_10090" target="_blank" bosszone="cp_2_4_5">彩贝</a>
                                  <a href="http://time.qq.com/?pgv_ref=qqcom" target="_blank" bosszone="cp_2_4_4">时光画轴</a>
                                  <a href="https://tianqi.qq.com/" target="_blank" bosszone="cp_2_4_3">天气</a>
                                  <a href="http://users.qq.com/" target="_blank" bosszone="cp_2_4_2">用户社区</a>
                                  <a href="https://dreamreader.qq.com/" target="_blank" bosszone="cp_2_4_1">海豚智音</a>
                                        </li>
                                                                          </ul>
  </div>
</div><!--9de1b512d09d0d4df1e399ec6e2cc872--><!--[if !IE]>|xGv00|f35e9792d735dd2619210d01e67978fc<![endif]-->
        <!-- /产品 -->

        <!-- 热门赛事 -->
        <div class="mod m-match" bossexpo="bg_rmss">
  <div class="hd cf">
    <h2 class="tit active fl">
      <a href="http://kbs.sports.qq.com/#hot" target="_blank" bosszone="rmss_logo">热门赛事</a>
    </h2>
    <div class="fr">
      <a id="match-info" class="match-info" href="http://kbs.sports.qq.com/#hot" target="_blank" bosszone="rmss_sc">
        <span class="match-time">8月6日</span>
        <span class="tit-line"></span>
        <span class="q-icons match-txt">上午好，今天有24场热门比赛</span>
      </a>
    </div>
  </div>
  <div class="bd">
    <ul class="news-list">
                            <li class="video-box click-pop-play" bosszone="rmss_1" bossvv="vv_rmss">
          <img src="//img1.gtimg.com/ninja/2/2019/08/ninja156505597898115.jpg" alt="李娜纪录片震撼上线：独家揭秘李娜愤怒来源">
          <i class="q-icons icon-play"></i>
          <span class="txt">李娜纪录片震撼上线：独家揭秘李娜愤怒来源</span>
          <div class="desc undis">g00318x1j6x</div>
                    <div id="mod-player1" class="mod-player" data-vid="g00318x1j6x" data-url="https://v.qq.com/x/cover/swvj84vmqs90ng7/g00318x1j6x.html" style="display: none;">   <txpdiv class="txp_player txp_player_desktop txp_autohide_progress txp_player_external txp_player_xs txp_player_mini txp_autohide" id="txplayer_8477900f66e6eafb9eb05710b44b60f5" style="width:100%;height:100%" tabindex="-1">   <div style="width:1px;height:1px;display:block;-webkit-user-select: auto;user-select: auto;"></div>   <txpdiv class="txp_gradient_top txp_none" data-role="txp-frame-gradient-top"></txpdiv>   <txpdiv class="txp_gradient_bottom"></txpdiv>   <txpdiv data-role="txp-video-wrapper" class="txp_video_container">   <video style="background-color: rgb(0, 0, 0); width: 100%; height: 100%; display: block;" webkit-playsinline="" x-webkit-airplay="" preload="auto" muted="" data-role="txp_video_tag"></video>   <video style="background-color: rgb(0, 0, 0); width: 100%; height: 100%; display: none;" webkit-playsinline="" x-webkit-airplay="" preload="auto" muted="" data-role="txp_video_tag"></video> <txpdiv data-role="txp-shadow-mod" class="txp_shadow" style="pointer-events: initial;"></txpdiv></txpdiv><txpdiv data-role="hd-ad-adapter-videoadcountdownlayer" class="txp_none" style="position: absolute; top: 0px; right: 0px; width: 100%; height: 100%; z-index: 4; pointer-events: none;"><txpdiv class="txp_ad_control txp_none" data-role="adplayer-enter-countdown">
    <txpdiv class="txp_ad_skip">
        <txpdiv class="txp_ad_countdown" data-role="adplayer-enter-countdown-num"></txpdiv>
        <txpdiv class="txp_ad_skip_text">进入广告</txpdiv>
    </txpdiv>
</txpdiv></txpdiv><txpdiv data-role="hd-ad-adapter-interactivelayer" class="" style="position: absolute; top: 0px; right: 0px; width: 100%; height: 100%; z-index: 4; pointer-events: none;"></txpdiv><txpdiv data-role="hd-ad-adapter-adlayer" class="txp_none" style="position: absolute; top: 0px; right: 0px; width: 100%; height: 100%; z-index: 4; background-color: rgb(0, 0, 0);"><style>
    .txp_btn_ad_volume{
        background: rgba(37, 37, 37, .7) url(https://ca.gtimg.com/adplugin/js/imgs/mutes.png) no-repeat;
        height: 28px;
        border: none;
        border-radius: 14px;
        width: 28px;
        margin-left: 8px;
        user-select: initial;
        outline: none;
    }
    .txp_btn_ad_mute{
        background-position-y: -28px;
    }
    /* adblock */
    .txp_cac_black_screen {
        position: absolute;
        top: 0;
        bottom: 0;
        left: 0;
        width: 100%;
        z-index: 1000;
        background-color: #000;
        text-align: center;
        display: flex;
        line-height: 1.5;
        flex-direction: column;
        justify-content: center;
    }
    .txp_cac_black_screen .txp_cac_black_screen_title {
        margin-bottom: 15px;
        font-size: 16px;
        color: #fff;
        text-align: center;
    }
    .txp_cac_black_screen .txp_cac_black_screen_em {
        display: inline;
        color: #ff7000;
    }
    
</style>
<txpdiv data-role="adplayer-video-container" class="txp_ad" style="width: 100%; height: 100%;">

    <!-- 广告 video 标签容器-->
    <txpdiv data-role="adplayer-video-ad-container" style="width: 100%; height: 100%; position: relative;"></txpdiv>

    <!-- 广告 富媒体容器标签 -->
    <txpdiv data-role="adplayer-video-rich-media-ad-container" style="width: 100%; height: 100%;"></txpdiv>

    <txp data-role="aplayer-video-black-screen" class="txp_cac_black_screen txp_none">
        <txp class="txp_cac_black_screen_title">广告被拦截插件误伤啦，<txp class="txp_cac_black_screen_em">1</txp>秒后播放</txp>
        <txp>关闭拦截插件恢复正常</txp>
    </txp>

    <!-- 内部区域 -->
    <txpdiv data-role="adplayer-video-inner" class="txp_ad_inner txp_none">
        <!-- 广告点击区域 -->
        <a data-role="adplayer-video-link-area" href="javascript:;" class="txp_ad_link"></a>

        <!-- 详情点击 -->
        <a data-role="adplayer-video-detail-btn" class="txp_ad_more" href="javascript:;"><txpdiv data-role="adplayer-video-detail-btn-text"></txpdiv><txpdiv class="txp_icon_arrow"></txpdiv></a>

        <!-- 底部介绍 -->
        <txpdiv data-role="adplayer-video-dsp-name-text" style="left:10px;bottom:10px;position:absolute;opacity:0.6;font-size:12px;text-shadow:2px 2px #000"></txpdiv>

        <!-- 无法跳过广告按钮 -->
        <txpdiv class="txp_ad_control" data-role="adplayer-video-ad-control">
            <txpdiv class="txp_ad_skip">
                <!-- 倒计时 -->
                <txpdiv data-role="adplayer-video-countdown" class="txp_ad_countdown"></txpdiv>

                <!-- 跳过广告文案或者进入广告文案 -->
                <txpdiv data-role="adplayer-video-skip-text" class="txp_ad_skip_text" style="cursor: pointer;"></txpdiv>

                <!-- 关闭广告按钮 -->
                <button data-role="adplayer-video-close-btn" class="txp_btn txp_btn_close"></button>

                <!-- 无法免广告说明 -->
                <button data-role="adplayer-video-no-skip-btn" class="txp_btn txp_btn_hint" title="无法跳过广告说明"></button>
            </txpdiv>
            <button data-role="adplayer-video-volume-btn" class="txp_btn txp_btn_ad_volume txp_none" style="z-index: 10;position: relative;">
            </button>
        </txpdiv>

        <!-- 无法免广告弹窗说明 -->
        <txpdiv data-role="adplayer-video-no-skip-dialog" class="txp_ad_dialog txp_none">
            <txpdiv class="txp_dialog_bd">
                为了给腾讯视频用户提供更多优质美剧，应<span data-role="adplayer-video-no-skip-author">版权方（华纳）</span>要求，好莱坞会员在观看华纳美剧时无法跳过广告（《吸血鬼日记》《破产姐妹》《无耻之徒》等）。我们会为会员用户继续争取免广告权益，请您谅解，谢谢！
            </txpdiv>
            <txpdiv data-role="adplayer-video-no-skip-know-btn" class="txp_ad_btn">我知道了!</txpdiv>
            <a class="txp_ad_fb" target="_blank" href="http://support.qq.com/write.shtml?fid=850">意见反馈</a>
            <button data-role="adplayer-video-no-skip-close-btn" class="txp_btn txp_btn_close"></button>
        </txpdiv>
    </txpdiv>
</txpdiv></txpdiv><txpdiv data-role="txp-ui-poster" class="txp_poster" style="background-image: url(&quot;https://vpic.video.qq.com/81161444/g00318x1j6x.png&quot;); background-size: cover;"></txpdiv><txpdiv class="txp_overlay_loading">   <txpdiv class="txp_text txp_none" data-role="txp-ui-continue-play"></txpdiv>   <txpdiv class="txp_icon_loading txp_none" data-role="txp-ui-loading"></txpdiv> </txpdiv><txpdiv data-role="txp-ui-tips" class="txp_alert_info txp_none">   <txpdiv class="txp_alert_content">     <txpdiv data-role="txp-ui-tips-text" class="txp_alert_text"></txpdiv>     <button data-role="txp-ui-tips-close" class="txp_btn txp_btn_close" title="关闭"></button>   </txpdiv> </txpdiv><txpdiv data-role="txp-ui-loading-with-ad" class="txp_overlay_loading txp_none">   <txpdiv class="txp_overlay_loading_content">     <txpdiv class="txp_overlay_loading_ad" data-role="txp-ui-loading-with-ad-layer"></txpdiv>          <img class="txp_overlay_loading_slogan" src="//vm.gtimg.cn/tencentvideo/txp/style/img/slogan.png" style="width:165px">     <txpdiv class="txp_overlay_loading_name">腾讯视频 v.qq.com</txpdiv>          <txpdiv data-role="txp-ui-loading-with-ad-speed" class="txp_overlay_loading_speed"></txpdiv>     <txpdiv class="txp_overlay_loading_canvas">       <canvas data-role="txp-ui-loading-with-ad-canvas" width="800" height="450"></canvas>     </txpdiv>   </txpdiv> </txpdiv><txpdiv data-role="txp-ui-error" class="txp_video_error">   <img data-role="txp-ui-error-tip" class="txp_error_pic" alt="" src="//i.gtimg.cn/qqlive/images/20170712/error_tip1.png" srcset="//i.gtimg.cn/qqlive/images/20170712/error_tip1@2x.png 2x">   <txpdiv class="txp_error_title">     <span data-role="txp-ui-error-msg">很抱歉，由于版权限制，您所在的地区暂时无法播放该视频</span>     <span data-role="txp-ui-error-refresh" class="txp_none">       你可以 <button class="txp_btn">刷新</button>       <span data-role="txp-ui-error-changeplayer" class="txp_none"> 或 <button class="txp_btn">使用兼容模式播放</button></span>       <span class="" data-role="txp-ui-error-when-coolopen">试试</span>     </span>   </txpdiv>   <txpdiv class="txp_error_title2 txp_none" data-role="txp-ui-error-client-title">     <span data-role="txp-ui-error-client-span">使用PC客户端播放更稳定 </span>     <a class="txp_link_btn" data-role="txp-ui-error-client-btn">立即下载</a>     <txpdiv class="txp_error_title2 txp_link_btn txp_none" data-role="txp-ui-error-play-btn" style="margin-right: 0;">       返回继续播放     </txpdiv>   </txpdiv>   <span class="txp_none" data-role="txp-ui-error-qqbrowser-btn" style="margin: 16px 0 0 0;">     或使用最新 <a style="display:inline; margin: 16px 0 0 0;text-decoration: underline!important;">QQ浏览器</a> / Chrome观看   </span>   <txpdiv class="txp_error_code"><span data-role="txp-ui-error-code">[ 错误码:62101.13080.1 ]</span> <a href="//support.qq.com/products/2208" target="_blank">我要反馈</a></txpdiv> </txpdiv> <txpdiv data-role="txp-control-wrap" class="txp_bottom" style="overflow:initial;">   <txpdiv class="txp_controls">     <txpdiv class="txp_left_controls" data-role="txp-control-left"><txpdiv data-role="txp-ui-control-playbtn" class="txp_btn txp_btn_play" data-status="play" aria-label="播放/暂停">      <svg class="txp_icon txp_icon_play" version="1.1" viewBox="0 0 36 36">     <use class="txp_svg_symbol txp_svg_play" xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#txp_svg_play"></use>     <use class="txp_svg_symbol txp_svg_pause" xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#txp_svg_pause"></use>     <use class="txp_svg_symbol txp_svg_stop" xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#txp_svg_stop"></use>     <use class="txp_svg_symbol txp_svg_replay" xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#txp_svg_replay"></use>   </svg>   <txpdiv data-role="txp-ui-control-playbtn-tips" class="txp_tooltip">播放</txpdiv>    </txpdiv><txpdiv data-role="txp-ui-control-play-next" class="txp_btn txp_btn_next txp_none" data-report="play-next" aria-label="下一集">   <svg class="txp_icon txp_icon_next" version="1.1" viewBox="0 0 36 36">     <use class="txp_svg_symbol txp_svg_next" xlink:href="#txp_svg_next"></use>   </svg>   <txpdiv class="txp_tooltip txp_none" data-role="txp-next-tip">下一集</txpdiv> </txpdiv><txpdiv data-role="txp-control-time-mod" class="txp_time_display">   <txpdiv class="txp_time_current" data-role="txp-control-currenttime">00:00</txpdiv>   <txpdiv class="txp_time_separator">/</txpdiv>   <txpdiv class="txp_time_duration" data-role="txp-control-duration">00:00</txpdiv>   <txpdiv class="txp_live_badge">直播</txpdiv> </txpdiv></txpdiv>     <txpdiv class="txp_progress_bar_container" data-role="txp-control-center"><txpdiv class="txp_progress_list" data-role="txp-control-progress-list" style="background-color: transparent;">   <txpdiv class="txp_progress_load" style="width:0%" data-role="txp-control-load-progress"></txpdiv>   <txpdiv class="txp_progress_play" style="width:0%" data-role="txp-control-play-progress"></txpdiv>   <txpdiv class="txp_interact_progress_list">     <txpdiv class="txp_interact_dot txp_none" data-role="txp-control-play-start-time-point"></txpdiv>     <txpdiv class="txp_interact_dot txp_none" data-role="txp-control-play-end-time-point"></txpdiv>   </txpdiv> </txpdiv>  <txpdiv class="txp_btn_scrubber" style="left:0%" data-role="txp-control-play-point">   <txpdiv class="txp_scrubber_indicator" data-role="txp-control-progress-indicator" style="left:0;top:0;"></txpdiv> </txpdiv></txpdiv>     <txpdiv class="txp_right_controls" data-role="txp-control-right"><txpdiv class="txp_time_display" data-role="txp-button-duration">  <txpdiv class="txp_time_duration" data-role="txp-button-duration-time">00:00</txpdiv> </txpdiv><button data-role="txp-ui-control-barrage-btn" class="txp_btn txp_btn_barrage txp_none" data-report="barrage-btn">  <txpdiv class="txp_btn_inner">弹幕</txpdiv> </button><txpdiv data-role="txp-ui-control-definition" class="txp_btn txp_btn_definition txp_none" aria-label="清晰度">     <txpdiv class="txp_label" data-role="txp-ui-control-definition-hover">自适应</txpdiv>     <txpdiv class="txp_popup txp_popup_definition">         <txpdiv class="txp_popup_content" data-role="txp-ui-control-definition-list">         </txpdiv>     </txpdiv> </txpdiv><txpdiv data-role="txp-button-speed" class="txp_btn txp_btn_definition txp_none">  <txpdiv data-role="txp-button-speed-label" class="txp_label">倍速</txpdiv>  <txpdiv data-role="txp-button-speed-list" class="txp_popup txp_popup_definition">   <txpdiv class="txp_popup_content">         <txpdiv class="txp_menuitem">0.5x</txpdiv>         <txpdiv class="txp_menuitem txp_current">1.0x</txpdiv>         <txpdiv class="txp_menuitem">1.25x</txpdiv>         <txpdiv class="txp_menuitem">1.5x</txpdiv>         <txpdiv class="txp_menuitem">2.0x</txpdiv>       </txpdiv>  </txpdiv>   <txpdiv data-role="txp-ui-control-settings-speed-tips" class="txp_speed_tips txp_none">   <txpdiv class="txp_speed_tips_highlight">倍速播放</txpdiv>   在这里   <txpdiv data-role="txp-ui-control-settings-speed-tips-arrow" class="txp_speed_tips_arrow" style="left: inherit;right: 50px;"></txpdiv>   <button data-role="txp-ui-control-settings-speed-tips-close" class="txp_btn txp_btn_close" title=""></button>  </txpdiv> </txpdiv><txpdiv class="txp_btn txp_btn_volume" data-role="txp-control-volume-button" data-status="mute" aria-label="音量">      <svg data-role="txp-control-volume-click-button" data-report="mute-toggle" class="txp_icon txp_icon_volume" version="1.1" viewBox="0 0 24 24">          <use class="txp_svg_symbol txp_svg_volume" xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#txp_svg_volume"></use>          <use class="txp_svg_symbol txp_svg_volume_mute" xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#txp_svg_volume_mute"></use>      </svg>        <txpdiv class="txp_popup txp_popup_volume" data-report="change-volume">          <txpdiv data-role="txp-control-volume-drag" class="txp_popup_content">              <txpdiv data-role="txp-control-volume-range" class="txp_volume_range">                  <txpdiv data-role="txp-control-volume-value" class="txp_volume_range_current" style="height: 0%;">                      <txpdiv data-role="txp-control-volume-handler" class="txp_volume_handle"></txpdiv>                  </txpdiv>              </txpdiv>          </txpdiv>      </txpdiv>  </txpdiv><txpdiv class="txp_btn txp_btn_fullscreen" data-role="txp-ui-control-fullscreenbtn" data-status="false" data-report="window-fullscreen" aria-label="系统全屏">   <svg class="txp_icon txp_icon_fullscreen" version="1.1" viewBox="0 0 24 24">     <use class="txp_svg_symbol txp_svg_fullscreen" xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#txp_svg_fullscreen"></use>     <use class="txp_svg_symbol txp_svg_fullscreen_true" xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#txp_svg_fullscreen_true"></use>   </svg>   <txpdiv class="txp_tooltip" data-role="window-fullscreen">全屏</txpdiv> </txpdiv> <a data-role="txp-ui-control-logo" class="txp_btn txp_btn_logo" data-report="click-logo" aria-label="腾讯视频logo">   <span class="txp_logo"></span>   <txpdiv class="txp_tooltip">到腾讯视频观看此视频</txpdiv> </a></txpdiv>   </txpdiv> </txpdiv><txpdiv class="txp_hint_next txp_none" data-role="txp-next-tip-mod"> <txpdiv class="txp_next_pic"><img data-role="txp-next-tip-preview" alt=""></txpdiv>  <txpdiv class="txp_next_wording">   <txpdiv class="txp_label">下一个</txpdiv>   <txpdiv class="txp_next_title" data-role="txp-next-tip-text"></txpdiv>  </txpdiv> </txpdiv> <txpdiv class="txp_overlay_next txp_none" data-role="txp-next-tip-content-mod"> <div class="txp_next_poster" data-role="txp-next-tip-content-poster" style="background-image:url()"></div> <txpdiv class="txp_next_content">  <txpdiv class="txp_label">即将播放</txpdiv>  <txpdiv class="txp_next_title" data-role="txp-next-tip-content-text"></txpdiv>  <a class="txp_cancel" href="javascript:" data-role="txp-next-tip-content-cancle">取消</a>  <button class="txp_btn txp_btn_play_lg" data-status="play" data-role="txp-next-tip-content-play">   <svg class="txp_icon txp_icon_play" viewBox="0 0 36 36">    <use class="txp_svg_symbol txp_svg_play" xlink:href="#txp_svg_play"></use>   </svg>   <svg class="txp_icon_cirlce" viewBox="0 0 72 72">    <circle r="34" cy="36" cx="36"></circle>   </svg>  </button> </txpdiv> </txpdiv><txpdiv data-role="txp_preview_mod" class="txp_tooltip_preview txp_tooltip_preview_hover txp_none" style="left:0;">   <txpdiv class="txp_tooltip_bg txp_tooltip_current_bg" data-role="txp-preview-image">    <txpdiv class="txp_tooltip_text" data-role="txp-preview-time-text"></txpdiv>    <txpdiv data-role="txp-ui-control-preview-ad" class="txp_tooltip_preview_ad">  </txpdiv></txpdiv>   <txpdiv class="txp_tooltip_dot_text txp_none"></txpdiv> </txpdiv><txpdiv class="txp_preview txp_none" data-role="txp-preview-image-poster-mod">  <txpdiv data-role="txp-preview-image-poster" class="txp_preview_img"></txpdiv> </txpdiv> <txpdiv data-role="txp_preview_mod_list" class="txp_tooltip_preview txp_none" style="width: 360px; left: -210px;"> <txpdiv class="txp_tooltip_bg txp_tooltip_current_bg" data-role="txp-preview-image-list"><txpdiv class="txp_tooltip_text" data-role="txp-preview-time-text-list"></txpdiv> <txpdiv data-role="txp-ui-control-preview-ad" class="txp_tooltip_preview_ad">  </txpdiv></txpdiv><txpdiv class="txp_tooltip_bg" data-role="txp-preview-image-list"><txpdiv class="txp_tooltip_text" data-role="txp-preview-time-text-list"></txpdiv></txpdiv></txpdiv><txpdiv class="txp_barrage" data-role="txp-interactive-mod"></txpdiv><txpdiv data-role="txp-ui-title-mod" class="txp_video_title txp_none">   <a data-role="txp-ui-title-text" class="txp_title_link"></a> </txpdiv><txpdiv data-role="txp-ui-screen-percent-wrap" class="txp_screen_percent txp_none">  <txpdiv data-role="txp-ui-screen-percent-50" data-percent="50" class="txp_screen_50">50%</txpdiv>  <txpdiv data-role="txp-ui-screen-percent-75" data-percent="75" class="txp_screen_75">75%</txpdiv>  <txpdiv data-role="txp-ui-screen-percent-100" data-percent="100" class="txp_screen_100 txp_current">100%</txpdiv> </txpdiv> <txpdiv data-role="txp-ui-favorite" class="txp_top_btns"><button data-role="txp-ui-pip-btn" class="txp_btn txp_btn_collect" data-status="false" style="display: none;">     <svg class="txp_icon txp_icon_popup" width="20px" height="20px" viewBox="0 0 20 20" version="1.1">         <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">             <rect id="Rectangle-3-Copy-3" fill="#FFFFFF" x="10" y="11" width="5" height="3"></rect>             <rect id="Rectangle-2-Copy-3" stroke="#FFFFFF" stroke-width="2" x="2" y="3" width="16" height="14" rx="1">             </rect>         </g>     </svg>     <txp data-role="txp-ui-pip-btn-label" class="txp_icon_text">画中画</txp> </button></txpdiv><txpdiv class="txp_overlay_play txp_none" "="" data-role="txp_overlay_play">  <button class="txp_btn txp_btn_play_lg" data-status="play" data-role="txp_overlay_play_status">   <svg class="txp_icon txp_icon_play" version="1.1" viewBox="0 0 36 36" width="36" height="36">    <use class="txp_svg_symbol txp_svg_play" xlink:href="#txp_svg_play"></use>    <use class="txp_svg_symbol txp_svg_pause" xlink:href="#txp_svg_pause"></use>    <use class="txp_svg_symbol txp_svg_replay" xlink:href="#txp_svg_replay"></use>   </svg>  </button> </txpdiv> <!-- 时间 --> <txpdiv data-role="txp-ui-clock-mod" class="txp_clock txp_none"></txpdiv> <txpdiv data-role="txp-ui-console" class="txp_console txp_none">   <txpdiv class="txp_console_inner">     <button data-role="txp-ui-console-close" class="txp_btn_close" title="关闭"></button>     <txpdiv data-role="txp-ui-console-report" class="txp_line" title="双击发送错误信息" style="cursor: pointer;">       <txpdiv class="txp_label">VID</txpdiv><txpdiv data-role="txp-ui-console-vid" class="txp_value">g00318x1j6x</txpdiv>     </txpdiv>     <txpdiv class="txp_line">       <txpdiv class="txp_label">播放模式</txpdiv><txpdiv data-role="txp-ui-console-playertype-mode" class="txp_value">chromehls</txpdiv>     </txpdiv>     <txpdiv class="txp_line">       <txpdiv class="txp_label">分辨率</txpdiv><txpdiv class="txp_value">1680 x 1050</txpdiv>     </txpdiv>     <txpdiv class="txp_line">       <txpdiv class="txp_label">视频宽高</txpdiv><txpdiv data-role="txp-ui-console-videoSize" class="txp_value"></txpdiv>     </txpdiv>     <txpdiv class="txp_line">       <txpdiv class="txp_label">音量</txpdiv><txpdiv data-role="txp-ui-console-volume" class="txp_value">0%</txpdiv>     </txpdiv>     <txpdiv class="txp_line">       <txpdiv class="txp_label">视频协议</txpdiv><txpdiv data-role="txp-ui-console-protocol" class="txp_value"></txpdiv>     </txpdiv>     <txpdiv class="txp_line">       <txpdiv class="txp_label">CDN</txpdiv><txpdiv data-role="txp-ui-console-cdn" class="txp_value" style="font-size: 10px;"></txpdiv>     </txpdiv>     <txpdiv class="txp_line">       <txpdiv class="txp_label">下载速度</txpdiv><txpdiv class="txp_value">         <txpdiv data-role="txp-ui-console-downloadspeed-chart" class="txp_box_progress"></txpdiv>         <span data-role="txp-ui-console-downloadspeed"></span>       </txpdiv>     </txpdiv>     <txpdiv class="txp_line">       <txpdiv class="txp_label">缓冲质量</txpdiv><txpdiv class="txp_value">         <txpdiv class="txp_box_progress">           <txpdiv data-role="txp-ui-console-buf-per" class="txp_box_value" style="width:0%"></txpdiv>         </txpdiv>         <span data-role="txp-ui-console-buf-seconds"></span>       </txpdiv>     </txpdiv>     <txpdiv class="txp_line">       <txpdiv class="txp_label">帧数</txpdiv><txpdiv data-role="txp-ui-console-dropped-frames" class="txp_value"></txpdiv>     </txpdiv>     <txpdiv data-role="txp-ui-console-errorcode-wrap" class="txp_line">       <txpdiv class="txp_label">错误码</txpdiv>       <txpdiv data-role="txp-ui-console-errorcode" class="txp_value">62101.13080.1</txpdiv>     </txpdiv>     <txpdiv class="txp_line">       <txpdiv class="txp_label">版本号</txpdiv>       <txpdiv class="txp_value">3.4.40-1.0.141 (2019-7-25 6:51:15 PM)</txpdiv>     </txpdiv>     <txpdiv class="txp_line">       <txpdiv class="txp_label">播放流水</txpdiv>       <txpdiv data-role="txp-ui-console-flowid" class="txp_value">8477900f66e6eafb9eb05710b44b60f5_70901</txpdiv>     </txpdiv>     <txpdiv class="txp_line" data-role="txp-ui-drm-flag">       <txpdiv class="txp_label">drm</txpdiv>       <txpdiv class="txp_value _drm_flag_value">false</txpdiv>     </txpdiv>     <txpdiv class="txp_line txp_none" data-role="txp-ui-console-local-log">       <txpdiv class="txp_label">本地日志</txpdiv>       <txpdiv class="txp_value">         <span style="cursor: pointer;" class="_download_txp_local_log">点击下载</span> /          <span style="cursor: pointer;" class="_delete_txp_local_log">点击清除</span>       </txpdiv>     </txpdiv>   </txpdiv> </txpdiv><txpdiv data-role="txp-ui-watermark-mod" class="txp-watermark txp_none"> </txpdiv><txpdiv data-role="txp-ui-watermark-action-mod" class="txp-watermark-action txp_none"> </txpdiv><txpdiv class="txp_overlay_link txp_none" data-role="txp-right-click-menu-copy-success">     <txpdiv class="txp_icon_link">         <svg class="txp_icon" version="1.1" viewBox="0 0 36 36">             <use class="txp_svg_symbol" xlink:href="#txp_svg_link"></use>         </svg>     </txpdiv> </txpdiv> <txpdiv class="txp_overlay_next txp_overlay_next_complete txp_none" data-role="txp-ui-endtip-mod">  <div class="txp_next_poster" data-role="txp-ui-endtip-background" style="background-image:url()"></div>  <txpdiv class="txp_next_content">   <txpdiv class="txp_label" data-role="txp-ui-endtip-label">腾讯视频观看完整版</txpdiv>   <txpdiv class="txp_next_title" style="cursor:pointer;" data-role="txp-ui-endtip-title"></txpdiv>   <button class="txp_btn txp_btn_play_lg" data-status="play" data-role="txp-ui-endtip-button">    <svg class="txp_icon txp_icon_play" viewBox="0 0 36 36">     <use class="txp_svg_symbol txp_svg_play" xlink:href="#txp_svg_play"></use>    </svg>    <svg class="txp_icon_cirlce" viewBox="0 0 72 72">     <circle r="34" cy="36" cx="36"></circle>    </svg>   </button>  </txpdiv> </txpdiv></txpdiv> </div>
          <div class="click-layer"></div>
        </li>
                                      <li bosszone="rmss_2">
            <a class="q-icons icon-video" href="https://view.inews.qq.com/a/20190806A02LK400" target="_blank">卡特同意与老鹰签约 将成为效力NBA时间最长球员</a>
          </li>
                                      <li bosszone="rmss_3">
            <a class="q-icons icon-video" href="https://v.qq.com/x/cover/0x6q9kgtjrw1dze/z0031iqz8u9.html" target="_blank">开营！美国男篮集训小鬼当家 众将轮番上演单挑</a>
          </li>
                                      <li bosszone="rmss_4">
            <a class="q-icons icon-video" href="https://view.inews.qq.com/a/20190805A0S2MY00" target="_blank">NBA官网评出近10年最佳阵容：詹皇杜兰特领衔入围</a>
          </li>
                                      <li bosszone="rmss_5">
            <a class="q-icons icon-video" href="https://v.qq.com/x/cover/v3ncbinr4dloq53/r0031pfyjpc.html" target="_blank">曼联宣布签下马奎尔 身价8000万镑成世界最贵后卫</a>
          </li>
                                      <li bosszone="rmss_6">
            <a class="q-icons icon-video" href="http://v.qq.com/x/page/p0909nmx936.html" target="_blank">武磊9岁比赛视频曝光：头球破门+长途奔袭晃过门将 </a>
          </li>
                  </ul>
  </div>
</div><!--1015f423a991e0df0e666974f31feb21--><!--[if !IE]>|xGv00|82adb92aa61dda90539e374f3b67c566<![endif]-->
        <!-- /热门赛事 -->

        <!-- 今日热播 -->
        <div class="mod m-todayhot" bossexpo="bg_jrrb">
  <div class="hd-2 cf">
    <h2 class="tit active fl">
      <a href="https://v.qq.com/" target="_blank" bosszone="jrrb_logo">今日热播</a>
    </h2>
  </div>
  <div class="bd">
    <ul class="news-list cf">
                                  <li class="video-item fl">
            <div class="pic video-box click-drag-play" bosszone="jrrb_1" bossvv="vv_jrrb">
              <img src="//img1.gtimg.com/ninja/2/2019/08/ninja156500820770716.jpg" alt="梳理成都车辆自燃事故全过程">
              <i class="q-icons icon-play2"></i>
              <div class="txt">梳理成都车辆自燃事故全过程</div>
              <div class="desc undis">w0909xuswou</div>
              <div id="mod-player2" class="mod-player" data-vid="w0909xuswou" data-url="https://v.qq.com/x/cover/f5yvp0mas8gecnv/w0909xuswou.html"></div>
              <div class="click-layer"></div>
            </div>
          </li>
                                          <li class="video-item fr">
            <div class="pic video-box click-drag-play" bosszone="jrrb_2" bossvv="vv_jrrb">
              <img src="//img1.gtimg.com/ninja/2/2019/08/ninja156500884483772.jpg" alt="法国“飞人”飞越英吉利海峡">
              <i class="q-icons icon-play2"></i>
              <div class="txt">法国“飞人”飞越英吉利海峡</div>
              <div class="desc undis">f0909v72m4o</div>
              <div id="mod-player3" class="mod-player" data-vid="f0909v72m4o" data-url="https://v.qq.com/x/page/f0909v72m4o.html"></div>
              <div class="click-layer"></div>
            </div>
          </li>
                                                      </ul><ul class="news-list">
                    <li class="item" bosszone="jrrb_3">
            <a class="q-icons icon-video" href="https://v.qq.com/x/page/x0909y8u5yz.html" target="_blank">河南固始警方挨家挨户追回上千个井盖：村民们都挺配合</a>
          </li>
                                                    <li class="item" bosszone="jrrb_4">
            <a class="q-icons icon-video" href="https://v.qq.com/x/cover/f5yvp0mas8gecnv/u09098zeag9.html" target="_blank">江西九江火灾消防员敲72间房门救出16人 有人累到呕吐</a>
          </li>
                                                    <li class="item" bosszone="jrrb_5">
            <a class="q-icons icon-video" href="https://v.qq.com/x/cover/f5yvp0mas8gecnv/f0909d5c0l8.html" target="_blank">男子海宁大缺口观潮拍视频 被潮水瞬间吞没死里逃生</a>
          </li>
                                                    <li class="item" bosszone="jrrb_6">
            <a class="q-icons icon-video" href="https://v.qq.com/x/cover/0mlnk5uw6smhvlj/s09095ug9w3.html" target="_blank">深夜被殴女子还原事发过程：多处受伤 不敢靠近事发地</a>
          </li>
                                                    <li class="item" bosszone="jrrb_7">
            <a class="q-icons icon-video" href="https://v.qq.com/x/page/x0909pwimse.html" target="_blank">醉驾男上演“梦游式”开车 一晚上碰撞剐蹭14次被刑拘</a>
          </li>
                  </ul>
  </div>
</div><!--c7deb22d355e98ef0307b78f5dfae696--><!--[if !IE]>|xGv00|a6b9d7ada7bb5dd18d11bf9b6d28657b<![endif]-->
        <!-- /今日热播 -->
      </div>

    </div>
    <!-- /要闻 -->

    <!-- 视觉焦点 -->
    <div class="layout qq-pics" bossexpo="bg_sjjd">
  <div class="title">
    <a class="txt active" href="https://new.qq.com/ch/photo/" target="_blank" bosszone="sjjd_logo">视觉焦点</a>
  </div>
  <div class="mainbody">
    <div id="picDir2" bosszone="sjjd_more">
      <a href="javascript:;" class="prev icon disabled" data-rel="#picUl21"></a>
      <a href="javascript:;" class="next icon" data-rel="#picUl22"></a>
    </div>
    <div class="wrap">
      <div class="wrapul cf" id="picWrap2">
        <ul id="picUl21" class="wp-inner cf" bosszone="sjjd_1" bossexpo="bg_sjjd_1">
                                  <li class="item">
              <a href="https://new.qq.com/omn/20190806/20190806A02NIE00.html" class="p1t" target="_blank">
                                <img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-original="https://inews.gtimg.com/newsapp_ls/0/9940710964_580328/0" alt="俄罗斯弹药库蹊跷爆炸！现场腾起蘑菇云，万余人大逃亡">
                                <p>俄罗斯弹药库蹊跷爆炸！现场腾起蘑菇云，万余人大逃亡</p>
              </a>
            </li>
                                  <li class="item">
              <a href="https://new.qq.com/omn/20190806/20190806A0387P00.html" class="p1t" target="_blank">
                                <img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-original="https://inews.gtimg.com/newsapp_ls/0/9940430912_580328/0" alt="航拍孤悬大连本土之外的棒棰岛，因上新闻联播走红，暑假游客爆满">
                                <p>航拍孤悬大连本土之外的棒棰岛，因上新闻联播走红，暑假游客爆满</p>
              </a>
            </li>
                                  <li class="item">
              <a href="https://new.qq.com/omn/20190804/20190804A0IM1200.html" class="p1t" target="_blank">
                                <img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-original="https://inews.gtimg.com/newsapp_ls/0/9932267800_580328/0" alt="乌克兰查获大量走私导弹，欣喜若狂都是俄国货，全部没收自己来用">
                                <p>乌克兰查获大量走私导弹，欣喜若狂都是俄国货，全部没收自己来用</p>
              </a>
            </li>
                                  <li class="item">
              <a href="https://new.qq.com/omn/20190806/20190806A02WGO00.html" class="p1t" target="_blank">
                                <img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-original="https://inews.gtimg.com/newsapp_ls/0/9940344284_580328/0" alt="老公打工，儿女上大学，她留守深山种地养猪精心照顾95岁婆婆">
                                <p>老公打工，儿女上大学，她留守深山种地养猪精心照顾95岁婆婆</p>
              </a>
            </li>
                                  <li class="item">
              <a href="https://new.qq.com/omn/20190806/20190806A01VCR00.html" class="p1t" target="_blank">
                                <img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-original="https://inews.gtimg.com/newsapp_ls/0/9940531410_580328/0" alt="河北农民种植“异形”水果，每个卖100元，啥稀罕物？">
                                <p>河北农民种植“异形”水果，每个卖100元，啥稀罕物？</p>
              </a>
            </li>
                                  <li class="item item-last">
              <a href="https://new.qq.com/omn/20190806/20190806A03AYQ00.html" class="p1t" target="_blank">
                                <img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-original="https://inews.gtimg.com/newsapp_ls/0/9940490888_580328/0" alt="天下第一泉水位连涨一周，喷涌活力明显加强，游客挤爆看新鲜">
                                <p>天下第一泉水位连涨一周，喷涌活力明显加强，游客挤爆看新鲜</p>
              </a>
            </li>
                                                  </ul><ul id="picUl22" class="wp-inner cf undis" bosszone="sjjd_2" bossexpo="bg_sjjd_2">
                        <li class="item">
              <a href="https://new.qq.com/omn/20190804/20190804A0I9EO00.html" class="p1t" target="_blank">
                                <img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-src="https://inews.gtimg.com/newsapp_ls/0/9932267860_580328/0" alt="美海军战机坠毁星战峡谷，坠机现场图太震撼，超低空钻峡谷多危险">
                                <p>美海军战机坠毁星战峡谷，坠机现场图太震撼，超低空钻峡谷多危险</p>
              </a>
            </li>
                                  <li class="item">
              <a href="https://new.qq.com/omn/20190806/20190806A001JS00.html" class="p1t" target="_blank">
                                <img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-src="https://inews.gtimg.com/newsapp_ls/0/9938784238_580328/0" alt="浙江建德：水上“清道夫” 江面保洁忙">
                                <p>浙江建德：水上“清道夫” 江面保洁忙</p>
              </a>
            </li>
                                  <li class="item">
              <a href="https://new.qq.com/omn/20190805/20190805A0FD3F00.html" class="p1t" target="_blank">
                                <img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-src="https://inews.gtimg.com/newsapp_ls/0/9935177344_580328/0" alt="1500户业主买房6年，开发商：商铺合同无效，住宅原价退款">
                                <p>1500户业主买房6年，开发商：商铺合同无效，住宅原价退款</p>
              </a>
            </li>
                                  <li class="item">
              <a href="https://new.qq.com/omn/20190805/20190805A0QHMP00.html" class="p1t" target="_blank">
                                <img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-src="https://inews.gtimg.com/newsapp_ls/0/9938174562_580328/0" alt="世界最贵的食材：麝香猫咖啡、金枪鱼、哈密瓜，还有来自中国的它">
                                <p>世界最贵的食材：麝香猫咖啡、金枪鱼、哈密瓜，还有来自中国的它</p>
              </a>
            </li>
                                  <li class="item">
              <a href="https://new.qq.com/omn/20190805/20190805A0GPPC00.html" class="p1t" target="_blank">
                                <img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-src="https://inews.gtimg.com/newsapp_ls/0/9935494741_580328/0" alt="东京4天19人疑似被热死 警方称他们都没使用空调">
                                <p>东京4天19人疑似被热死 警方称他们都没使用空调</p>
              </a>
            </li>
                                  <li class="item item-last">
              <a href="https://new.qq.com/omn/20190805/20190805A0GOPQ00.html" class="p1t" target="_blank">
                                <img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-src="https://inews.gtimg.com/newsapp_ls/0/9935489547_580328/0" alt="15岁少女从酒店房间离奇失踪，至今下落不明">
                                <p>15岁少女从酒店房间离奇失踪，至今下落不明</p>
              </a>
            </li>
                                                  </ul><ul id="picUl22" class="wp-inner cf undis" bosszone="sjjd_2" bossexpo="bg_sjjd_2">
                        <li class="item">
              <a href="https://new.qq.com/omn/20190720/20190720A000BG00.html" class="p1t" target="_blank">
                                <img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-src="https://inews.gtimg.com/newsapp_ls/0/9771404198_580328/0" alt="俄罗斯17岁少女遭两闺蜜联手毁容杀害，疑因颜值太高招嫉恨">
                                <p>俄罗斯17岁少女遭两闺蜜联手毁容杀害，疑因颜值太高招嫉恨</p>
              </a>
            </li>
                  </ul>
      </div>
    </div>
  </div>
</div><!--[if !IE]>|xGv00|be72d290d78b10ab24e0e9b064415f0c<![endif]-->
    <!-- /视觉焦点 -->

    <!-- 广告2 -->
    <div class="layout qq-gg gg-2 cf">
      <div class="col-1 fl">
        <!--NEW_QQCOM_N_Width2_div AD begin...."l=NEW_QQCOM_N_Width2&log=off"--><div id="NEW_QQCOM_N_Width2" style="width: 920px; height: 90px; display: block; position: relative; zoom: 1;" class="l_qq_com" adconfig_lview="l.qq.com" adconfig_charset="gbk" adconfig_lview_template="//l.qq.com/lview?c=www&amp;loc={loc}" oid="4506252" btoid="0" display="banner"><a href="https://c.l.qq.com/lclick?oid=4506252&amp;loc=NEW_QQCOM_N_Width2&amp;soid=m1vEkgAAXUjvJQDmkQLmIf8IAZLm&amp;click_data=dXNlcl9pbmZvPW9BRGptenc4RUI0PSZwYWdlX3R5cGU9MSZzc3A9MSZ1cF92ZXJzaW9uPVMxMDB8TDg2NiZzaT0xNTM0NTQ3Njk=&amp;index=1&amp;chl=478" target="_blank" style="display:block;cursor:pointer;width:920px;height:90px;background-image:url(//wa.gtimg.com/website/201907/Ot_D_20190713232539748897.png);background-size:920px 90px;background-position:50% 50%;filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(src='//wa.gtimg.com/website/201907/Ot_D_20190713232539748897.png',sizingMethod='scale');"></a><a class="absolute a_cover" href="https://c.l.qq.com/lclick?oid=4506252&amp;loc=NEW_QQCOM_N_Width2&amp;soid=m1vEkgAAXUjvJQDmkQLmIf8IAZLm&amp;click_data=dXNlcl9pbmZvPW9BRGptenc4RUI0PSZwYWdlX3R5cGU9MSZzc3A9MSZ1cF92ZXJzaW9uPVMxMDB8TDg2NiZzaT0xNTM0NTQ3Njk=&amp;index=1&amp;chl=478&amp;k=&amp;t=%E8%85%BE%E8%AE%AF%E9%A6%96%E9%A1%B5&amp;r=&amp;s=" target="_blank" rel="nofollow" style="position:absolute;width:920px;height:90px;left:0px;top:0px;cursor:pointer;z-index:10;background-color:#fff;filter:alpha(opacity=0);opacity:0;"></a><div style="position: absolute; left: 0px; bottom: 0px; width: 26px; height: 16px; z-index: 12; background-image: url(&quot;https://ra.gtimg.com/web/res/icon/leftbottom_new.png&quot;); background-position: right top; background-repeat: no-repeat no-repeat;"></div></div><!--NEW_QQCOM_N_Width2 AD end --><!--[if !IE]>|xGv00|fbeca37d15deeb51401925a2478cc2a3<![endif]-->
      </div>
      <div class="col-2 fr">
        <!--NEW_QQCOM_N_button1_div AD begin...."l=NEW_QQCOM_N_button1&log=off"--><div id="NEW_QQCOM_N_button1" style="width: 440px; height: 90px; overflow: hidden; display: block; position: relative;" class="l_qq_com" adconfig_lview="l.qq.com" adconfig_charset="gbk" adconfig_lview_template="//l.qq.com/lview?c=www&amp;loc={loc}" oid="100" btoid="0" display="auto"><a href="http://users.qq.com" target="_blank" style="display:block;cursor:pointer;width:440px;height:90px;background-image:url(//ra.gtimg.com/web/default_fodders/qq/440x90_0.png);background-size:440px 90px;background-position:50% 50%;filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(src='//ra.gtimg.com/web/default_fodders/qq/440x90_0.png',sizingMethod='scale');"></a></div><!--NEW_QQCOM_N_button1 AD end --><!--[if !IE]>|xGv00|55d494537bd76ac5f5022bf2405adcf3<![endif]-->
      </div>
    </div>
    <!-- /广告2 -->

    <!-- 娱乐/体育/NBA -->
    <div class="layout qq-channel2col channelent cf">

      <div class="col col-2 fl">

        <!-- 娱乐 -->
        <div class="mod-ch">
          <div class="title nst">
            <a class="txt active" href="https://new.qq.com/ch/ent/" target="_blank" bosszone="yule_logo">娱乐</a>
            <span bosszone="yule_dh">
              <a class="txt" href="https://new.qq.com/ch2/tv" target="_blank">电视剧</a>
              <a class="txt" href="https://new.qq.com/ch2/movie" target="_blank">电影</a>
              <a class="txt" href="https://new.qq.com/ch2/music" target="_blank">音乐</a>
            </span>
            <ul class="label" bosszone="yule_om">
              	<li><a href="https://new.qq.com/omn/author/32" target="_blank">贵圈</a></li>
	<li><a href="https://new.qq.com/omn/author/26135" target="_blank">懂小姐</a></li>
	<li><a href="https://new.qq.com/omn/author/6853487" target="_blank">认真映画</a></li>
<!--1e82868b9b613b843e2551bde0c7cb28--><!--[if !IE]>|xGv00|056220db2a7bb51ced7b5ce4c533f73d<![endif]-->
            </ul>
          </div>
          <div class="bdwrap js_chyh">
            

<div class="bd cf" id="js_entbd1" bosszone="yule_1" bossexpo="bg_yule_1">
  <div class="bdleft">
    <div class="prt cf">
  <a href="https://new.qq.com/omn/20190806/20190806A02LHN00.html" target="_blank" class="picwrap">
    <img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-original="https://inews.gtimg.com/newsapp_ls/0/9940752451_580328/0" class="pic" alt="杨紫李现合体拍摄时尚杂志，现场照曝光两人穿情侣装很甜蜜">
  </a>
  <div class="text">
    <a href="https://new.qq.com/omn/20190806/20190806A02LHN00.html" target="_blank">
      <p class="tit">杨紫李现合体拍摄时尚杂志，现场照曝光两人穿情侣装很甜蜜</p>
    </a>
    <a class="from" href="https://new.qq.com/omn/20190806/20190806A02LHN00.html" target="_blank">
      <span class="author">艺闻有看点</span>
      <span class="comment">661评</span>    </a>
  </div>
</div>
<ul class="txtArea">
            <li>
      <a class="" href="https://new.qq.com/omn/20190806/20190806A02YF600.html" target="_blank">吴京独自带儿子旅行10天，吴所谓骑爸爸头上背影超暖</a>
    </li>
                <li>
      <a class="" href="https://new.qq.com/omn/20190806/20190806A024U900.html" target="_blank">易烊千玺王俊凯王源同框庆TFBOYS出道6周年，画面引回忆杀</a>
    </li>
                <li>
      <a class="" href="https://new.qq.com/omn/20190806/20190806A01DOS00.html" target="_blank">上映5天6.48亿，面对神作《哪吒》，黄晓明终究顶住了压力</a>
    </li>
                <li>
      <a class="" href="https://new.qq.com/omn/20190806/20190806A03R3D00.html" target="_blank">吴昕有了新恋情？与小3岁男星郑凯被拍，两人疑似已同居</a>
    </li>
                                                                </ul>

  </div>
  <div class="bdright">
    <a href="https://new.qq.com/omn/20190806/20190806A0373600.html" target="_blank">
      <h2>张馨予产后复出现身机场，与妈妈穿同款鞋秀幸福</h2>
    </a>
    <div class="line"></div>
    <ul class="txtArea">
                                                                                                                      <li>
            <a class="" href="https://new.qq.com/omn/20190805/20190805A0OUMH00.html" target="_blank">洗米嫂海上冲浪超有范儿，性感火辣与运动天赋并存</a>
          </li>
                                                    <li>
            <a class="" href="https://new.qq.com/omn/20190806/20190806A01EZP00.html" target="_blank">2019年播出的12部强阵容剧为何多数变炮灰？</a>
          </li>
                                                    <li>
            <a class="" href="https://new.qq.com/omn/20190806/20190806A03I6F00.html" target="_blank">洗米华50亿财富曝光，小三Mandy资产总值竟胜过正室洗米嫂</a>
          </li>
                                                    <li>
            <a class="" href="https://new.qq.com/omn/20190806/20190806A01G1J00.html" target="_blank">豆瓣评分速降至6.8分，《九州缥缈录》的铁甲依然在吗？</a>
          </li>
                                                    <li>
            <a class="" href="https://new.qq.com/omn/20190806/20190806A038JQ00.html" target="_blank">学渣与学霸之间，只差着一个心理医生</a>
          </li>
                                                                                                                                                                                                                                                                                                                                                              </ul>
  </div>
</div>

<div class="bd cf undis" id="js_entbd2" bosszone="yule_2" bossexpo="bg_yule_2">
  <div class="bdleft">
    <div class="prt cf">
  <a href="https://new.qq.com/omn/20190806/20190806A037LI00.html" target="_blank" class="picwrap">
    <img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-original="https://inews.gtimg.com/newsapp_ls/0/9940412113_580328/0" class="pic" alt="杜淳：只做好演员，很纯粹">
  </a>
  <div class="text">
    <a href="https://new.qq.com/omn/20190806/20190806A037LI00.html" target="_blank">
      <p class="tit">杜淳：只做好演员，很纯粹</p>
    </a>
    <a class="from" href="https://new.qq.com/omn/20190806/20190806A037LI00.html" target="_blank">
      <span class="author">中国青年报</span>
      <span class="comment">16评</span>    </a>
  </div>
</div>
<ul class="txtArea">
                                  <li>
      <a class="" href="https://new.qq.com/omn/20190806/20190806A05K5100.html" target="_blank">请记住他：热爱电影，痴迷表演的张颂文</a>
    </li>
                <li>
      <a class="" href="https://new.qq.com/omn/20190806/20190806A06CXK00.html" target="_blank">编剧述平：希望片方能像对待演员一样对编剧</a>
    </li>
                <li>
      <a class="" href="https://new.qq.com/omn/20190806/20190806A06NHY00.html" target="_blank">导演汪俊：拍《小欢喜》比拍《小别离》更过瘾</a>
    </li>
                <li>
      <a class="q-icons icon-pic" href="https://new.qq.com/omn/20190806/20190806A06Q2L00.html" target="_blank">准备结婚了？小李子带女友意大利度假 双方父母同时现身</a>
    </li>
                                          </ul>

  </div>
  <div class="bdright">
    <div class="prt cf">
  <a href="https://new.qq.com/omn/20190806/20190806A0450Y00.html" target="_blank" class="picwrap">
    <img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-original="https://inews.gtimg.com/newsapp_ls/0/9940784617_580328/0" class="pic" alt="鹿晗方回应千元电影票：个别影院和黄牛所为">
  </a>
  <div class="text">
    <a href="https://new.qq.com/omn/20190806/20190806A0450Y00.html" target="_blank">
      <p class="tit">鹿晗方回应千元电影票：个别影院和黄牛所为</p>
    </a>
    <a class="from" href="https://new.qq.com/omn/20190806/20190806A0450Y00.html" target="_blank">
      <span class="author">观察者网</span>
      <span class="comment">8评</span>    </a>
  </div>
</div>
<ul class="txtArea">
                                            <li>
      <a class="" href="https://new.qq.com/omn/20190806/20190806A01EZB00.html" target="_blank">沙溢胡可演话剧，不只是探讨婚姻困境</a>
    </li>
                <li>
      <a class="" href="https://new.qq.com/omn/20190806/20190806A03L8000.html" target="_blank">从87年前的今天起，电影有了一双翅膀</a>
    </li>
                <li>
      <a class="" href="https://new.qq.com/omn/20190806/20190806A01CNG00.html" target="_blank">红花会贝贝疑因受网络暴力困扰，直播剁手指证清白吓坏网友</a>
    </li>
                <li>
      <a class="" href="https://new.qq.com/omn/20190806/20190806A00VON00.html" target="_blank">张柏芝昔日孕肚及产后爆肥照曝光，跟生三胎前后判若两人</a>
    </li>
                                </ul>

  </div>
</div>

<div class="bd cf undis" id="js_entbd3" bosszone="yule_3" bossexpo="bg_yule_3">
  <div class="bdleft">
    <div class="prt cf">
  <a href="https://new.qq.com/omn/20190806/20190806A008HM00.html" target="_blank" class="picwrap">
    <img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-original="https://inews.gtimg.com/newsapp_ls/0/9938879340_580328/0" class="pic" alt="演妈妈辈的她颜值回春？脸部紧致身材少女，同框美过马思纯">
  </a>
  <div class="text">
    <a href="https://new.qq.com/omn/20190806/20190806A008HM00.html" target="_blank">
      <p class="tit">演妈妈辈的她颜值回春？脸部紧致身材少女，同框美过马思纯</p>
    </a>
    <a class="from" href="https://new.qq.com/omn/20190806/20190806A008HM00.html" target="_blank">
      <span class="author">新氧App</span>
      <span class="comment">10评</span>    </a>
  </div>
</div>
<ul class="txtArea">
                                                      <li>
      <a class="" href="https://new.qq.com/omn/20190806/20190806A00TFO00.html" target="_blank">《僵尸家族》童星因为神秘力量退圈？近况曝光型男范儿十足</a>
    </li>
                <li>
      <a class="" href="https://new.qq.com/omn/20190806/20190806A03ZAH00.html" target="_blank">网友兰桂坊偶遇向太夫妇，向华强70岁仍然身姿挺拔</a>
    </li>
                <li>
      <a class="" href="https://new.qq.com/omn/20190806/20190806A03UED00.html" target="_blank">奇异、诡谲、恐怖、惊悚，奈飞当家大剧第三季又来了</a>
    </li>
                <li>
      <a class="" href="https://new.qq.com/omn/20190806/20190806A03T3H00.html" target="_blank">这年头，还有9.2分的女明星旅行真人秀？</a>
    </li>
                      </ul>

  </div>
  <div class="bdright">
    <div class="prt cf">
  <a href="https://new.qq.com/omn/20190806/20190806A00ET200.html" target="_blank" class="picwrap">
    <img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-original="https://inews.gtimg.com/newsapp_ls/0/9938883385_580328/0" class="pic" alt="脸上婴儿肥退化，为什么热巴显老而倪妮状态超好？">
  </a>
  <div class="text">
    <a href="https://new.qq.com/omn/20190806/20190806A00ET200.html" target="_blank">
      <p class="tit">脸上婴儿肥退化，为什么热巴显老而倪妮状态超好？</p>
    </a>
    <a class="from" href="https://new.qq.com/omn/20190806/20190806A00ET200.html" target="_blank">
      <span class="author">新氧App</span>
      <span class="comment">6评</span>    </a>
  </div>
</div>
<ul class="txtArea">
                                                                <li>
      <a class="" href="https://new.qq.com/omn/20190806/20190806A00C7100.html" target="_blank">陈思诚胖成小岳岳，离婚传闻后放飞自我？</a>
    </li>
                <li>
      <a class="" href="https://new.qq.com/omn/20190806/20190806A00SQ900.html" target="_blank">我能想到最浪漫的事，绝不是花十块钱买王一博的电话号码</a>
    </li>
                <li>
      <a class="" href="https://new.qq.com/omn/20190805/20190805A06AX100.html" target="_blank">多少热播国产剧，都逃不过一个沙雕英文名</a>
    </li>
                <li>
      <a class="" href="https://new.qq.com/omn/20190805/20190805A0M89800.html" target="_blank">给乔碧萝们打赏百万的人，其实“身不由己”？</a>
    </li>
            </ul>

  </div>
</div><!--[if !IE]>|xGv00|f7c935840ad07113bebff0ce59cf008b<![endif]-->
            <div class="hyh js_hyh" bosszone="yule_more">
              <span class="htxt">换一换</span>
              <ul class="hwrap" id="js_enthyh">
                <li class="hpoint active" data-rel="#js_entbd1"></li>
                <li class="hpoint" data-rel="#js_entbd2"></li>
                <li class="hpoint" data-rel="#js_entbd3"></li>
              </ul>
            </div>
          </div>
        </div>
        <!-- /娱乐 -->

        <!-- 体育 -->
        <div class="mod-ch">
          <div class="title nst">
            <a class="txt active" href="http://sports.qq.com/" target="_blank" bosszone="tiyu_logo">体育</a>
            <span bosszone="tiyu_dh">
              <a class="txt" href="http://sports.qq.com/cba/" target="_blank">CBA</a>
              <a class="txt" href="http://sports.qq.com/premierleague/" target="_blank">英超</a>
              <a class="txt" href="http://fans.sports.qq.com/#/" target="_blank">社区</a>
            </span>
            <ul class="label" bosszone="tiyu_om">
              	<li><a href="http://sports.qq.com/video/djsp.htm" target="_blank">电竞视频</a></li>
	<li><a href="http://fiba.qq.com/fibawc/" target="_blank">男篮世界杯</a></li>
	<li><a href="http://sports.qq.com/basket/SuperPENGUINleague/" target="_blank">超级企鹅联盟</a></li>
	<li><a href="https://sports.qq.com/pr/2019/" target="_blank">特步企鹅跑</a></li>
<!--b6e9ed002f20379ff37998349083b6e4--><!--[if !IE]>|xGv00|dd881aa09d94a3112204187ddd4011ac<![endif]-->
            </ul>
          </div>
          <div class="bdwrap js_chyh">
            

<div class="bd nbabd cf" id="js_sportsbd1" bosszone="tiyu_1" bossexpo="bg_tiyu_1">
  <div class="bdleft">
    <div class="prt cf">
  <a href="https://new.qq.com/omn/rose.htm?id=SPO2019073100734100" target="_blank" class="picwrap">
    <img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-original="https://inews.gtimg.com/newsapp_ls/0/9940528417_580328/0" class="pic" alt="正视频直播MLB勇士vs双城 跨分区强强对话上演">
  </a>
  <div class="text">
    <a href="https://new.qq.com/omn/rose.htm?id=SPO2019073100734100" target="_blank">
      <p class="tit">正视频直播MLB勇士vs双城 跨分区强强对话上演</p>
    </a>
    <a class="from" href="https://new.qq.com/omn/rose.htm?id=SPO2019073100734100" target="_blank">
      <span class="author">腾讯体育</span>
      <span class="comment">680评</span>    </a>
  </div>
</div>
<ul class="txtArea">
            <li>
      <a class="q-icons icon-video" href="https://new.qq.com/omn/20190806/20190806A0388U00.html" target="_blank">重走罗本老路？曝贝尔或租借加盟拜仁 阿迪成幕后推手</a>
    </li>
                <li>
      <a class="" href="https://new.qq.com/omn/SPO20190/SPO2019080600320500.html" target="_blank">秀操作翻车还没完！郭艾伦慈善赛后上错大巴一脸呆萌</a>
    </li>
                <li>
      <a class="" href="https://new.qq.com/omn/SPO20190/SPO2019080600336300.html" target="_blank">经济效益！武磊助球队获千万欧赞助 西媒盛赞总领事怒夸</a>
    </li>
                <li>
      <a class="" href="https://new.qq.com/omn/SPO20190/SPO2019080600223600.html" target="_blank">亚冠-马宁+傅明联袂执法 沙特豪门2-1逆转占据先手</a>
    </li>
                                                              </ul>

  </div>
  <div class="bdright">
    <div class="index cf" bosszone="tiyu_sc">
      <div class="ntop">
        <span id="js_sportstitle" class="hidesplit">
          <a href="http://kbs.sports.qq.com/#hot" class="link active" target="_blank" data-rel="#js_sportslive">赛事直播</a>
          <span class="wsplit"></span>
          <span class="nsplit"></span>
          
        </span>
        <ul class="nlabel">
          <li class="nlabel-item"><a href="http://sports.qq.com/cba/" target="_blank">CBA</a></li>
          <li class="nlabel-item"><a href="http://sports.qq.com/premierleague/" target="_blank">英超</a></li>
        </ul>
      </div>
      <div class="nwrap">
        <ul class="live" id="js_sportslive"><li><a href="http://kbs.sports.qq.com/kbsweb/game.htm?mid=100800:567017" target="_blank"><span class="name over">MLB常规赛</span><span class="date over">今天</span><span class="icon-live over">直播</span><span class="team over left">勇士</span><span class="icon-vs over">vs</span><span class="team over right">双城</span></a></li><li><a href="http://kbs.sports.qq.com/kbsweb/game.htm?mid=100002:20207274" target="_blank"><span class="name over">18-19赛季猛龙全回顾</span><span class="date over">今天</span><span class="time over">09:00</span><span class="team over one">18-19赛季NBA猛龙队常规赛回顾：常规赛G43-G49</span></a></li></ul>
        <ul class="playback undis" id="js_sportsplay"></ul>
      </div>
    </div>
    <ul class="txtArea">
                                                                                              <li>
            <a class="" href="https://new.qq.com/omn/SPO20190/SPO2019080600112700.html" target="_blank">脚踏风火轮 双足堪比火尖枪！绿茵哪吒C罗踩单车瞬间大赏</a>
          </li>
                                <li>
            <a class="q-icons icon-video" href="https://new.qq.com/omn/20190806/20190806A02LK400.html" target="_blank">42岁卡特同意与老鹰签约 或在下赛季结束后选择退役</a>
          </li>
                                <li>
            <a class="q-icons icon-video" href="https://new.qq.com/omn/SPO20190/SPO2019080600138500.html" target="_blank">广州男篮海外拉练归来 10月赴美打NBA季前赛</a>
          </li>
                                <li>
            <a class="" href="https://new.qq.com/omn/SPO20190/SPO2019080600066200.html" target="_blank">小豌豆上帝之手破门！英超裁判亮瞎眼的误判合集</a>
          </li>
                                                                                                                                                                                                                                                                                                                                                                  </ul>
  </div>
</div>

<div class="bd cf undis" id="js_sportsbd2" bosszone="tiyu_2" bossexpo="bg_tiyu_2">
  <div class="bdleft">
  <div class="prt cf">
  <a href="https://new.qq.com/omn/20190806/20190806A0385W00.html" target="_blank" class="picwrap">
    <img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-original="https://inews.gtimg.com/newsapp_ls/0/9940562898_580328/0" class="pic" alt="德国足协承认错误：基米希踩踏桑乔应该吃红牌">
  </a>
  <div class="text">
    <a href="https://new.qq.com/omn/20190806/20190806A0385W00.html" target="_blank">
      <p class="tit">德国足协承认错误：基米希踩踏桑乔应该吃红牌</p>
    </a>
    <a class="from" href="https://new.qq.com/omn/20190806/20190806A0385W00.html" target="_blank">
      <span class="author">肆客足球</span>
      <span class="comment">9评</span>    </a>
  </div>
</div>
<ul class="txtArea">
                              <li>
      <a class="" href="https://new.qq.com/omn/SPO20190/SPO2019080600110900.html" target="_blank">英格兰奇迹男孩！科学解析桑乔为什么如此出色</a>
    </li>
                <li>
      <a class="q-icons icon-video" href="https://new.qq.com/omn/SPO20190/SPO2019080600159100.html" target="_blank">沪媒：里皮8月22日左右回中国 国足首期集训约25人</a>
    </li>
                <li>
      <a class="" href="https://new.qq.com/omn/SPO20190/SPO2019080600110100.html" target="_blank">忠诚勤勉的绝对门神！纳瓦斯赛季高光神扑集锦</a>
    </li>
                <li>
      <a class="q-icons icon-video" href="https://new.qq.com/omn/20190806/20190806A04KD500.html" target="_blank">鲁尼欲结束美职盟生涯 接近加盟英冠队出任球员兼教练</a>
    </li>
                                            </ul>

  </div>
  <div class="bdright">
  <div class="prt cf">
  <a href="https://new.qq.com/omn/SPO20190/SPO2019080600107500.html" target="_blank" class="picwrap">
    <img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-original="https://inews.gtimg.com/newsapp_ls/0/9940526924_580328/0" class="pic" alt="史上12大争议红牌！梅西C罗上榜 卡瓦尼庆祝也躺枪">
  </a>
  <div class="text">
    <a href="https://new.qq.com/omn/SPO20190/SPO2019080600107500.html" target="_blank">
      <p class="tit">史上12大争议红牌！梅西C罗上榜 卡瓦尼庆祝也躺枪</p>
    </a>
    <a class="from" href="https://new.qq.com/omn/SPO20190/SPO2019080600107500.html" target="_blank">
      <span class="author">腾讯体育</span>
      <span class="comment">3评</span>    </a>
  </div>
</div>
<ul class="txtArea">
                                        <li>
      <a class="" href="https://new.qq.com/omn/SPO20190/SPO2019080600184200.html" target="_blank">大腿归来自带气场 马内结束假期返回利物浦</a>
    </li>
                <li>
      <a class="" href="https://new.qq.com/omn/20190806/20190806A025CA00.html" target="_blank">前切尔西队长自由身加盟水晶宫 和昔日英格兰主帅再合作</a>
    </li>
                <li>
      <a class="" href="https://new.qq.com/omn/SPO20190/SPO2019080600174700.html" target="_blank">几个菜就喝成这样？保加利亚联赛门将上演超级失误</a>
    </li>
                <li>
      <a class="q-icons icon-video" href="https://new.qq.com/omn/20190806/20190806A021V100.html" target="_blank">庄神：我一直都在练三分 根本不在意别人怎么说</a>
    </li>
                                  </ul>

  </div>
</div>

<div class="bd cf undis" id="js_sportsbd3" bosszone="tiyu_3" bossexpo="bg_tiyu_3">
  <div class="bdleft">
  <div class="prt cf">
  <a href="https://new.qq.com/omn/20190806/20190806A00LUC00.html" target="_blank" class="picwrap">
    <img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-original="https://inews.gtimg.com/newsapp_ls/0/9939579814_580328/0" class="pic" alt="国锦赛-梁文博连救4赛点逆转取胜 小特两破百胜张安达">
  </a>
  <div class="text">
    <a href="https://new.qq.com/omn/20190806/20190806A00LUC00.html" target="_blank">
      <p class="tit">国锦赛-梁文博连救4赛点逆转取胜 小特两破百胜张安达</p>
    </a>
    <a class="from" href="https://new.qq.com/omn/20190806/20190806A00LUC00.html" target="_blank">
      <span class="author">狂野之城</span>
      <span class="comment">10评</span>    </a>
  </div>
</div>
<ul class="txtArea">
                                                  <li>
      <a class="q-icons icon-video" href="https://new.qq.com/omn/20190805/20190805A02VX200.html" target="_blank">奥利尼克还是德拉季奇？库班：混乱沟通让我们错失交易</a>
    </li>
                <li>
      <a class="" href="https://new.qq.com/omn/SPO20190/SPO2019080500130700.html" target="_blank">法国真人版钢铁侠 仅用时22分钟成功飞越英吉利海峡</a>
    </li>
                <li>
      <a class="" href="https://new.qq.com/omn/SPO20190/SPO2019080500601500.html" target="_blank">豪赚1.1亿奖金！中国选手最贵扑克赛夺冠</a>
    </li>
                <li>
      <a class="" href="https://new.qq.com/omn/20190805/20190805A00GA800.html" target="_blank">国锦赛：希金斯救赛点6-5吴宜泽 马奎尔零封晋级</a>
    </li>
                        </ul>

  </div>
  <div class="bdright">
  <div class="prt cf">
  <a href="https://new.qq.com/omn/SPO20190/SPO2019080600114000.html" target="_blank" class="picwrap">
    <img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-original="https://inews.gtimg.com/newsapp_ls/0/9940543984_580328/0" class="pic" alt="回顾齐达内治下皇马最强时刻 还有那些令人惊叹的进球">
  </a>
  <div class="text">
    <a href="https://new.qq.com/omn/SPO20190/SPO2019080600114000.html" target="_blank">
      <p class="tit">回顾齐达内治下皇马最强时刻 还有那些令人惊叹的进球</p>
    </a>
    <a class="from" href="https://new.qq.com/omn/SPO20190/SPO2019080600114000.html" target="_blank">
      <span class="author">腾讯体育</span>
          </a>
  </div>
</div>
<ul class="txtArea">
                                                            <li>
      <a class="" href="https://new.qq.com/omn/20190805/20190805A010LC00.html" target="_blank">范迪克神纪录遭终结！65场正式比赛之后 他终于被过掉了</a>
    </li>
                <li>
      <a class="q-icons icon-video" href="https://new.qq.com/omn/20190805/20190805A096VB00.html" target="_blank">河北放弃对国安争议点球上诉：不再执着不可改变的比分</a>
    </li>
                <li>
      <a class="q-icons icon-video" href="https://new.qq.com/omn/SPO20190/SPO2019080500963900.html" target="_blank">中国篮球往事：姚明叶莉大婚 08北京奥运开幕式</a>
    </li>
                <li>
      <a class="" href="https://new.qq.com/omn/20190805/20190805A0IK2G00.html" target="_blank">打破常规？恒大锋线酝酿3＋2定双冠！2本土小将已独造40球</a>
    </li>
              </ul>

  </div>
</div><!--[if !IE]>|xGv00|72f792a99aa5832f97e0abb9f572c16b<![endif]-->
            <div class="hyh js_hyh" bosszone="tiyu_more">
              <span class="htxt">换一换</span>
              <ul class="hwrap" id="js_sportshyh">
                <li class="hpoint active" data-rel="#js_sportsbd1"></li>
                <li class="hpoint" data-rel="#js_sportsbd2"></li>
                <li class="hpoint" data-rel="#js_sportsbd3"></li>
              </ul>
            </div>
          </div>
        </div>
        <!-- /体育 -->

        <!-- NBA -->
        <div class="mod-ch">
          <div class="title nst">
            <a class="txt active" href="http://sports.qq.com/nba/" target="_blank" bosszone="nba_logo">NBA</a>
            <ul class="label" bosszone="nba_om">
              	<li><a href="http://sports.qq.com/nbavideo/" target="_blank">NBA视频</a></li>
	<li><a href="http://sports.qq.com/nbavideo/topsk/" target="_blank">TOP时刻</a></li>
	<li><a href="http://nba.stats.qq.com/stats/" target="_blank">数据中心</a></li>
<!--6d53cccf9c0ee8e250df3d63048c39e4--><!--[if !IE]>|xGv00|4c1ef157870297fdc07394b3cb1497e3<![endif]-->
            </ul>
          </div>
          <div class="bdwrap js_chyh">
            

<div class="bd nbabd cf" id="js_nbabd1" bosszone="nba_1" bossexpo="bg_nba_1">
      <div class="bdleft">
      <div class="prt cf">
  <a href="https://new.qq.com/omn/NBA20190/NBA2019080600330300.html" target="_blank" class="picwrap">
    <img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-original="https://inews.gtimg.com/newsapp_ls/0/9941443811_580328/0" class="pic" alt="刘帅良打球什么水平？曾获乔丹颁奖 双绝杀加冕超级企鹅冠军">
  </a>
  <div class="text">
    <a href="https://new.qq.com/omn/NBA20190/NBA2019080600330300.html" target="_blank">
      <p class="tit">刘帅良打球什么水平？曾获乔丹颁奖 双绝杀加冕超级企鹅冠军</p>
    </a>
    <a class="from" href="https://new.qq.com/omn/NBA20190/NBA2019080600330300.html" target="_blank">
      <span class="author">腾讯体育</span>
          </a>
  </div>
</div>
<ul class="txtArea">
            <li>
      <a class="q-icons icon-video" href="https://new.qq.com/omn/20190806/20190806A04RPF00.html" target="_blank">火箭五虎最新备战消息！哈登跟戈登正狂练新绝技</a>
    </li>
                <li>
      <a class="q-icons icon-pic" href="https://new.qq.com/omn/NBA20190/NBA2019080600119900.html" target="_blank">加拿大男篮集训 穆雷心情不错奥利尼克活跃</a>
    </li>
                <li>
      <a class="" href="https://new.qq.com/omn/NBA20190/NBA2019080500140700.html" target="_blank">再起争议！沃尔质疑勇士总决赛隐瞒杜兰特伤情</a>
    </li>
                <li>
      <a class="" href="https://new.qq.com/omn/NBA20190/NBA2019080600216600.html" target="_blank">盘点季后赛赢球最多的5支球队 勇士42次仅垫底</a>
    </li>
                                                              </ul>

      </div>
      <div class="bdright">
          <div class="index cf" bosszone="nba_sc">
              <div class="ntop">
                <span id="js_nbatitle">
                  <a href="http://kbs.sports.qq.com/#nba" class="link active" target="_blank" data-rel="#js_nbalive">赛事直播</a>
                  <span class="wsplit"></span>
                  <span class="nsplit"></span>
                  <a href="http://kbs.sports.qq.com/#nba" class="link" target="_blank" data-rel="#js_nbaplay">精彩回放</a>
                </span>
                <ul class="nlabel">
                  <li class="nlabel-item"><a href="http://sports.qq.com/nba/" target="_blank">NBA</a></li>
                </ul>
              </div>
              <div class="nwrap">
                <ul class="live" id="js_nbalive"><li><a href="http://kbs.sports.qq.com/kbsweb/game.htm?mid=100002:20207274" target="_blank"><span class="name over">18-19赛季猛龙全回顾</span><span class="date over">今天</span><span class="icon-live over">直播</span><span class="team over one">18-19赛季NBA猛龙队常规赛回顾：常规赛G43-G49</span></a></li><li><a href="http://kbs.sports.qq.com/kbsweb/game.htm?mid=100002:20207275" target="_blank"><span class="name over">18-19赛季猛龙全回顾</span><span class="date over">08-07</span><span class="time over">09:00</span><span class="team over one">18-19赛季NBA猛龙队常规赛回顾：常规赛G50-G56</span></a></li></ul>
                <ul class="playback undis" id="js_nbaplay"><li><a href="http://kbs.sports.qq.com/kbsweb/game.htm?mid=100002:20207272" target="_blank"><span class="name over">18-19赛季猛龙全回顾</span><span class="date over">08-04</span><span class="team over oneback">18-19赛季NBA猛龙队常规赛回顾：常规赛G29-G35</span></a></li><li><a href="http://kbs.sports.qq.com/kbsweb/game.htm?mid=100002:20207273" target="_blank"><span class="name over">18-19赛季猛龙全回顾</span><span class="date over">08-05</span><span class="team over oneback">18-19赛季NBA猛龙队常规赛回顾：常规赛G36-G42</span></a></li></ul>
              </div>
            </div>
           <ul class="txtArea">
                                                                                                                            <li><a class="" href="https://new.qq.com/omn/NBA20190/NBA2019080500126000.html" target="_blank">库里18-19赛季最佳进球合集 终场前0.5秒上篮绝杀快船</a></li>
                                          <li><a class="" href="https://new.qq.com/omn/20190805/20190805A074NH00.html" target="_blank">美媒评NBA历史10大分卫 麦蒂第8艾弗森仅第5</a></li>
                                          <li><a class="" href="https://new.qq.com/omn/NBA20190/NBA2019080600151300.html" target="_blank">美国男篮开训小鬼当家 塔图姆福克斯布朗轮番单挑</a></li>
                                          <li><a class="q-icons icon-video" href="https://new.qq.com/omn/NBA20190/NBA2019080500176900.html" target="_blank">吴尊打篮球什么水平？他曾入选国家队 面对易建联进绝杀</a></li>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                         </ul>
      </div>
     </div>
     <div class="bd cf undis" id="js_nbabd2" bosszone="nba_2" bossexpo="bg_nba_2">
            <div class="bdleft">
              <div class="prt cf">
  <a href="https://new.qq.com/omn/NBA20190/NBA2019080500083300.html" target="_blank" class="picwrap">
    <img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-original="https://inews.gtimg.com/newsapp_ls/0/9931813161_580328/0" class="pic" alt="回顾2018年5场圣诞大战  哈登狂砍41分詹皇伤退">
  </a>
  <div class="text">
    <a href="https://new.qq.com/omn/NBA20190/NBA2019080500083300.html" target="_blank">
      <p class="tit">回顾2018年5场圣诞大战  哈登狂砍41分詹皇伤退</p>
    </a>
    <a class="from" href="https://new.qq.com/omn/NBA20190/NBA2019080500083300.html" target="_blank">
      <span class="author">腾讯体育</span>
      <span class="comment">32评</span>    </a>
  </div>
</div>
<ul class="txtArea">
                              <li>
      <a class="" href="https://new.qq.com/omn/NBA20190/NBA2019080500114200.html" target="_blank">星斗场第6期抢先看：吴尊携外援回归 禾浩辰王鹤棣组队应战</a>
    </li>
                <li>
      <a class="q-icons icon-video" href="https://new.qq.com/omn/20190806/20190806A04D0500.html" target="_blank">美媒体列哈登新赛季三大目标 常规赛MVP＋FMVP全都要？</a>
    </li>
                <li>
      <a class="q-icons icon-video" href="https://new.qq.com/omn/20190806/20190806A05OSG00.html" target="_blank">庄神为健身已不吃红肉 每日仅喝啤酒补充热量</a>
    </li>
                <li>
      <a class="q-icons icon-video" href="https://new.qq.com/omn/NBA20190/NBA2019080600071600.html" target="_blank">历史上的今天：海军上将出生 亿元先生被禁10场</a>
    </li>
                                            </ul>

            </div>
            <div class="bdright">
              <div class="prt cf">
  <a href="https://new.qq.com/omn/20190805/20190805A0FRLZ00.html" target="_blank" class="picwrap">
    <img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-original="https://inews.gtimg.com/newsapp_ls/0/9935436069_580328/0" class="pic" alt="勇士王朝没落？4个数字告诉你，杜兰特的离开并非世界末日">
  </a>
  <div class="text">
    <a href="https://new.qq.com/omn/20190805/20190805A0FRLZ00.html" target="_blank">
      <p class="tit">勇士王朝没落？4个数字告诉你，杜兰特的离开并非世界末日</p>
    </a>
    <a class="from" href="https://new.qq.com/omn/20190805/20190805A0FRLZ00.html" target="_blank">
      <span class="author">篮板侧沿</span>
      <span class="comment">604评</span>    </a>
  </div>
</div>
<ul class="txtArea">
                                        <li>
      <a class="q-icons icon-video" href="https://new.qq.com/omn/20190806/20190806A036AQ00.html" target="_blank">波式妙语来了！波帅调侃邓肯：他不懂执教 不知为何雇他</a>
    </li>
                <li>
      <a class="" href="https://new.qq.com/omn/NBA20190/NBA2019080600124600.html" target="_blank">没有顶级球星也要开练了 美国男篮众将抵达球馆正式开营</a>
    </li>
                <li>
      <a class="" href="https://new.qq.com/omn/NBA20190/NBA2019080600099100.html" target="_blank">不想看美国队一直赢 恩比德直言希望中国队世界杯夺冠</a>
    </li>
                <li>
      <a class="q-icons icon-pic" href="https://new.qq.com/omn/NBA20190/NBA2019080600072400.html" target="_blank">美国男篮集训布朗玩背扣 波波维奇一脸严肃</a>
    </li>
                                  </ul>

            </div>
       </div>
      <div class="bd cf undis" id="js_nbabd3" bosszone="nba_3" bossexpo="bg_nba_3">
            <div class="bdleft">
             <div class="prt cf">
  <a href="https://new.qq.com/omn/NBA20190/NBA2019080600286500.html" target="_blank" class="picwrap">
    <img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-original="https://inews.gtimg.com/newsapp_ls/0/9941275529_580328/0" class="pic" alt="新鲜出炉！美国男篮定妆照 看看这届梦之队都有谁？">
  </a>
  <div class="text">
    <a href="https://new.qq.com/omn/NBA20190/NBA2019080600286500.html" target="_blank">
      <p class="tit">新鲜出炉！美国男篮定妆照 看看这届梦之队都有谁？</p>
    </a>
    <a class="from" href="https://new.qq.com/omn/NBA20190/NBA2019080600286500.html" target="_blank">
      <span class="author">腾讯体育</span>
      <span class="comment">120评</span>    </a>
  </div>
</div>
<ul class="txtArea">
                                                  <li>
      <a class="q-icons icon-video" href="https://new.qq.com/omn/20190805/20190805A0N8ET00.html" target="_blank">美媒体预测詹皇新赛季总助攻升至历史第八 退役前进前三</a>
    </li>
                <li>
      <a class="q-icons icon-video" href="https://new.qq.com/omn/20190805/20190805A0N0X500.html" target="_blank">拉塞尔：有信心融入勇士体系 和库里将成危险组合</a>
    </li>
                <li>
      <a class="q-icons icon-video" href="https://new.qq.com/omn/20190805/20190805A0CFIC00.html" target="_blank">美媒预测新赛季6大奖项：字母哥最佳防守 浓眉哥MVP</a>
    </li>
                <li>
      <a class="" href="https://new.qq.com/omn/NBA20190/NBA2019080500073400.html" target="_blank">哈登18-19赛季进攻精彩混剪 经典后撤步三分手到擒来</a>
    </li>
                        </ul>

            </div>
            <div class="bdright">
             <div class="prt cf">
  <a href="https://new.qq.com/omn/NBA20190/NBA2019080600067900.html" target="_blank" class="picwrap">
    <img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-original="https://inews.gtimg.com/newsapp_ls/0/9940388156_580328/0" class="pic" alt="签约老鹰继续飞翔 回顾42岁卡特赛季十佳球">
  </a>
  <div class="text">
    <a href="https://new.qq.com/omn/NBA20190/NBA2019080600067900.html" target="_blank">
      <p class="tit">签约老鹰继续飞翔 回顾42岁卡特赛季十佳球</p>
    </a>
    <a class="from" href="https://new.qq.com/omn/NBA20190/NBA2019080600067900.html" target="_blank">
      <span class="author">腾讯体育</span>
      <span class="comment">102评</span>    </a>
  </div>
</div>
<ul class="txtArea">
                                                            <li>
      <a class="q-icons icon-video" href="https://new.qq.com/omn/20190805/20190805A04BRQ00.html" target="_blank">里弗斯揭秘招募小卡过程：我只谈了篮球和赢球</a>
    </li>
                <li>
      <a class="" href="https://new.qq.com/omn/NBA20190/NBA2019080500081200.html" target="_blank">勇士18-19赛季劲爆镜头合集 库里逆天3分杜兰特长臂劈扣</a>
    </li>
                <li>
      <a class="" href="https://new.qq.com/omn/NBA20190/NBA2019080600220600.html" target="_blank">君临天下 詹姆斯生涯34大劲爆扣篮高光集锦</a>
    </li>
                <li>
      <a class="q-icons icon-pic" href="https://new.qq.com/omn/NBA20190/NBA2019080600101300.html" target="_blank">美国男篮群星为篮球签名 库兹马塔克超有范儿</a>
    </li>
              </ul>

            </div>
       </div><!--[if !IE]>|xGv00|862e1b3e90c9c3d12efdc4b66da70b2d<![endif]-->
             <div class="hyh js_hyh" bosszone="nba_more">
              <span class="htxt">换一换</span>
              <ul class="hwrap" id="js_nbahyh">
                <li class="hpoint active" data-rel="#js_nbabd1"></li>
                <li class="hpoint" data-rel="#js_nbabd2"></li>
                <li class="hpoint" data-rel="#js_nbabd3"></li>
              </ul>
            </div>
          </div>
        </div>
        <!-- /NBA -->
      </div>

      <div class="col col-1 fr">
        <div id="mod-recommend" class="mod mod-recommend">
          <i class="line"></i>
          <div class="hd cf">
            <h2 class="tit fl">为你推荐</h2>
            <a class="more-btn fr" href="javascript:;" data-src="https://new.qq.com/" bosszone="wntj_more">点击查看 7 条新内容</a>
            <i class="icon-dot"></i>
          </div>
          <div class="bd">
            <div class="list"><ul bosszone="wntj_1" bossexpo="bg_wntj_1"><li class="news-pic-txt cf" data-id="20190806A05SKW" data-strategy="1" data-sourceid="26320" data-articletype="0" data-sorder="0" bosszone="wntjlist_0" bossexpo="bg_wntjlist_0"><i class="icon-dot"></i><div class="pic fl"><a href="https://new.qq.com/omn/20190806/20190806A05SKW00.html" target="_blank"><img src="https://inews.gtimg.com/newsapp_ls/0/9941223769_580328/0" alt="在职场中混，拥有这五个好心态，能帮你混得越来越好"></a></div><div class="txt fl"><a href="https://new.qq.com/omn/20190806/20190806A05SKW00.html" target="_blank">在职场中混，拥有这五个好心态，能帮你混得越来越好</a><div class="info"><a href="https://new.qq.com/omn/20190806/20190806A05SKW00.html" target="_blank" class="source">我的职场攻略</a></div></div></li><li data-id="20190805V0Q0ZH" data-strategy="1" data-sourceid="5822122" data-articletype="56" data-sorder="1" bosszone="wntjlist_1" bossexpo="bg_wntjlist_1"><i class="icon-dot"></i><a href="https://new.qq.com/omn/20190805/20190805V0Q0ZH00.html" target="_blank">虽然脾气火爆，却获得许多男生喜爱的三个生肖女生</a></li><li data-id="20190804A0IT1A" data-strategy="1" data-sourceid="5199324" data-articletype="0" data-sorder="2" bosszone="wntjlist_2" bossexpo="bg_wntjlist_2"><i class="icon-dot"></i><a href="https://new.qq.com/omn/20190804/20190804A0IT1A00.html" target="_blank">行得端坐得正，无所畏惧的生肖</a></li><li data-id="20190806A06LUF" data-strategy="1" data-sourceid="5215397" data-articletype="0" data-sorder="3" bosszone="wntjlist_3" bossexpo="bg_wntjlist_3"><i class="icon-dot"></i><a href="https://new.qq.com/omn/20190806/20190806A06LUF00.html" target="_blank">古代士大夫的衣袖，在中国历史上扮演着特别的角色</a></li><li data-id="20190806A0662S" data-strategy="1" data-sourceid="5443519" data-articletype="0" data-sorder="4" bosszone="wntjlist_4" bossexpo="bg_wntjlist_4"><i class="icon-dot"></i><a class="q-icons icon-video" href="https://new.qq.com/omn/20190806/20190806A0662S00.html" target="_blank">我们的命是空调给的，那古代人的命是谁给的？</a></li><li data-id="20190806A06F7B" data-strategy="1" data-sourceid="5147949" data-articletype="0" data-sorder="5" bosszone="wntjlist_5" bossexpo="bg_wntjlist_5"><i class="icon-dot"></i><a href="https://new.qq.com/omn/20190806/20190806A06F7B00.html" target="_blank">努比亚双屏旗舰新配色公布：锦鲤红</a></li><li data-id="20190806A0466N" data-strategy="1" data-sourceid="17177851" data-articletype="0" data-sorder="6" bosszone="wntjlist_6" bossexpo="bg_wntjlist_6"><i class="icon-dot"></i><a href="https://new.qq.com/omn/20190806/20190806A0466N00.html" target="_blank">记者：于汉超已在德国进行第二次手术 本赛季基本报销</a></li></ul><ul bosszone="wntj_2" bossexpo="bg_wntj_2"><li class="news-pic-txt cf" data-id="20190806A02YYY" data-strategy="1" data-sourceid="5626754" data-articletype="0" data-sorder="7" bosszone="wntjlist_7" bossexpo="bg_wntjlist_7"><i class="icon-dot"></i><div class="pic fl"><a href="https://new.qq.com/omn/20190806/20190806A02YYY00.html" target="_blank"><img src="https://inews.gtimg.com/newsapp_ls/0/9940326278_580328/0" alt="林肯第一款国产SUV，只卖二十多万，汉兰达还加价吗？"></a></div><div class="txt fl"><a href="https://new.qq.com/omn/20190806/20190806A02YYY00.html" target="_blank">林肯第一款国产SUV，只卖二十多万，汉兰达还加价吗？</a><div class="info"><a href="https://new.qq.com/omn/20190806/20190806A02YYY00.html" target="_blank" class="source">靓车大咖会 22次评</a></div></div></li><li data-id="20190805V0PWS4" data-strategy="1" data-sourceid="5822122" data-articletype="56" data-sorder="8" bosszone="wntjlist_8" bossexpo="bg_wntjlist_8"><i class="icon-dot"></i><a href="https://new.qq.com/omn/20190805/20190805V0PWS400.html" target="_blank">喜欢独来独往，却也害怕寂寞的三个生肖女生</a></li><li data-id="20190806A05LOG" data-strategy="1" data-sourceid="5148804" data-articletype="0" data-sorder="9" bosszone="wntjlist_9" bossexpo="bg_wntjlist_9"><i class="icon-dot"></i><a href="https://new.qq.com/omn/20190806/20190806A05LOG00.html" target="_blank">卡带再现，复古回潮，蓝牙连接外放，听歌录音一个不落</a></li><li data-id="20190806A05MLN" data-strategy="1" data-sourceid="26320" data-articletype="0" data-sorder="10" bosszone="wntjlist_10" bossexpo="bg_wntjlist_10"><i class="icon-dot"></i><a href="https://new.qq.com/omn/20190806/20190806A05MLN00.html" target="_blank">工作中，掌握这四种能力，能帮你在职场中脱颖而出</a></li><li data-id="20190806V04K41" data-strategy="1" data-sourceid="5178438" data-articletype="56" data-sorder="11" bosszone="wntjlist_11" bossexpo="bg_wntjlist_11"><i class="icon-dot"></i><a href="https://new.qq.com/omn/20190806/20190806V04K4100.html" target="_blank">张恕：不忘初心写忠诚 牢记使命铸警魂</a></li><li data-id="20190806A06TCN" data-strategy="1" data-sourceid="5140123" data-articletype="0" data-sorder="12" bosszone="wntjlist_12" bossexpo="bg_wntjlist_12"><i class="icon-dot"></i><a href="https://new.qq.com/omn/20190806/20190806A06TCN00.html" target="_blank">星座女神 塔罗测试：未来一个月的感情运势如何？</a></li><li data-id="20190806A05P8K" data-strategy="1" data-sourceid="26134" data-articletype="0" data-sorder="13" bosszone="wntjlist_13" bossexpo="bg_wntjlist_13"><i class="icon-dot"></i><a href="https://new.qq.com/omn/20190806/20190806A05P8K00.html" target="_blank">台湾花莲县海域发生4.9级地震 震源深度13千米</a></li></ul><ul bosszone="wntj_3" bossexpo="bg_wntj_3"><li class="news-pic-txt cf" data-id="20190805A0O3AX" data-strategy="1" data-sourceid="5009900" data-articletype="0" data-sorder="14" bosszone="wntjlist_14" bossexpo="bg_wntjlist_14"><i class="icon-dot"></i><div class="pic fl"><a href="https://new.qq.com/omn/20190805/20190805A0O3AX00.html" target="_blank"><img src="https://inews.gtimg.com/newsapp_ls/0/9937334082_580328/0" alt="荣耀V20、Magic2、9X PRO，到底怎么选？"></a></div><div class="txt fl"><a href="https://new.qq.com/omn/20190805/20190805A0O3AX00.html" target="_blank">荣耀V20、Magic2、9X PRO，到底怎么选？</a><div class="info"><a href="https://new.qq.com/omn/20190805/20190805A0O3AX00.html" target="_blank" class="source">瓦力评测</a></div></div></li><li data-id="20190731A0RM0V" data-strategy="1" data-sourceid="5199324" data-articletype="0" data-sorder="15" bosszone="wntjlist_15" bossexpo="bg_wntjlist_15"><i class="icon-dot"></i><a href="https://new.qq.com/omn/20190731/20190731A0RM0V00.html" target="_blank">下半年灵感爆发，水到渠成的生肖</a></li><li data-id="20190806A06B1W" data-strategy="1" data-sourceid="5447917" data-articletype="0" data-sorder="16" bosszone="wntjlist_16" bossexpo="bg_wntjlist_16"><i class="icon-dot"></i><a href="https://new.qq.com/omn/20190806/20190806A06B1W00.html" target="_blank">自动打包的小橘，提着就能走</a></li><li data-id="20190804V0A016" data-strategy="1" data-sourceid="10808991" data-articletype="56" data-sorder="17" bosszone="wntjlist_17" bossexpo="bg_wntjlist_17"><i class="icon-dot"></i><a href="https://new.qq.com/omn/20190804/20190804V0A01600.html" target="_blank">李晨深夜聚餐买醉疑似借酒疗情伤，数位性感妹子作陪</a></li><li data-id="20190806A000TK" data-strategy="1" data-sourceid="5087314" data-articletype="0" data-sorder="18" bosszone="wntjlist_18" bossexpo="bg_wntjlist_18"><i class="icon-dot"></i><a href="https://new.qq.com/omn/20190806/20190806A000TK00.html" target="_blank">天海进攻被吹，人和同病相怜？</a></li></ul></div>
          </div>
        </div>
      </div>

    </div>
    <!-- /娱乐/体育/NBA -->

    <!-- 财经/大家 -->
    <div class="layout channel2col qq-channel2col  cf">
      <div class="col col-2 fl">
        <div class="title nst">
          <a class="txt active" href="http://finance.qq.com" target="_blank" bosszone="caijing_logo">财经</a>
          <span bosszone="caijing_dh">
            <a class="txt" href="http://stock.qq.com/" target="_blank">证券</a>
            <a class="txt" href="http://money.qq.com/" target="_blank">理财</a>
          </span>
          <ul class="label" bosszone="caijing_om">
            	<li><a href="https://new.qq.com/omn/author/5178949" target="_blank">第一财经</a></li>
	<li><a href="https://new.qq.com/omn/author/5564731" target="_blank">界面新闻</a></li>
	<li><a href="https://new.qq.com/omn/author/5005722" target="_blank">每日经济新闻</a></li>
	<li><a href="https://new.qq.com/omn/author/5373662" target="_blank">财约你</a></li>
<!--bc199ce1f7deeb7afd7b010332754ab4--><!--[if !IE]>|xGv00|bf6bf2afc43cb97229dc8d7f46dfd633<![endif]-->
          </ul>
        </div>
        <div class="bdwrap js_chyh">
          <div class="bd stockbd cf" id="js_stockbd1" bosszone="caijing_1" bossexpo="bg_caijing_1">
            <div class="bdleft">
                        <div class="prt cf">
            <a href="https://new.qq.com/omn/FIN20190/FIN2019080600051700.html" target="_blank" class="picwrap"><img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-original="https://inews.gtimg.com/newsapp_ls/0/9940446330_580328/0" class="pic" alt="财经早报| 美股遭血洗4天蒸发17万亿！国内油价预计不涨了"></a>
            <div class="text">
              <a href="https://new.qq.com/omn/FIN20190/FIN2019080600051700.html" target="_blank">
                <p class="tit">财经早报| 美股遭血洗4天蒸发17万亿！国内油价预计不涨了</p>
              </a>
             <a class="from" href="https://new.qq.com/omn/FIN20190/FIN2019080600051700.html" target="_blank"><span class="author">腾讯财经</span><span class="comment">139评</span></a>
            </div>
          </div>
          <ul class="txtArea">
                                                                      <li><a class="" href="https://new.qq.com/omn/FIN20190/FIN2019080600054100.html" target="_blank">你不知道的另一种教育移民：乡村父母为子女上学在城镇买房</a></li>
                                                                          <li><a class="" href="https://new.qq.com/omn/FIN20190/FIN2019080600244700.html" target="_blank">差别化监管来了！保险资产负债管理监管暂行办法落地</a></li>
                                                                          <li><a class="" href="https://new.qq.com/omn/20190806/20190806A02LI900.html" target="_blank">声援华为？公交秘书应用宣布暂停iPhone服务！</a></li>
                                                                          <li><a class="" href="https://new.qq.com/omn/20190806/20190806A05TEM00.html" target="_blank">“三条纹”纠纷案终结，斯凯奇与阿迪达斯庭外和解</a></li>
                                                                          <li><a class="" href="https://new.qq.com/omn/20190806/20190806A066GZ00.html" target="_blank">从网红锦鲤到旅游博主，信小呆人设转变引争议</a></li>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              </ul><!--[if !IE]>|xGv00|604203d4459f47f27b23046facae9d47<![endif]-->
            </div>
            <div class="bdright">
              <div class="index cf" bosszone="caijing_sc">
                <div class="sleft">
                  <div class="st-item st-item-t">
                    <a href="http://gu.qq.com/sh000001/zs" target="_blank" class="st-title">上证综指</a>
                    <div class="detail">
                    <a href="http://gu.qq.com/sh000001/zs" target="_blank" id="js_stocksh" class="detail-down"><span class="price"><span class="icon-num-2"></span><span class="icon-num-7"></span><span class="icon-num-4"></span><span class="icon-num-7"></span><span class="icon-num-d"></span><span class="icon-num-7"></span><span class="icon-num-7"></span></span><span class="float">-73.73</span><span class="percent">-2.61%</span></a>
                    </div>
                  </div>
                  <div class="st-item">
                    <a href="http://gu.qq.com/usDJI/zs" target="_blank" class="st-title">道琼斯</a>
                    <div class="detail">
                      <a href="http://gu.qq.com/usDJI/zs" target="_blank" id="js_stockdqs" class="detail-down"><span class="price"><span class="icon-num-2"></span><span class="icon-num-5"></span><span class="icon-num-7"></span><span class="icon-num-1"></span><span class="icon-num-7"></span><span class="icon-num-d"></span><span class="icon-num-7"></span><span class="icon-num-4"></span></span><span class="float">-767.27</span><span class="percent">-2.90%</span></a>
                    </div>
                  </div>
                </div>
                <div class="sright">
                  <div class="st-item st-item-t">
                    <a href="http://gu.qq.com/hkHSI/zs" target="_blank" class="st-title">恒生指数</a>
                    <div class="detail">
                      <a href="http://gu.qq.com/hkHSI/zs" target="_blank" id="js_stockhs" class="detail-down"><span class="price"><span class="icon-num-2"></span><span class="icon-num-5"></span><span class="icon-num-5"></span><span class="icon-num-3"></span><span class="icon-num-6"></span><span class="icon-num-d"></span><span class="icon-num-8"></span><span class="icon-num-4"></span></span><span class="float">-614.48</span><span class="percent">-2.35%</span></a>
                    </div>
                  </div>
                  <div class="st-item">
                    <a href="http://gu.qq.com/sh000847/zs" target="_blank" class="st-title">腾讯济安</a>
                    <div class="detail">
                      <a href="http://gu.qq.com/sh000847/zs" target="_blank" id="js_stockten" class="detail-down"><span class="price"><span class="icon-num-1"></span><span class="icon-num-8"></span><span class="icon-num-5"></span><span class="icon-num-7"></span><span class="icon-num-d"></span><span class="icon-num-5"></span><span class="icon-num-9"></span></span><span class="float">-73.00</span><span class="percent">-3.78%</span></a>
                    </div>
                  </div>
                </div>
              </div>
                        <ul class="txtArea">
                                                <li><a class="" href="https://new.qq.com/omn/20190806/20190806A04FP900.html" target="_blank">科迪乳业再现神操作：手握17亿现金，却还不上1.4亿奶款</a></li>
                                                                          <li><a class="" href="https://new.qq.com/omn/20190806/20190806A03RF400.html" target="_blank">每月花400亿，王首富大转折，还要押上多少个小目标？</a></li>
                                                                          <li><a class="q-icons icon-video" href="https://new.qq.com/zt/template/?id=STO2019070900521600" target="_blank">A股三大指数跌幅收窄！沪指跌1.77% 国防军工板块异动</a></li>
                                                                          <li><a class="" href="https://new.qq.com/omn/STO20190/STO2019080600022700.html" target="_blank">美股全线暴跌道指跌超760点 标普500创年内最大单日跌幅</a></li>
                                                                          <li><a class="" href="https://new.qq.com/omn/20190806/20190806A03F2V00.html" target="_blank">康美市值蒸发超300亿！白马股频爆雷 外资还会看好吗</a></li>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        </ul><!--[if !IE]>|xGv00|8e34b18a3148e52c2a47bbf69cf657c5<![endif]-->
            </div>
          </div>
          <div class="bd cf undis" id="js_stockbd2" bosszone="caijing_2" bossexpo="bg_caijing_2">
            <div class="bdleft">
                        <div class="prt cf">
            <a href="https://new.qq.com/omn/20190806/20190806A0613D00.html" target="_blank" class="picwrap"><img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-original="https://inews.gtimg.com/newsapp_ls/0/9941286990_580328/0" class="pic" alt="区块链电子发票一周年：日均开4.4万张 接入企业超5000家"></a>
            <div class="text">
              <a href="https://new.qq.com/omn/20190806/20190806A0613D00.html" target="_blank">
                <p class="tit">区块链电子发票一周年：日均开4.4万张 接入企业超5000家</p>
              </a>
              <a class="from" href="https://new.qq.com/omn/20190806/20190806A0613D00.html" target="_blank"><span class="author">经济观察报</span></a>
            </div>
          </div>
          <ul class="txtArea">
                                                                                                                                                                                                            <li><a class="" href="https://new.qq.com/omn/20190806/20190806A066G300.html" target="_blank">食之秘上海直营店全关门高峰期有近百家，运营公司工商失联</a></li>
                                                                            <li><a class="" href="https://new.qq.com/omn/20190806/20190806A03E2J00.html" target="_blank">交易1万提成120，借道支付宝跑分成洗钱帮凶？</a></li>
                                                                            <li><a class="" href="https://new.qq.com/omn/20190806/20190806A060AD00.html" target="_blank">遭泰山石化向香港法院提清盘呈请 中海重工挫22％创新低</a></li>
                                                                            <li><a class="" href="https://new.qq.com/omn/FIN20190/FIN2019080600324200.html" target="_blank">20号胶的诞生：全球年消费近830万吨 中国是五大消费地之一</a></li>
                                                                            <li><a class="" href="https://new.qq.com/omn/20190806/20190806A02JXO00.html" target="_blank">“债”的背后您不知道的秘密！</a></li>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          </ul><!--[if !IE]>|xGv00|043af6c1a05421d17ffa072d3ef6e77f<![endif]-->
            </div>
            <div class="bdright">
                      <div class="prt cf">
            <a href="https://new.qq.com/omn/20190805/20190805A0QIGP00.html" target="_blank" class="picwrap"><img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-original="https://inews.gtimg.com/newsapp_ls/0/9938129437_580328/0" class="pic" alt="下半年房地产开局全线遇冷！四大龙头房企销售额全面下滑"></a>
            <div class="text">
              <a href="https://new.qq.com/omn/20190805/20190805A0QIGP00.html" target="_blank">
                <p class="tit">下半年房地产开局全线遇冷！四大龙头房企销售额全面下滑</p>
              </a>
              <a class="from" href="https://new.qq.com/omn/20190805/20190805A0QIGP00.html" target="_blank"><span class="author">南方都市报</span><span class="comment">76评</span></a>
            </div>
          </div>
          <ul class="txtArea">
                                                                                                                                                                                      <li><a class="" href="https://new.qq.com/omn/FIN20190/FIN2019080600099400.html" target="_blank">离岸人民币兑美元短线拉升近200点，收复7.12关口</a></li>
                                                                            <li><a class="q-icons icon-video" href="https://new.qq.com/zt/template/?id=STO2019071000166800" target="_blank">恒指跌2.33%报25541点 地产板块领跌蓝筹股</a></li>
                                                                            <li><a class="" href="https://new.qq.com/omn/20190806/20190806A02XKY00.html" target="_blank">全球股市大跌，A股会迎来黄金抄底机会吗？</a></li>
                                                                            <li><a class="" href="https://new.qq.com/omn/FIN20190/FIN2019080600247100.html" target="_blank">小米跌超3%股价创历史新低 传公司已解散Mi VR团队</a></li>
                                                                            <li><a class="" href="https://new.qq.com/omn/20190806/20190806A05LM700.html" target="_blank">退出中国市场的铃木：第一财季营业利润暴跌46％</a></li>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul><!--[if !IE]>|xGv00|496dda9b2c58cd97f3e4890c68f2dc00<![endif]-->
            </div>
          </div>
          <div class="bd cf undis" id="js_stockbd3" bosszone="caijing_3" bossexpo="bg_caijing_3">
            <div class="bdleft">
                        <div class="prt cf">
            <a href="https://new.qq.com/omn/FIN20190/FIN2019080600343200.html" target="_blank" class="picwrap"><img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-original="https://inews.gtimg.com/newsapp_ls/0/9941491245_580328/0" class="pic" alt="车市入冬 奔驰宝马车企巨头受挫利润下滑"></a>
            <div class="text">
              <a href="https://new.qq.com/omn/FIN20190/FIN2019080600343200.html" target="_blank">
                <p class="tit">车市入冬 奔驰宝马车企巨头受挫利润下滑</p>
              </a>
              <a class="from" href="https://new.qq.com/omn/FIN20190/FIN2019080600343200.html" target="_blank"><span class="author">时代周报</span></a>
            </div>
          </div>
          <ul class="txtArea">
                                                                                                                                                                                                                                                                                                                                                <li><a class="" href="https://new.qq.com/omn/20190806/20190806A03LZD00.html" target="_blank">减证便民！税务总局再取消25项税务证明事项</a></li>
                                                                            <li><a class="" href="https://new.qq.com/omn/20190806/20190806A0385N00.html" target="_blank">首开旗下项目再出质量问题：交房1年外墙脱落 十余辆车被砸</a></li>
                                                                            <li><a class="" href="https://new.qq.com/omn/20190806/20190806A03D6200.html" target="_blank">冯仑：年轻人不婚不生孩子是一种进步</a></li>
                                                                            <li><a class="" href="https://new.qq.com/omn/20190806/20190806A02LG600.html" target="_blank">咋回事儿？Facebook旗下多款APP集体宕机</a></li>
                                                                            <li><a class="" href="https://new.qq.com/omn/20190806/20190806A037JI00.html" target="_blank">哪吒“封神”票房要冲30亿，动漫产业的春天来了？</a></li>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      </ul><!--[if !IE]>|xGv00|eee8b3a265c781baeaa215d7c9956a63<![endif]-->
            </div>
            <div class="bdright">
                        <div class="prt cf">
            <a href="https://new.qq.com/omn/20190806/20190806A05EC900.html" target="_blank" class="picwrap"><img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-original="https://inews.gtimg.com/newsapp_ls/0/9941325535_580328/0" class="pic" alt="浙商锐评：冯鑫VS贾跃亭 明星企业家命运滑铁卢照见的景象"></a>
            <div class="text">
              <a href="https://new.qq.com/omn/20190806/20190806A05EC900.html" target="_blank">
                <p class="tit">浙商锐评：冯鑫VS贾跃亭 明星企业家命运滑铁卢照见的景象</p>
              </a>
              <a class="from" href="https://new.qq.com/omn/20190806/20190806A05EC900.html" target="_blank"><span class="author">浙商杂志</span></a>
            </div>
          </div>
          <ul class="txtArea">
                                                                                                                                                                                                                                                                                                                          <li><a class="" href="https://new.qq.com/omn/20190806/20190806A05LXF00.html" target="_blank">海底捞联手饿了么推外卖，二线城市保卫战？</a></li>
                                                                            <li><a class="" href="https://new.qq.com/omn/FIN20190/FIN2019080600265300.html" target="_blank">伊利股份开盘快速走低！股价大跌9% 创4个月来新低</a></li>
                                                                            <li><a class="" href="https://new.qq.com/omn/20190806/20190806A060HU00.html" target="_blank">中国银行吉林遵义路违法遭罚 违反外汇账户管理规定</a></li>
                                                                            <li><a class="" href="https://new.qq.com/omn/20190806/20190806A066OA00.html" target="_blank">科创板3家中止企业更新财务数据，陆续恢复审核</a></li>
                                                                            <li><a class="" href="https://new.qq.com/omn/FIN20190/FIN2019080600272300.html" target="_blank">视觉中国早盘逆市大涨，一度冲击涨停</a></li>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </ul><!--[if !IE]>|xGv00|b8cde06c535f0fc479f005a6d96f2a16<![endif]-->
            </div>
          </div>
          <div class="hyh js_hyh" bosszone="caijing_more">
            <span class="htxt">换一换</span>
            <ul class="hwrap" id="js_stockhyh">
              <li class="hpoint active" data-rel="#js_stockbd1"></li>
              <li class="hpoint" data-rel="#js_stockbd2"></li>
              <li class="hpoint" data-rel="#js_stockbd3"></li>
            </ul>
          </div>
        </div>
      </div>
      <div class="col col-1 fr" bossexpo="bg_dajia">
        <div class="title">
          <a class="txt active" href="http://dajia.qq.com/" target="_blank" bosszone="dajia_logo">大家</a>
        </div>
        <div bosszone="dajia">
                    <div class="prt cf">
            <a href="https://new.qq.com/omn/20190805/20190805A0GEHC00.html" target="_blank" class="picwrap"><img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-original="//inews.gtimg.com/newsapp_ls/0/9938773390_196130/0" class="pic" alt="大家 | 从洛阳花到醉翁亭，他为中国文人构建了两个精神故乡"></a>
            <div class="text">
              <a href="https://new.qq.com/omn/20190805/20190805A0GEHC00.html" target="_blank">
                <p class="tit">大家 | 从洛阳花到醉翁亭，他为中国文人构建了两个精神故乡</p>
              </a>
              <a class="from" href="https://new.qq.com/omn/20190805/20190805A0GEHC00.html" target="_blank"><span class="author">腾讯大家</span><span class="comment">2评</span></a>
            </div>
          </div>
          <ul class="txtArea">
                                                                        <li><a class="" href="https://new.qq.com/omn/20190805/20190805A0G99Y00.html" target="_blank">大家 | 为什么美国高中生暑期忙着打工</a></li>
                                                                            <li><a class="" href="https://new.qq.com/omn/20190802/20190802A0GBQ200.html" target="_blank">大家丨近代上海真是中国的一个例外吗？</a></li>
                                                                            <li><a class="" href="https://new.qq.com/omn/20190801/20190801A0KAIU00.html" target="_blank">大家丨从机会主义者到纳粹帮凶：无情对无脑的胜利？</a></li>
                                                                            <li><a class="" href="https://new.qq.com/omn/20190801/20190801A0JHAB00.html" target="_blank">大家丨《哪吒》成爆款，在今日中国是正常还是反常</a></li>
                                                                            <li><a class="" href="https://new.qq.com/omn/20190731/20190731A0HWR200.html" target="_blank">大家丨南宋的抗金政治学：四大权相，三种立场，皆成奸臣</a></li>
                                              </ul><!--[if !IE]>|xGv00|ddff3a36cc6e01e7042ce3dd124ef711<![endif]-->
        </div>
      </div>
    </div>
    <!-- 财经/大家 -->

    <!-- 科技/时尚 -->
    <div class="layout channel2col qq-channel2col cf">
      <div class="col col-2 fl">
        <div class="title nst">
          <a class="txt active" href="https://new.qq.com/ch/tech/" target="_blank" bosszone="keji_logo">科技</a>
          <span bosszone="keji_dh">
            <a class="txt" href="http://kepu.qq.com/" target="_blank">科普</a>
          </span>
          <ul class="label" bosszone="keji_om">
            	<li><a href="https://new.qq.com/zt/template/?id=TEC2018091206055500" target="_blank">产品+</a></li>
	<li><a href="https://new.qq.com/zt/template/?id=TEC2017092703535100" target="_blank">创投圈</a></li>
	<li><a href="https://new.qq.com/zt/template/?id=TEC2018020602489500" target="_blank">AI行业精选</a></li>
	<li><a href="https://new.qq.com/omn/author/5464974" target="_blank">电脑管家</a></li>
<!--a1d774e72aba1977d9dc20ff09dff0c4--><!--[if !IE]>|xGv00|ef2bbcb3e871338cf1e2c7775dbea3c1<![endif]-->
          </ul>
        </div>
        <div class="bdwrap js_chyh">
          

	    <div class="bd cf" id="js_techbd1" bosszone="keji_1" bossexpo="bg_keji_1">
	      <div class="bdleft">
			<div class="prt cf">
  <a href="https://new.qq.com/omn/20190805/20190805A0R7QF00.html" target="_blank" class="picwrap">
    <img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-original="https://inews.gtimg.com/newsapp_ls/0/9941276621_580328/0" class="pic" alt="魅族锤子们的最后时刻：黄章与罗永浩理想主义湮灭">
  </a>
  <div class="text">
    <a href="https://new.qq.com/omn/20190805/20190805A0R7QF00.html" target="_blank">
      <p class="tit">魅族锤子们的最后时刻：黄章与罗永浩理想主义湮灭</p>
    </a>
    <a class="from" href="https://new.qq.com/omn/20190805/20190805A0R7QF00.html" target="_blank">
      <span class="author">首席人物观</span>
      <span class="comment">63评</span>    </a>
  </div>
</div>
<ul class="txtArea">
      	    <li>
      <a class="" href="https://new.qq.com/omn/20190806/20190806A030UL00.html" target="_blank">5G演义之日韩先行：一个三星，就几乎搞定了整个韩国</a>
    </li>
          	    <li>
      <a class="" href="https://new.qq.com/omn/TEC20190/TEC2019080600060400.html" target="_blank">潜望｜“今日头条”入局搜索：流量巨头的生存空间之战</a>
    </li>
          	    <li>
      <a class="q-icons icon-pic" href="https://new.qq.com/omn/20190806/20190806A02KTM00.html" target="_blank">荣耀9X对比红米K20：哪款是2千元内最佳“水桶机”？</a>
    </li>
          	    <li>
      <a class="" href="https://new.qq.com/omn/20190806/20190806A00D1P00.html" target="_blank">主播曝“直播打赏”套路：400万元流水只有5万是真的</a>
    </li>
          	    <li>
      <a class="" href="https://new.qq.com/omn/TEC20190/TEC2019080600246400.html" target="_blank">日本政府支持利用动物胚胎培育人类器官：异种移植争议不断</a>
    </li>
                                                                        </ul>

		  </div>
		  <div class="bdright">
		  	<a href="https://new.qq.com/omn/20190806/20190806A05R8200.html" target="_blank">
	          <h2>特斯拉车主想踩油门，结果发现踏板没了</h2>
	        </a>
	        <div class="line"></div>
	         <ul class="txtArea">
	        	        					        					        					        					        					        					        					        					  		          <li>
		            <a class="" href="https://new.qq.com/omn/20190806/20190806A06CAJ00.html" target="_blank">手机按键越变越少，未来还够用吗？</a>
		          </li>
		          	         					        					  		          <li>
		            <a class="" href="https://new.qq.com/omn/TEC20190/TEC2019080600144300.html" target="_blank">SpaceX推出“卫星拼火箭”服务：发射费最低225万美元</a>
		          </li>
		          	         					        					  		          <li>
		            <a class="" href="https://new.qq.com/omn/TEC20190/TEC2019080600206300.html" target="_blank">传小米解散VR头盔团队 合作方称会继续开发</a>
		          </li>
		          	         					        					  		          <li>
		            <a class="" href="https://new.qq.com/omn/TEC20190/TEC2019080600154900.html" target="_blank">谷歌承诺：2022年全部产品添加可回收材料</a>
		          </li>
		          	         					        					  		          <li>
		            <a class="" href="https://new.qq.com/omn/TEC20190/TEC2019080600294500.html" target="_blank">英国拟加强监督 监管机构要求FB提供更多加密货币信息</a>
		          </li>
		          	         					        					  		          <li>
		            <a class="q-icons icon-video" href="https://new.qq.com/omn/20190806/20190806A03R3A00.html" target="_blank">中国移动前董事长谈飞信失败：起步早太注重技术</a>
		          </li>
		          	         					        					        					        					        					        					        					        					        					        					        					        					        					        					        					        					        					        					        					        					        					        					        					        					        					        					        							 </ul>
		  </div>
		 </div>
		 <div class="bd cf undis" id="js_techbd2" bosszone="keji_2" bossexpo="bg_keji_2">
	          <div class="bdleft">
	          	<div class="prt cf">
  <a href="https://new.qq.com/omn/TEC20190/TEC2019080600054900.html" target="_blank" class="picwrap">
    <img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-original="https://inews.gtimg.com/newsapp_ls/0/9940329383_580328/0" class="pic" alt="欧洲两大外卖商同意合并交易 将和Uber外卖争夺全球老大">
  </a>
  <div class="text">
    <a href="https://new.qq.com/omn/TEC20190/TEC2019080600054900.html" target="_blank">
      <p class="tit">欧洲两大外卖商同意合并交易 将和Uber外卖争夺全球老大</p>
    </a>
    <a class="from" href="https://new.qq.com/omn/TEC20190/TEC2019080600054900.html" target="_blank">
      <span class="author">腾讯科技</span>
      <span class="comment">1评</span>    </a>
  </div>
</div>
<ul class="txtArea">
                                	    <li>
      <a class="" href="https://new.qq.com/omn/20190806/20190806A06UJD00.html" target="_blank">搜狐系美股全线大跌，搜狐跌27％创历史新低</a>
    </li>
          	    <li>
      <a class="" href="https://new.qq.com/omn/TEC20190/TEC2019080600304600.html" target="_blank">沃尔玛旗下印度电商Flipkart将推免费视频服务</a>
    </li>
          	    <li>
      <a class="" href="https://new.qq.com/omn/20190806/20190806A032ZY00.html" target="_blank">华为开始宣传基于安卓10的全新系统：将跟鸿蒙有联动</a>
    </li>
          	    <li>
      <a class="" href="https://new.qq.com/omn/20190806/20190806A03BH700.html" target="_blank">中国快递的战国时代</a>
    </li>
          	    <li>
      <a class="" href="https://new.qq.com/omn/20190806/20190806A06R0Y00.html" target="_blank">苹果为特定用户免费发特别版iPhone：为iOS系统找Bug</a>
    </li>
                                              </ul>

	          </div>
	          <div class="bdright">
	          	<div class="prt cf">
  <a href="https://new.qq.com/omn/TEC20190/TEC2019080600043700.html" target="_blank" class="picwrap">
    <img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-original="https://inews.gtimg.com/newsapp_ls/0/9940255300_580328/0" class="pic" alt="前程无忧第二季度净利润980万美元 同比扭亏">
  </a>
  <div class="text">
    <a href="https://new.qq.com/omn/TEC20190/TEC2019080600043700.html" target="_blank">
      <p class="tit">前程无忧第二季度净利润980万美元 同比扭亏</p>
    </a>
    <a class="from" href="https://new.qq.com/omn/TEC20190/TEC2019080600043700.html" target="_blank">
      <span class="author">腾讯科技</span>
      <span class="comment">1评</span>    </a>
  </div>
</div>
<ul class="txtArea">
                                            	    <li>
      <a class="" href="https://new.qq.com/omn/20190806/20190806A03Q7Z00.html" target="_blank">蚂蚁金服完成对智慧畅行A轮投资：比移动支付更大的故事</a>
    </li>
          	    <li>
      <a class="" href="https://new.qq.com/omn/TEC20190/TEC2019080600149500.html" target="_blank">贝索斯上周套现28亿美元 曾承诺每年投资蓝色起源10亿美元</a>
    </li>
          	    <li>
      <a class="" href="https://new.qq.com/omn/20190806/20190806A03RUO00.html" target="_blank">电商平台齐加码直播业务，带货格局将如何重整</a>
    </li>
          	    <li>
      <a class="" href="https://new.qq.com/omn/20190806/20190806A0458D00.html" target="_blank">无人机物流扩大配送范围，但未来发展仍有诸多难题</a>
    </li>
          	    <li>
      <a class="" href="https://new.qq.com/omn/20190806/20190806A02UH500.html" target="_blank">网购电脑屏幕开裂 未当面验收索赔难</a>
    </li>
                                  </ul>

	          </div>
	     </div>
	     <div class="bd cf undis" id="js_techbd3" bosszone="keji_3" bossexpo="bg_keji_3">
	          <div class="bdleft">
	           <div class="prt cf">
  <a href="https://new.qq.com/omn/TEC20190/TEC2019080600044400.html" target="_blank" class="picwrap">
    <img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-original="https://inews.gtimg.com/newsapp_ls/0/9940265346_580328/0" class="pic" alt="美国股市遭遇重挫 五大科技巨头市值蒸发1620亿美元">
  </a>
  <div class="text">
    <a href="https://new.qq.com/omn/TEC20190/TEC2019080600044400.html" target="_blank">
      <p class="tit">美国股市遭遇重挫 五大科技巨头市值蒸发1620亿美元</p>
    </a>
    <a class="from" href="https://new.qq.com/omn/TEC20190/TEC2019080600044400.html" target="_blank">
      <span class="author">腾讯科技</span>
      <span class="comment">29评</span>    </a>
  </div>
</div>
<ul class="txtArea">
                                                        	    <li>
      <a class="" href="https://new.qq.com/omn/20190806/20190806A036AX00.html" target="_blank">柔性电子，不断刷新你的认知</a>
    </li>
          	    <li>
      <a class="" href="https://new.qq.com/omn/TEC20190/TEC2019080600213400.html" target="_blank">智能助手被指侵犯用户隐私 美三大科技巨头面临调查</a>
    </li>
          	    <li>
      <a class="" href="https://new.qq.com/omn/20190805/20190805A0MSNS00.html" target="_blank">lCO六年简明史：天才、骗局和暴富神话</a>
    </li>
          	    <li>
      <a class="" href="https://new.qq.com/omn/20190805/20190805A0FXY100.html" target="_blank">一飞冲天，大展宏图：北斗服务商航天宏图</a>
    </li>
          	    <li>
      <a class="" href="https://new.qq.com/omn/20190805/20190805A08NSR00.html" target="_blank">华为海外注册P300等商标：之前抢注R系列 倒逼OPPO调整</a>
    </li>
                      </ul>

	          </div>
	          <div class="bdright">
	           <div class="prt cf">
  <a href="https://new.qq.com/omn/20190805/20190805A0AAA600.html" target="_blank" class="picwrap">
    <img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-original="https://inews.gtimg.com/newsapp_ls/0/9938506924_580328/0" class="pic" alt="三星、SK海力士半导体材料库存或仅能维持1.5个月">
  </a>
  <div class="text">
    <a href="https://new.qq.com/omn/20190805/20190805A0AAA600.html" target="_blank">
      <p class="tit">三星、SK海力士半导体材料库存或仅能维持1.5个月</p>
    </a>
    <a class="from" href="https://new.qq.com/omn/20190805/20190805A0AAA600.html" target="_blank">
      <span class="author">闪存市场</span>
      <span class="comment">20评</span>    </a>
  </div>
</div>
<ul class="txtArea">
                                                                    	    <li>
      <a class="" href="https://new.qq.com/omn/20190805/20190805A0P4NN00.html" target="_blank">商场数字化该怎么做？改造过万达广场的丙晟这么看</a>
    </li>
          	    <li>
      <a class="" href="https://new.qq.com/omn/20190805/20190805A0IJMB00.html" target="_blank">日本NEC公开测试“飞行汽车”，能悬停一分钟</a>
    </li>
          	    <li>
      <a class="" href="https://new.qq.com/omn/20190805/20190805A0MTJC00.html" target="_blank">敬汉卿被“抢注”商标：其实抢注并没那么可怕</a>
    </li>
          	    <li>
      <a class="" href="https://new.qq.com/omn/20190804/20190804A0AC6J00.html" target="_blank">揭秘最流氓互联网公司：竟坐拥2.6亿用户 放400亿高利贷</a>
    </li>
          	    <li>
      <a class="" href="https://new.qq.com/omn/20190805/20190805A0KZ9K00.html" target="_blank">助力脑医学科研和临床应用，慧脑云获A轮融资5000万元</a>
    </li>
          </ul>

	          </div>
	     </div><!--[if !IE]>|xGv00|a327a42ec833dae324602776b8aa6a61<![endif]-->
          <div class="hyh js_hyh" bosszone="keji_more">
            <span class="htxt">换一换</span>
            <ul class="hwrap" id="js_techhyh">
              <li class="hpoint active" data-rel="#js_techbd1"></li>
              <li class="hpoint" data-rel="#js_techbd2"></li>
              <li class="hpoint" data-rel="#js_techbd3"></li>
            </ul>
          </div>
         </div>
      </div>
      <div class="col col-1 fr" bossexpo="bg_shishang">
        <div class="title">
          <a class="txt active" href="https://new.qq.com/ch/fashion/" target="_blank" bosszone="shishang_logo">时尚</a>
        </div>
        <div bosszone="shishang">
                    <div class="prt cf">
            <a href="https://new.qq.com/zt/template/?id=FAS2019061700851400" target="_blank" class="picwrap"><img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-original="https://inews.gtimg.com/newsapp_ls/0/9941105799_580328/0" class="pic" alt="颜究院 | 6款大热平价品牌PK，最后结果我真香了"></a>
            <div class="text">
              <a href="https://new.qq.com/zt/template/?id=FAS2019061700851400" target="_blank">
                <p class="tit">颜究院 | 6款大热平价品牌PK，最后结果我真香了</p>
              </a>
              <a class="from" href="https://new.qq.com/zt/template/?id=FAS2019061700851400" target="_blank"><span class="author">腾讯新闻</span></a>
            </div>
          </div>
          <ul class="txtArea">
                                                                        <li><a class="" href="https://new.qq.com/omn/20190805/20190805A05JAT00.html" target="_blank">适合素颜涂的温柔口红推荐！绝对是你能够驾驭的口红色号</a></li>
                                                                            <li><a class="" href="https://new.qq.com/omn/20190806/20190806A05CAM00.html" target="_blank">李嘉欣把薄纱当上衣穿，49岁还这么性感，让别人怎么活？</a></li>
                                                                            <li><a class="" href="https://new.qq.com/omn/20190806/20190806A05DGU00.html" target="_blank">小仙女郑爽换了新发型，清新可爱有一种当年楚雨荨的感觉</a></li>
                                                                            <li><a class="" href="https://new.qq.com/omn/20190806/20190806A05G2V00.html" target="_blank">巧妙给衣服打个结，衣品也悄悄加分！</a></li>
                                                                            <li><a class="" href="https://new.qq.com/omn/20190805/20190805A0KVH700.html" target="_blank">美妆圈 | 从大数据看高速扩张的中国化妆品业</a></li>
                                              </ul><!--[if !IE]>|xGv00|a87fae48e48d6421bc9f0fe10f763926<![endif]-->
        </div>
      </div>
    </div>
    <!-- 科技/时尚 -->

    <!-- 汽车/房产 -->
    <div class="layout channel2col qq-channel2col cf">
      <div class="col col-2 fl">
        <div class="title nst">
          <a class="txt active" href="http://auto.qq.com/" target="_blank" bosszone="qiche_logo">汽车</a>
          <ul class="label" bosszone="qiche_om">
            	<li><a href="http://auto.qq.com/newcar.htm" target="_blank">重磅新车</a></li>
	<li><a href="http://data.auto.qq.com/car_brand/index.shtml" target="_blank">车型大全</a></li>
	<li><a href="http://v.qq.com/auto/" target="_blank">精彩视频</a></li>
	<li><a href="http://automall.qq.com/web" target="_blank">汽车商城</a></li>
<!--6e928c5a09b99b44ea59a0157a61dfcd--><!--[if !IE]>|xGv00|94ce4999be87e555e97293a725da59ea<![endif]-->
          </ul>
        </div>
        <div class="bdwrap js_chyh">
          

	    <div class="bd cf" id="js_autobd1" bosszone="qiche_1" bossexpo="bg_qiche_1">
	      <div class="bdleft">
			<div class="prt cf">
  <a href="https://new.qq.com/omn/20190806/20190806A031XN00.html" target="_blank" class="picwrap">
    <img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-original="https://inews.gtimg.com/newsapp_ls/0/9941156688_580328/0" class="pic" alt="新一代国产神车！标配5G的豪华SUV，还有鸥翼门和液晶座舱">
  </a>
  <div class="text">
    <a href="https://new.qq.com/omn/20190806/20190806A031XN00.html" target="_blank">
      <p class="tit">新一代国产神车！标配5G的豪华SUV，还有鸥翼门和液晶座舱</p>
    </a>
    <a class="from" href="https://new.qq.com/omn/20190806/20190806A031XN00.html" target="_blank">
      <span class="author">DIOS车评</span>
      <span class="comment">57评</span>    </a>
  </div>
</div>
<ul class="txtArea">
      	    <li>
      <a class="" href="https://new.qq.com/omn/20190806/20190806A03PQE00.html" target="_blank">汉兰达的最强对手！新款福特锐界，将8月16日即将登场！</a>
    </li>
          	    <li>
      <a class="" href="https://new.qq.com/omn/20190805/20190805A0BEQJ00.html" target="_blank">销量下滑大众也扛不住了 朗逸优惠2.3万/宝来暴降2.8万</a>
    </li>
          	    <li>
      <a class="" href="https://new.qq.com/omn/20190806/20190806A03BI100.html" target="_blank">气场强大的新旗舰！外观霸气内饰豪华，3.0T V6动力配四驱</a>
    </li>
          	    <li>
      <a class="" href="https://d.automall.qq.com/web/svw" target="_blank">途昂逐云版，追光逐云专属定制</a>
    </li>
          	    <li>
      <a class="" href="https://new.qq.com/omn/20190806/20190806A030BE00.html" target="_blank">什么叫做神车？就是每一次的改动，都是为了消费者着想</a>
    </li>
                                                                              </ul>

		  </div>
		  <div class="bdright">
		  	<a href="https://new.qq.com/omn/20190804/20190804A0576000.html" target="_blank">
	          <h2>5月卖得最好的6款SUV，款款精品，第一名热销24086辆</h2>
	        </a>
	        <div class="line"></div>
	         <ul class="txtArea">
	        	        					        					        					        					        					        					        					        		         			          <li>
		            <a class="" href="https://new.qq.com/omn/20190806/20190806A00EDR00.html" target="_blank">李现情感剧热播 看剧中人物都开什么车？</a>
		          </li>
		          	         					        		         			          <li>
		            <a class="" href="https://new.qq.com/omn/20190806/20190806A00PBH00.html" target="_blank">网友发现停车场闸门Bug，手机照片能骗过摄像头？</a>
		          </li>
		          	         					        		         			          <li>
		            <a class="" href="https://new.qq.com/omn/20190806/20190806A05JI300.html" target="_blank">全面升级，新一代路虎揽胜极光蓄势待发</a>
		          </li>
		          	         					        		         			          <li>
		            <a class="" href="https://new.qq.com/omn/20190806/20190806A05SRF00.html" target="_blank">北汽新能源EC5上市 补贴后售价9.99万-11.99万元</a>
		          </li>
		          	         					        		         			          <li>
		            <a class="" href="https://new.qq.com/omn/20190806/20190806A05O0L00.html" target="_blank">邦德的新座驾试驾阿斯顿·马丁DBS Superleggera</a>
		          </li>
		          	         					        		         			          <li>
		            <a class="" href="https://new.qq.com/omn/20190806/20190806A02VLJ00.html" target="_blank">跑一趟高速换一个牌照？阿城一男子被罚1万元拘20天记24分</a>
		          </li>
		          	         					        					        					        					        					        					        					        					        					        					        					        					        					        					        					        					        					        					        					        					        					        					        					        					        					        					        					        					        					        							 </ul>
		  </div>
		 </div>
		 <div class="bd cf undis" id="js_autobd2" bosszone="qiche_2" bossexpo="bg_qiche_2">

	          <div class="bdleft">
	          	<div class="prt cf">
  <a href="https://new.qq.com/omn/20190806/20190806A05RZR00.html" target="_blank" class="picwrap">
    <img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-original="https://inews.gtimg.com/newsapp_ls/0/9941220528_580328/0" class="pic" alt="跟其它“小钢炮”相比 领克03＋还差了什么？">
  </a>
  <div class="text">
    <a href="https://new.qq.com/omn/20190806/20190806A05RZR00.html" target="_blank">
      <p class="tit">跟其它“小钢炮”相比 领克03＋还差了什么？</p>
    </a>
    <a class="from" href="https://new.qq.com/omn/20190806/20190806A05RZR00.html" target="_blank">
      <span class="author">车界微视auto</span>
          </a>
  </div>
</div>
<ul class="txtArea">
                                	    <li>
      <a class="" href="https://new.qq.com/omn/20190806/20190806A05SM100.html" target="_blank">实测4毛一公里，这台高颜值国产家轿，1.5T＋6MT真省油</a>
    </li>
          	    <li>
      <a class="" href="https://new.qq.com/omn/20190806/20190806A033UZ00.html" target="_blank">今年上半年卖得最火的三款中级车出来了，一起来看看</a>
    </li>
          	    <li>
      <a class="" href="https://new.qq.com/omn/20190806/20190806A05SQA00.html" target="_blank">全新沃尔沃V60上市 不一定能走量但一定坚守信念</a>
    </li>
          	    <li>
      <a class="" href="https://new.qq.com/omn/20190806/20190806A03A8A00.html" target="_blank">全新飞度要来了，传说中的gk5，你喜欢吗？</a>
    </li>
          	    <li>
      <a class="" href="https://new.qq.com/omn/20190806/20190806A05TYX00.html" target="_blank">国机智骏GX5下线 续航338km/四季度上市</a>
    </li>
                                                    </ul>

	          </div>
	          <div class="bdright">
	          	<div class="prt cf">
  <a href="https://new.qq.com/omn/20190806/20190806A05WOU00.html" target="_blank" class="picwrap">
    <img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-original="https://inews.gtimg.com/newsapp_ls/0/9941257878_580328/0" class="pic" alt="6座豪华中大型SUV 试驾凯迪拉克XT6">
  </a>
  <div class="text">
    <a href="https://new.qq.com/omn/20190806/20190806A05WOU00.html" target="_blank">
      <p class="tit">6座豪华中大型SUV 试驾凯迪拉克XT6</p>
    </a>
    <a class="from" href="https://new.qq.com/omn/20190806/20190806A05WOU00.html" target="_blank">
      <span class="author">SUV大咖</span>
          </a>
  </div>
</div>
<ul class="txtArea">
                                            	    <li>
      <a class="" href="https://new.qq.com/omn/20190806/20190806A0602700.html" target="_blank">打败法拉利，这位传奇人物功不可没！</a>
    </li>
          	    <li>
      <a class="" href="https://new.qq.com/omn/20190806/20190806A062V300.html" target="_blank">售52.99—71.49万元 新款Jeep大切诺基正式上市</a>
    </li>
          	    <li>
      <a class="" href="https://new.qq.com/omn/20190806/20190806A037CU00.html" target="_blank">19款“丰田威驰”预售价曝光，能东山再起吗？</a>
    </li>
          	    <li>
      <a class="" href="https://new.qq.com/omn/20190806/20190806A02XYH00.html" target="_blank">丰田将给东京奥运会带来一款高端电瓶车？</a>
    </li>
          	    <li>
      <a class="" href="https://new.qq.com/omn/20190806/20190806A01EUP00.html" target="_blank">思域是台什么车？碾压昂克赛拉和福克斯，实力来自哪？</a>
    </li>
                                        </ul>

	          </div>
	     </div>
	      <div class="bd cf undis" id="js_autobd3" bosszone="qiche_3" bossexpo="bg_qiche_3">
	          <div class="bdleft">
	           <div class="prt cf">
  <a href="https://new.qq.com/omn/20190806/20190806A03CTH00.html" target="_blank" class="picwrap">
    <img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-original="https://inews.gtimg.com/newsapp_ls/0/9940505606_580328/0" class="pic" alt="雷克萨斯中国的“三杯茶”">
  </a>
  <div class="text">
    <a href="https://new.qq.com/omn/20190806/20190806A03CTH00.html" target="_blank">
      <p class="tit">雷克萨斯中国的“三杯茶”</p>
    </a>
    <a class="from" href="https://new.qq.com/omn/20190806/20190806A03CTH00.html" target="_blank">
      <span class="author">汽扯扒谈</span>
      <span class="comment">2评</span>    </a>
  </div>
</div>
<ul class="txtArea">
                                                        	    <li>
      <a class="" href="https://new.qq.com/omn/AUT20190/AUT2019080600112100.html" target="_blank">车辆6年免检 真不用去车管所吗 很多人都吃过亏</a>
    </li>
          	    <li>
      <a class="" href="https://new.qq.com/omn/AUT20190/AUT2019080600115000.html" target="_blank">让4S店往车辆上装这些装置的 不是钱多就是人傻</a>
    </li>
          	    <li>
      <a class="" href="https://new.qq.com/omn/20190806/20190806A02UC700.html" target="_blank">全新一代广汽传祺GA6核心零部件供应商一览</a>
    </li>
          	    <li>
      <a class="" href="https://new.qq.com/omn/AUT20190/AUT2019080600110500.html" target="_blank">车窗雨天容易起雾 学学老司机的几种解决办法</a>
    </li>
          	    <li>
      <a class="" href="https://new.qq.com/omn/20190806/20190806A02LWQ00.html" target="_blank">这6条冷门交规，罚一次就会罚到你哭！</a>
    </li>
                            </ul>

	          </div>
	          <div class="bdright">
	           <div class="prt cf">
  <a href="https://new.qq.com/omn/20190806/20190806A03HXP00.html" target="_blank" class="picwrap">
    <img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-original="https://inews.gtimg.com/newsapp_ls/0/9940567117_580328/0" class="pic" alt="买不起CRV不要紧，同样1.5T发动机，油耗不高还便宜了6万">
  </a>
  <div class="text">
    <a href="https://new.qq.com/omn/20190806/20190806A03HXP00.html" target="_blank">
      <p class="tit">买不起CRV不要紧，同样1.5T发动机，油耗不高还便宜了6万</p>
    </a>
    <a class="from" href="https://new.qq.com/omn/20190806/20190806A03HXP00.html" target="_blank">
      <span class="author">话说车世界</span>
          </a>
  </div>
</div>
<ul class="txtArea">
                                                                    	    <li>
      <a class="" href="https://new.qq.com/omn/AUT20190/AUT2019080600098100.html" target="_blank">谷歌推出升级版Android Auto 新界面有哪些新功能？</a>
    </li>
          	    <li>
      <a class="" href="https://new.qq.com/omn/20190806/20190806A02TTB00.html" target="_blank">销冠全球不容易！车市转冷，但新能源汽车如此热</a>
    </li>
          	    <li>
      <a class="" href="https://new.qq.com/omn/AUT20190/AUT2019080600086700.html" target="_blank">印度销量陷入低谷 铃木全球最大市场被爆裁员</a>
    </li>
          	    <li>
      <a class="q-icons icon-video" href="https://new.qq.com/omn/20190806/20190806A03HM400.html" target="_blank">这个百年品牌，造了一款离经叛道的新车</a>
    </li>
          	    <li>
      <a class="" href="https://new.qq.com/omn/AUT20190/AUT2019080600078500.html" target="_blank">FCA首席执行官：对合并结盟持开放态度 自己也能继续前进</a>
    </li>
                </ul>

	          </div>
	     </div><!--[if !IE]>|xGv00|d2f926d0d45bc959773a2a1e85a4bd68<![endif]-->
          <div class="hyh js_hyh" bosszone="qiche_more">
            <span class="htxt">换一换</span>
            <ul class="hwrap" id="js_autohyh">
              <li class="hpoint active" data-rel="#js_autobd1"></li>
              <li class="hpoint" data-rel="#js_autobd2"></li>
              <li class="hpoint" data-rel="#js_autobd3"></li>
            </ul>
          </div>
        </div>
      </div>
      <div class="col col-1 fr" bossexpo="bg_fangchan">
        <div class="title">
          <a class="txt active" href="http://house.qq.com/" target="_blank" bosszone="fangchan_logo">房产</a>
        </div>
        <div bosszone="fangchan">
                    <div class="prt cf">
            <a href="https://new.qq.com/omn/20190806/20190806A05BMW00.html" target="_blank" class="picwrap"><img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-original="https://inews.gtimg.com/newsapp_ls/0/9941112646_580328/0" class="pic" alt="2019上半年太原房地产开发投资贡献超七成 增长13.2％"></a>
            <div class="text">
              <a href="https://new.qq.com/omn/20190806/20190806A05BMW00.html" target="_blank">
                <p class="tit">2019上半年太原房地产开发投资贡献超七成 增长13.2％</p>
              </a>
              <a class="from" href="https://new.qq.com/omn/20190806/20190806A05BMW00.html" target="_blank"><span class="author">乐居网山西</span></a>
            </div>
          </div>
          <ul class="txtArea">
                                                                        <li><a class="" href="https://new.qq.com/omn/20190806/20190806A05ENV00.html" target="_blank">自降买地门槛，GDP连续5年倒数第二，增城是不是缺钱了？</a></li>
                                                                            <li><a class="" href="https://new.qq.com/omn/HOS20190/HOS2019080600068800.html" target="_blank">风口上频频踩雷 长租公寓怎么了</a></li>
                                                                            <li><a class="" href="https://new.qq.com/omn/HOS20190/HOS2019080600089100.html" target="_blank">北京年内集中网签38套破亿元豪宅</a></li>
                                                                            <li><a class="" href="https://new.qq.com/omn/20190806/20190806A05YDS00.html" target="_blank">上海购房指南：看你的月收入，能在上海买什么样的房？</a></li>
                                                                            <li><a class="" href="https://new.qq.com/omn/20190806/20190806A066CX00.html" target="_blank">绿地控股：为两家公司提供合计80.392亿元融资担保</a></li>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          </ul><!--[if !IE]>|xGv00|8d5ad02b55c1602d2929718cbda31092<![endif]-->
        </div>
      </div>
    </div>
    <!-- /汽车/房产 -->

    <!-- 综艺影视剧 -->
    <div class="layout qq-videos m40">
      <div class="title" id="js_vtitle">
        <a class="txt active" href="https://v.qq.com/x/variety/" target="_blank" data-rel="#js_bdzy" bosszone="zongyi_logo">综艺</a>
        <span class="split"></span>
        <a class="txt" href="http://v.qq.com/tv/" target="_blank" data-rel="#js_bdysj" bosszone="zongyi_logo">电视剧</a>
        <span class="split"></span>
        <a class="txt" href="http://v.qq.com/movie/" target="_blank" data-rel="#js_bdmv" bosszone="dianying_logo">电影</a>
        <span class="split"></span>
        <a class="txt" href="https://v.qq.com/child" target="_blank" data-rel="#js_bdchild" bosszone="shaoer_logo">少儿</a>
        <ul class="label" bosszone="zongyi_om">
          	<li><a href="https://v.qq.com/cartoon" target="_blank">动漫</a></li>
	<li><a href="http://v.qq.com/sports/" target="_blank">体育</a></li>
	<li><a href="https://v.qq.com/x/channel/doco" target="_blank">纪录片</a></li>
	<li><a href="https://v.qq.com/x/cover/jx7g4sm320sqm7i/y0027ta8e2a.html" target="_blank">风味人间</a></li>
<!--cb9788120ee161040272784bdd220636--><!--[if !IE]>|xGv00|7798e125e72206f614df084dd62d79a4<![endif]-->
        </ul>
      </div>
      <div class="mainbody" id="js_videosbd">
        <div id="js_bdzy" bossexpo="bg_zongyi">
          <div class="bdwrap">
            <div class="bd-inner cf" id="js_zyCon"><div id="js_zyCon_0" class="bd cf" bosszone="zongyi_1" bossexpo="bg_zongyi_1"><a class="video-boxv fl js_bigvideo" data-boss="vv_zongyi" data-alt="明日之子·毛不易看呆" data-cid="pzdfade2ghizkgn" data-cvid="r0031ll8biz" data-vid="i19056zm7s3" href="javascript:;" data-href="https://v.qq.com/x/cover/pzdfade2ghizkgn.html?videoMark="><img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-original="https://puui.qpic.cn/vupload/0/20190801_1564831966267_m754rs2605s.jpeg/0" alt="明日之子·毛不易看呆"><div class="txt"><span>明日之子·毛不易看呆</span></div><i class="q-icons icon-play"></i><i class="icon-label icon-label-type icon-label-rt">自制</i><i class="icon-label icon-label-info icon-label-rb"> 2019-08-03  期</i></a><div class="pics-box fl" data-href="https://v.qq.com/x/cover/2mojj0egt6wji77/u0031vt1t90.html?videoMark="><div class="top"><img data-boss="vv_zongyi" data-url="https://v.qq.com/x/cover/2mojj0egt6wji77/u0031vt1t90.html?videoMark=" src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-original="//puui.qpic.cn/media_img/lena/PIC38ywlj_720_1280/0" alt="极限挑战5·演唱会" class="js_bigvideo" data-cid="2mojj0egt6wji77" data-cvid="q0031t17vlp" data-vid="y1905kkimeh"><i class="icon-label icon-label-info icon-label-lb">2019-08-04 期</i><i class="icon-label icon-label-type icon-label-rt">VIP</i></div><a href="https://v.qq.com/x/cover/2mojj0egt6wji77/u0031vt1t90.html?videoMark=" target="_blank"><div class="info"><p class="vtitle over f16">极限挑战5·演唱会</p><p class="comer over">热巴华晨宇rap合唱酷翻</p><span class="watch over">嘉宾：迪丽热巴 黄渤 王迅</span></div></a></div><div class="pics-box fl" data-href="https://v.qq.com/x/cover/9z3bvof8smb3kh8/v0031tefcl8.html?videoMark="><div class="top"><img data-boss="vv_zongyi" data-url="https://v.qq.com/x/cover/9z3bvof8smb3kh8/v0031tefcl8.html?videoMark=" src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-original="https://puui.qpic.cn/vupload/0/20190804_1564930357058_t4jpu3pazv.jpeg/0" alt="合唱吧300·脸红心跳" class="js_bigvideo" data-cid="9z3bvof8smb3kh8" data-cvid="f0031vizb2m" data-vid="q1905u2okkv"><i class="icon-label icon-label-info icon-label-lb">2019-08-04 期</i><i class="icon-label icon-label-type icon-label-rt">自制</i></div><a href="https://v.qq.com/x/cover/9z3bvof8smb3kh8/v0031tefcl8.html?videoMark=" target="_blank"><div class="info"><p class="vtitle over f16">合唱吧300·脸红心跳</p><p class="comer over">周震南被夏之光抱起来转圈</p><span class="watch over">嘉宾：R1SE 草蜢</span></div></a></div><div class="pics-box fl" data-href="https://v.qq.com/x/cover/v8ig3qlm8uadgse/d0031loakm2.html?videoMark="><div class="top"><img data-boss="vv_zongyi" data-url="https://v.qq.com/x/cover/v8ig3qlm8uadgse/d0031loakm2.html?videoMark=" src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-original="//puui.qpic.cn/media_img/lena/PICt2jal0_304_540/0" alt="脱口秀大会·被骂渣" class="js_bigvideo" data-cid="v8ig3qlm8uadgse" data-cvid="f0031dc81io" data-vid="g1905cd6pos"><i class="icon-label icon-label-info icon-label-lb">2019-08-04 期</i><i class="icon-label icon-label-type icon-label-rt">自制</i></div><a href="https://v.qq.com/x/cover/v8ig3qlm8uadgse/d0031loakm2.html?videoMark=" target="_blank"><div class="info"><p class="vtitle over f16">脱口秀大会·被骂渣</p><p class="comer over">于小彤聊抢女友陈小纭手机</p><span class="watch over">嘉宾：于谦 李诞 吴昕</span></div></a></div><div class="pics-box fl pics-last" data-href="https://v.qq.com/x/cover/w85xfpwcmhk3zeo/u00318qm7yl.html?videoMark="><div class="top"><img data-boss="vv_zongyi" data-url="https://v.qq.com/x/cover/w85xfpwcmhk3zeo/u00318qm7yl.html?videoMark=" src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-original="https://puui.qpic.cn/vupload/0/20190802_1565005350684_38x88iokrwo.jpeg/0" alt="邻家诗话·再秀新乐器" class="js_bigvideo" data-cid="w85xfpwcmhk3zeo" data-cvid="g0031klmdas" data-vid="v1905musb9g"><i class="icon-label icon-label-info icon-label-lb">2019-08-05 期</i><i class="icon-label icon-label-type icon-label-rt">自制</i></div><a href="https://v.qq.com/x/cover/w85xfpwcmhk3zeo/u00318qm7yl.html?videoMark=" target="_blank"><div class="info"><p class="vtitle over f16">邻家诗话·再秀新乐器</p><p class="comer over">阿兰vs国乐大师对弹奚琴</p><span class="watch over">嘉宾：阿兰·达瓦卓玛 方锦龙 郦波</span></div></a></div></div><div id="js_zyCon_1" class="bd cf undis" bosszone="zongyi_2" bossexpo="bg_zongyi_2"><a class="video-boxv fl js_bigvideo" data-boss="vv_zongyi" data-alt="我家小两口·超想要娃" data-cid="evkwn79xql1dnud" data-cvid="w0031t27wnc" data-vid="r1905o76397" href="javascript:;" data-href="https://v.qq.com/x/cover/evkwn79xql1dnud.html?videoMark="><img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-src="//puui.qpic.cn/media_img/lena/PIC5mvu1c_304_540/0" alt="我家小两口·超想要娃"><div class="txt"><span>我家小两口·超想要娃</span></div><i class="q-icons icon-play"></i><i class="icon-label icon-label-type icon-label-rt">VIP</i><i class="icon-label icon-label-info icon-label-rb"> 2019-08-03  期</i></a><div class="pics-box fl" data-href="https://v.qq.com/x/cover/ruc6zptj4zrhfjl.html?videoMark="><div class="top"><img data-boss="vv_zongyi" data-url="https://v.qq.com/x/cover/ruc6zptj4zrhfjl.html?videoMark=" src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-src="//puui.qpic.cn/media_img/lena/PIC6kxlje_720_1280/0" alt="好声音·翻版赖美云" class="js_bigvideo" data-cid="ruc6zptj4zrhfjl" data-cvid="n0031kqqji0" data-vid="g1905mvnaar"><i class="icon-label icon-label-info icon-label-lb">2019-08-02 期</i><i class="icon-label icon-label-type icon-label-rt">VIP</i></div><a href="https://v.qq.com/x/cover/ruc6zptj4zrhfjl.html?videoMark=" target="_blank"><div class="info"><p class="vtitle over f16">好声音·翻版赖美云</p><p class="comer over">热辣开唱一秒征服王力宏</p><span class="watch over">嘉宾：王力宏 那英 庾澄庆</span></div></a></div><div class="pics-box fl" data-href="https://v.qq.com/x/cover/j77clxzmipfv8x3.html?videoMark="><div class="top"><img data-boss="vv_zongyi" data-url="https://v.qq.com/x/cover/j77clxzmipfv8x3.html?videoMark=" src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-src="//puui.qpic.cn/media_img/lena/PIC0opr2s_720_1280/0" alt="中餐厅3·黄晓明不罢休" class="js_bigvideo" data-cid="j77clxzmipfv8x3" data-cvid="z0031hf97z2" data-vid="o1905x9v435"><i class="icon-label icon-label-info icon-label-lb">2019-08-02 期</i><i class="icon-label icon-label-type icon-label-rt">VIP</i></div><a href="https://v.qq.com/x/cover/j77clxzmipfv8x3.html?videoMark=" target="_blank"><div class="info"><p class="vtitle over f16">中餐厅3·黄晓明不罢休</p><p class="comer over">杨紫花式撒娇拒绝称体重</p><span class="watch over">嘉宾：杨紫 秦海璐 黄晓明</span></div></a></div><div class="pics-box fl" data-href="https://v.qq.com/x/cover/sdkf4rtllxbc0hn.html?videoMark="><div class="top"><img data-boss="vv_zongyi" data-url="https://v.qq.com/x/cover/sdkf4rtllxbc0hn.html?videoMark=" src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-src="//puui.qpic.cn/media_img/lena/PIC46j7e5_720_1280/0" alt="声入人心2·唱醉张惠妹" class="js_bigvideo" data-cid="sdkf4rtllxbc0hn" data-cvid="b0031gv61e2" data-vid="a1905yf2cc8"><i class="icon-label icon-label-info icon-label-lb">2019-08-02 期</i><i class="icon-label icon-label-type icon-label-rt">VIP</i></div><a href="https://v.qq.com/x/cover/sdkf4rtllxbc0hn.html?videoMark=" target="_blank"><div class="info"><p class="vtitle over f16">声入人心2·唱醉张惠妹</p><p class="comer over">《莫斯科郊外的晚上》超好听</p><span class="watch over">嘉宾：尚雯婕 张惠妹 廖昌永</span></div></a></div><div class="pics-box fl pics-last" data-href="https://v.qq.com/x/cover/zspj0kxmoeyrp44.html?videoMark="><div class="top"><img data-boss="vv_zongyi" data-url="https://v.qq.com/x/cover/zspj0kxmoeyrp44.html?videoMark=" src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-src="//puui.qpic.cn/vcover_hz_pic/0/zspj0kxmoeyrp441564547847/332" alt="极限青春" class="js_bigvideo" data-cid="zspj0kxmoeyrp44" data-cvid="t00314vnbiz" data-vid="g1905gry28m"><i class="icon-label icon-label-info icon-label-lb">2019-08-01 期</i><i class="icon-label icon-label-type icon-label-rt">自制</i></div><a href="https://v.qq.com/x/cover/zspj0kxmoeyrp44.html?videoMark=" target="_blank"><div class="info"><p class="vtitle over f16">极限青春</p><p class="comer over">王一博被陈乔恩追得满街跑</p><span class="watch over">嘉宾：王珞丹 陈乔恩 王一博</span></div></a></div></div></div>
          </div>
          <div id="js_zydir" bosszone="zongyi_more">
            <a href="javascript:;" class="prev icon disabled" data-rel="#js_zyCon_0"></a>
            <a href="javascript:;" class="next icon" data-rel="#js_zyCon_1"></a>
          </div>
        </div>
        <div id="js_bdysj" class="undis" bossexpo="bg_dsj">
          <div class="bdwrap">
            <div class="bd-inner cf" id="js_ysjCon"><div id="js_ysjCon_0" class="bd cf" bosszone="dsj_1" bossexpo="bg_dsj_1"><a class="video-boxv fl js_bigvideo" data-boss="vv_dsj" data-alt="加油，你是最棒的" data-cid="p19ym44r2sidp8p" data-cvid="d00310nqr06" data-vid="j19058runjq" href="javascript:;" data-href="https://v.qq.com/x/cover/p19ym44r2sidp8p.html"><img data-url="https://v.qq.com/x/cover/p19ym44r2sidp8p.html" src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-src="//i.gtimg.cn/qqlive/img/jpgcache/files/qqvideo/hori/p/p19ym44r2sidp8p_big.jpg" alt="加油，你是最棒的"><div class="txt"><span>加油，你是最棒的</span></div><i class="q-icons icon-play"></i><i class="icon-label icon-label-type icon-label-rt">VIP</i><i class="icon-label icon-label-info icon-label-rb"> 更新至10集 </i></a><div class="pics-box fl" data-href="https://v.qq.com/x/cover/mkdomuqy3y7xfz6.html"><div class="top"><img data-boss="vv_dsj" data-url="https://v.qq.com/x/cover/mkdomuqy3y7xfz6.html" src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-src="//i.gtimg.cn/qqlive/img/jpgcache/files/qqvideo/hori/m/mkdomuqy3y7xfz6_big.jpg" data-cvid="t00311piwht" alt="遗失的1/2[会员看下周]" class="js_bigvideo" data-cid="mkdomuqy3y7xfz6" data-vid="i19051pzicc"><i class="icon-label icon-label-info icon-label-lb">更新至10集</i><i class="icon-label icon-label-type icon-label-rt">VIP</i></div><a href="https://v.qq.com/x/cover/mkdomuqy3y7xfz6.html" target="_blank"><div class="info"><p class="vtitle over f16">遗失的1/2[会员看下周]</p><p class="comer over">陈玺安黄姵嘉共谱今夏恋曲</p><span class="watch over">主演：黄姵嘉 陈玺安 王家梁</span></div></a></div><div class="pics-box fl" data-href="https://v.qq.com/x/cover/xpu952oo5tr9yzl.html"><div class="top"><img data-boss="vv_dsj" data-url="https://v.qq.com/x/cover/xpu952oo5tr9yzl.html" src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-src="//i.gtimg.cn/qqlive/img/jpgcache/files/qqvideo/hori/x/xpu952oo5tr9yzl_big.jpg" data-cvid="t00310qju1r" alt="全职高手[会员抢先看]" class="js_bigvideo" data-cid="xpu952oo5tr9yzl" data-vid="b1905zvnfqx"><i class="icon-label icon-label-info icon-label-lb">更新至18集</i><i class="icon-label icon-label-type icon-label-rt">VIP</i></div><a href="https://v.qq.com/x/cover/xpu952oo5tr9yzl.html" target="_blank"><div class="info"><p class="vtitle over f16">全职高手[会员抢先看]</p><p class="comer over">杨洋江疏影共赴荣耀之路</p><span class="watch over">主演：杨洋 江疏影 赖雨濛</span></div></a></div><div class="pics-box fl" data-href="https://v.qq.com/x/cover/vbb35hm6m6da1wc.html"><div class="top"><img data-boss="vv_dsj" data-url="https://v.qq.com/x/cover/vbb35hm6m6da1wc.html" src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-src="//i.gtimg.cn/qqlive/img/jpgcache/files/qqvideo/hori/v/vbb35hm6m6da1wc_big.jpg" data-cvid="w0031s4gikk" alt="陈情令" class="js_bigvideo" data-cid="vbb35hm6m6da1wc" data-vid="p1905xku1s1"><i class="icon-label icon-label-info icon-label-lb">更新至40集</i><i class="icon-label icon-label-type icon-label-rt">VIP</i></div><a href="https://v.qq.com/x/cover/vbb35hm6m6da1wc.html" target="_blank"><div class="info"><p class="vtitle over f16">陈情令</p><p class="comer over">肖战王一博共闯侠义江湖</p><span class="watch over">主演：肖战 王一博 孟子义</span></div></a></div><div class="pics-box fl pics-last" data-href="https://v.qq.com/x/cover/ez00dy0uu12rc4j.html"><div class="top"><img data-boss="vv_dsj" data-url="https://v.qq.com/x/cover/ez00dy0uu12rc4j.html" src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-src="//i.gtimg.cn/qqlive/img/jpgcache/files/qqvideo/hori/e/ez00dy0uu12rc4j_big.jpg" data-cvid="b00318l66nt" alt="小欢喜[会员抢先看]" class="js_bigvideo" data-cid="ez00dy0uu12rc4j" data-vid="f1906nw4pgw"><i class="icon-label icon-label-info icon-label-lb">更新至10集</i><i class="icon-label icon-label-type icon-label-rt">VIP</i></div><a href="https://v.qq.com/x/cover/ez00dy0uu12rc4j.html" target="_blank"><div class="info"><p class="vtitle over f16">小欢喜[会员抢先看]</p><p class="comer over">黄磊海清携手带娃备战高考</p><span class="watch over">主演：黄磊 海清 陶虹</span></div></a></div></div><div id="js_ysjCon_1" class="bd cf undis" bosszone="dsj_2" bossexpo="bg_dsj_2"><a class="video-boxv fl js_bigvideo" data-boss="vv_dsj" data-alt="浅情人不知[会员抢先看]" data-cid="xpibrzkr0p8nl0i" data-cvid="l0031nzko16" data-vid="i19058lpcsc" href="javascript:;" data-href="https://v.qq.com/x/cover/xpibrzkr0p8nl0i.html"><img data-url="https://v.qq.com/x/cover/xpibrzkr0p8nl0i.html" src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-src="//i.gtimg.cn/qqlive/img/jpgcache/files/qqvideo/hori/x/xpibrzkr0p8nl0i_big.jpg" alt="浅情人不知"><div class="txt"><span>浅情人不知[会员抢先看]</span></div><i class="q-icons icon-play"></i><i class="icon-label icon-label-type icon-label-rt">VIP</i><i class="icon-label icon-label-info icon-label-rb"> 更新至28集 </i></a><div class="pics-box fl" data-href="https://v.qq.com/x/cover/215clyixyo03ydm.html"><div class="top"><img data-boss="vv_dsj" data-url="https://v.qq.com/x/cover/215clyixyo03ydm.html" src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-src="//i.gtimg.cn/qqlive/img/jpgcache/files/qqvideo/hori/2/215clyixyo03ydm_big.jpg" data-cvid="t0031h0aq58" alt="归还世界给你[首播]" class="js_bigvideo" data-cid="215clyixyo03ydm" data-vid="i1906elfgnr"><i class="icon-label icon-label-info icon-label-lb">更新至32集</i><i class="icon-label icon-label-type icon-label-rt">VIP</i></div><a href="https://v.qq.com/x/cover/215clyixyo03ydm.html" target="_blank"><div class="info"><p class="vtitle over f16">归还世界给你[首播]</p><p class="comer over">杨烁娜扎演绎时尚圈虐恋</p><span class="watch over">主演：杨烁 古力娜扎 徐正溪</span></div></a></div><div class="pics-box fl" data-href="https://v.qq.com/x/cover/a7fcajz5pwkp9w4.html"><div class="top"><img data-boss="vv_dsj" data-url="https://v.qq.com/x/cover/a7fcajz5pwkp9w4.html" src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-src="//i.gtimg.cn/qqlive/img/jpgcache/files/qqvideo/hori/a/a7fcajz5pwkp9w4_big.jpg" data-cvid="y0031qxd85e" alt="九州缥缈录" class="js_bigvideo" data-cid="a7fcajz5pwkp9w4" data-vid="f190533hpnm"><i class="icon-label icon-label-info icon-label-lb">更新至30集</i><i class="icon-label icon-label-type icon-label-rt">VIP</i></div><a href="https://v.qq.com/x/cover/a7fcajz5pwkp9w4.html" target="_blank"><div class="info"><p class="vtitle over f16">九州缥缈录</p><p class="comer over">刘昊然谱写乱世英雄录</p><span class="watch over">主演：刘昊然 宋祖儿 陈若轩</span></div></a></div><div class="pics-box fl" data-href="https://v.qq.com/x/cover/u3k8zgmqqrd0qnb.html"><div class="top"><img data-boss="vv_dsj" data-url="https://v.qq.com/x/cover/u3k8zgmqqrd0qnb.html" src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-src="//i.gtimg.cn/qqlive/img/jpgcache/files/qqvideo/hori/u/u3k8zgmqqrd0qnb_big.jpg" data-cvid="d00313z0uyr" alt="高塔公主[会员全集]" class="js_bigvideo" data-cid="u3k8zgmqqrd0qnb" data-vid="e1904kph1fh"><i class="icon-label icon-label-info icon-label-lb">更新至06集</i><i class="icon-label icon-label-type icon-label-rt">VIP</i></div><a href="https://v.qq.com/x/cover/u3k8zgmqqrd0qnb.html" target="_blank"><div class="info"><p class="vtitle over f16">高塔公主[会员全集]</p><p class="comer over">未婚女孩的飒爽人生</p><span class="watch over">主演：孟耿如 莫允雯 郑茵声</span></div></a></div><div class="pics-box fl pics-last" data-href="https://v.qq.com/x/cover/tl95gterhbffeve.html"><div class="top"><img data-boss="vv_dsj" data-url="https://v.qq.com/x/cover/tl95gterhbffeve.html" src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-src="//i.gtimg.cn/qqlive/img/jpgcache/files/qqvideo/hori/t/tl95gterhbffeve_big.jpg" data-cvid="h0031x14b7m" alt="时间都知道" class="js_bigvideo" data-cid="tl95gterhbffeve" data-vid="g1905sjhbtg"><i class="icon-label icon-label-info icon-label-lb">更新至41集</i><i class="icon-label icon-label-type icon-label-rt">VIP</i></div><a href="https://v.qq.com/x/cover/tl95gterhbffeve.html" target="_blank"><div class="info"><p class="vtitle over f16">时间都知道</p><p class="comer over">唐嫣窦骁回到过去重寻真爱</p><span class="watch over">主演：唐嫣 窦骁 杨烁</span></div></a></div></div></div>
          </div>
          <div id="js_ysjdir" bosszone="dsj_more">
            <a href="javascript:;" class="prev icon disabled" data-rel="#js_ysjCon_0"></a>
            <a href="javascript:;" class="next icon" data-rel="#js_ysjCon_1"></a>
          </div>
        </div>
        <div id="js_bdmv" class="undis" bossexpo="bg_dianying">
          <div class="bdwrap">
            <div class="bd-inner cf" id="js_mvCon"><div id="js_mvCon_0" class="bd cf" bosszone="dianying_1" bossexpo="bg_dianying_1"><a class="video-boxv fl js_bigvideo" data-boss="vv_dianying" data-alt="大漠悍刀行" data-cid="m6ay4xnj08wei9s" data-cvid="k00315wt3r3" data-vid="m19068li2s5" href="javascript:;" data-href="https://v.qq.com/x/cover/m6ay4xnj08wei9s.html"><img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-src="//i.gtimg.cn/qqlive/img/jpgcache/files/qqvideo/hori/m/m6ay4xnj08wei9s_big.jpg" alt="大漠悍刀行"><div class="txt"><span>大漠悍刀行</span></div><i class="q-icons icon-play"></i><i class="icon-label icon-label-type icon-label-rt">VIP</i></a><div class="pics-box fl" data-href="https://v.qq.com/x/cover/fgi913qjsxva0rw.html"><div class="top"><img data-boss="vv_dianying" data-url="https://v.qq.com/x/cover/fgi913qjsxva0rw.html" src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-src="//i.gtimg.cn/qqlive/img/jpgcache/files/qqvideo/hori/f/fgi913qjsxva0rw_big.jpg" data-cvid="y0031mja2xk" alt="未来机器城" class="js_bigvideo" data-cid="fgi913qjsxva0rw" data-vid="p19052gvyue"><i class="icon-label icon-label-type icon-label-rt">VIP</i><i class="icon-label icon-label-info icon-label-rb icon-label-point"><span class="no1">5</span>.9</i></div><a href="https://v.qq.com/x/cover/fgi913qjsxva0rw.html" target="_blank"><div class="info"><p class="vtitle over f16">未来机器城</p><p class="comer over">暖心机器人守护萝莉</p></div></a></div><div class="pics-box fl" data-href="https://v.qq.com/x/cover/o7w2szqpp8j7gvo.html"><div class="top"><img data-boss="vv_dianying" data-url="https://v.qq.com/x/cover/o7w2szqpp8j7gvo.html" src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-src="//i.gtimg.cn/qqlive/img/jpgcache/files/qqvideo/hori/o/o7w2szqpp8j7gvo_big.jpg" data-cvid="b0031ipfoou" alt="妖宴长安" class="js_bigvideo" data-cid="o7w2szqpp8j7gvo" data-vid="i19050clfx8"><i class="icon-label icon-label-type icon-label-rt">VIP</i></div><a href="https://v.qq.com/x/cover/o7w2szqpp8j7gvo.html" target="_blank"><div class="info"><p class="vtitle over f16">妖宴长安</p><p class="comer over">赵品霖带队热血捉妖</p><span class="watch over">主演：赵品霖 石雪婧 罗家英</span></div></a></div><div class="pics-box fl" data-href="https://v.qq.com/x/cover/hsfd6c75jbzpopi.html"><div class="top"><img data-boss="vv_dianying" data-url="https://v.qq.com/x/cover/hsfd6c75jbzpopi.html" src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-src="//i.gtimg.cn/qqlive/img/jpgcache/files/qqvideo/hori/h/hsfd6c75jbzpopi_big.jpg" data-cvid="n0031mh732d" alt="九龙不败" class="js_bigvideo" data-cid="hsfd6c75jbzpopi" data-vid="x1905gs5jbh"><i class="icon-label icon-label-type icon-label-rt">VIP</i><i class="icon-label icon-label-info icon-label-rb icon-label-point"><span class="no1">3</span>.1</i></div><a href="https://v.qq.com/x/cover/hsfd6c75jbzpopi.html" target="_blank"><div class="info"><p class="vtitle over f16">九龙不败</p><p class="comer over">张晋激战MMA拳王</p><span class="watch over">主演：张晋 安德森·席尔瓦 郑嘉颖</span></div></a></div><div class="pics-box fl pics-last" data-href="https://v.qq.com/x/cover/3hyu8aiwglyfpom.html"><div class="top"><img data-boss="vv_dianying" data-url="https://v.qq.com/x/cover/3hyu8aiwglyfpom.html" src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-src="//i.gtimg.cn/qqlive/img/jpgcache/files/qqvideo/hori/3/3hyu8aiwglyfpom_big.jpg" data-cvid="o0031qk617i" alt="真相漩涡" class="js_bigvideo" data-cid="3hyu8aiwglyfpom" data-vid="b1905fuatfe"><i class="icon-label icon-label-type icon-label-rt">VIP</i><i class="icon-label icon-label-info icon-label-rb icon-label-point"><span class="no1">5</span>.9</i></div><a href="https://v.qq.com/x/cover/3hyu8aiwglyfpom.html" target="_blank"><div class="info"><p class="vtitle over f16">真相漩涡</p><p class="comer over">警界老司机带你探案</p><span class="watch over">主演：皮尔斯·布鲁斯南 盖·皮尔斯 明妮·德里弗</span></div></a></div></div><div id="js_mvCon_1" class="bd cf undis" bosszone="dianying_2" bossexpo="bg_dianying_2"><a class="video-boxv fl js_bigvideo" data-boss="vv_dianying" data-alt="鼠胆英雄·独家纪录片" data-cid="ssjp4sps7189hzn" data-cvid="l0031w530jn" data-vid="m1905dqvzqf" href="javascript:;" data-href="https://v.qq.com/x/cover/ssjp4sps7189hzn.html"><img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-src="//i.gtimg.cn/qqlive/img/jpgcache/files/qqvideo/hori/s/ssjp4sps7189hzn_big.jpg" alt="《鼠胆英雄》腾讯视频独家纪录片"><div class="txt"><span>鼠胆英雄·独家纪录片</span></div><i class="q-icons icon-play"></i><i class="icon-label icon-label-type icon-label-rt">VIP</i></a><div class="pics-box fl" data-href="https://v.qq.com/x/cover/offiqxg9mhhbbqb.html"><div class="top"><img data-boss="vv_dianying" data-url="https://v.qq.com/x/cover/offiqxg9mhhbbqb.html" src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-src="//i.gtimg.cn/qqlive/img/jpgcache/files/qqvideo/hori/o/offiqxg9mhhbbqb_big.jpg" data-cvid="u0031cue2nl" alt="妈阁是座城" class="js_bigvideo" data-cid="offiqxg9mhhbbqb" data-vid="f1905onqq9w"><i class="icon-label icon-label-type icon-label-rt">VIP</i><i class="icon-label icon-label-info icon-label-rb icon-label-point"><span class="no1">5</span>.8</i></div><a href="https://v.qq.com/x/cover/offiqxg9mhhbbqb.html" target="_blank"><div class="info"><p class="vtitle over f16">妈阁是座城</p><p class="comer over">白百何达康揭秘澳门赌场</p><span class="watch over">主演：白百何 黄觉 吴刚</span></div></a></div><div class="pics-box fl" data-href="https://v.qq.com/x/cover/rncejht5q3dgv2p.html"><div class="top"><img data-boss="vv_dianying" data-url="https://v.qq.com/x/cover/rncejht5q3dgv2p.html" src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-src="//i.gtimg.cn/qqlive/img/jpgcache/files/qqvideo/hori/r/rncejht5q3dgv2p_big.jpg" data-cvid="f0031ee3xyp" alt="守卫恶魔镇" class="js_bigvideo" data-cid="rncejht5q3dgv2p" data-vid="o1905b96r6x"><i class="icon-label icon-label-type icon-label-rt">VIP</i></div><a href="https://v.qq.com/x/cover/rncejht5q3dgv2p.html" target="_blank"><div class="info"><p class="vtitle over f16">守卫恶魔镇</p><p class="comer over">东北捉妖师搭配硬核指环王</p><span class="watch over">主演：闫佩伦 于艺翎 蔡明凯</span></div></a></div><div class="pics-box fl" data-href="https://v.qq.com/x/cover/4o40lp5iyk0oynr.html"><div class="top"><img data-boss="vv_dianying" data-url="https://v.qq.com/x/cover/4o40lp5iyk0oynr.html" src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-src="//i.gtimg.cn/qqlive/img/jpgcache/files/qqvideo/hori/4/4o40lp5iyk0oynr_big.jpg" data-cvid="a0031p2a0ej" alt="锦衣卫之镇魂角" class="js_bigvideo" data-cid="4o40lp5iyk0oynr" data-vid="h1904u50gz8"><i class="icon-label icon-label-type icon-label-rt">VIP</i></div><a href="https://v.qq.com/x/cover/4o40lp5iyk0oynr.html" target="_blank"><div class="info"><p class="vtitle over f16">锦衣卫之镇魂角</p><p class="comer over">孙耀威破灭门惨案洗牌锦衣卫</p><span class="watch over">主演：孙耀威 李水诺 卢勇</span></div></a></div><div class="pics-box fl pics-last" data-href="https://v.qq.com/x/cover/9524p43l8i7w369.html"><div class="top"><img data-boss="vv_dianying" data-url="https://v.qq.com/x/cover/9524p43l8i7w369.html" src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-src="//i.gtimg.cn/qqlive/img/jpgcache/files/qqvideo/hori/9/9524p43l8i7w369_big.jpg" data-cvid="d00315lsw3s" alt="素人特工" class="js_bigvideo" data-cid="9524p43l8i7w369" data-vid="x1903x2qf22"><i class="icon-label icon-label-type icon-label-rt">VIP</i><i class="icon-label icon-label-info icon-label-rb icon-label-point"><span class="no1">3</span>.7</i></div><a href="https://v.qq.com/x/cover/9524p43l8i7w369.html" target="_blank"><div class="info"><p class="vtitle over f16">素人特工</p><p class="comer over">女战神米拉肉搏枪战A爆了</p><span class="watch over">主演：王大陆 张榕容 米拉·乔沃维奇</span></div></a></div></div></div>
          </div>
          <div id="js_mvdir" bosszone="dianying_more">
            <a href="javascript:;" class="prev icon disabled" data-rel="#js_mvCon_0"></a>
            <a href="javascript:;" class="next icon" data-rel="#js_mvCon_1"></a>
          </div>
        </div>
         <div id="js_bdchild" class="undis" bossexpo="bg_shaoer">
          <div class="bdwrap">
            <div class="bd-inner cf" id="js_childCon"><div id="js_childCon_0" class="bd cf" bosszone="shaoer_1" bossexpo="bg_shaoer_1"><a class="video-boxv fl js_bigvideo" data-boss="vv_shaoer" data-alt="跳跃战士2" data-cid="m09n5s7nfl5ohj4" data-cvid="h09046xmvi1" data-vid="" href="javascript:;" data-href="https://v.qq.com/x/cover/m09n5s7nfl5ohj4/h09046xmvi1.html"><img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-src="//puui.qpic.cn/tv/0/202834829_414230/0" alt="跳跃战士2"><div class="txt"><span>跳跃战士2</span></div><i class="q-icons icon-play"></i><i class="icon-label icon-label-info icon-label-rb"> 更新至10集 </i></a><div class="pics-box fl" data-href="https://v.qq.com/x/cover/edtnqi7acrqvltg/x0907ao92pa.html"><div class="top"><img data-boss="vv_shaoer" data-url="https://v.qq.com/x/cover/edtnqi7acrqvltg/x0907ao92pa.html" src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-src="//puui.qpic.cn/tv/0/198550596_414230/0" alt="跳跳鱼世界合集" class="js_bigvideo" data-cid="edtnqi7acrqvltg" data-cvid="x0907ao92pa" data-vid=""><i class="icon-label icon-label-info icon-label-lb"> 更新至185集 </i></div><a href="https://v.qq.com/x/cover/edtnqi7acrqvltg/x0907ao92pa.html" target="_blank"><div class="info"><p class="vtitle over f16">跳跳鱼世界合集</p><p class="comer over">足球比赛，友谊第一</p><span class="watch over">两条小鱼的搞笑日常</span></div></a></div><div class="pics-box fl" data-href="https://v.qq.com/x/cover/q9fcxubnjow4epa/f0907b1q0gt.html"><div class="top"><img data-boss="vv_shaoer" data-url="https://v.qq.com/x/cover/q9fcxubnjow4epa/f0907b1q0gt.html" src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-src="//puui.qpic.cn/tv/0/198175771_414230/0" alt="会说话的汤姆猫家族" class="js_bigvideo" data-cid="q9fcxubnjow4epa" data-cvid="f0907b1q0gt" data-vid="n1550t3hpdc"><i class="icon-label icon-label-info icon-label-lb"> 更新至220集 </i></div><a href="https://v.qq.com/x/cover/q9fcxubnjow4epa/f0907b1q0gt.html" target="_blank"><div class="info"><p class="vtitle over f16">会说话的汤姆猫家族</p><p class="comer over">汤姆猫英雄小队：巨型泡泡</p><span class="watch over">搞笑动物的日常</span></div></a></div><div class="pics-box fl" data-href="https://v.qq.com/x/cover/2v5gun8dtikhwn4/j0030239s5k.html"><div class="top"><img data-boss="vv_shaoer" data-url="https://v.qq.com/x/cover/2v5gun8dtikhwn4/j0030239s5k.html" src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-src="//puui.qpic.cn/tv/0/198580701_414230/0" alt="咖宝车神第一季" class="js_bigvideo" data-cid="2v5gun8dtikhwn4" data-cvid="j0030239s5k" data-vid="q1891jvgcd1"><i class="icon-label icon-label-info icon-label-lb"> 全26集 </i></div><a href="https://v.qq.com/x/cover/2v5gun8dtikhwn4/j0030239s5k.html" target="_blank"><div class="info"><p class="vtitle over f16">咖宝车神第一季</p><p class="comer over">咖宝合力抓捕肇事逃逸车</p><span class="watch over">房间里出现的变形酷车</span></div></a></div><div class="pics-box fl pics-last" data-href="https://v.qq.com/x/cover/hg8bvxwa5e7h224/x0907sxg1es.html"><div class="top"><img data-boss="vv_shaoer" data-url="https://v.qq.com/x/cover/hg8bvxwa5e7h224/x0907sxg1es.html" src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-src="//puui.qpic.cn/tv/0/198047779_414230/0" alt="豆乐国学小剧场" class="js_bigvideo" data-cid="hg8bvxwa5e7h224" data-cvid="x0907sxg1es" data-vid="i17051sg2t0"><i class="icon-label icon-label-info icon-label-lb"> 更新至57集 </i><i class="icon-label icon-label-type icon-label-rt">自制</i></div><a href="https://v.qq.com/x/cover/hg8bvxwa5e7h224/x0907sxg1es.html" target="_blank"><div class="info"><p class="vtitle over f16">豆乐国学小剧场</p><p class="comer over">亡羊补牢，未为迟也</p><span class="watch over">宝宝能看懂的趣味国学</span></div></a></div></div><div id="js_childCon_1" class="bd cf undis" bosszone="shaoer_2" bossexpo="bg_shaoer_2"><a class="video-boxv fl js_bigvideo" data-boss="vv_shaoer" data-alt="可可小爱公益教育剧合集" data-cid="8w7k0yan997qiii" data-cvid="l0904bk2l2q" data-vid="" href="javascript:;" data-href="https://v.qq.com/x/cover/8w7k0yan997qiii/l0904bk2l2q.html"><img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-src="//puui.qpic.cn/tv/0/193996659_414230/0" alt="可可小爱公益教育剧合集"><div class="txt"><span>可可小爱公益教育剧合集</span></div><i class="q-icons icon-play"></i><i class="icon-label icon-label-info icon-label-rb"> 更新至53集 </i></a><div class="pics-box fl" data-href="https://v.qq.com/x/cover/nnjrt62wfa51161/h0025tfnoeg.html"><div class="top"><img data-boss="vv_shaoer" data-url="https://v.qq.com/x/cover/nnjrt62wfa51161/h0025tfnoeg.html" src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-src="//puui.qpic.cn/tv/0/198583437_414230/0" alt="爆笑虫子合集" class="js_bigvideo" data-cid="nnjrt62wfa51161" data-cvid="h0025tfnoeg" data-vid="n17253fmn1c"><i class="icon-label icon-label-info icon-label-lb"> 全259集 </i><i class="icon-label icon-label-type icon-label-rt">VIP</i></div><a href="https://v.qq.com/x/cover/nnjrt62wfa51161/h0025tfnoeg.html" target="_blank"><div class="info"><p class="vtitle over f16">爆笑虫子合集</p><p class="comer over">茶水有神奇魔力！</p><span class="watch over">超治愈爆笑兄弟</span></div></a></div><div class="pics-box fl" data-href="https://v.qq.com/x/cover/hkck1i38yrhrqhy/y0901p221ad.html"><div class="top"><img data-boss="vv_shaoer" data-url="https://v.qq.com/x/cover/hkck1i38yrhrqhy/y0901p221ad.html" src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-src="//puui.qpic.cn/tv/0/188734663_414230/0" alt="汽车小镇" class="js_bigvideo" data-cid="hkck1i38yrhrqhy" data-cvid="y0901p221ad" data-vid=""><i class="icon-label icon-label-type icon-label-rt">VIP</i></div><a href="https://v.qq.com/x/cover/hkck1i38yrhrqhy/y0901p221ad.html" target="_blank"><div class="info"><p class="vtitle over f16">汽车小镇</p><p class="comer over">开心！得到了好朋友的帮助</p><span class="watch over">一起认识各种交通工具</span></div></a></div><div class="pics-box fl" data-href="https://v.qq.com/x/cover/wt0n3gu1mhj4yht/f0028m8lzob.html"><div class="top"><img data-boss="vv_shaoer" data-url="https://v.qq.com/x/cover/wt0n3gu1mhj4yht/f0028m8lzob.html" src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-src="//puui.qpic.cn/tv/0/185735489_414230/0" alt="猪猪侠之竞球小英雄合集" class="js_bigvideo" data-cid="wt0n3gu1mhj4yht" data-cvid="f0028m8lzob" data-vid="f1790gty72c"><i class="icon-label icon-label-info icon-label-lb"> 全78集 </i></div><a href="https://v.qq.com/x/cover/wt0n3gu1mhj4yht/f0028m8lzob.html" target="_blank"><div class="info"><p class="vtitle over f16">猪猪侠之竞球小英雄合集</p><p class="comer over">和外星队的较量</p><span class="watch over">勇往直前终极一战！</span></div></a></div><div class="pics-box fl pics-last" data-href="https://v.qq.com/x/cover/sdtpog35j7lqjv9/u0029zqmbsm.html"><div class="top"><img data-boss="vv_shaoer" data-url="https://v.qq.com/x/cover/sdtpog35j7lqjv9/u0029zqmbsm.html" src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-src="//puui.qpic.cn/tv/0/185735209_414230/0" alt="萌鸡小队合集" class="js_bigvideo" data-cid="sdtpog35j7lqjv9" data-cvid="u0029zqmbsm" data-vid=""><i class="icon-label icon-label-info icon-label-lb"> 全104集 </i></div><a href="https://v.qq.com/x/cover/sdtpog35j7lqjv9/u0029zqmbsm.html" target="_blank"><div class="info"><p class="vtitle over f16">萌鸡小队合集</p><p class="comer over">海螺壳里能听到大海的声音</p><span class="watch over">启迪小萌鸡，欢乐再延续！</span></div></a></div></div></div>
          </div>
          <div id="js_childdir" bosszone="shaoer_more">
            <a href="javascript:;" class="prev icon disabled" data-rel="#js_childCon_0"></a>
            <a href="javascript:;" class="next icon" data-rel="#js_childCon_1"></a>
          </div>
        </div>
        <div class="vplayer" style="display: none;">
          <div class="layer"></div>
          <div id="js_videoplayer">

          </div>
        </div>
      </div>
    </div>
    <!-- /综艺影视剧 -->

    <!-- 广告3 -->
    <div class="layout qq-gg gg-3 cf">
      <div class="col-1 fl">
        <!--NEW_QQCOM_N_Width3_div AD begin...."l=NEW_QQCOM_N_Width3&log=off"--><div id="NEW_QQCOM_N_Width3" style="width: 920px; height: 90px; display: block; position: relative; zoom: 1;" class="l_qq_com" adconfig_lview="l.qq.com" adconfig_charset="gbk" adconfig_lview_template="//l.qq.com/lview?c=www&amp;loc={loc}" oid="4993208" btoid="0" display="banner"><a href="https://c.l.qq.com/lclick?oid=4993208&amp;cid=3396498&amp;loc=NEW_QQCOM_N_Width3&amp;soid=m1vEkgAAXUjvJQDmkQR5+/F9AZLm&amp;click_data=dXNlcl9pbmZvPW9BRGptenc4RUI0PSZwYWdlX3R5cGU9MSZzc3A9MSZ1cF92ZXJzaW9uPVMxMDB8TDg2NiZzaT0xNTM0NTQ3Njk=&amp;index=1&amp;chl=478" target="_blank" style="display:block;cursor:pointer;width:920px;height:90px;background-image:url(//wa.gtimg.com/website/201907/cqca_NQNW_20190705100744338844.jpg);background-size:920px 90px;background-position:50% 50%;filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(src='//wa.gtimg.com/website/201907/cqca_NQNW_20190705100744338844.jpg',sizingMethod='scale');"></a><a class="absolute a_cover" href="https://c.l.qq.com/lclick?oid=4993208&amp;cid=3396498&amp;loc=NEW_QQCOM_N_Width3&amp;soid=m1vEkgAAXUjvJQDmkQR5+/F9AZLm&amp;click_data=dXNlcl9pbmZvPW9BRGptenc4RUI0PSZwYWdlX3R5cGU9MSZzc3A9MSZ1cF92ZXJzaW9uPVMxMDB8TDg2NiZzaT0xNTM0NTQ3Njk=&amp;index=1&amp;chl=478&amp;k=&amp;t=%E8%85%BE%E8%AE%AF%E9%A6%96%E9%A1%B5&amp;r=&amp;s=" target="_blank" rel="nofollow" style="position:absolute;width:920px;height:90px;left:0px;top:0px;cursor:pointer;z-index:10;background-color:#fff;filter:alpha(opacity=0);opacity:0;"></a><div style="position: absolute; left: 0px; bottom: 0px; width: 26px; height: 16px; z-index: 12; background-image: url(&quot;https://ra.gtimg.com/web/res/icon/leftbottom_new.png&quot;); background-position: right top; background-repeat: no-repeat no-repeat;"></div></div><!--NEW_QQCOM_N_Width3 AD end --><!--[if !IE]>|xGv00|70117f038d403ee9748b944e95631917<![endif]-->
      </div>
      <div class="col-2 fr">
        <!--NEW_QQCOM_N_button2_div AD begin...."l=NEW_QQCOM_N_button2&log=off"--><div id="NEW_QQCOM_N_button2" style="width: 440px; height: 90px; overflow: hidden; display: block; position: relative;" class="l_qq_com" adconfig_lview="l.qq.com" adconfig_charset="gbk" adconfig_lview_template="//l.qq.com/lview?c=www&amp;loc={loc}" oid="100" btoid="0" display="auto"><a href="http://users.qq.com" target="_blank" style="display:block;cursor:pointer;width:440px;height:90px;background-image:url(//ra.gtimg.com/web/default_fodders/qq/440x90_1.png);background-size:440px 90px;background-position:50% 50%;filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(src='//ra.gtimg.com/web/default_fodders/qq/440x90_1.png',sizingMethod='scale');"></a></div><!--NEW_QQCOM_N_button2 AD end --><!--[if !IE]>|xGv00|4cb6c87a1f60044c8b16c528842ef4da<![endif]-->
      </div>
    </div>
    <!-- /广告3 -->

    <!-- 军事/历史/文化佛学 -->
    <div class="layout qq-channel3col cf">
      <div class="col col-1">
        <div class="title">
          <a class="txt active" href="https://new.qq.com/ch/edu/" target="_blank" bosszone="jiaoyu_logo">教育</a>
        </div>
        <div bosszone="jiaoyu" bossexpo="bg_jiaoyu">
                    <div class="prt cf">
            <a href="https://new.qq.com/omn/20190806/20190806A05H9E00.html" target="_blank" class="picwrap"><img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-original="https://inews.gtimg.com/newsapp_ls/0/9941142569_580328/0" class="pic" alt="外教市场雷声滚滚，行业正规化需社会舆论和监督"></a>
            <div class="text">
              <a href="https://new.qq.com/omn/20190806/20190806A05H9E00.html" target="_blank">
                <p class="tit">外教市场雷声滚滚，行业正规化需社会舆论和监督</p>
              </a>
              <a class="from" href="https://new.qq.com/omn/20190806/20190806A05H9E00.html" target="_blank"><span class="author">蓝鲸教育</span></a>
            </div>
          </div>
          <ul class="txtArea">
                                                                        <li><a class="" href="https://new.qq.com/omn/20190806/20190806A065NA00.html" target="_blank">广东省发布外教管理通知，要求培训机构主动公示外教资料</a></li>
                                                                            <li><a class="" href="https://new.qq.com/omn/20190806/20190806A03CRI00.html" target="_blank">5元动画电影专场没观众，小县城孩子暑假都去了辅导班</a></li>
                                                                            <li><a class="" href="https://new.qq.com/omn/20190806/20190806A06OOB00.html" target="_blank">香港大学联招放榜 辅导机构：升学应以兴趣志向为先</a></li>
                                                                            <li><a class="" href="https://new.qq.com/omn/20190806/20190806A06JAM00.html" target="_blank">广州外教拍教师证与安全套叠放照片 校方辟谣</a></li>
                                                                            <li><a class="" href="https://new.qq.com/omn/20190806/20190806A051BQ00.html" target="_blank">高二成绩在400分左右，如何让自己在高三快速拔高成绩？</a></li>
                                                                    </ul><!--[if !IE]>|xGv00|c1a5c7141121de0108e7ff058a8ea0a0<![endif]-->
        </div>
      </div>
      <div class="col col-1">
        <div class="title" id="js_histitle">
          <a class="txt active" href="https://new.qq.com/ch/milite/" target="_blank" data-rel="#js_bdmil" bosszone="junshi_logo">军事</a>
          <span class="split"></span>
          <a class="txt" href="https://new.qq.com/omn/author/41" target="_blank" data-rel="#js_bdhis" bosszone="lishi_logo">历史</a>
        </div>
        <div class="bdwrap">
          <div class="bd" id="js_bdmil" bosszone="junshi" bossexpo="bg_junshi">
                      <div class="prt cf">
            <a href="https://new.qq.com/omn/20190806/20190806A0095R00.html" target="_blank" class="picwrap"><img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-original="https://inews.gtimg.com/newsapp_ls/0/9940412970_580328/0" class="pic" alt="突发！印度做出一项历史性决定！"></a>
            <div class="text">
              <a href="https://new.qq.com/omn/20190806/20190806A0095R00.html" target="_blank">
                <p class="tit">突发！印度做出一项历史性决定！</p>
              </a>
              <a class="from" href="https://new.qq.com/omn/20190806/20190806A0095R00.html" target="_blank"><span class="author">环球时报热点</span><span class="comment">358评</span></a>
            </div>
          </div>
          <ul class="txtArea">
                                                                        <li><a class="" href="https://new.qq.com/omn/20190806/20190806A02UIP00.html" target="_blank">“古巴五人组”成员：美国“复活”了冷战思维</a></li>
                                                                            <li><a class="" href="https://new.qq.com/omn/20190806/20190806A05M9Z00.html" target="_blank">奇闻！台军遗失20枚步枪子弹 翻遍营区竟藏在兵舍顶楼</a></li>
                                                                            <li><a class="" href="https://new.qq.com/omn/20190806/20190806A05B6600.html" target="_blank">俄一军火库爆炸 造成8人受伤 方圆20公里内的居民被疏散</a></li>
                                                                            <li><a class="q-icons icon-video" href="https://new.qq.com/omn/20190806/20190806A03ENY00.html" target="_blank">这项国际比赛，中国军人刷新了纪录！</a></li>
                                                                            <li><a class="" href="https://new.qq.com/omn/20190805/20190805A030CL00.html" target="_blank">美欲在亚洲部署中程导弹，分析指其盟友并不愿接受部署</a></li>
                                                                                                                                                                                                                                                    </ul><!--[if !IE]>|xGv00|f4bc4a880ffe606eb9a03650a9411032<![endif]-->
          </div>
          <div class="bd undis" id="js_bdhis" bosszone="lishi" bossexpo="bg_lishi">
                      <div class="prt cf">
            <a href="https://new.qq.com/omn/20190806/20190806A056WU00.html" target="_blank" class="picwrap"><img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-original="https://inews.gtimg.com/newsapp_ls/0/9941070766_580328/0" class="pic" alt="关于清宫四大奇案，你知道多少，最后一个最离谱"></a>
            <div class="text">
              <a href="https://new.qq.com/omn/20190806/20190806A056WU00.html" target="_blank">
                <p class="tit">关于清宫四大奇案，你知道多少，最后一个最离谱</p>
              </a>
              <a class="from" href="https://new.qq.com/omn/20190806/20190806A056WU00.html" target="_blank"><span class="author">以史为镜的背后</span></a>
            </div>
          </div>
          <ul class="txtArea">
                                                                        <li><a class="" href="https://new.qq.com/omn/20190805/20190805A0RR2X00.html" target="_blank">1700年的印度有多强大，人口是奥斯曼帝国5倍，波斯20倍</a></li>
                                                                            <li><a class="" href="https://new.qq.com/omn/20190806/20190806A062VO00.html" target="_blank">哪吒形象简史：曾经，我很凶！</a></li>
                                                                            <li><a class="" href="https://new.qq.com/omn/20190806/20190806A02VP900.html" target="_blank">宋朝皇帝有多惨？想买个熏笼还要写申请打报告，等大半个月</a></li>
                                                                            <li><a class="" href="https://new.qq.com/omn/20190806/20190806A032PL00.html" target="_blank">贾诩，三国真正最聪明的人，永远不说废话</a></li>
                                                                            <li><a class="" href="https://new.qq.com/omn/20190805/20190805A0BDTT00.html" target="_blank">诸葛亮战场上骂过四人，气死三个，只有他活了下来！</a></li>
                                                                    </ul><!--[if !IE]>|xGv00|92d3cb427dd93ff8bfb79e1f4eb4f020<![endif]-->
          </div>
        </div>
      </div>
      <div class="col col-1 col-last">
        <div class="title" id="js_title1">
          <a class="txt active" href="https://new.qq.com/ch/cul/" target="_blank" data-rel="#js_bdcul" bosszone="wenhua_logo">文化</a>
          <span class="split"></span>
          <a class="txt" href="https://new.qq.com/ch/cul_ru/" target="_blank" data-rel="#js_bdbud" bosszone="foxue_logo">新国风</a>
        </div>
        <div class="bdwrap">
          <div class="bd" id="js_bdcul" bosszone="wenhua" bossexpo="bg_wenhua">
                      <div class="prt cf">
            <a href="https://new.qq.com/omn/20190806/20190806A00GS200.html" target="_blank" class="picwrap"><img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-original="https://inews.gtimg.com/newsapp_ls/0/9941028941_580328/0" class="pic" alt="妻不如妾，贾琏敢去多姑娘家厮混，为什么不与平儿暗中行事"></a>
            <div class="text">
              <a href="https://new.qq.com/omn/20190806/20190806A00GS200.html" target="_blank">
                <p class="tit">妻不如妾，贾琏敢去多姑娘家厮混，为什么不与平儿暗中行事</p>
              </a>
              <a class="from" href="https://new.qq.com/omn/20190806/20190806A00GS200.html" target="_blank"><span class="author">君笺雅侃红楼</span></a>
            </div>
          </div>
          <ul class="txtArea">
                                                                        <li><a class="" href="https://new.qq.com/omn/20190806/20190806A05BI900.html" target="_blank">最强求不来的是爱情，最解释不来的也是爱情</a></li>
                                                                            <li><a class="" href="https://new.qq.com/omn/20190806/20190806A032N400.html" target="_blank">为什么做事要方，做人要圆？看后醍醐灌顶</a></li>
                                                                            <li><a class="" href="https://new.qq.com/omn/20190806/20190806A02MKA00.html" target="_blank">七夕：写给生命美丽的情书</a></li>
                                                                            <li><a class="" href="https://new.qq.com/omn/20190806/20190806A032NU00.html" target="_blank">如何有效管理情绪，决定了一个人的格局</a></li>
                                                                            <li><a class="" href="https://new.qq.com/omn/20190806/20190806A02MUJ00.html" target="_blank">相处，要懂得换位思考，将心比心</a></li>
                                                                    </ul><!--[if !IE]>|xGv00|c3d4f711a8477dad1d7466eb935c8d8a<![endif]-->
          </div>
          <div class="bd undis" id="js_bdbud" bosszone="foxue" bossexpo="bg_foxue">
                      <div class="prt cf">
            <a href="https://new.qq.com/omn/20190806/20190806A032M500.html" target="_blank" class="picwrap"><img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-original="https://inews.gtimg.com/newsapp_ls/0/9940348925_580328/0" class="pic" alt="余生，静而不争，也是一种难得的大智慧"></a>
            <div class="text">
              <a href="https://new.qq.com/omn/20190806/20190806A032M500.html" target="_blank">
                <p class="tit">余生，静而不争，也是一种难得的大智慧</p>
              </a>
              <a class="from" href="https://new.qq.com/omn/20190806/20190806A032M500.html" target="_blank"><span class="author">读史</span><span class="comment">7评</span></a>
            </div>
          </div>
          <ul class="txtArea">
                                                                        <li><a class="" href="https://new.qq.com/omn/20190806/20190806A0667D00.html" target="_blank">苏轼送给好友一幅字，却把自己贬到了海南……</a></li>
                                                                            <li><a class="" href="https://new.qq.com/omn/20190806/20190806A0665100.html" target="_blank">学书法，要打几年基本功？</a></li>
                                                                            <li><a class="" href="https://new.qq.com/omn/20190806/20190806A00S5T00.html" target="_blank">猪八戒当真比孙悟空弱？你错了，看看他们在福陵山打了多久</a></li>
                                                                            <li><a class="" href="https://new.qq.com/omn/20190806/20190806A03ILF00.html" target="_blank">江郎才未尽，别恨在人间，几人能解？</a></li>
                                                                            <li><a class="" href="https://new.qq.com/omn/20190806/20190806A032P700.html" target="_blank">幻想信小呆杨超越式的“锦鲤生活”？马祖：平常心是道</a></li>
                                                                    </ul><!--[if !IE]>|xGv00|42b7cc9f3289d4308eb0b4e1f0e77ed8<![endif]-->
          </div>
        </div>
      </div>
    </div>
    <!-- /军事/历史/文化佛学 -->

    <!-- 星座每日运势/游戏动漫/财报 -->
    <div class="layout qq-channel3col cf">
      <div class="col col-1">
        <div class="title" id="js_title2">
          <a class="txt active" href="http://astro.fashion.qq.com/" target="_blank" data-rel="#js_bdastro" bosszone="xingzuo_logo">星座</a>
          <span class="split"></span>
          <a class="txt" href="http://astro.fashion.qq.com/" target="_blank" data-rel="#js_bdfortune" bosszone="yunshi_logo">今日运势</a>
        </div>
        <div class="bdwrap bdwrapast">
          <div class="bd" id="js_bdastro" bosszone="xingzuo" bossexpo="bg_xingzuo">
                      <div class="prt cf">
            <a href="https://new.qq.com/rain/a/AST2019080500988900" target="_blank" class="picwrap"><img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-original="//img1.gtimg.com/ninja/2/2019/08/ninja156505663291934.png" class="pic" alt="李现面相揭秘：星运辉煌无人能及"></a>
            <div class="text">
              <a href="https://new.qq.com/rain/a/AST2019080500988900" target="_blank">
                <p class="tit">李现面相揭秘：星运辉煌无人能及</p>
              </a>
              <a class="from" href="https://new.qq.com/rain/a/AST2019080500988900" target="_blank"><span class="author">腾讯星座</span></a>
            </div>
          </div>
          <ul class="txtArea">
                                                                        <li><a class="" href="https://new.qq.com/rain/a/AST2019080500959300" target="_blank">8月咸鱼要翻身，一定要逆袭的星座</a></li>
                                                                            <li><a class="" href="https://new.qq.com/rain/a/AST2019080500959500" target="_blank">八月爱情运势最好的生肖！</a></li>
                                                                            <li><a class="" href="https://new.qq.com/rain/a/AST2019080500958300" target="_blank">处处争先，不喜欢落后于人的生肖</a></li>
                                                                            <li><a class="" href="https://new.qq.com/rain/a/AST2019080500960300" target="_blank">近一个月你身边的贵人星座，有你吗？</a></li>
                                                                            <li><a class="" href="https://astro.fashion.qq.com/original/constellationControl/xijing.html" target="_blank">12星座谁有“戏精病”？张弛有度，简直艺术家</a></li>
                                                                                                                                                                                                        </ul><!--[if !IE]>|xGv00|09346cbbff5e586ab8e4496c2f7f62d7<![endif]-->
          </div>
          <div class="undis col-astrobd" id="js_bdfortune" bosszone="yunshi" bossexpo="bg_yunshi">
            <div class="astop cf">
              <a class="asleft" href="https://new.qq.com/ch2/divination?name=shizizuo&amp;date=today" id="js_aimg" target="_blank"><span class="icon Leo" title="狮子座"></span><p class="name">狮子座</p></a>
              <div class="asright">
                <div class="asdesc" id="js_adetail"><div class="desc fortune"><span class="label">今日运势：</span><div class="fortune-star"><span class="bottom iconastro"></span><span class="top iconastro" style="width:63px;"></span></div></div><div class="desc luck"><span class="label">幸运颜色：青色</span></div><div class="desc lucknum"><span class="label">幸运数字：3</span></div></div>
                <div class="select">
                  <div class="selected iconastro" id="js_aselect">狮子座 07.23-08.22</div>
                  <ul class="list" id="js_aselectlist" style="display: none;">
                    <li class="astroItem" data-value="0">白羊座 03.21-04.19</li>
                    <li class="astroItem" data-value="1">金牛座 04.20-05.20</li>
                    <li class="astroItem" data-value="2">双子座 05.21-06.21</li>
                    <li class="astroItem" data-value="3">巨蟹座 06.22-07.22</li>
                    <li class="astroItem active" data-value="4">狮子座 07.23-08.22</li>
                    <li class="astroItem" data-value="5">处女座 08.23-09.22</li>
                    <li class="astroItem" data-value="6">天秤座 09.23-10.23</li>
                    <li class="astroItem" data-value="7">天蝎座 10.24-11.22</li>
                    <li class="astroItem" data-value="8">射手座 11.23-12.21</li>
                    <li class="astroItem" data-value="9">摩羯座 12.22-01.19</li>
                    <li class="astroItem" data-value="10">水瓶座 01.20-02.18</li>
                    <li class="astroItem" data-value="11">双鱼座 02.19-03.20</li>
                  </ul>
                </div>
              </div>
            </div>
            <p class="astxt" id="js_atxt">今天要注意防骗，不要参与钱财借贷或是投资。另外今天也要注意健康问题，依旧是肠胃和睡眠。今天最好是佛系生活，饮食也要保持清淡。<a class="label label-more" target="_blank" href="https://new.qq.com/ch2/divination?name=shizizuo&amp;date=today">详细</a></p>
            <ul class="txtArea">
                  <li><a class="" href="https://v.qq.com/x/cover/iqebkeresubhxp9/z05382y323g.html" target="_blank">苏珊·米勒：土星进入摩羯未来两年12星座运势</a></li>
                            <li><a class="" href="https://v.qq.com/x/cover/iqebkeresubhxp9/b0752jgrfvu.html" target="_blank">伦敦占星学院院长：2019年十二星座运势</a></li>
                            <li><a class="" href="https://v.qq.com/x/cover/iqebkeresubhxp9/v0800q34ojm.html" target="_blank">滴天居士2019年12生肖运势，谁万事顺利</a></li>
                            <li><a class="" href="https://v.qq.com/x/cover/iqebkeresubhxp9/z0815e67d9v.html" target="_blank">杨清华2019年五行运势详解，这些人财运滚滚来</a></li>
            </ul><!--ed514186dc00045074da9bacf3dcd775--><!--[if !IE]>|xGv00|0bf354d15086d62fcb1d75360f616c88<![endif]-->
          </div>
        </div>
      </div>
      <div class="col col-1">
        <div class="title" id="js_title3">
          <a class="txt active" href="https://new.qq.com/ch/games/" target="_blank" data-rel="#js_bdgame" bosszone="youxi_logo">游戏</a>
          <span class="split"></span>
          <a class="txt" href="https://new.qq.com/ch/comic/" target="_blank" data-rel="#js_bdcomic" bosszone="dongman_logo">动漫</a>
        </div>
        <div class="bdwrap">
          <div class="bd" id="js_bdgame" bosszone="youxi" bossexpo="bg_youxi">
                      <div class="prt cf">
            <a href="https://new.qq.com/omn/20190805/20190805A0QD0Q00.html" target="_blank" class="picwrap"><img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-original="https://inews.gtimg.com/newsapp_ls/0/9938065462_580328/0" class="pic" alt="前职业选手理解太可怕！Cat解说险些神预言登热搜"></a>
            <div class="text">
              <a href="https://new.qq.com/omn/20190805/20190805A0QD0Q00.html" target="_blank">
                <p class="tit">前职业选手理解太可怕！Cat解说险些神预言登热搜</p>
              </a>
              <a class="from" href="https://new.qq.com/omn/20190805/20190805A0QD0Q00.html" target="_blank"><span class="author">暴龙电竞</span></a>
            </div>
          </div>
          <ul class="txtArea">
                                                                        <li><a class="" href="https://new.qq.com/omn/20190805/20190805A0LFDL00.html" target="_blank">王者峡谷可爱担当，梦奇成功上榜，第一才是真正的卡哇伊！</a></li>
                                                                            <li><a class="" href="https://new.qq.com/omn/20190806/20190806A054ZS00.html" target="_blank">真有你的育碧！CJ展会穿模桌子加土豆，将自黑进行到底</a></li>
                                                                            <li><a class="" href="https://new.qq.com/omn/20190805/20190805A0P36M00.html" target="_blank">韩跑跑招牌韩信，力挽狂澜，即便再逆风也有翻盘的可能！</a></li>
                                                                            <li><a class="" href="https://new.qq.com/omn/20190806/20190806A05K6900.html" target="_blank">《第五人格》与《P5》联动形象发布 还原各角色特点！</a></li>
                                                                            <li><a class="" href="https://new.qq.com/omn/20190806/20190806A03F9800.html" target="_blank">DNF：首位普雷钝器剑宗诞生，团本遭受质疑，团长未必会放</a></li>
                                                                                                                </ul><!--[if !IE]>|xGv00|a52ab927e73dc7347b5bd0fa9c3a4e19<![endif]-->
          </div>
          <div class="bd undis" id="js_bdcomic" bosszone="dongman" bossexpo="bg_dongman">
                      <div class="prt cf">
            <a href="https://new.qq.com/omn/20190722/20190722A0LTGD00.html" target="_blank" class="picwrap"><img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-original="https://inews.gtimg.com/newsapp_ls/0/9809944143_580328/0" class="pic" alt="也许并不是给成年人看的18R动画——《灵笼》"></a>
            <div class="text">
              <a href="https://new.qq.com/omn/20190722/20190722A0LTGD00.html" target="_blank">
                <p class="tit">也许并不是给成年人看的18R动画——《灵笼》</p>
              </a>
              <a class="from" href="https://new.qq.com/omn/20190722/20190722A0LTGD00.html" target="_blank"><span class="author">动漫之家</span></a>
            </div>
          </div>
          <ul class="txtArea">
                                                                        <li><a class="" href="https://new.qq.com/omn/20190722/20190722A0MGSB00.html" target="_blank">泰迦奥特曼8月文字预告公开 光子大地形态蓄势待发</a></li>
                                                                            <li><a class="" href="https://new.qq.com/omn/ACF20190/ACF2019072200868300.html" target="_blank">BML2019梦幻嘉宾阵容 引爆燃情夏日</a></li>
                                                                            <li><a class="" href="https://new.qq.com/omn/20190722/20190722A0TFK600.html" target="_blank">一拳超人：希巴巴瓦婆婆的预言只是笑话吗？是我们想少了！</a></li>
                                                                            <li><a class="" href="https://new.qq.com/omn/20190722/20190722A0QAZM00.html" target="_blank">美杜莎女王要晋阶了！《斗破苍穹》第3季最终预告发布</a></li>
                                                                            <li><a class="" href="https://new.qq.com/omn/20190722/20190722A0MLUZ00.html" target="_blank">一之濑帆波两连冠！像会去援助交际的动画角色排行榜2019</a></li>
                                                                                          </ul><!--[if !IE]>|xGv00|1bb7a41b0d7ec541fc67e56f79c8035d<![endif]-->
          </div>
        </div>
      </div>
      <div class="col col-1 col-last col-tencent" bosszone="caibao" bossexpo="bg_caibao">
        <div class="title">
          <a class="txt active" href="https://www.tencent.com/zh-cn/company.html" target="_blank" bosszone="caibao_logo">财报</a>
        </div>
        <div bosszone="caibao">
                    <div class="prt cf">
            <a href="https://new.qq.com/cmsn/20190515/20190515006618.html" target="_blank" class="picwrap"><img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-original="//inews.gtimg.com/newsapp_ls/0/8968593168_640330/0" class="pic" alt="腾讯公布2019年第一季度业绩"></a>
            <div class="text">
              <a href="https://new.qq.com/cmsn/20190515/20190515006618.html" target="_blank">
                <p class="tit">腾讯公布2019年第一季度业绩</p>
              </a>
              <a class="from" href="https://new.qq.com/cmsn/20190515/20190515006618.html" target="_blank"><span class="author"></span></a>
            </div>
          </div>
      <ul class="txtArea">
																		<li><a href="https://new.qq.com/cmsn/20190321/20190321008183.html" target="_blank">腾讯公布2018年第四季度及全年业绩</a></li>
															<li><a href="https://new.qq.com/cmsn/20181114/20181114013100.html" target="_blank">腾讯公布2018年第三季度业绩</a></li>
															<li><a href="http://tech.qq.com/a/20180815/054575.htm" target="_blank">腾讯公布2018年第二季度及中期业绩</a></li>
															<li><a href="http://tech.qq.com/a/20180516/030778.htm" target="_blank">腾讯公布2018年第一季度业绩</a></li>
															<li><a href="http://tech.qq.com/a/20180321/030319.htm" target="_blank">腾讯公布2017年第四季度及全年业绩</a></li>
																					      </ul><!--611b1a5c49e08925ce742d9cdec9e50e--><!--[if !IE]>|xGv00|908d4a71a0068316e31cb1a8cbf8b037<![endif]-->
        </div>
      </div>
    </div>
    <!-- 星座每日运势/游戏动漫/财报 -->

    <!-- 高清组图 -->
    <div class="layout qq-pics">
  <div class="title">
    <a class="txt active" href="https://new.qq.com/ch/photo/" target="_blank" bosszone="gqzt_logo">高清组图</a>
  </div>
  <div class="mainbody">
    <div id="picDir" bosszone="gqzt_4">
      <a href="javascript:;" class="prev icon disabled" data-rel="#picUl1"></a>
      <a href="javascript:;" class="next icon" data-rel="#picUl2"></a>
    </div>
    <div class="wrap">
      <div class="wrapul cf" id="picWrap">
        <ul id="picUl1" class="wp-inner cf" bosszone="gqzt_1" bossexpo="bg_gqzt_1">
                                  <li class="item">
              <a href="https://new.qq.com/omn/20190806/20190806A04YZX00.html" class="p1t" target="_blank">
                                <img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-original="https://inews.gtimg.com/newsapp_ls/0/9941086242_580328/0" alt="俄举行“国际军事比赛-2019”，世界最好的坦克都来了">
                                <p>俄举行“国际军事比赛-2019”，世界最好的坦克都来了</p>
              </a>
            </li>
                                  <li class="item">
              <a href="https://new.qq.com/omn/20190805/20190805A099N700.html" class="p1t" target="_blank">
                                <img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-original="https://inews.gtimg.com/newsapp_ls/0/9940773823_580328/0" alt="银行职员从北京到贵州当第一书记 先学苗语和吃辣椒">
                                <p>银行职员从北京到贵州当第一书记 先学苗语和吃辣椒</p>
              </a>
            </li>
                                  <li class="item">
              <a href="https://new.qq.com/omn/20190805/20190805A0KVRK00.html" class="p1t" target="_blank">
                                <img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-original="https://inews.gtimg.com/newsapp_ls/0/9940160148_580328/0" alt="女儿靠呼吸机续命却遇停电，爸爸奔走全村向人借油发电">
                                <p>女儿靠呼吸机续命却遇停电，爸爸奔走全村向人借油发电</p>
              </a>
            </li>
                                  <li class="item">
              <a href="https://new.qq.com/omn/20190806/20190806A01W3M00.html" class="p1t" target="_blank">
                                <img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-original="https://inews.gtimg.com/newsapp_ls/0/9941166426_580328/0" alt="37岁的她高调挑战透视裙，网友：开挂式长开？">
                                <p>37岁的她高调挑战透视裙，网友：开挂式长开？</p>
              </a>
            </li>
                                  <li class="item">
              <a href="https://new.qq.com/omn/20190806/20190806A02TIV00.html" class="p1t" target="_blank">
                                <img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-original="https://inews.gtimg.com/newsapp_ls/0/9940317539_580328/0" alt="美国军人所见，五十年代后期的韩国">
                                <p>美国军人所见，五十年代后期的韩国</p>
              </a>
            </li>
                                  <li class="item item-last">
              <a href="https://new.qq.com/omn/20190806/20190806A01W4W00.html" class="p1t" target="_blank">
                                <img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-original="https://inews.gtimg.com/newsapp_ls/0/9941151755_580328/0" alt="罗晋的老婆唐嫣，她的美一直很真实">
                                <p>罗晋的老婆唐嫣，她的美一直很真实</p>
              </a>
            </li>
                                                  </ul><ul id="picUl2" class="wp-inner cf undis" bosszone="gqzt_2" bossexpo="bg_gqzt_2">
                        <li class="item">
              <a href="https://new.qq.com/omn/20190806/20190806A01W3000.html" class="p1t" target="_blank">
                                <img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-src="https://inews.gtimg.com/newsapp_ls/0/9941170999_580328/0" alt="顶着“初恋脸”现身机场，李沁私服也有小心机">
                                <p>顶着“初恋脸”现身机场，李沁私服也有小心机</p>
              </a>
            </li>
                                  <li class="item">
              <a href="https://new.qq.com/omn/20190806/20190806A02L8500.html" class="p1t" target="_blank">
                                <img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-src="https://inews.gtimg.com/newsapp_ls/0/9940181686_580328/0" alt="著名摄影师镜头下的“夏天”">
                                <p>著名摄影师镜头下的“夏天”</p>
              </a>
            </li>
                                  <li class="item">
              <a href="https://new.qq.com/omn/20190806/20190806A01W4R00.html" class="p1t" target="_blank">
                                <img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-src="https://inews.gtimg.com/newsapp_ls/0/9941154787_580328/0" alt="面对娱乐圈的黑暗，有些女星选择接受，有些明确拒绝">
                                <p>面对娱乐圈的黑暗，有些女星选择接受，有些明确拒绝</p>
              </a>
            </li>
                                  <li class="item">
              <a href="https://new.qq.com/omn/20190806/20190806A01VO400.html" class="p1t" target="_blank">
                                <img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-src="https://inews.gtimg.com/newsapp_ls/0/9941212168_580328/0" alt="陈妍希不再是曾经的小笼包，初恋脸其实就是普通脸？">
                                <p>陈妍希不再是曾经的小笼包，初恋脸其实就是普通脸？</p>
              </a>
            </li>
                                  <li class="item">
              <a href="https://new.qq.com/omn/20190806/20190806A04SF800.html" class="p1t" target="_blank">
                                <img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-src="https://inews.gtimg.com/newsapp_ls/0/9941081504_580328/0" alt="阿榕视角《浣溪沙》">
                                <p>阿榕视角《浣溪沙》</p>
              </a>
            </li>
                                  <li class="item item-last">
              <a href="https://new.qq.com/omn/20190806/20190806A041I800.html" class="p1t" target="_blank">
                                <img src="//mat1.gtimg.com/www/qq2018/imgs/default_b.png" data-src="https://inews.gtimg.com/newsapp_ls/0/9940986258_580328/0" alt="街拍：穿新潮牛仔裙的美女，新颖时尚">
                                <p>街拍：穿新潮牛仔裙的美女，新颖时尚</p>
              </a>
            </li>
                  </ul>
      </div>
    </div>
  </div>
</div><!--[if !IE]>|xGv00|7a19ec5344dbceefa81dce59c3b40035<![endif]-->
    <!-- /高清组图 -->

    <!-- 广告4 -->
    <div class="layout qq-gg gg-4">
      <!--NEW_QQCOM_N_Width4_div AD begin...."l=NEW_QQCOM_N_Width4&log=off"--><div id="NEW_QQCOM_N_Width4" style="width: 1400px; height: 90px; overflow: hidden; display: block; position: relative;" class="l_qq_com" adconfig_lview="l.qq.com" adconfig_charset="gbk" adconfig_lview_template="//l.qq.com/lview?c=www&amp;loc={loc}" oid="100" btoid="0" display="auto"><a href="https://news.qq.com/mobile/index.htm" target="_blank" style="display:block;cursor:pointer;width:1400px;height:90px;background-image:url(//ra.gtimg.com/web/default_fodders/1400x90_www.png);background-size:1400px 90px;background-position:50% 50%;filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(src='//ra.gtimg.com/web/default_fodders/1400x90_www.png',sizingMethod='scale');"></a></div><!--NEW_QQCOM_N_Width4 AD end --><!--[if !IE]>|xGv00|94450b939bcdbdc0162e34bb0afc868b<![endif]-->
    </div>
    <!-- /广告4 -->

    <!--NEW_WWW_RM_RightMove1_div AD begin...."l=NEW_WWW_RM_RightMove1&log=off"--><div id="NEW_WWW_RM_RightMove1" style="width:400px;height:300px;display:none;margin:0 auto;" class="l_qq_com" adconfig_lview="l.qq.com" adconfig_charset="gbk" adconfig_lview_template="//l.qq.com/lview?c=www&amp;loc={loc}" oid="1" btoid="0" display="null"></div><!--NEW_WWW_RM_RightMove1 AD end --><!--[if !IE]>|xGv00|3b2478b06ddfae7bab274578a3dec4fe<![endif]-->
    <!--NEW_QQ_Couplet_div AD begin...."l=NEW_QQ_Couplet&log=off"--><div id="NEW_QQ_Couplet" style="width:100px;height:300px;display:none;" class="l_qq_com" adconfig_lview="l.qq.com" adconfig_charset="gbk" adconfig_lview_template="//l.qq.com/lview?c=www&amp;loc={loc}" oid="1" btoid="0" display="null"></div><!--NEW_QQ_Couplet AD end --><!--[if !IE]>|xGv00|844ffa0b9793f349898d467df0e57173<![endif]-->

    <!-- 版权信息 -->
    <div class="layout qq-footer" bosszone="dibu" bossexpo="bg_dibu">
      <a href="http://www.tencent.com/" target="_blank" rel="nofollow">关于腾讯</a> | <a href="http://www.tencent.com/index_e.shtml" target="_blank" rel="nofollow">About Tencent</a> | <a href="http://www.qq.com/contract.shtml" target="_blank" rel="nofollow">服务协议</a>
      | <a href="https://privacy.qq.com/" target="_blank" rel="nofollow">隐私政策</a> | <a href="http://open.qq.com/" target="_blank" rel="nofollow">开放平台</a><!--  | <a href="http://www.tencentmind.com/" target="_blank" rel="nofollow">广告服务</a> -->
      | <a href="http://www.tencent.com/about/corp.shtml" target="_blank" rel="nofollow">商务洽谈</a> | <a href="http://hr.tencent.com/" target="_blank" rel="nofollow">腾讯招聘</a> | <a href="http://gongyi.qq.com/" target="_blank" rel="nofollow">腾讯公益</a>
      | <a href="http://kf.qq.com/" target="_blank" rel="nofollow">客服中心</a> | <a href="http://www.qq.com/map/" target="_blank" rel="nofollow">网站导航</a> | <a href="http://dldir1.qq.com/dlomg/qqcom/mini/QQNewsMini5.exe" rel="nofollow">客户端下载</a>
      | <a href="http://www.tencent.com/law/mo_law.shtml?/law/copyright.htm" target="_blank" rel="nofollow">版权所有</a><br>
      <a href="http://szwljb.gov.cn/" target="_blank" rel="nofollow">深圳举报中心</a> | <a href="http://ga.sz.gov.cn" target="_blank" rel="nofollow">深圳公安局</a> | <a href="http://www.qq.com/dzwfggcns.htm" target="_blank" rel="nofollow">抵制违法广告承诺书</a><!--  | <a class="lchot" href="http://www.gdis.cn/admin/newstext_netsun.asp" target="_blank" rel="nofollow">阳光·绿色网络工程</a> -->
      | <a href="http://www.qq.com/copyright.shtml" target="_blank" rel="nofollow">版权保护投诉指引</a> | <a href="https://gdca.miit.gov.cn/" target="_blank" rel="nofollow">广东省通管局</a><br>
      <span><a href="http://www.qq.com/culture.shtml" target="_blank" rel="nofollow">粤网文[2017]6138-1456号</a> <a href="http://www.qq.com/internet_licence.htm" target="_blank" rel="nofollow">新出网证（粤）字010号</a> <a href="http://www.qq.com/cbst.shtml" target="_blank" rel="nofollow">网络视听许可证1904073号</a>
        增值电信业务经营许可证：<a href="http://www.qq.com/icp.shtml" target="_blank" rel="nofollow">粤B2-20090059</a> <a href="http://www.qq.com/icp1.shtml" target="_blank" rel="nofollow">B2-20090028</a>
      </span><br>
      <a href="http://www.qq.com/scio.htm" target="_blank" rel="nofollow">新闻信息服务许可证</a> <a href="http://www.qq.com/xwdz.shtml" target="_blank" rel="nofollow">粤府新函[2001]87号</a> 违法和不良信息举报电话：0755-83765566-9 <a style="" target="_blank" href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=44030002000001"><span>粤公网安备
          44030002000001号</span></a><br>
      <a href="http://www.qq.com/spyp.htm" target="_blank">互联网药品信息服务资格证书 （粤）—非营业性—2017-0153</a><br>
      <span>Copyright  1998 - </span><span id="currentFullYear">2019</span> <span>Tencent. All Rights Reserved</span>
      <div class="footernew">
        <div class="footernewdiv">
        <p>
          <span class="fl"><a href="http://www.hd315.gov.cn/beian/view.asp?bianhao=0272000112400002" target="_blank" rel="nofollow"><img width="35" height="43" border="0" alt="经营性网站备案信息" src="//mat1.gtimg.com/www/images/qq2012/ind36.gif"></a></span>
          <span class="fr"><a target="_blank" class="lcblack" href="http://www.hd315.gov.cn/beian/view.asp?bianhao=0272000112400002" rel="nofollow">经营性网站<br>
          备案信息</a></span>
        </p>
        <p>
          <span style="width:44px;" class="fl"><a href="http://www.12377.cn/" target="_blank" rel="nofollow"><img width="44" height="44" border="0" alt="中国互联网举报中心" src="//mat1.gtimg.com/www/images/qq2012/buliang.png"></a></span>
          <span style="width:64px;" class="fr"><a class="lcblack" href="http://www.12377.cn/" target="_blank" rel="nofollow">中国互联网<br>
          举报中心</a></span>
        </p>
        <p>
          <span style="width:44px;" class="fl"><a href="http://www.wenming.cn" target="_blank" rel="nofollow"><img width="44" height="42" border="0" alt="中国文明网传播文明" src="//mat1.gtimg.com/www/images/qq2012/wmlogo.gif"></a></span>
          <span style="width:64px;" class="fr"><a class="lcblack" href="http://www.wenming.cn" target="_blank" rel="nofollow">中国文明网<br>传播文明</a></span>
        </p>
        <p style="width:128px;height:52px;border:0;">
          <span style="padding:0;" class="fl"><a href="https://ss.knet.cn/verifyseal.dll?sn=2010051300100001081&amp;ct=df&amp;a=1&amp;pa=337337" target="_blank" rel="nofollow"><img border="0" alt="诚信网站" src="//mat1.gtimg.com/www/images/qq2012/cxrz5.png"></a></span>
        </p>
        <p>
          <span style="width:44px;" class="fl"><a href="http://szcert.ebs.org.cn/6917b6fe-b844-4e12-97c5-85b8d1df30ed" target="_blank" rel="nofollow"><img src="//mat1.gtimg.com/www/images/qq2012/gswj2015.jpg" title="深圳市市场监督管理局企业主体身份公示" alt="深圳市市场监督管理局企业主体身份公示"></a></span>
          <span style="width:64px;" class="fr"><a class="lcblack" href="http://szcert.ebs.org.cn/6917b6fe-b844-4e12-97c5-85b8d1df30ed" target="_blank" rel="nofollow">工商网监<br>电子标识</a></span>
        </p>
        </div>  
      </div>
    </div>
    <script type="text/javascript">
      var currentFullYear = (new Date()).getFullYear();
      document.getElementById('currentFullYear').innerHTML = currentFullYear;
    </script><!--0ec88fdef34d4b10afc8fe4c76a1c9df--><!--[if !IE]>|xGv00|d05315842e25bfe687624695fa715ecd<![endif]-->
    <!-- /版权信息 -->

    <!-- 电梯 -->
    <div class="elevator" id="elevator" style="display: none;">
      <a href="javascript:" class="refresh fix" id="js_refresh" title="刷新" bosszone="shuaxin"><span class="icon"></span><br>刷新</a>
      <a href="https://support.qq.com/products/4312" target="_blank" class="feedback fix" title="用户反馈" bosszone="fankui">用户<br>反馈</a>
      <a href="javascript:void(0)" target="_self" class="backtop" id="js_gotop" title="返回顶部" bosszone="dingbu"><span class="icon"></span></a>
    </div>
    <!-- /电梯 -->

  </div>

  <!-- 视频弹层 -->
  <div id="pop-player" class="pop-player">
  <div class="inner">
    <div class="player-hd">
      <div id="video-pop" class="player-container"></div>
      <div class="tit"></div>
      <a class="close-btn" href="javascript:;">关闭</a>
    </div>
    <div class="player-ft cf">
      <div class="scroll-mod">
        <ul class="player-list cf"></ul>
        <a href="javascript:;" class="q-icons btn btn-left"></a>
        <a href="javascript:;" class="q-icons btn btn-right"></a>
      </div>
    </div>
  </div>
</div>

<div id="pop-player2" class="pop-player pop-player2">
  <div class="inner">
    <div class="player-hd">
      <div id="video-pop2" class="player-container"></div>
      <div class="tit"></div>
      <a class="close-btn" href="javascript:;">关闭</a>
      <div class="hd-info"></div>
    </div>
    <div class="player-ft cf">
      <div class="scroll-mod">
        <ul class="player-list cf"></ul>
      </div>
      <a href="javascript:;" class="q-icons btn btn-left"></a>
      <a href="javascript:;" class="q-icons btn btn-right"></a>
    </div>
  </div>
</div>

<div id="min-player" class="min-player">
  <div class="min-hd cf">
    <h2 class="tit fl"></h2>
    <a class="close-btn fr" href="javascript:;">关闭</a>
  </div>
  <div class="min-bd">
    <div id="video-min" class="player-container"></div>
  </div>
</div><!--ec4544fe058862e423cdc3225e110e49--><!--[if !IE]>|xGv00|6254f87b049c4c938babd0b80a015de3<![endif]-->
  <!-- /视频浮层 -->

  
  <script type="text/javascript">
  //<![CDATA[
  var serverTime = new Date(2019, 08-1, 06, 10, 58, 41);
  //]]>
  </script>
  <script src="//mat1.gtimg.com/www/asset/lib/jquery/jquery/jquery-1.11.1.min.js"></script>
  <script src="//vm.gtimg.cn/tencentvideo/txp/js/txplayer.js" charset="utf-8"></script>
  <script src="//mat1.gtimg.com/pingjs/ext2020/configF2017/5d09e4c5.js" charset="utf-8"></script>
  <script src="//mat1.gtimg.com/pingjs/ext2020/dc2017/publicjs/m/ping.js"></script>
	<script>if(typeof(pgvMain) == 'function')pgvMain();</script>
  <script src="//mat1.gtimg.com/pingjs/ext2020/qqindex2018/dist/js/qq_aef129e2.js" charset="utf-8"></script>

  <script type="text/javascript" src="//imgcache.qq.com/qzone/biz/comm/js/qbs.js"></script>
<script type="text/javascript">
var TIME_BEFORE_LOAD_CRYSTAL = (new Date).getTime();
</script>
<script src="//ra.gtimg.com/web/crystal/v4.7Beta04Build040/crystal-min.js" id="l_qq_com" arguments="{'extension_js_src':'//ra.gtimg.com/web/crystal/v4.7Beta04Build040/crystal_ext-min.js', 'jsProfileOpen':'false', 'mo_page_ratio':'0.01', 'mo_ping_ratio':'0.01', 'mo_ping_script':'//ra.gtimg.com/sc/mo_ping-min.js'}"></script>
<script type="text/javascript">
if(typeof crystal === 'undefined' && Math.random() <= 1) {
  (function() {
    var TIME_AFTER_LOAD_CRYSTAL = (new Date).getTime();
    var img = new Image(1,1);
    img.src = "//dp3.qq.com/qqcom/?adb=1&dm=www&err=1002&blockjs="+(TIME_AFTER_LOAD_CRYSTAL-TIME_BEFORE_LOAD_CRYSTAL);
  })();
}
</script>
<style>.absolute{position:absolute;}</style>
<!--[if !IE]>|xGv00|34ba8056fb38cac38d53027a9f08814a<![endif]-->

  <script>
  // 腾讯分析代码
  var _mtac = {};
  (function() {
      var mta = document.createElement("script");
      mta.src = "//pingjs.qq.com/h5/stats.js?v2.0.2";
      mta.setAttribute("name", "MTAH5");
      mta.setAttribute("sid", "500460529");
      var s = document.getElementsByTagName("script")[0];
      s.parentNode.insertBefore(mta, s);
  })();
  </script>



<svg class="_txplayer_svg_sprite txp_svg_sprite" display="none" version="1.1" xmlns="http://www.w3.org/2000/svg">   <symbol id="txp_svg_collect" viewBox="0 0 36 36">   <path d="M32.5 26H29v3.5a1.5 1.5 0 0 1-3 0V26h-3.5a1.5 1.5 0 1 1 0-3H26v-3.469a1.5 1.5 0 1 1 3 0V23h3.5a1.5 1.5 0 1 1 0 3zm.319-11.407c-.139.684-.716 1.209-1.442 1.209a1.5 1.5 0 0 1-1.5-1.5c0-.083.035-.154.048-.234l-.014-.002c.243-1.122.145-2.386-.598-3.584-.655-1.055-2.288-2.461-3.803-2.461-2.045 0-3.443.622-4.661 1.806l-3.358 3.182-3.485-3.207c-1.113-1.054-3.172-1.786-4.736-1.786-1.259 0-2.803.987-3.654 2.57-.975 1.809-.986 4.04.755 5.962l11.116 9.485.001-.001 1.015.928c.02.019.041.035.06.054l.004.004-.001.001c.256.269.419.629.419 1.03a1.5 1.5 0 0 1-1.5 1.5c-.435 0-.819-.191-1.093-.487L4.46 18.931c-3.285-3.209-3.285-8.357-.049-11.52C5.998 5.857 8.116 5 10.371 5c2.257 0 4.374.856 5.963 2.411l1.153 1.128 1.152-1.128C20.227 5.856 22.345 5 24.602 5c2.256 0 4.374.856 5.962 2.411a7.992 7.992 0 0 1 2.283 7.187l-.028-.005z"></path>  </symbol>  <symbol id="txp_svg_collected" viewBox="0 0 36 36">   <path d="M27 14.5a9.5 9.5 0 0 0-9.5 9.5c0 1.515.364 2.941.994 4.211l-1.507 1.28L3.96 18.431C.675 15.222.675 10.074 3.911 6.911 5.498 5.357 7.616 4.5 9.871 4.5c2.257 0 4.374.856 5.963 2.411l1.153 1.128 1.152-1.128C19.727 5.356 21.845 4.5 24.102 4.5c2.256 0 4.374.856 5.962 2.411a7.99 7.99 0 0 1 1.755 8.912A9.445 9.445 0 0 0 27 14.5zm0 2a7.5 7.5 0 1 1 0 15 7.5 7.5 0 0 1 0-15zm-4.042 9.485l1.811 1.81c.054.082.09.172.161.244a1.45 1.45 0 0 0 1.075.421 1.44 1.44 0 0 0 1.067-.418c.066-.066.097-.148.147-.222l3.851-3.851a1.463 1.463 0 1 0-2.069-2.07l-3.008 3.007-.978-.978a1.455 1.455 0 0 0-2.057 2.057z"></path>  </symbol>  <symbol id="txp_svg_share" viewBox="0 0 36 36">   <path d="M32.946 23.601l.023.009C30.694 29.675 24.86 34 18 34 9.163 34 2 26.837 2 18c0-6.095 3.42-11.372 8.435-14.072a1.48 1.48 0 0 1 .982-.387 1.5 1.5 0 0 1 1.5 1.5c0 .557-.317 1.023-.767 1.282l.032.064C7.927 8.523 5 12.915 5 18c0 7.18 5.82 13 13 13 5.577 0 10.319-3.518 12.165-8.45l.047.017c.154-.665.722-1.171 1.434-1.171a1.5 1.5 0 0 1 1.5 1.5c0 .26-.084.492-.2.705zM32 14.5a1.5 1.5 0 1 1-3 0V9.086l-9.455 9.455a1.498 1.498 0 0 1-2.117-2.117L26.852 7H21.5a1.5 1.5 0 0 1 0-3h8.929a1.47 1.47 0 0 1 .64.115c.546.224.931.758.931 1.385v9z"></path>  </symbol>  <symbol id="txp_svg_play" viewBox="0 0 36 36">   <path d="M25.8 18c0 .6-.3 1.1-.8 1.3L12.5 27c-.2.1-.5.2-.8.2-.8 0-1.5-.6-1.5-1.5V10c0-.8.7-1.5 1.5-1.5.3 0 .5.1.8.2l12.7 7.9c.4.5.6.9.6 1.4z"></path>  </symbol>  <symbol id="txp_svg_replay" viewBox="0 0 36 36">   <path d="M17.9 28c-4.9 0-9-3.6-9.8-8.3V19.4c0-.8.7-1.4 1.5-1.4s1.5.6 1.5 1.4c.8 3.8 4.5 6.2 8.3 5.4s6.2-4.5 5.4-8.3c-.7-3.2-3.5-5.6-6.9-5.6-1.8 0-3.6.7-4.8 2h1.3c.8 0 1.5.7 1.5 1.5s-.6 1.6-1.5 1.6h-4c-.8 0-1.5-.7-1.5-1.5v-4c0-.8.7-1.5 1.5-1.5.7 0 1.2.5 1.4 1.1C13.6 8.7 15.7 8 17.9 8c5.5 0 10 4.5 10 10s-4.4 10-10 10z"></path>  </symbol>  <symbol id="txp_svg_pause" viewBox="0 0 36 36">         <path d="M12 9h1c.6 0 1 .4 1 1v16c0 .6-.4 1-1 1h-1c-.6 0-1-.4-1-1V10c0-.6.4-1 1-1zm11 0h1c.6 0 1 .4 1 1v16c0 .6-.4 1-1 1h-1c-.6 0-1-.4-1-1V10c0-.6.4-1 1-1z"></path>     </symbol>  <symbol id="txp_svg_search" viewBox="0 0 24 24">         <path d="M19.4 17.2L17.2 15c0.8-1.1 1.3-2.5 1.3-4 0-3.9-3.1-7-7-7s-7 3.1-7 7 3.1 7 7 7c1.5 0 2.8-0.4 3.9-1.2l2.2 2.2c0.5 0.5 1.3 0.5 1.8 0S19.9 17.7 19.4 17.2zM6.5 11c0-2.8 2.2-5 5-5s5 2.2 5 5 -2.2 5-5 5S6.5 13.8 6.5 11z"></path>     </symbol>  <symbol id="svg_icon_refresh" viewBox="0 0 20 20">   <path d="M10 19a9 9 0 0 1-9-8.999V10a1 1 0 1 1 2 0 7 7 0 1 0 7-7 6.952 6.952 0 0 0-4.877 2H7a1 1 0 0 1 0 2H3a1 1 0 0 1-1-1V2a1 1 0 0 1 2 0v1.314A8.935 8.935 0 0 1 10 1c4.971 0 9 4.029 9 9s-4.029 9-9 9z"></path>  </symbol>  <symbol id="txp_svg_next" viewBox="0 0 36 36">         <path d="M26 9h1c.6 0 1 .4 1 1v16c0 .6-.4 1-1 1h-1c-.6 0-1-.4-1-1V10c0-.6.4-1 1-1zm-14.8 1.3l9.2 6.6c.6.4.8 1.3.3 2-.1.1-.2.3-.3.3l-9.2 6.6c-.6.4-1.5.3-1.9-.3-.2-.3-.3-.6-.3-.9V11.4c0-.8.6-1.4 1.4-1.4.3 0 .6.1.8.3z"></path>     </symbol>     <symbol id="txp_svg_stop" viewBox="0 0 36 36">         <path d="M24 26H12c-1.1 0-2-0.9-2-2V12c0-1.1 0.9-2 2-2h12c1.1 0 2 0.9 2 2v12C26 25.1 25.1 26 24 26z"></path>     </symbol>  <symbol id="txp_svg_shop" viewBox="0 0 24 24">   <path d="M18 13.836V14H8.793l-.552 2H18a2 2 0 1 1-2 2c0-.368.106-.707.278-1H8.722c.172.294.278.633.278 1a2 2 0 1 1-2-2h.206l.552-2H7v-.223L5.34 5H3V4h3v.01L6.147 4l.377 2H20v1h-.206L18 13.835zM18 19a1 1 0 1 0 0-2 1 1 0 0 0 0 2zM7 17a1 1 0 1 0 0 1.998 1 1 0 0 0 0-2zM6.714 7l1.134 6h9.357l1.575-6H6.714z"></path>  </symbol>  <symbol id="txp_svg_eye" viewBox="0 0 24 24">   <path d="M12 18c-5.468 0-9-6-9-6s3.533-6 9-6c5.467 0 9 6 9 6s-3.533 6-9 6zm0-11c-5.033 0-8 5-8 5s2.967 5 8 5c5.033 0 8-5 8-5s-2.967-5-8-5zm0 8a3 3 0 1 1 0-6 3 3 0 0 1 0 6zm0-5a2 2 0 1 0 0 3.998 2 2 0 0 0 0-4z"></path>  </symbol>  <symbol id="txp_svg_volume" viewBox="0 0 20 20">         <path d="M16.714 15.593l-.01-.01a1 1 0 0 1-1.705-.708c0-.287.124-.542.317-.724C16.354 13.073 17 11.614 17 10s-.645-3.072-1.682-4.151A.993.993 0 0 1 15 5.125a1 1 0 0 1 1-1c.3 0 .561.139.744.348l.017-.016A7.969 7.969 0 0 1 19 10c0 2.178-.874 4.15-2.286 5.593zm-3.999 3.122a.956.956 0 0 1-.688.28c-.009 0-.018.005-.027.005a.984.984 0 0 1-.75-.357L5.818 15H2a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1h3.818l5.432-3.643A.984.984 0 0 1 12 1c.009 0 .017.005.026.005a.954.954 0 0 1 .968.967c.001.01.006.018.006.028v16c0 .009-.005.017-.005.026a.959.959 0 0 1-.28.689zM6.75 6.643A.984.984 0 0 1 6 7H3v6h3c.304 0 .567.143.75.357l4.25 2.85V3.792L6.75 6.643z"></path>     </symbol>  <symbol id="txp_svg_volume_mute" viewBox="0 0 20 20">   <path d="M16.394 12.566A5.88 5.88 0 0 0 17 10a5.97 5.97 0 0 0-1.682-4.151.993.993 0 0 1-.318-.724 1 1 0 0 1 1-1c.3 0 .561.139.745.348l.016-.016A7.969 7.969 0 0 1 19 10a7.934 7.934 0 0 1-1.116 4.055l-1.49-1.489zM11 3.792L8.978 5.149 7.62 3.792l3.63-2.435A.984.984 0 0 1 12 1c.009 0 .017.005.026.005a.954.954 0 0 1 .968.967c.001.01.006.018.006.028v7.171l-2-2V3.792zm7.864 14.072a.999.999 0 0 1-1.414 0L2.136 2.55a1 1 0 1 1 1.415-1.415L18.864 16.45a1 1 0 0 1 0 1.414zM3.171 5l2 2H3v6h3c.304 0 .567.143.75.357l4.25 2.85v-3.379l2 2V18c0 .009-.005.017-.005.027a.955.955 0 0 1-.967.968c-.01 0-.019.005-.028.005a.984.984 0 0 1-.75-.357L5.818 15H2a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1h1.171z"></path>  </symbol>   <symbol id="txp_svg_setting" viewBox="0 0 24 24">   <path d="M21 11v2l-2 1v-.3c-.2.7-.5 1.5-.9 2.1l.2-.2.7 2.1-1.4 1.4-2.1-.7.2-.2c-.7.4-1.4.7-2.1.9h.4l-1 2h-2l-1-2h.3c-.7-.2-1.5-.5-2.1-.9l.2.2-2.1.7-1.4-1.4.7-2.1.2.2c-.4-.7-.7-1.4-.9-2.1v.3l-2-1v-2l2-1v.4c.2-.8.5-1.6 1-2.3l-.3.4-.7-2.2 1.4-1.4 2.1.7-.3.4c.7-.5 1.5-.8 2.3-1H10l1-2h2l1 2h-.4c.8.2 1.6.5 2.3.9l-.3-.3 2.1-.7 1.4 1.4-.7 2.1-.3-.3c.4.7.7 1.4.9 2.2V10l2 1zm-9-4c-2.8 0-5 2.2-5 5s2.2 5 5 5 5-2.2 5-5-2.2-5-5-5z"></path>  </symbol>  <symbol id="txp_svg_bulb" viewBox="0 0 24 24">   <path d="M15 16.317V17c0 .186-.065.35-.153.5.088.15.153.313.153.5v2a1 1 0 0 1-1 1h-4a1 1 0 0 1-1-1v-2c0-.186.064-.35.153-.5A.97.97 0 0 1 9 17v-.683A6.994 6.994 0 0 1 5 10a7 7 0 0 1 14 0 6.994 6.994 0 0 1-4 6.317zM10 20h4v-2h-4v2zm2-16a6 6 0 0 0-6 6c0 2.215 1.214 4.128 3 5.167V15c.452.36 1 .593 1 .593V17h4v-1.5s.462-.096 1-.5v.167c1.786-1.04 3-2.953 3-5.167a6 6 0 0 0-6-6z"></path>  </symbol>  <symbol id="txp_svg_window" viewBox="0 0 24 24">   <path d="M19 16H9a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h10a1 1 0 0 1 1 1v10a1 1 0 0 1-1 1zm0-11H9v10h10V5zM5 19h10v-2h1v2a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V9a1 1 0 0 1 1-1h2v1H5v10z"></path>  </symbol>  <symbol id="txp_svg_size_true" viewBox="0 0 24 24">   <path d="M20 19H4c-.6 0-1-.4-1-1V6c0-.6.4-1 1-1h16c.6 0 1 .4 1 1v12c0 .6-.4 1-1 1zM5 7v10h14V7H5z"></path>  </symbol>  <symbol id="txp_svg_size" viewBox="0 0 24 24">   <path d="M20 19H4c-.6 0-1-.4-1-1V6c0-.6.4-1 1-1h16c.6 0 1 .4 1 1v12c0 .6-.4 1-1 1zM5 17h10V7H5v10zM19 7h-2v10h2V7z"></path>  </symbol>  <symbol id="txp_svg_fake" viewBox="0 0 24 24">   <path d="M20 20H4c-.6 0-1-.4-1-1V5c0-.6.4-1 1-1h16c.6 0 1 .4 1 1v14c0 .6-.4 1-1 1zM5 6v12h14V6H5zm12 11h-2c-.6 0-1-.4-1-1s.4-1 1-1h1v-1c0-.6.4-1 1-1s1 .4 1 1v2c0 .6-.4 1-1 1zm0-6c-.6 0-1-.4-1-1V9h-1c-.6 0-1-.4-1-1s.4-1 1-1h2c.6 0 1 .4 1 1v2c0 .6-.4 1-1 1zm-8 6H7c-.6 0-1-.4-1-1v-2c0-.6.4-1 1-1s1 .4 1 1v1h1c.6 0 1 .4 1 1s-.4 1-1 1zm0-8H8v1c0 .6-.4 1-1 1s-1-.4-1-1V8c0-.6.4-1 1-1h2c.6 0 1 .4 1 1s-.4 1-1 1z"></path>  </symbol>  <symbol id="txp_svg_fake_true" viewBox="0 0 24 24">   <path d="M20 20H4c-.6 0-1-.4-1-1V5c0-.6.4-1 1-1h16c.6 0 1 .4 1 1v14c0 .6-.4 1-1 1zM5 6v12h14V6H5zm12 9h-1v1c0 .6-.4 1-1 1s-1-.4-1-1v-2c0-.6.4-1 1-1h2c.6 0 1 .4 1 1s-.4 1-1 1zm0-4h-2c-.6 0-1-.4-1-1V8c0-.6.4-1 1-1s1 .4 1 1v1h1c.6 0 1 .4 1 1s-.4 1-1 1zm-8 6c-.6 0-1-.4-1-1v-1H7c-.6 0-1-.4-1-1s.4-1 1-1h2c.6 0 1 .4 1 1v2c0 .6-.4 1-1 1zm0-6H7c-.6 0-1-.4-1-1s.4-1 1-1h1V8c0-.6.4-1 1-1s1 .4 1 1v2c0 .6-.4 1-1 1z"></path>  </symbol>  <symbol id="txp_svg_fullscreen" viewBox="0 0 24 24">   <path d="M19.7 19.7c-.2.2-.5.3-.7.3h-4c-.6 0-1-.4-1-1s.4-1 1-1h1.6l-3.3-3.3c-.4-.4-.3-1.1.1-1.4.4-.4 1-.4 1.4 0l3.3 3.3V15c0-.6.4-1 1-1s1 .4 1 1v4c-.1.2-.2.5-.4.7zM19 10c-.6 0-1-.4-1-1V7.4l-3.3 3.3c-.4.4-1 .4-1.4 0-.4-.4-.4-1 0-1.4L16.6 6H15c-.6 0-1-.4-1-1s.4-1 1-1h4c.3 0 .5.1.7.3.2.2.3.5.3.7v4c0 .6-.4 1-1 1zM7.4 18H9c.6 0 1 .4 1 1s-.4 1-1 1H5c-.3 0-.5-.1-.7-.3-.2-.2-.3-.5-.3-.7v-4c0-.6.4-1 1-1s1 .4 1 1v1.6l3.3-3.3c.4-.4 1.1-.3 1.4.1.4.4.4 1 0 1.4L7.4 18zm1.9-7.3L6 7.4V9c0 .6-.4 1-1 1s-1-.4-1-1V5c0-.3.1-.5.3-.7.2-.2.5-.3.7-.3h4c.6 0 1 .4 1 1s-.4 1-1 1H7.4l3.3 3.3c.4.4.4 1 0 1.4-.4.4-1 .4-1.4 0z"></path>  </symbol>  <symbol id="txp_svg_fullscreen_true" viewBox="0 0 24 24">   <path d="M16.4 9H18c.6 0 1 .4 1 1s-.4 1-1 1h-4c-.3 0-.5-.1-.7-.3-.2-.2-.3-.5-.3-.7V6c0-.6.4-1 1-1s1 .4 1 1v1.6l3.3-3.3c.4-.4 1.1-.3 1.4.1.4.4.4 1 0 1.4L16.4 9zM10 19c-.6 0-1-.4-1-1v-1.6l-3.3 3.3c-.4.4-1 .4-1.4 0-.4-.4-.4-1 0-1.4L7.6 15H6c-.6 0-1-.4-1-1s.4-1 1-1h4c.3 0 .5.1.7.3.2.2.3.5.3.7v4c0 .5-.4 1-1 1zm0-8H6c-.6 0-1-.4-1-1s.4-1 1-1h1.6L4.3 5.7c-.4-.4-.4-1 .1-1.4.4-.4 1-.4 1.4 0L9 7.6V6c0-.6.4-1 1-1s1 .4 1 1v4c0 .3-.1.5-.3.7-.2.2-.5.3-.7.3zm4 2h4c.6 0 1 .4 1 1s-.4 1-1 1h-1.6l3.3 3.3c.4.4.4 1 0 1.4s-1 .4-1.4 0L15 16.4V18c0 .6-.4 1-1 1s-1-.4-1-1v-4c0-.3.1-.5.3-.7.2-.2.5-.3.7-.3z"></path>  </symbol>  <symbol id="txp_svg_select" viewBox="0 0 12 12">   <path d="M6 12c-3.3 0-6-2.7-6-6s2.7-6 6-6 6 2.7 6 6-2.7 6-6 6zM6 .9C3.2.9.9 3.2.9 6s2.3 5.1 5.1 5.1 5.1-2.3 5.1-5.1S8.8.9 6 .9z"></path>  </symbol>  <symbol id="txp_svg_select_true" viewBox="0 0 12 12">   <path d="M6 12c-3.3 0-6-2.7-6-6s2.7-6 6-6 6 2.7 6 6-2.7 6-6 6zM6 .9C3.2.9.9 3.2.9 6s2.3 5.1 5.1 5.1 5.1-2.3 5.1-5.1S8.8.9 6 .9zm-.3 7.4c-.3.3-.8.3-1.2 0L2.8 6.6c-.3-.3-.3-.8 0-1.2.3-.3.8-.3 1.2 0l1.2 1.2L8 3.7c.3-.3.8-.3 1.2 0 .3.3.3.8 0 1.2L5.7 8.3z"></path>  </symbol>  <symbol id="txp_svg_link" viewBox="0 0 36 36">   <path d="M26.5 26h-5c-.8 0-1.5-.7-1.5-1.5s.7-1.5 1.5-1.5h5c2.5 0 4.5-2 4.5-4.5S29 14 26.5 14h-5c-.8 0-1.5-.7-1.5-1.5s.7-1.5 1.5-1.5h5c4.1 0 7.5 3.4 7.5 7.5S30.6 26 26.5 26zM12 18.5c0-.8.7-1.5 1.5-1.5h9c.8 0 1.5.7 1.5 1.5s-.7 1.5-1.5 1.5h-9c-.8 0-1.5-.7-1.5-1.5zm2.5-4.5h-5C7 14 5 16 5 18.5S7 23 9.5 23h5c.8 0 1.5.7 1.5 1.5s-.7 1.5-1.5 1.5h-5C5.4 26 2 22.6 2 18.5S5.4 11 9.5 11h5c.8 0 1.5.7 1.5 1.5s-.7 1.5-1.5 1.5z"></path>  </symbol>  <symbol id="txp_svg_icon_like" viewBox="0 0 20 20">   <path d="M18.4 8.5l-2 9.4c-0.2 0.6-0.2 1.1-0.6 1.3 -0.4 0.3-1 0.2-1.9 0.2 -2.9 0-10.4 0-10.4 0l0-12 2.1-5c0 0 0.6-2 1.7-2 1.4 0 1.2 2 1.2 2s0 1.3 0 3c0 0.7 0.2 1 1 1 6.5 0 6.9 0 6.9 0 0 0 0 0 0 0 0 0 0 0 0 0 0.5 0 1.6-0.2 1.9 0.5C18.5 7.4 18.6 7.9 18.4 8.5zM1.5 19.5c-0.6 0-1-0.4-1-1v-10c0-0.6 0.4-1 1-1s1 0.4 1 1v10C2.5 19.1 2.1 19.5 1.5 19.5z"></path>  </symbol>  <symbol id="txp_svg_loop" viewBox="0 0 36 36">         <path d="M13 13h8l-3-3-.8-.8c-.1-.1-.3-.2-.4-.2h-.5c-.2 0-.3.1-.3.3V11h-3c-2.8 0-5 2.2-5 5v4c0 2.4 1.7 4.4 4 4.9v-2.1c-1.2-.4-2-1.5-2-2.8v-4c0-1.7 1.3-3 3-3zm11-1.9v2.1c1.2.4 2 1.5 2 2.8v4c0 1.7-1.3 3-3 3h-8l3.1 3.1.8.8c.1.1.3.2.4.2h.5c.2 0 .3-.1.3-.3V25h3c2.8 0 5-2.2 5-5v-4c-.1-2.4-1.8-4.4-4.1-4.9z"></path>     </symbol>   <symbol id="txp_svg_loop_off" viewBox="0 0 36 36">         <path d="M16 11V9.3c0-.2.1-.3.3-.3h.5c.2 0 .3.1.4.2L21 13h-8c-1.7 0-3 1.3-3 3v4c0 1.7 1.3 3 3 3h1v2h-1c-2.8 0-5-2.2-5-5v-4c0-2.8 2.2-5 5-5h3zm4.1 11.2l2.8 2.8c.2.3.2.7 0 .9-.3.2-.7.2-.9 0l-2.8-2.8c-.2-.3-.2-.7 0-.9.3-.2.7-.2.9 0zM21 19c2.8 0 5 2.2 5 5s-2.2 5-5 5-5-2.2-5-5 2.2-5 5-5zm0 9c2.2 0 4-1.8 4-4s-1.8-4-4-4-4 1.8-4 4 1.8 4 4 4zm3-16.9c2.3.5 4 2.5 4 4.9v4c0 .6-.1 1.2-.3 1.8-.4-1-1-1.9-1.7-2.7V16c0-1.3-.8-2.4-2-2.8v-2.1z"></path>     </symbol>  <symbol id="txp_svg_selected" viewBox="0 0 16 16">   <path d="M1 8l5 5 9-10 -1-1 -8 9.2L2 7 1 8z"></path>  </symbol>  <symbol id="txp_svg_icon_hot" viewBox="0 0 16 16">   <path d="M8.5 4.25c-.547-1.879.5-3.11.5-3.11s-2.25.891-2.25 3.11c0 2.104 1.517 3.45-.068 3.45-.723-.022-1.228-.365-1.228-1.312 0-.851.546-1.619.546-1.619-1.313.696-3 2.153-3 5.556 0 2.517 2.289 4.811 4.5 4.811s4.5-2.105 4.5-4.622c0-4.046-2.975-4.493-3.5-6.264z"></path>  </symbol>  <symbol id="txp_svg_popup" viewBox="0 0 20 20">   <path d="M17 18H3c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h5c.6 0 1 .4 1 1s-.4 1-1 1H3v12h14v-3c0-.6.4-1 1-1s1 .4 1 1v3c0 1.1-.9 2-2 2zm2-10c0 .6-.4 1-1 1s-1-.4-1-1V5.4l-4.4 4.4c-.4.4-1 .4-1.4 0-.4-.4-.4-1 0-1.3L15.6 4H13c-.6 0-1-.4-1-1s.4-1 1-1h5c.5 0 .9.4 1 .9V8z"></path>  </symbol>     <symbol id="txp_svg_hd" viewBox="0 0 28 28">         <path d="M13 6h-2.8c0.1 0.7 0.2 1.4 0.2 2.4v3.6H2.8V8.5c0-1 0-1.6 0.2-2.4H0.1c0.1 0.7 0.2 1.3 0.2 2.4v10.1c0 1.1 0 1.7-0.2 2.4h2.8c-0.1-0.8-0.2-1.3-0.2-2.4v-4.3h7.6v4.3c0 1.1 0 1.7-0.2 2.4H13c-0.1-0.8-0.2-1.3-0.2-2.4V8.5C12.8 7.4 12.9 6.8 13 6z"></path>         <path d="M25.8 7.7C24.6 6.5 23.1 6 20.7 6h-3.4c-1.2 0-1.6 0-2.4-0.1 0.1 0.8 0.2 1.4 0.2 2.4v10.2c0 1.1 0 1.7-0.2 2.5 0.8 0 1.2-0.1 2.4-0.1h3.4c2.2 0 3.7-0.5 4.9-1.6 1.5-1.4 2.2-3.4 2.2-6C27.9 11 27.2 9 25.8 7.7zM23.9 17.6c-0.8 0.8-1.8 1.2-3.3 1.2h-3V8.3h3c1.6 0 2.6 0.3 3.4 1.1 0.9 0.9 1.3 2.2 1.3 4C25.3 15.2 24.8 16.6 23.9 17.6z"></path>     </symbol>     <symbol id="txp_svg_lightning" viewBox="0 0 28 28">         <path d="M24 12.3c-0.1-0.1-0.1-0.1-0.2-0.1C23.7 12 23.5 12 23.4 12h-6.9l2.3-10c0-0.1 0-0.2 0-0.3 0-0.2-0.1-0.3-0.2-0.5 -0.3-0.3-0.7-0.3-1 0L4.2 14.8C4.1 14.9 4 15.1 4 15.3c0 0.2 0.1 0.4 0.2 0.5 0.1 0.1 0.3 0.2 0.5 0.2h7.1l-2.4 9.9c0 0.1 0 0.1 0 0.2 -0.1 0.3 0 0.5 0.2 0.7 0.1 0.1 0.3 0.2 0.5 0.2 0.2 0 0.4-0.1 0.5-0.2L24 13.2c0.1-0.1 0.2-0.3 0.2-0.5C24.2 12.6 24.1 12.4 24 12.3L24 12.3z"></path>     </symbol>     <symbol id="txp_svg_vip_star_lg" viewBox="0 0 28 28">         <path d="M7.5 19.5C8.4 19.9 9.2 20 10 20c2.4 0 4.7-1 6.5-2.8 1.9-1.9 2.8-4.6 2.6-7.1l-1.4-0.2 -3.6-7.3L14 2.5c0 0-0.1 0-0.1 0.1l-3.6 7.3 -8.2 1.2c0 0-0.1 0-0.1 0.1v0.1l5.9 5.8L7.5 19.5zM7.3 20.6L6.6 25v0.1c0 0 0 0 0.1 0 0 0 0 0 0.1 0l6.5-3.5c-0.5 0.1-0.8 0.1-1.3 0.1C10.3 21.9 8.7 21.5 7.3 20.6zM18.7 19.2c-1.2 1.2-2.8 2-4.3 2.5l7 3.6c0 0 0 0 0.1 0h0.1c0 0 0.1-0.1 0-0.1l-1.3-7.9C19.8 17.9 19.3 18.6 18.7 19.2zM25.9 11.1l-4.7-0.7c0.5 2.2 0.1 4.4-1 6.5l5.8-5.5C26 11.3 26 11.3 25.9 11.1 26 11.1 25.9 11.1 25.9 11.1z"></path>     </symbol>     <symbol id="txp_svg_clock" viewBox="0 0 28 28">         <path d="M14 0.5c-6.6 0-12 5.4-12 12 0 6.6 5.4 12 12 12 0.4 0 0.7 0 1.1-0.1 0.1 0 0.3 0.1 0.4 0.1 0.8 0 1.5-0.7 1.5-1.5 0-0.8-0.7-1.5-1.5-1.5 -0.1 0-0.1 0-0.2 0l0-0.1c-0.4 0.1-0.9 0.1-1.3 0.1 -5 0-9-4-9-9 0-5 4-9 9-9 5 0 9 4 9 9 0 2-0.7 3.9-1.8 5.4l0.2 0.1C21.1 18.3 21 18.6 21 19c0 0.8 0.7 1.5 1.5 1.5 0.8 0 1.4-0.6 1.5-1.4 1.3-1.9 2-4.2 2-6.6C26 5.9 20.6 0.5 14 0.5zM18.4 12.5h-3.1l-2.5-4.3c-0.4-0.7-1.3-0.9-2-0.5 -0.7 0.4-0.9 1.2-0.5 1.9l3 5.2c0.2 0.4 0.6 0.6 1 0.7 0.1 0 0.3 0.1 0.4 0.1h3.8c0.9 0 1.6-0.7 1.6-1.5C20 13.2 19.3 12.5 18.4 12.5z"></path>     </symbol>     <symbol id="txp_svg_update" viewBox="0 0 28 28">         <path d="M13 16.4l0-5.9C13 9.7 13.7 9 14.5 9c0.8 0 1.5 0.6 1.4 1.4l0 4.6h2.4c0.9 0 1.6 0.7 1.6 1.5 0 0.8-0.7 1.5-1.6 1.5h-3.8c0 0-0.1 0-0.1 0 0 0 0 0 0 0 -0.8 0-1.5-0.6-1.5-1.4v0C13 16.5 13 16.5 13 16.4 13 16.5 13 16.5 13 16.4zM15 26c-6.7 0-12-5.4-12-12 0-1.9 0.4-3.7 1.2-5.2L2.9 9.1C2.1 9.3 1.3 8.8 1.1 8 0.9 7.2 1.3 6.4 2.1 6.2L7 4.9c0.8-0.2 1.6 0.3 1.8 1.1l1.3 4.8c0.2 0.8-0.3 1.6-1.1 1.8 -0.8 0.2-1.6-0.3-1.8-1.1l-0.4-1.4c-0.6 1.2-0.9 2.5-0.9 3.9 0 5 4 9 9 9 5 0 9-4 9-9 0-5-4-9-9-9 -0.1 0-0.1 0-0.2 0l0-0.1C14.6 5 14.6 5 14.5 5 13.6 5 13 4.3 13 3.5 13 2.7 13.6 2 14.5 2c0 0 0.1 0 0.1 0 0.1 0 0.3 0 0.4 0 6.7 0 12 5.4 12 12C27 20.6 21.6 26 15 26z"></path>   </symbol>   <symbol id="txp_svg_close" viewBox="0 0 16 16">   <path d="M9.275 8l4.461-4.461c0.352-0.352 0.352-0.923 0-1.275 -0.352-0.352-0.923-0.352-1.275 0L8 6.725 3.539 2.264c-0.352-0.352-0.923-0.352-1.275 0 -0.352 0.352-0.352 0.923 0 1.275L6.725 8l-4.461 4.461c-0.352 0.352-0.352 0.923 0 1.275 0.352 0.352 0.923 0.352 1.275 0L8 9.275l4.461 4.461c0.352 0.352 0.923 0.352 1.275 0 0.352-0.352 0.352-0.923 0-1.275L9.275 8z"></path>  </symbol>  <symbol id="txp_svg_icon_report" viewBox="0 0 20 20">   <path d="M8 9c-.552 0-1-.448-1-1v-3c0-.552.448-1 1-1s1 .448 1 1v3c0 .552-.448 1-1 1zm0 3c-.552 0-1-.448-1-1s.448-1 1-1 1 .448 1 1-.448 1-1 1zm6.323-1.086c-.116.424-.487.742-.948.742-.552 0-1-.448-1-1 0-.148.036-.285.094-.412l-.019-.01c.34-.675.55-1.427.55-2.235 0-2.762-2.239-5-5-5-2.762 0-5 2.238-5 5 0 2.761 2.239 5 5 5 .766 0 1.484-.186 2.133-.494l.013.03c.128-.059.267-.097.417-.097.552 0 1 .448 1 1 0 .471-.332.847-.771.954-.858.378-1.795.608-2.792.608-3.866 0-7-3.134-7-7s3.134-7 7-7 7 3.134 7 7c-.001 1.047-.261 2.024-.677 2.914z"></path>  </symbol>  <symbol id="txp_svg_right_xs" viewBox="0 0 12 12">   <path d="M4.4 10.4l-.8-.8L7.3 6 3.6 2.4l.8-.8 4 4L8 6l.4.4z"></path>  </symbol>  <symbol id="txp_svg_refresh" viewBox="0 0 20 20">   <path d="M10 19a9 9 0 0 1-9-8.999V10a1 1 0 1 1 2 0 7 7 0 1 0 7-7 6.952 6.952 0 0 0-4.877 2H7a1 1 0 0 1 0 2H3a1 1 0 0 1-1-1V2a1 1 0 0 1 2 0v1.314A8.935 8.935 0 0 1 10 1c4.971 0 9 4.029 9 9s-4.029 9-9 9z"></path>  </symbol>  <symbol id="txp_svg_left_xs" viewBox="0 0 12 12">   <path d="M7.7 10.4l-4-4 .4-.4-.4-.4 4-4 .8.8L4.8 6l3.7 3.6z"></path>  </symbol> </svg><txpdiv class="txp_contextmenu txp_none" data-role="txp-right-click-menu-wrapper" style="overflow:hidden">     <txpdiv class="txp_menuitem" data-role="txp-right-click-menu-video-info">视频信息</txpdiv>     <txpdiv class="txp_menuitem" data-role="txp-right-click-menu-copy-current-page-url">复制视频页面地址</txpdiv>     <txpdiv class="txp_menuitem" data-role="txp-right-click-menu-copy-current-time-page-url">复制当前时间的页面地址</txpdiv>     <txpdiv class="txp_menuitem" data-role="txp-right-click-menu-copy-console">复制调试信息</txpdiv>     <txpdiv class="txp_menuitem" data-role="txp-right-click-menu-copy-player-version">3.4.40 (2019-7-25 6:51:15 PM)</txpdiv>     <textarea class="txp_clipboard" style="position: absolute; left: 100%; top: 0px;"></textarea>     <!--<textarea class="ytp-html5-clipboard" style="position: absolute; left: -9999px; top: 0px;"></textarea>--> </txpdiv> <script src="https://captcha.gtimg.com/public/2/web-token.0.0.1.js" defer=""></script><div id="udata_fp3id1" style="visibility: hidden; position: absolute;"></div></body></html>
"""

html = etree.HTML(html_data)
print(etree.tostring(html).decode())