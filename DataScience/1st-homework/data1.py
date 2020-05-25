# 데이터 클리닝/변형
# 측정값이 모두 0으로 들어간 결측치 값이 들어간 행을 삭제한 파일
# cdate, acode, aname, scode, sname, fdust, ufdust, ozone, nd, cm, sages
import csv
import pandas as pd
import numpy as np

data = pd.read_csv("./seoul_dust_info_2018.csv", encoding="utf-8")

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

np.nan = 0
data_no_zero = data.dropna(how = 'any')
'''
                    data.acode != 0, 
                    data.aname != 0, 
                    data.scode != 0,
                    data.sname != 0,
                    data.fdust != 0,
                    data.ufdust != 0,
                    data.ozone != 0,
                    data.nd != 0,
                    data.cm != 0,
                    data.sagas != 0]


data_dropna = data.drop(["0"])
'''
# 결측치 제거 안함
print(data)

# 결측치 제거
print(data_no_zero)
