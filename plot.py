import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv("message_records_2X.csv")
x = df.iloc[:,0]
y = df.iloc[:,1]
#fit = np.polyfit(x,y,1)
#fit_line = np.poly1d(fit)
plt.plot(x, y, c='b', marker='.', label='2 Devices')
#plt.plot(x,y, 'yo', x, fit_line(x), 'r')

df = pd.read_csv("message_records_3X.csv")
x = df.iloc[:,0]
y = df.iloc[:,1]
#fit = np.polyfit(x,y,1)
#fit_line = np.poly1d(fit)
plt.plot(x, y, c='g', marker='.', label='3 Devices')
#plt.plot(x,y, 'ko', x, fit_line(x), 'r')

df = pd.read_csv("message_records_X.csv")
x = df.iloc[:,0]
y = df.iloc[:,1]
#fit = np.polyfit(x,y,1)
#fit_line = np.poly1d(fit)
plt.plot(x, y, c='r', marker='.', label='4 Devices')
#plt.plot(x,y, 'co', x, fit_line(x), 'r')

df = pd.read_csv("message_records_5X.csv")
x = df.iloc[:,0]
y = df.iloc[:,1]
#fit = np.polyfit(x,y,1)
#fit_line = np.poly1d(fit)
plt.plot(x, y, c='c', marker='.', label='5 Devices')
#plt.plot(x,y, 'co', x, fit_line(x), 'r')

df = pd.read_csv("message_records_6X.csv")
x = df.iloc[:,0]
y = df.iloc[:,1]
#fit = np.polyfit(x,y,1)
#fit_line = np.poly1d(fit)
plt.plot(x, y, c='m', marker='.', label='6 Devices')
#plt.plot(x,y, 'co', x, fit_line(x), 'r')

plt.xlabel('Time intervals (minutes)')
plt.ylabel('Packet success rate')
plt.ylim(0.2, 1)
plt.xlim(0, 25200)
plt.legend(loc='lower right')
#plt.title('Four device setup')
plt.savefig('Mess_Rec_4.png')