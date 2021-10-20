import os
os.getcwd()

import pandas as pd
from pandas import ExcelWriter
from pandas import DataFrame
import csv
import numpy as np
import matplotlib
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import seaborn as sns
import time
from sklearn.preprocessing import RobustScaler


# Step 1: 변수 파일 불러오기
## P0
#SWRF001.Y(p1)
data_01 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/SWRF001.Y_1.csv', sep=',',
     names=["time", "value"])
data_01 = data_01[:-2]
data_02 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/SWRF001.Y_2.csv', sep=',',
     names=["time", "value"])
data_02 = data_02[:-1]
SWRF001Y = pd.concat([data_01, data_02],ignore_index = True)
SWRF001Y['value'] = pd.to_numeric(SWRF001Y['value'], errors= 'coerce')
#print(SWRF001Y.info())
#print(SWRF001Y)

#SWFC004Y(p1)
data_01 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/SWFC004.Y_1.csv', sep=',',
     names=["time", "value"])
data_01 = data_01[:-2]
data_02 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/SWFC004.Y_2.csv', sep=',',
     names=["time", "value"])
data_02 = data_02[:-1]
SWFC004Y = pd.concat([data_01, data_02],ignore_index = True)
SWFC004Y['value'] = pd.to_numeric(SWFC004Y['value'], errors= 'coerce')
#print(SWFC004Y.info())


#SWFC001Y(p1)(2016-2019)
data_01 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/SWFC001.Y_2016.csv', sep=',',
     names=["time", "value"])
data_01 = data_01[:-2]
data_02 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/SWFC001.Y_2017.csv', sep=',',
     names=["time", "value"])
data_02 = data_02[:-2]
data_03 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/SWFC001.Y_2018.csv', sep=',',
     names=["time", "value"])
data_03 = data_03[:-2]
data_04 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/SWFC001.Y_2019.csv', sep=',',
     names=["time", "value"])
data_04 = data_04[:-1]
SWFC001Y = pd.concat([data_01, data_02, data_03, data_04],ignore_index = True)
SWFC001Y['value'] = pd.to_numeric(SWFC001Y['value'], errors= 'coerce')

#print(SWFC001Y.info())
#print(SWFC001Y)

#SORF001Y(p1)
data_01 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/SORF001.Y_1.csv', sep=',',
     names=["time", "value"])
data_01 = data_01[:-2]
data_02 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/SORF001.Y_2.csv', sep=',',
     names=["time", "value"])
data_02 = data_02[:-1]
SORF001Y = pd.concat([data_01, data_02],ignore_index = True)
SORF001Y['value'] = pd.to_numeric(SORF001Y['value'], errors= 'coerce')


#SOFC007Y(p1)
data_01 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/SOFC007.Y_1.csv', sep=',',
     names=["time", "value"])
data_01 = data_01[:-2]
data_02 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/SOFC007.Y_2.csv', sep=',',
     names=["time", "value"])
data_02 = data_02[:-1]
SOFC007Y = pd.concat([data_01, data_02],ignore_index = True)
SOFC007Y['value'] = pd.to_numeric(SOFC007Y['value'], errors= 'coerce')

#SOFC002Y(p1)
data_01 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/SOFC002.Y_1.csv', sep=',',
     names=["time", "value"])
data_01 = data_01[:-2]
data_02 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/SOFC002.Y_2.csv', sep=',',
     names=["time", "value"])
data_02 = data_02[:-1]
SOFC002Y = pd.concat([data_01, data_02],ignore_index = True)
SOFC002Y['value'] = pd.to_numeric(SOFC002Y['value'], errors= 'coerce')

#CULC508Y(p1)
data_01 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/CULC508.Y_1.csv', sep=',',
     names=["time", "value"])
data_01 = data_01[:-2]
data_02 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/CULC508.Y_2.csv', sep=',',
     names=["time", "value"])
data_02 = data_02[:-1]
CULC508Y = pd.concat([data_01, data_02],ignore_index = True)
CULC508Y['value'] = pd.to_numeric(CULC508Y['value'], errors= 'coerce')

#CULC501Y(p1)
data_01 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/CULC501.Y_1.csv', sep=',',
     names=["time", "value"])
data_01 = data_01[:-2]
data_02 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/CULC501.Y_2.csv', sep=',',
     names=["time", "value"])
data_02 = data_02[:-1]
CULC501Y = pd.concat([data_01, data_02],ignore_index = True)
CULC501Y['value'] = pd.to_numeric(CULC501Y['value'], errors= 'coerce')
'''
#CUII503Y(p1) XX
data_01 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/CUII503.Y_1.csv', sep=',',
     names=["time", "value"])
data_01 = data_01[:-2]
data_02 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/CUII503.Y_2.csv', sep=',',
     names=["time", "value"])
data_02 = data_02[:-1]
CUII503Y = pd.concat([data_01, data_02],ignore_index = True)
CUII503Y['value'] = pd.to_numeric(CUII503Y['value'], errors= 'coerce')


#CUII502Y(p1)  --> 2개년이라 사용하지 않음
CUII502Y = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/CUII502.Y_2.csv', sep=',',
     names=["time", "value"])
CUII502Y = CUII502Y[:-1]
'''

#CUFI008Y(p1)
data_01 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/CUFI008.Y_1.csv', sep=',',
     names=["time", "value"])
data_01 = data_01[:-2]
data_02 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/CUFI008.Y_2.csv', sep=',',
     names=["time", "value"])
data_02 = data_02[:-1]
CUFI008Y = pd.concat([data_01, data_02],ignore_index = True)
CUFI008Y['value'] = pd.to_numeric(CUFI008Y['value'], errors= 'coerce')

'''#CUEI503Y(p1)2016-2019 XX
data_01 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/CUEI503.Y_2016.csv', sep=',',
     names=["time", "value"])
data_01 = data_01[:-2]
data_02 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/CUEI503.Y_2017.csv', sep=',',
     names=["time", "value"])
data_02 = data_02[:-2]
data_03 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/CUEI503.Y_2018_2019.csv', sep=',',
     names=["time", "value"])
data_03 = data_03[:-1]
CUEI503Y = pd.concat([data_01, data_02, data_03],ignore_index = True)
CUEI503Y['value'] = pd.to_numeric(CUEI503Y['value'], errors= 'coerce')

#CUEI502Y(p1)2016-2019
data_01 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/CUEI502.Y_2016.csv', sep=',',
     names=["time", "value"])
data_01 = data_01[:-2]
data_02 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/CUEI502.Y_2017.csv', sep=',',
     names=["time", "value"])
data_02 = data_02[:-2]
data_03 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/CUEI502.Y_2018_2019.csv', sep=',',
     names=["time", "value"])
data_03 = data_03[:-1]
CUEI502Y = pd.concat([data_01, data_02, data_03],ignore_index = True)
CUEI502Y['value'] = pd.to_numeric(CUEI502Y['value'], errors= 'coerce')

#CUEI501Y(p1)2016-2019
data_01 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/CUEI501.Y_2016.csv', sep=',',
     names=["time", "value"])
data_01 = data_01[:-2]
data_02 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/CUEI501.Y_2017.csv', sep=',',
     names=["time", "value"])
data_02 = data_02[:-2]
data_03 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/CUEI501.Y_2018.csv', sep=',',
     names=["time", "value"])
data_03 = data_03[:-2]
data_04 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/CUEI501.Y_2019.csv', sep=',',
     names=["time", "value"])
data_04 = data_04[:-1]
CUEI501Y = pd.concat([data_01, data_02, data_03, data_04],ignore_index = True)
CUEI501Y['value'] = pd.to_numeric(CUEI501Y['value'], errors= 'coerce')'''

#700LI770BY(p1)
data_01 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/700LI770B.Y_1.csv', sep=',',
     names=["time", "value"])
data_01 = data_01[:-2]
data_02 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/700LI770B.Y_2.csv', sep=',',
     names=["time", "value"])
data_02 = data_02[:-1]
p1700LI770BY = pd.concat([data_01, data_02],ignore_index = True)
p1700LI770BY['value'] = pd.to_numeric(p1700LI770BY['value'], errors= 'coerce')

#700II783CY(p1)
data_01 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/700II783C.Y_1.csv', sep=',',
     names=["time", "value"])
data_01 = data_01[:-2]
data_02 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/700II783C.Y_2.csv', sep=',',
     names=["time", "value"])
data_02 = data_02[:-1]
p1700II783CY = pd.concat([data_01, data_02],ignore_index = True)
p1700II783CY['value'] = pd.to_numeric(p1700II783CY['value'], errors= 'coerce')

#700II782CY(p1)
data_01 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/700II782C.Y_1.csv', sep=',',
     names=["time", "value"])
data_01 = data_01[:-2]
data_02 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/700II782C.Y_2.csv', sep=',',
     names=["time", "value"])
data_02 = data_02[:-1]
p1700II782CY = pd.concat([data_01, data_02],ignore_index = True)
p1700II782CY['value'] = pd.to_numeric(p1700II782CY['value'], errors= 'coerce')

#700II781CY(p1)
data_01 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/700II781C.Y_1.csv', sep=',',
     names=["time", "value"])
data_01 = data_01[:-2]
data_02 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/700II781C.Y_2.csv', sep=',',
     names=["time", "value"])
data_02 = data_02[:-1]
p1700II781CY = pd.concat([data_01, data_02],ignore_index = True)
p1700II781CY['value'] = pd.to_numeric(p1700II781CY['value'], errors= 'coerce')

#700FIC028Y(p1)
data_01 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/700FIC028.Y_1.csv', sep=',',
     names=["time", "value"])
data_01 = data_01[:-2]
data_02 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/700FIC028.Y_2.csv', sep=',',
     names=["time", "value"])
data_02 = data_02[:-1]
p1700FIC028Y = pd.concat([data_01, data_02],ignore_index = True)
p1700FIC028Y['value'] = pd.to_numeric(p1700FIC028Y['value'], errors= 'coerce')


# -------------------------------------------------------------------------------------------------------

## P1
# WWCON.Y
data_01 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/WWCON.Y_1.csv', sep=',',
     names=["time", "value"])
data_01 = data_01[:-2]
data_02 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/WWCON.Y_2.csv', sep=',',
     names=["time", "value"])
data_02 = data_02[:-1]
WWCONY = pd.concat([data_01, data_02],ignore_index = True)

# WWAI781B.Y
data_01 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/WWAI781B.Y_1.csv', sep=',',
     names=["time", "value"])
data_01 = data_01[:-2]
data_02 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/WWAI781B.Y_2.csv', sep=',',
     names=["time", "value"])
data_02 = data_02[:-1]
WWAI781BY = pd.concat([data_01, data_02],ignore_index = True)

# WWAI781A.Y
data_01 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/WWAI781A.Y_1.csv', sep=',',
     names=["time", "value"])
data_01 = data_01[:-2]
data_02 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/WWAI781A.Y_2.csv', sep=',',
     names=["time", "value"])
data_02 = data_02[:-1]
WWAI781AY = pd.concat([data_01, data_02],ignore_index = True)

# TI484001.PV
data_01 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/TI484001.PV_1.csv', sep=',',
     names=["time", "value"])
data_01 = data_01[:-2]
data_02 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/TI484001.PV_2.csv', sep=',',
     names=["time", "value"])
data_02 = data_02[:-1]
TI484001PV = pd.concat([data_01, data_02],ignore_index = True)

# NAFI005.Y
data_01 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/NAFI005.Y_1.csv', sep=',',
     names=["time", "value"])
data_01 = data_01[:-2]
data_02 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/NAFI005.Y_2.csv', sep=',',
     names=["time", "value"])
data_02 = data_02[:-1]
NAFI005Y = pd.concat([data_01, data_02],ignore_index = True)

# AI481779.PV
data_01 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/AI481779.PV_1.csv', sep=',',
     names=["time", "value"])
data_01 = data_01[:-2]
data_02 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/AI481779.PV_2.csv', sep=',',
     names=["time", "value"])
data_02 = data_02[:-1]
AI481779PV = pd.concat([data_01, data_02],ignore_index = True)

# AI481777.PV
data_01 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/AI481777.PV_2016_2017.csv', sep=',',
     names=["time", "value"])
data_01 = data_01[:-2]
data_02 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/AI481777.PV_2018.csv', sep=',',
     names=["time", "value"])
data_02 = data_02[:-2]
data_03 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/AI481777.PV_2019.csv', sep=',',
     names=["time", "value"])
data_03 = data_03[:-1]
AI481777PV = pd.concat([data_01, data_02, data_03],ignore_index = True)

# AI481776.PV
data_01 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/AI481776.PV_1.csv', sep=',',
     names=["time", "value"])
data_01 = data_01[:-2]
data_02 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/AI481776.PV_2.csv', sep=',',
     names=["time", "value"])
data_02 = data_02[:-1]
AI481776PV = pd.concat([data_01, data_02],ignore_index = True)

# AI481774.PV
data_01 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/AI481774.PV_1.csv', sep=',',
     names=["time", "value"])
data_01 = data_01[:-2]
data_02 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/AI481774.PV_2.csv', sep=',',
     names=["time", "value"])
data_02 = data_02[:-1]
AI481774PV = pd.concat([data_01, data_02],ignore_index = True)

# AI481773.PV
data_01 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/AI481773.PV_2016_2017.csv', sep=',',
     names=["time", "value"])
data_01 = data_01[:-2]
data_02 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/AI481773.PV_2018.csv', sep=',',
     names=["time", "value"])
data_02 = data_02[:-2]
data_03 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/AI481773.PV_2019.csv', sep=',',
     names=["time", "value"])
data_03 = data_03[:-1]
AI481773PV = pd.concat([data_01, data_02, data_03],ignore_index = True)

# LIT481773.PV
data_01 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/LIT481773.PV_1.csv', sep=',',
     names=["time", "value"])
data_01 = data_01[:-2]
data_02 = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/LIT481773.PV_2.csv', sep=',',
     names=["time", "value"])
data_02 = data_02[:-1]
LIT481773PV = pd.concat([data_01, data_02],ignore_index = True)

# WWCOD002.L // Y변수
WWCOD002L = pd.read_csv('C:/Users/dongju/Desktop/20190716/P1, P2/WWCOD002.L.csv', sep=',',
                        names=["time", "value"])
WWCOD002L = WWCOD002L[:-1]
WWCOD002L= pd.DataFrame(WWCOD002L)
print(WWCOD002L.info())


# Step 2: 데이터 프레임으로 만들기
x_df = pd.DataFrame(data = {'time':SWRF001Y['time'],'SWRF001Y' : SWRF001Y['value'],'SWFC004Y':SWFC004Y['value'],'SWFC001Y': SWFC001Y['value'],
                             'SORF001Y': SORF001Y['value'], 'SOFC007Y': SOFC007Y['value'], 'SOFC002Y': SOFC002Y['value'],
                             'CULC508Y':CULC508Y['value'], 'CULC501Y': CULC501Y['value'],'CUFI008Y': CUFI008Y['value'],
                             'p1700LI770BY':p1700LI770BY['value'], 'p1700II783CY': p1700II783CY['value'], 'p1700II782CY':p1700II782CY['value'],
                             'p1700II781CY':p1700II781CY['value'], 'p1700FIC028Y':p1700FIC028Y['value'], 'WWCONY': WWCONY['value'],
                             'WWAI781BY': WWAI781BY['value'], 'WWAI781AY': WWAI781AY['value'], 'TI484001PV': TI484001PV['value'],
                             'NAFI005Y':NAFI005Y['value'],'AI481779PV':AI481779PV['value'],'AI481777PV':AI481777PV['value'],
                             'AI481776PV':AI481776PV['value'],'AI481774PV':AI481774PV['value'],'AI481773PV': AI481773PV['value'],
                             'LIT481773PV':LIT481773PV['value']}) #여기에 Y변수 추가하기
print(x_df)
# 결측치 빼고 평균을 채우고
# 정각 단위로 만든 다음에
# merge
# 그 time lag 적용한 
'''aaa = x_df.iloc[0:50000, 0:6]
print(aaa)

aaa.shape()

x_df_01 = pd.merge(WWCOD002L, x_df, on = 'time')
print(x_df_01)'''
# csv로 저장하기
x_df.to_csv('C:/Users/dongju/Desktop/x_df.csv', na_rep='NaN')

# Y변수를 추가하여 데이터프레임 만들기
# 방법 1
'''y_time = WWCOD002L['time']
# x_df['WWCOD002L'] = ''
empty_list = []

# 새로운 칼럼에 값 넣기
for i in range():
     for j in range():
          if WWCOD002L['time'][i] == x_df['time'][j]:
               x_df['WWCOD002L'][j] = WWCOD002L['value'][i]
               i = i + 1
               j = j + 1
          else:
               j = j + 1

#print(x_df)
x_df.to_csv('C:/Users/dongju/Desktop/x_df_test.csv', na_rep='NaN')'''

'''for i in range(500):
     for j in range(500):
          if WWCOD002L['time'][i] == x_df['time'][j]:
               # 리스트에 추가하고

          else:
               # 틀리면 NA값을 넣고'''

# 방법 2: 24시간 마다 값 넣기 (이 방법은 안됨 y변수가 24시간마다 있지 않음)
# 방법 1-1: 빈 리스트 만들고, 거기에 y값 넣어서 x 변수 데이터 프레임에 추가하기 (row 수 맞추기)
# 방법 3: x_df 데이터 프레임과 같은 row를 가진 y변수 리스트 만들고 -> 리스트를 데이터 프레임으로 전환 -> 데이터 프레임에 추가
#print(WWCOD002L)
'''y_list = SWRF001Y['value']
for i in range(100):
     for j in range(100):
          if SWRF001Y['time'][i] == WWCOD002L['time'][j]: # i는 비교변수 j는 y변수
          # WWCOD002L값을 y_list에 넣고
               y_list[i] = WWCOD002L['value'][j]
               j = j +1
          else:
               # 아니면 na값(혹은 '')을 넣어주기
               y_list[i] = ''
     i = i +1

print(y_list)
print(len(y_list))
print(y_list[:425])'''

'''standard_date = []
standard_date = WWCOD002L['time']
subset_SWRF001Y_time = []
subset_SWRF001Y_value = []

for i in range(10):
    for j in range(10):
        if standard_date[i] == SWRF001Y['time'][j]:
               # subset_SWRF001Y = SWRF001Y[i][시간] & [value]
               #subset_SWRF001Y[,1] = SWRF001Y['time'][i] == standard_date[i]
               #subset_SWRF001Y[,2] = SWRF001Y['value'][i]
            subset_SWRF001Y_time = SWRF001Y['time'][j]
            subset_SWRF001Y_value = SWRF001Y['value'][j]
            i = i+1
            j = j+1
            print(subset_SWRF001Y_time)
            print(subset_SWRF001Y_value)
        else:
            j = j+1
#subset_SWRF001Y = pd.DataFrame(data=[subset_SWRF001Y_time, subset_SWRF001Y_value], index=range(0, len(p1700BSW012L)), columns=['time','value'])
subset_SWRF001Y = pd.DataFrame(data=[subset_SWRF001Y_time, subset_SWRF001Y_value],  columns=['time','value'])
print(subset_SWRF001Y)

standard_date = []
standard_date = WWCOD002L['time']

subset_SWRF001Y_time = []
subset_SWRF001Y_value = []
for i in range(10):  # len(WWCOD002L)
     for j in range(10): # len(SWRF001Y)
          if standard_date[i] == SWRF001Y['time'][j]:
               # subset_SWRF001Y = SWRF001Y[i][시간] & [value]
               #subset_SWRF001Y[,1] = SWRF001Y['time'][i] == standard_date[i]
               #subset_SWRF001Y[,2] = SWRF001Y['value'][i]
               subset_SWRF001Y_time= SWRF001Y['time'][j] == standard_date[i]
               subset_SWRF001Y_value = SWRF001Y['value'][i]
               i = i+1
               j = j+1
          else:
               j = j+1
#subset_SWRF001Y = pd.DataFrame(data=[subset_SWRF001Y_time, subset_SWRF001Y_value], index=range(0, len(WWCOD002L)), columns=['time','value'])
subset_SWRF001Y = pd.DataFrame(data=[subset_SWRF001Y_time, subset_SWRF001Y_value],  columns=['time','value'])

print(subset_SWRF001Y)
'''
