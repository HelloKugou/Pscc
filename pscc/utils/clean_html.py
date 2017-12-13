#!/usr/bin/env python3
#-*-coding:utf-8-*-
# __all__=""
# __datetime__=""
# __purpose__="清除html标签"
text = """<?xml version='1.0' encoding='utf-8'?>

      <p>原标题：人美心善热心肠！伊能静捐款寻找走失女童</p>
            <p>昨日，因健身视频成为励志女神的伊能静在自己的微博发布了一篇寻找失踪女童杨悦的文章，她表示，自己自愿捐赠三万元作为寻找江西失踪女童的线索鼓励金，希望借助自己的绵薄之力增添一份希望。 </p>
<p><img src="http://cityparlor.oss-cn-beijing.aliyuncs.com/img/201710/49d285a29ca1422599abece2238d9a34.jpeg" max-/></p>
<p>说到伊能静，近几年的她可以说完美蜕变，家庭美满、事业有成、默默做慈善参与公益项目，瘦身成功的她人美心善，满满的正能量。伊能静做慈善方面数十年如一日，成功创办“静新图书基金”，迄今已经资助过无数山区儿童。地震募捐、资助贫困生、救助病患儿童等一系列爱心活动从来都不曾少了伊能静的身影。 </p>
<p><img src="http://cityparlor.oss-cn-beijing.aliyuncs.com/img/201710/d257c8a30f1f44cea9f59470dd412b3a.jpeg" max-/></p>
<p>数十年来，伊能静向困境中的灾民、磨难中的孩童频频伸出援手。记得在不久前，伊能静就曾半夜报警解救一个疑似遭家暴的儿童，警方接到报警寻找线索，最终找到了女童，并且女童对父亲进行了教育。曾在多年前，她发现一名路边摆摊贩的少年因家中贫穷无法上学，为他捐助了全部学费，其他更有许多数不清的善行。明星做公益并不罕见，但像伊能静这样坚持事必躬亲，几乎每个月一次的公益活动频率，值得让人敬佩。 </p>
<p><img src="http://cityparlor.oss-cn-beijing.aliyuncs.com/img/201710/1b77b406c61f4ac3ab31695771a467ba.jpeg" max-/></p>
<p>除了帮助贫困受难儿童，伊能静生活中也毫无私心跟粉丝分享她的瘦身、美容、保养、带娃心得，平易近人。以前大家对伊能静的印象无非是很爱唠叨，很少女心，甚至在《妈妈是超人》给大家很辛苦的感觉，但其实久了，越来越多人了解伊能静就是拥有很多爱很多能量可以分享给大家的热心肠的善良女人。 </p>
<p><img src="http://cityparlor.oss-cn-beijing.aliyuncs.com/img/201710/d21de7900e534130bbc4aa6d6c068bae.jpeg" max-/></p>
<p>在最新寻找失踪女童的微博发布后，伊能静将此条作为置顶，可见真心。网友也纷纷留言称伊能静是真正的人美心善：“静姐，总是那么暖心”、“静姐作为一个明星，平日那么忙，还能帮忙转发呼吁媒体及大家之力量帮忙寻找，是很大善举。”、“这才是真正的正能量，为静姐点赞”。</p>
<p><img src="http://cityparlor.oss-cn-beijing.aliyuncs.com/img/201710/be90e120c2ec44daa96d9c49b7c8cfc5.jpeg" max-/>
</article>
  """
# -*- coding: utf-8-*-
import re
# 过滤HTML中的标签
# 将HTML中标签等信息去掉
#@param htmlstr HTML字符串.


def filter_tags(htmlstr):
    # 先过滤CDATA
    re_cdata = re.compile('//<!\[CDATA\[[^>]*//\]\]>', re.I)  # 匹配CDATA
    re_script = re.compile(
        '<\s*script[^>]*>[^<]*<\s*/\s*script\s*>',
        re.I)  # Script
    re_style = re.compile(
        '<\s*style[^>]*>[^<]*<\s*/\s*style\s*>',
        re.I)  # style
    re_br = re.compile('<br\s*?/?>')  # 处理换行
    re_h = re.compile('</?\w+[^>]*>')  # HTML标签
    re_comment = re.compile('<!--[^>]*-->')  # HTML注释
    re_xml = re.compile('<[\S\s]xml[\s\S]*>')  # 去掉xml头
    s = re_cdata.sub('', htmlstr)  # 去掉CDATA
    s = re_script.sub('', s)  # 去掉SCRIPT
    s = re_style.sub('', s)  # 去掉style
    s = re_br.sub('\n', s)  # 将br转换为换行
    s = re_h.sub('', s)  # 去掉HTML 标签
    s = re_comment.sub('', s)  # 去掉HTML注释
    s = re_xml.sub('', s)  # 去掉xml头
    # 去掉多余的空行
    blank_line = re.compile('\n+')
    s = blank_line.sub('\n', s)
    s = replaceCharEntity(s)  # 替换实体
    return s

# 替换常用HTML字符实体.
# 使用正常的字符替换HTML中特殊的字符实体.
# 你可以添加新的实体字符到CHAR_ENTITIES中,处理更多HTML字符实体.
#@param htmlstr HTML字符串.


def replaceCharEntity(htmlstr):
    CHAR_ENTITIES = {'nbsp': ' ', '160': ' ',
                     'lt': '<', '60': '<',
                     'gt': '>', '62': '>',
                     'amp': '&', '38': '&',
                     'quot': '"', '34': '"', }

    re_charEntity = re.compile(r'&#?(?P<name>\w+);')
    sz = re_charEntity.search(htmlstr)
    while sz:
        entity = sz.group()  # entity全称，如&gt;
        key = sz.group('name')  # 去除&;后entity,如&gt;为gt
        try:
            htmlstr = re_charEntity.sub(CHAR_ENTITIES[key], htmlstr, 1)
            sz = re_charEntity.search(htmlstr)
        except KeyError:
            # 以空串代替
            htmlstr = re_charEntity.sub('', htmlstr, 1)
            sz = re_charEntity.search(htmlstr)
    return htmlstr


def repalce(s, re_exp, repl_string):
    return re_exp.sub(repl_string, s)


def filter(html):
    text = filter_tags(replaceCharEntity(html))
    return text