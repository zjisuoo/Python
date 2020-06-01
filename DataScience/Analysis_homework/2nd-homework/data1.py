# 데이터 클리닝/변형
# 측정값이 모두 0 으로 들어간 결측치 값이 들어간 행을 삭제한 파일 구하기
# cdata, acode, aname, scode, sname, fdust, ufdust, ozone, nd, cm, sagas
import pandas as pd
import numpy as np

data = pd.read_csv("./environment_2018.csv", encoding = "utf-8")

# 컬럼명 변경
data.rename(columns = 
            {"측정일자": "cdate", 
            "권역코드" : "acode", 
            "권역명": "aname",
            "측정소코드": "scode", 
            "측정소명": "sname", 
            "미세먼지(㎍/㎥)": "fdust", 
            "초미세먼지(㎍/㎥)": "ufdust", 
            "오존(ppm)": "ozone", 
            "이산화질소농도(ppm)": "nd", 
            "일산화탄소농도(ppm)": "cm", 
            "아황산가스농도(ppm)": "sagas"}, inplace = True)

# 결측치 제거 안함
print(data)
print("data shape : ", data.shape)

# 측정값이 모두 0으로 들어간 결측치 list
zero = list()

# 0으로 들어간 결측치 제거
for i in range(len(data.index)) :
    if data['fdust'][i] == 0 and data['ufdust'][i] == 0 and data['ozone'][i] == 0.0 and data['nd'][i] == 0.0 and data['cm'][i] == 0.0 and data['sagas'][i] == 0.0 :
        data = data.drop(i)
        zero.append(i)

# 결측치 제거되었는지 확인
print(data)
print("data shape : ", data.shape)

data.to_csv("data1.csv", index = False)
