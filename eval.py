import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


record_template = {2:0, 3:0, 4:0, 5:0, 6:0}
summary = {
    'Average': dict(record_template),
    'Minimum': dict(record_template),
    'Maximum': dict(record_template)
}

df = pd.read_csv("message_records_2X.csv")
y = df.iloc[:,1][:83]
summary['Average'][2] = np.average(y)
summary['Minimum'][2] = np.amin(y)
summary['Maximum'][2] = np.amax(y)

df = pd.read_csv("message_records_3X.csv")
y = df.iloc[:,1][:83]
summary['Average'][3] = np.average(y)
summary['Minimum'][3] = np.amin(y)
summary['Maximum'][3] = np.amax(y)

df = pd.read_csv("message_records_X.csv")
y = df.iloc[:,1][:83]
summary['Average'][4] = np.average(y)
summary['Minimum'][4] = np.amin(y)
summary['Maximum'][4] = np.amax(y)

df = pd.read_csv("message_records_5X.csv")
y = df.iloc[:,1][:83]
summary['Average'][5] = np.average(y)
summary['Minimum'][5] = np.amin(y)
summary['Maximum'][5] = np.amax(y)

df = pd.read_csv("message_records_6X.csv")
y = df.iloc[:,1][:83]
summary['Average'][6] = np.average(y)
summary['Minimum'][6] = np.amin(y)
summary['Maximum'][6] = np.amax(y)

print(summary)