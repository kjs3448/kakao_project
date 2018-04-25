import pandas as pd
import numpy as np
import csv

data = pd.read_csv('dataset\dataset.tsv', delimiter = '\t')
print(list(data.columns.values))
print(data.tail(35))

# x1 ~ x15의 input & y output
#	[x1~x8: 고객 정보]
#	x1 - 연령
#	x2 - 직업 종류 ("admin.","unknown","unemployed","management","housemaid","entrepreneur","student","blue-collar","self-employed","retired","technician","services")
#	x3 - 결혼여부 ("married","divorced","single")
#	x4 - 교육수준 ("unknown","저학력","중학력","고학력")
#	x5 - 채무 불이행 유무 ("yes","no")
#	x6 - 연 평균 잔고 (1,000원 단위)
#	x7 - 주택 자금 대출 여부 ("yes","no")
#	x8 - 개인 신용 대출 여부 ("yes","no")

# 	[x9~x11: 현재 캠페인에서, 고객과의 마지막 연락을 기준]
#	x9 - 통화 유형 ("unknown","유선","무선")
# 	x10 - 마지막으로 연락한 날
#	x11 - 마지막으로 연락한 달 ("jan", "feb", "mar", ..., "nov", "dec")

#	[x12~x15: 기타 정보]
#	x12 - 현재 캠페인에서 고객에게 연락한 횟수
#	x13 - 이전 캠페인에서 마지막으로 고객과 연락된 후로부터 경과된 일수 (-1 은 이전에 연락이 되지 않은 고객을 의미)
#	x14 - 이전 캠페인에서 고객에게 연락한 횟수
#	x15 - 이전 캠페인의 결과 ("failure","unknown","success")


############ 문제1: x1~x8데이터로부터 클러스터링. 알고리즘을 선택한 이유와 클러스터 결과 분석




############ 문제2: 전체 데이터로부터 output을 예측하기 위한 분류기를 만들고 과정을 설명
