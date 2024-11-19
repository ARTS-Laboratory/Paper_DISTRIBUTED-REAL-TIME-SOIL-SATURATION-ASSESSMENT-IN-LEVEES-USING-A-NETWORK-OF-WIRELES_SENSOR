# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 14:58:49 2024

@author: chypu
"""

# Importing libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import ScalarFormatter #n this example, ScalarFormatter is used to format the y-axis ticks in scientific notation. 
#%% plotting with specific parameters
plt.rcdefaults()
# Updating Parameters for Paper
params = {
    'lines.linewidth' :1,
    'lines.markersize' :0.5,
   'axes.labelsize': 8,
    'axes.titlesize':8,
    'axes.titleweight':'normal',
    'font.size': 8,
    'font.family': 'Times New Roman', # 'Times New RomanArial'
    'font.weight': 'normal',
    'mathtext.fontset': 'stix',
    'legend.shadow':'False',
   'legend.fontsize': 8,
   'xtick.labelsize':8,
   'ytick.labelsize':8,
   'text.usetex': False,
    'figure.autolayout': True,
   'figure.figsize': [3.5,2.5] # 6,4 for test3, ansys data 6,7
   }
plt.rcParams.update(params)

#%% new plot with linestyle only
#%% Reading data
filename = "data/combined_data_all_time_5spikes.csv" 

D1=pd.read_csv(filename,skiprows=1)
# X1=acceleration=D1.to_numpy()[:,3]#convert dataframe(csv file to numpy)
# time=D1.to_numpy()[:,0]
# TD=D1.to_numpy()[:,4]#TD average
# t1=D1.iloc[:,0] # time in second
t1=D1.iloc[:,0]/60 # time in minute
s1=D1.iloc[:,1] # spike 1
s2=D1.iloc[:,2] #spike 2
s3=D1.iloc[:,3] # spike 3
s4=D1.iloc[:,4] # spike 4
s5=D1.iloc[:,5] # spike 5

#%%
fig1 = plt.figure()
ax = fig1.add_subplot(111)
ax.plot(t1,s1,linestyle='-', label='spike 1')
ax.plot(t1,s2,linestyle='--', label='spike 2')
ax.plot(t1,s3,linestyle='-.', label='spike 3')
ax.plot(t1,s4,linestyle=':',label='spike 4')
ax.plot(t1,s5,linestyle='-', label='spike 5')
ax.plot([100/60,100/60],[1.055,-.04],'--',color='black',linewidth=1)# TS1
ax.plot([216/60,216/60],[1.055,-.04],'--',color='black',linewidth=1)# TS2
ax.plot([472/60,472/60],[1.055,-.04],'--',color='black',linewidth=1)# TS3
ax.plot([624/60,624/60],[1.055,-.04],'--',color='black',linewidth=1)# TS4
ax.plot([1402/60,1402/60],[1.055,-.04],'--',color='black',linewidth=1)# TS5
ax.plot([2339/60,2339/60],[1.055,-.04],'--',color='black',linewidth=1)# TS6
ax.legend(loc='lower right',bbox_to_anchor=(0.95,0.01),ncol=1,facecolor='white', edgecolor = 'black', framealpha=1)
plt.xlim(0,2365/60)
plt.ylim(-.04,1.055)
plt.xlabel('time (minute)') #sample points
plt.ylabel('voltage (v)')

plt.savefig('plots/5spikes_2D_plot_minute_3.5_mark_TS6.pdf', dpi=100)
plt.savefig('plots/5spikes_2D_plot_minute_3.5_mark_TS6.png', dpi=100)




