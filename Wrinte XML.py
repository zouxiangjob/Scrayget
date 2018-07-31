#!/usr/bin/python3
# coding:UTF-8

import xml.dom.minidom
import sys
import os
import os.path
#传入父节点本节点，节点信息，将节点信息添加到节点上去，然后将本节点和父节点关联起来。
def Setnode(Node,Parent,Line,Headslist):
    length =  len(Line)
    i=0
    for Head in Headslist:
        Node.setAttribute(Head[i],Line[i])
        i=i+1
    if i == len(Headslist):
        Parent.appendChild(Node)
        return Node
    else:
        return False
#传入根节点，列表中行信息，表头，将行信息里面的父节点名字进行匹配，找到父节点。将节点信息添加到节点上，并将节点联系起来。
def Findnode(root,Line,Headslist):
    # Ptype,Pname是列表的父名和父类型，Nodename是列表中的本名
    Ptype = Line[ptype]
    Pname = Line[pname]
    Nodename = Line[nodename]
    Nodetype = Line[nodetype]
    Taglist =  root.getElementsByTagName(Ptype)
    Taglist.append(root)

    for Parent in Taglist:
        if Pname == Parent.getAttribute(Nodename):
            Node = doc.createElement(Nodetype)
            Setnode(Node,Parent,Line,Headslist)
            return True
        else:
            continue
    return False
#传入根节点，和符合规范的二维列表，将二维列表写成DOM树。
def Getnodelist(root,Textlist):
    Headlist = Textlist[0]
    Partlist = Textlist
    del Partlist[0]
    for Part in Partlist:
        Issue = Findnode(root,Part,Headlist)
        if Issue == False:
            Notfindlist.append(Part)
        else:
            continue
    return True


#对文本进行读取，传出二维列表
def Gettxt(Path,Textlist):
    fp = open(Path,'r')
    lines = fp.readlines()

    for line in lines:
        Kline = line.replace('\n','')
        Tline = Kline.split('\t')
        Textlist.append(Tline)

    length = len(Textlist[0])
    i=0
    for line in Textlist:
        if len(Textlist[i])!=length:
            print('The line {0} error，Please check the text！'.format(i))
            return False
        else:
            i=i+1
            continue
    fp.close()
    return True


#全局变量

Textlist = list()
Notfindlist = list()
Path = 'name.txt'
nodename = 1
nodetype = 2
ptype =  3
pname = 4


#主程序
#建立Dom树和根节点，设置根节点属性。
doc = xml.dom.minidom.Document()
Root = doc.createElement('Part')
Root.setAttribute('type','Part')
Root.setAttribute('name','Wong')
doc.appendChild(Root)

Glo=Gettxt(Path,Textlist)
#如果txt文件读取符合规则，进行DOM树建立，否则退出
if  Glo != False:
    Getnodelist(Root,Textlist)
    print(Notfindlist)
else:
    print('The txt file error！')


#将XML写入文件中。
fp = open('part.xml','w',encoding="utf-8")
doc.writexml(fp, indent='\t', addindent='\n', newl='', encoding="utf-8")
fp.close


