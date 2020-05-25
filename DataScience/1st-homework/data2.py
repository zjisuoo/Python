# 데이터 조작
# 데이터 정규화, 제곱, 다양한 결합값 등을 컬럼으로 추가
# 초미세먼지 값을 구하기 위한 컬럼 이용하여 선형회귀분석 식 beta, R^2 출력
# 출력 결과 캡쳐
import csv
import sys

f = open('./seoul_dust_info_2018.csv', encoding="cp949")
dust = csv.reader(f)

for line in dust : 
    cdate, acode, aname, scode, sname, fdust, ufdust, ozone, nd, cm, sages = line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9], line[10]
    for date in cdate.split('; ') :
        print (cdate, acode, aname, scode, sname, fdust, ufdust, ozone, nd, cm, sages)

f.close()