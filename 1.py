import re
import json
import os

province_zhixia = ['����', '���', '�Ϻ�', '����']

def get_phone(can):
    ret = re.search(r'\d{11}', can)
    if ret == None:
        return ""
    else:
        return ret.group(0)


def get_province(can):
    if(can[0:2] in province_zhixia):
        ret = can[0:2]
        return ret
    else:
        if(re.search(("(.*?ʡ)|(.*?������)"), can) != None):
            ret = re.search(("(.*?ʡ)|(.*?������)"), can)
        else:
            if(can[0:3] == "������"):
                return "������"
            else:
                return (can[0:2])
    return ret.group(0)


def get_city(can):
    if(re.search(".*?��", can) != None):
        return (re.search(".*?��", can)).group(0)
    else:
        return ''


def get_qu(can):
    if(re.search(("(.*?��)|(.*?��)|(.*?��)"), can) != None):
        return (re.search(("(.*?��)|(.*?��)|(.*?��)"), can)).group(0)
    else:
        return ''


def get_zheng(can):
    if(re.search(("(.*?�ֵ�)|(.*?��)|(.*?��)"), can) != None):
        return (re.search(("(.*?�ֵ�)|(.*?��)|(.*?��)"), can)).group(0)
    else:
        return ''


def get_lu(can):
    if(re.search(".*?·", can) != None):
        return (re.search(".*?·", can)).group(0)
    else:
        return ''


def get_hao(can):
    if(re.search(".*?��", can) != None):
        return (re.search(".*?��", can)).group(0)
    else:
        return ''

shuru = input()
flag = shuru[0]
ans = {}
place = []
sp = shuru.split(',')
ans['����'] = sp[0][2:4]  # ��������
res = sp[1]
phone = get_phone(res)
res = res.replace(phone, '')
ans['�绰'] = phone
province = get_province(res)  # ����ʡ
l = len(province)
if(res[0:2] in province_zhixia or l >= 5):
    province_t = province
else:
    if(province[-1] != 'ʡ'):
        province_t = province + 'ʡ'
    else:
        province_t = province
place.append(province_t)
if(res[0:2] not in province_zhixia):
    res = res.replace(province, '')
city = get_city(res)  # ������
place.append(city)
res = res.replace(city, '')
qu = get_qu(res)  # ������/��/�ؼ���
place.append(qu)
res = res.replace(qu, '')
zheng = get_zheng(res)  # �����ֵ�/��/��
place.append(zheng)
res = res.replace(zheng, '')
if(flag != '1'):
    lu = get_lu(res)  # ����·
    place.append(lu)
    res = res.replace(lu, '')
    hao = get_hao(res)  # �������ƺ�
    place.append(hao)
    res = res.replace(hao, '')
place.append(res)
ans['��ַ'] = place
# print(res)
# print(place)
# print(province)
print(ans)
