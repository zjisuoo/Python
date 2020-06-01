# 데이터 조작
# 데이터 정규화, 제곱, 다양한 결합값 등을 컬럼으로 추가
# 초미세먼지 값을 구하기 위한 컬럼 이용하여 선형회귀분석 식 beta, R^2 출력
# 출력 결과 캡쳐
import pandas as pd
import numpy as np

# 컬럼명 변경, 0이 들어간 결측치 값을 제거한 data1.csv 사용
data = pd.read_csv("./data1.csv", encoding = "utf-8")
 
# 최대, 최소 데이터 정규화
def min_max_normalize(val) :
    normalized = list()

    for value in val :
        normalized_num = (value - min(val)) / (max(val) - min(val))
        normalized.append(round(normalized_num, 3))

    return normalized

def z_score_normalized(val) :
    zNormalized = list()

    for value in val :
        zNormalized_num = (value - np.mean(val)) / np.std(val)
        zNormalized.append(round(zNormalized_num, 3))
    
    return zNormalized

def MinMaxScaler(val) :
    numerator = val - np.min(val, 0)
    denominator = np.max(val, 0) - np.min(val, 0)
    return numerator / (denominator + 1e-7)

# 미세먼지 max : 217 / min : 0
f_dust = min_max_normalize(data['fdust'])
# print(f_dust)
data['fdust_Normalized'] = f_dust
# print(data)

# 초미세먼지 max : 985 / min : 0
uf_dust = min_max_normalize(data['ufdust'])
# print(uf_dust)
data['ufdust_Normalized'] = uf_dust
# print(data)

# 미세먼지 max : 217 / min : 0
z_f_dust = z_score_normalized(data['fdust'])
# print(z_f_dust)
data['Z_fdust_Normalized'] = z_f_dust
# print(data)

# 초미세먼지 max : 985 / min : 0
z_uf_dust = z_score_normalized(data['ufdust'])
# print(z_uf_dust)
data['Z_ufdust_Normalized'] = z_uf_dust
# print(data)

o_zone = min_max_normalize(data['ozone'])
data['Ozone_Normalized'] = o_zone

z_o_zone = z_score_normalized(data['ozone'])
data['Z_ozone_Normalized'] = z_o_zone
# print(data)

mm_fdust = MinMaxScaler(data['fdust'])
data['MinMaxScaler'] = mm_fdust
print(data)
