# -*- coding: utf-8 -*-

import STN
from STN.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,sys
import re,string,os
import os.path,sys,urllib,shutil,subprocess


cl = STN.LINE()
cl.login(token='authoken punya kalian')
cl.loginResult()

print u"PRANK BOTLIKE SUCCESS LOGIN"
reload(sys)
sys.setdefaultencoding('utf-8')

KAC = [cl]
mid = cl.getProfile().mid

Bots = [mid]
admsa="mid kalian"
wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':False,
    'message':"❂••••••••AUTO ADD••••••••❂\nhttps://line.me/R/ti/p/%40iya4481p\n『⊰์◉⊱ᎢᎬᎪᎷ ᏴᏞᎪᏟᏦ ❂Ғ ᏀᎪᎷᎬᎡ⊰์◉⊱』",
    "lang":"JP",
    "comment1":"❂••••••••••••••••••••••••••❂\n https://line.me/R/ti/p/%40iya4481p\n『⊰์◉⊱ᎢᎬᎪᎷ ᏴᏞᎪᏟᏦ ❂Ғ ᏀᎪᎷᎬᎡ⊰์◉⊱』",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "posts":True,
	}
	
wait2 = {
	'readMember':{},
	'readPoint':{},
	'ROM':{},
	'setTime':{}
    }
	
setTime = {}
setTime = wait2["setTime"]

res = {
    'num':{},
    'us':{},
    'au':{},
}


def Cmd(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = [""]
    for texX in tex:
        for command in commands:
            if string ==texX + command:
                return True
    return False

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
    
    
def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == mid:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = cl.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            cl.updateGroup(X)
                        except:
                            cl.sendText(msg.to,"error")                    
        if msg.contentType == 16:
            url = msg.contentMetadata["postEndUrl"]
            cl.like(url[25:58], url[66:], likeType=1001)
            cl.comment(url[25:58], url[66:], wait["comment1"])
            
        elif msg.contentType == 16:
            if wait["timeline"] == True:
                msg.contentType = 0
                if wait["lang"] == "JP":
                    msg.text = "menempatkan URL\n" + msg.contentMetadata["postEndUrl"]
                else:
                    msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                cl.sendText(msg.to,msg.text)
        elif msg.text is None:
            return            
            
#--------------------Fungsi Tag All Finish--------------------#
            elif "Mid" == msg.text:
                cl.sendText(msg.to,mid)
#-------------------------------------------------------------------#
            elif msg.text in ["愛のプレゼント","Gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                                    
             elif "Me" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
		
            elif "Tagall" in msg.text:
                group = cl.getGroup(msg.to)
                k = len(group.members)//100
                for j in xrange(k+1):
                    msg = Message(to=msg.to)
                    txt = u''
                    s=0
                    d=[]
                    for i in group.members[j*100 : (j+1)*100]:
                        d.append({"S":str(s), "E" :str(s+8), "M":i.mid})
                        s += 9
                        txt += u'@Krampus\n'
                    msg.text = txt
                    msg.contentMetadata = {u'MENTION':json.dumps({"MENTIONEES":d})}
                    cl.sendMessage(msg)             
                    
while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
