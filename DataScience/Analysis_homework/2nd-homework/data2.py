# 데이터 조작
import pandas as pd
import numpy as np

# 문제 1에서 만든 data1.csv 사용
data = pd.read_csv("./data1.csv", encoding="utf-8")

# 컬럼 삭제
del data["acode"]
del data["scode"]
del data["sname"]
del data["aname"]
del data["ufdust"]

# 0, 1, 2, 3, 4, 5, 6, 7
fdust_air = list()
ufdust_air = list()
ozone_air = list()
nd_air = list()
cm_air = list()
sagas_air = list()
total_air = list()

for i in range(len(data)) :
    # 미세먼지
    if data['fdust'][i] >= 0 and data['fdust'][i] <= 15 :
        fdust_air.append(7) # 최고
    elif data['fdust'][i] >= 16 and data['fdust'][i] <= 30 :
        fdust_air.append(6) # 좋음
    elif data['fdust'][i] >= 31 and data['fdust'][i] <= 40 :
        fdust_air.append(5) # 양호
    elif data['fdust'][i] >= 41 and data['fdust'][i] <= 50 :
        fdust_air.append(4) # 보통
    elif data['fdust'][i] >= 51 and data['fdust'][i] <= 75 :
        fdust_air.append(3) # 나쁨
    elif data['fdust'][i] >= 76 and data['fdust'][i] <= 100 :
        fdust_air.append(2) # 상당히 나쁨
    elif data['fdust'][i] >= 101 and data['fdust'][i] <= 150 :
        fdust_air.append(1) # 매우 나쁨
    elif data['fdust'][i] >= 151 :
        fdust_air.append(0) # 최악
    
    # 오존
    if data['ozone'][i] >= 0 and data['ozone'][i] < 0.02 :
        ozone_air.append(7) # 최고
    elif data['ozone'][i] >= 0.02 and data['ozone'][i] < 0.03 :
        ozone_air.append(6) # 좋음
    elif data['ozone'][i] >= 0.03 and data['ozone'][i] < 0.06 :
        ozone_air.append(5) # 양호
    elif data['ozone'][i] >= 0.06 and data['ozone'][i] < 0.09 :
        ozone_air.append(4) # 보통
    elif data['ozone'][i] >= 0.09 and data['ozone'][i] < 0.012 :
        ozone_air.append(3) # 나쁨
    elif data['ozone'][i] >= 0.012 and data['ozone'][i] < 0.015 :
        ozone_air.append(2) # 상당히 나쁨
    elif data['ozone'][i] >= 0.015 and data['ozone'][i] < 0.038 :
        ozone_air.append(1) # 매우 나쁨
    elif data['ozone'][i] >= 0.038 :
        ozone_air.append(0) # 최악
    
    # 이산화질소
    if data['nd'][i] >= 0 and data['nd'][i] < 0.02 :
        nd_air.append(7) # 최고
    elif data['nd'][i] >= 0.02 and data['nd'][i] < 0.03 :
        nd_air.append(6) # 좋음
    elif data['nd'][i] >= 0.03 and data['nd'][i] < 0.05 :
        nd_air.append(5) # 양호
    elif data['nd'][i] >= 0.05 and data['nd'][i] < 0.06 :
        nd_air.append(4) # 보통
    elif data['nd'][i] >= 0.06 and data['nd'][i] < 0.13 :
        nd_air.append(3) # 나쁨
    elif data['nd'][i] >= 0.13 and data['nd'][i] < 0.2 :
        nd_air.append(2) # 상당히 나쁨
    elif data['nd'][i] >= 0.2 and data['nd'][i] < 1.1 :
        nd_air.append(1) # 매우 나쁨
    elif data['nd'][i] >= 1.1 and data['nd'][i] < 2 :
        nd_air.append(0) # 최악

    # 일산화탄소
    if data['cm'][i] >= 0 and data['cm'][i] < 1 :
        cm_air.append(7) # 최고
    elif data['cm'][i] >= 1 and data['cm'][i] < 2 :
        cm_air.append(6) # 좋음
    elif data['cm'][i] >= 2 and data['cm'][i] < 5.5 :
        cm_air.append(5) # 양호
    elif data['cm'][i] >= 5.5 and data['cm'][i] < 9 :
        cm_air.append(4) # 보통
    elif data['cm'][i] >= 9 and data['cm'][i] < 12 :
        cm_air.append(3) # 나쁨
    elif data['cm'][i] >= 12 and data['cm'][i] < 15 :
        cm_air.append(2) # 상당히 나쁨
    elif data['cm'][i] >= 15 and data['cm'][i] < 32 :
        cm_air.append(1) # 매우 나쁨
    elif data['cm'][i] >= 32 :
        cm_air.append(0) # 최악
    
    # 아황산가스
    if data['sagas'][i] >= 0 and data['sagas'][i] < 0.01 :
        sagas_air.append(7) # 최고
    elif data['sagas'][i] >= 0.01 and data['sagas'][i] < 0.02 :
        sagas_air.append(6) # 좋음
    elif data['sagas'][i] >= 0.02 and data['sagas'][i] < 0.04 :
        sagas_air.append(5) # 양호
    elif data['sagas'][i] >= 0.04 and data['sagas'][i] < 0.05 :
        sagas_air.append(4) # 보통
    elif data['sagas'][i] >= 0.05 and data['sagas'][i] < 0.1 :
        sagas_air.append(3) # 나쁨
    elif data['sagas'][i] >= 0.1 and data['sagas'][i] < 0.15 :
        sagas_air.append(2) # 상당히 나쁨
    elif data['sagas'][i] >= 0.15 and data['sagas'][i] < 0.6 :
        sagas_air.append(1) # 매우 나쁨
    elif data['sagas'][i] >= 0.6 :
        sagas_air.append(0) # 최악

for i in range(len(data)) :
    if min(fdust_air[i], ozone_air[i], nd_air[i], cm_air[i], sagas_air[i]) == 0 :
        total_air.append("worst")
    elif min(fdust_air[i], ozone_air[i], nd_air[i], cm_air[i], sagas_air[i]) == 1 :
        total_air.append("serious")
    elif min(fdust_air[i], ozone_air[i], nd_air[i], cm_air[i], sagas_air[i]) == 2 :
        total_air.append("worse")
    elif min(fdust_air[i], ozone_air[i], nd_air[i], cm_air[i], sagas_air[i]) == 3 :
        total_air.append("bad")
    elif min(fdust_air[i], ozone_air[i], nd_air[i], cm_air[i], sagas_air[i]) == 4 :
        total_air.append("normal")
    elif min(fdust_air[i], ozone_air[i], nd_air[i], cm_air[i], sagas_air[i]) == 5 :
        total_air.append("good")
    elif min(fdust_air[i], ozone_air[i], nd_air[i], cm_air[i], sagas_air[i]) == 6 :
        total_air.append("better")
    elif min(fdust_air[i], ozone_air[i], nd_air[i], cm_air[i], sagas_air[i]) == 7 :
        total_air.append("best")

# airquality 컬럼 추가
data['airquality'] = total_air

airindex = list()
for i in range(len(data)) :
    if data['airquality'][i] == 'best' :
        airindex.append(1)
    elif data['airquality'][i] == "better" :
        airindex.append(2)
    elif data['airquality'][i] == "good" :
        airindex.append(3)
    elif data['airquality'][i] == 'normal' :
        airindex.append(4)
    elif data['airquality'][i] == "bad" :
        airindex.append(5)
    elif data['airquality'][i] == "worse" :
        airindex.append(6)
    elif data['airquality'][i] == 'serious' :
        airindex.append(7)
    elif data['airquality'][i] == "worst" :
        airindex.append(8)

# air_index 컬럼 추가
data['air_index'] = airindex

print("data shape : ", data.shape)

data = data[['cdate', 'fdust', 'ozone', 'nd', 'cm', 'sagas', 'airquality', 'air_index']]

print(data)

# data를 data2.csv 파일로 저장, index값 제거
data.to_csv("data2.csv", index = False)