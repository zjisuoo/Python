# 데이터 조작
# 데이터 정규화, 제곱, 다양한 결합값 등을 컬럼으로 추가
import pandas as pd
import numpy as np

# 컬럼명 변경, 0이 들어간 결측치 값을 제거한 data1.csv 사용
data = pd.read_csv("./data1.csv", encoding = "utf-8")
 
# 회귀 분석 시 권역코드, 권역명, 측정소코드, 오존, 일산화탄소 농도, 아황산가스농도 필요없기 때문에 컬럼 삭제
del data["acode"]
del data["scode"]
del data["sname"]
del data["ozone"]
del data["cm"]
del data["sagas"]

# 권역 명 변경
data.loc[data.aname == "도심권", "aname"] = "CENTER"
data.loc[data.aname == "동북권", "aname"] = "EN"
data.loc[data.aname == "동남권", "aname"] = "ES"
data.loc[data.aname == "서북권", "aname"] = "WN"
data.loc[data.aname == "서남권", "aname"] = "WS"

# u_grade 리스트에 범위에 따라 good, normal, bad, terrible 값 추가
u_grade = list()
for i in range(len(data)) :
    if data['ufdust'][i] >= 0 and data['ufdust'][i] <= 15 :
        u_grade.append("good")
    elif data['ufdust'][i] >= 16 and data['ufdust'][i] <= 35 :
        u_grade.append("normal")
    elif data['ufdust'][i] >= 36 and data['ufdust'][i] <= 75 :
        u_grade.append("bad")
    elif data['ufdust'][i] >= 76 :
        u_grade.append("terrible")

# ufdust_grade 열 생성
data['ufdust_grade'] = u_grade

# nd_pass 빈 열 추가 후, nd 값에 따라 no pass 이면 0, pass 이면 1로 값 변경 
data['nd_pass'] = None
data.loc[data.nd > 0.05, "nd_pass"] = "0"
data.loc[data.nd <= 0.05, "nd_pass"] = "1"

# 열 순서 변경
data = data[['cdate', 'aname', 'fdust', 'ufdust', 'ufdust_grade', 'nd', 'nd_pass']]

# 최종 변경된 data와 data shape 출력
print(data)
print("data shape : ", data.shape)

# data를 data2.csv 파일로 저장, index값 제거
data.to_csv("data2.csv", encoding = 'utf-8', index = False)