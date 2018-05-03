#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
t1 = time.time()

def panduan(q):
    # 第三题开始
    if q[3] == "a" and q[3] != q[6] and q[6] == q[2] and q[2] == q[4]:
        pass
    elif q[3] == "b" and q[6] != q[3] and q[3] == q[2] and q[2] == q[4]:
        pass
    elif q[3] == "c" and q[2] != q[3] and q[3] == q[6] and q[6] == q[4]:
        pass
    elif q[3] == "d" and q[4] != q[3] and q[3] == q[2] and q[2] == q[6]:
        pass
    else:
        return -1
    # 顺利通过第三题
    
    # 第四题开始
    # 1 = 5, q[4] = 'a' 
    if q[4] == 'a' and q[1] == q[5] and q[2] != q[7] \
        and q[1] != q[9] and q[6] != q[10]:
        pass
    elif q[4] == 'b' and q[1] != q[5] and q[2] == q[7] \
        and q[1] != q[9] and q[6] != q[10]:
        pass
    elif q[4] == 'c' and q[1] != q[5] and q[2] != q[7] \
        and q[1] == q[9] and q[6] != q[10]:
        pass
    elif q[5] == 'd' and q[1] != q[5] and q[2] != q[7] \
        and q[1] != q[9] and q[6] == q[10]:
        pass
    else:
        return -1
    # 顺利通过第四题
    # 第五题开始
    if q[5] == 'a' and q[8] == q[5] and q[4] != q[5] and q[9] != q[5] and q[7] != q[5]:
        pass
    elif q[5] == 'b' and q[8] != q[5] and q[4] == q[5] and q[9] != q[5] and q[7] != q[5]:
        pass
    elif q[5] == 'c' and q[8] != q[5] and q[4] != q[5] and q[9] == q[5] and q[7] != q[5]:
        pass
    elif q[5] == 'd' and q[8] != q[5] and q[4] != q[5] and q[9] != q[5] and q[7] == q[5]:
        pass
    else:
        return -1
    # 顺利通过第五题
    # 第六题开始
    if q[6] == 'a' and q[2] == q[4] and q[4] == q[8] \
        and (not (q[1] == q[8] and q[6] == q[8])) \
        and (not (q[3] == q[8] and q[10] == q[8])) \
        and (not (q[5] == q[8] and q[9] == q[8])):
        pass
    elif q[6] == 'b' and q[1] == q[8] and q[6] == q[8] \
        and (not (q[2] == q[4] and q[4] == q[8])) \
        and (not (q[3] == q[8] and q[10] == q[8])) \
        and (not (q[5] == q[8] and q[9] == q[8])):
        pass
    elif q[6] == 'c' and q[3] == q[8] and q[10] == q[8] \
        and (not (q[1] == q[8] and q[6] == q[8])) \
        and (not (q[2] == q[4] and q[4] == q[8])) \
        and (not (q[5] == q[8] and q[9] == q[8])):
        pass
    elif q[6] == 'a' and q[5] == q[8] and q[9] == q[8] \
        and (not (q[1] == q[8] and q[6] == q[8])) \
        and (not (q[3] == q[8] and q[10] == q[8])) \
        and (not (q[2] == q[4] and q[4] == q[8])):
        pass
    else:
        return -1
    # 顺利通过第六题
    # 第七题开始
    leasts = least(q)
    if q[7] == 'a' and 'c' in leasts:
        pass
    elif q[7] == 'b' and 'b' in leasts:
        pass
    elif q[7] == 'c' and 'a' in leasts:
        pass
    elif q[7] == 'd' and 'd' in leasts:
        pass
    else:
        return -1
    # 第七题结束
    # 第八题开始
    if q[8] == 'a':
        if q[1] == 'a' and q[7] not in ['a', 'b']: 
            pass
        elif q[1] == 'b' and q[7] == 'd':
            pass
        elif q[1] == 'c' and q[7] == 'a':
            pass
        elif q[1] == 'd' and q[7] not in ['c','d']:
            pass
        else:
            return -1
    elif q[8] == 'b':
        if q[1] == 'a' and q[5] not in ['a', 'b']: 
            pass
        elif q[1] == 'b' and q[5] == 'd':
            pass
        elif q[1] == 'c' and q[5] == 'a':
            pass
        elif q[1] == 'd' and q[5] not in ['c','d']:
            pass
        else:
            return -1
    elif q[8] == 'c':
        if q[1] == 'a' and q[2] not in ['a', 'b']: 
            pass
        elif q[1] == 'b' and q[2] == 'd':
            pass
        elif q[1] == 'c' and q[2] == 'a':
            pass
        elif q[1] == 'd' and q[2] not in ['c','d']:
            pass
        else:
            return -1
    elif q[8] == 'd':
        if q[1] == 'a' and q[10] not in ['a', 'b']: 
            pass
        elif q[1] == 'b' and q[10] == 'd':
            pass
        elif q[1] == 'c' and q[10] == 'a':
            pass
        elif q[1] == 'd' and q[10] not in ['c','d']:
            pass
        else:
            return -1
    else:
        return -1
    # 第八题顺利通过
    # 第九题
    if q[9] == 'a':
        if q[1] == q[6] and q[6] != q[5] and q[10] == q[5] and q[2] == q[5] and q[9] == q[5]:
            pass
        elif q[1] != q[6] and q[6] == q[5] and q[10] != q[5] and q[2] != q[5] and q[9] != q[5]:
            pass
        else:
            return -1
    elif q[9] == 'b':
        if q[1] == q[6] and q[6] == q[5] and q[10] != q[5] and q[2] == q[5] and q[9] == q[5]:
            pass
        elif q[1] != q[6] and q[6] != q[5] and q[10] == q[5] and q[2] != q[5] and q[9] != q[5]:
            pass
        else:
            return -1
    elif q[9] == 'c':
        if q[1] == q[6] and q[6] == q[5] and q[10] == q[5] and q[2] != q[5] and q[9] == q[5]:
            pass
        elif q[1] != q[6] and q[6] != q[5] and q[10] != q[5] and q[2] == q[5] and q[9] != q[5]:
            pass
        else:
            return -1
    elif q[9] == 'd':
        if q[1] == q[6] and q[6] == q[5] and q[10] == q[5] and q[2] == q[5] and q[9] != q[5]:
            pass
        elif q[1] != q[6] and q[6] != q[5] and q[10] != q[5] and q[2] != q[5] and q[9] == q[5]:
            pass
        else:
            return -1
    else:
        return -1
    # 第九题顺利通过
    # 第十题
    cha = minus(q)
    if q[10] == 'a' and cha == 3:
        pass
    elif q[10] == 'b' and cha == 2:
        pass
    elif q[10] == 'c' and cha == 4:
        pass
    elif q[10] == 'd' and cha == 1:
        pass
    else:
        return -1
    print "find one:" + str(q)

def least(q):
    times = [0,0,0,0]
    for o in q:
        if o == 'a':
            times[0]+=1
        elif o == 'b':
            times[1]+=1
        elif o == 'c':
            times[2]+=1
        elif o == 'd':
            times[3]+=1
    least = min(times[0],times[1],times[2],times[3])
    leasts = []
    if least == times[0]:
        leasts.append('a')
    if least == times[1]:
        leasts.append('b')
    if least == times[2]:
        leasts.append('c')
    if least == times[3]:
        leasts.append('d')
    return leasts

def minus(q):
    times = [0,0,0,0]
    for o in q:
        if o == 'a':
            times[0]+=1
        elif o == 'b':
            times[1]+=1
        elif o == 'c':
            times[2]+=1
        elif o == 'd':
            times[3]+=1
    least = min(times[0],times[1],times[2],times[3])
    most = max(times[0],times[1],times[2],times[3])
    return most - least

q = ["e","a","a","a","a","a","a","a","a","a","a"]
selections = ["a","b","c","d"]
for i1 in selections:
    q[1] = i1
    for i2 in selections:
        q[2] = i2
        for i3 in selections:
            q[3] = i3
            for i4 in selections:
                q[4] = i4
                for i5 in selections:
                    q[5] = i5
                    for i6 in selections:
                        q[6] = i6
                        for i7 in selections:
                            q[7] = i7
                            for i8 in selections:
                                q[8] = i8
                                for i9 in selections:
                                    q[9] = i9
                                    for i10 in selections:
                                        q[10] = i10
                                        panduan(q)
t2 = time.time()
print("总共用时:" + str(t2-t1))
