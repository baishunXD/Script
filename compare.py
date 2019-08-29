import re
process = {"360tray.exe":"360安全卫士","360sd.exe":"360杀毒","MsMpEng.exe":"Microsoft Security Essentials",
     "avp.exe":"卡巴斯基","KvMonXP.exe":"江民杀毒","RavMonD.exe":"瑞星杀毒","kxetray.exe":"金山毒霸",
     "avcenter.exe":"Avira(小红伞)","ashDisp.exe":"Avast网络安全","rtvscan.exe":"诺顿杀毒","ksafe.exe":"金山卫士"
    ,"QQPCRTP.exe":"QQ电脑管家","mssecess.exe":"微软杀毒","remupd.exe":"熊猫卫士","safedog.exe":"安全狗"
    ,"ananwidget.exe":"墨者安全专家","rfwmain.exe":"瑞星防火墙","ServUDaemon.exe":"Serv-UFTPServer"
    ,"BaiduSdSvc.exe":"百度杀软","D_Safe_Manage.exe":"D盾","d_manage.exe":"D盾","SafeDogGuardCenter.exe":"安全狗",
     "safedogupdatecenter.exe":"安全狗","SafeDogSiteIIS.exe":"安全狗","yunsuo_agent_service.exe":"云锁",
     "yunsuo_agent_daemon.exe":"云锁","HwsPanel.exe":"护卫神","hws_ui.exe":"护卫神","hws.exe":"护卫神",
     "hwsd.exe":"护卫神","hipstray.exe":"火绒","wsctrl.exe":"火绒","usysdiag.exe":"火绒","ekrn.exe":"ESET NOD32"}

print("请将进程粘贴到此处,输入'end'结束！")
name = input()
list = []
while name != "end":
    list.append(name)
    name = input()

for ID in process:
    re_id = re.findall(ID,str(list))
    if re_id != []:
        print("进程为 "+ID+" : "+process[ID])