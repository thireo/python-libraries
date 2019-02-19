import logcattimediffer as ltd
import os

for file in os.listdir('C:/Users/at/Desktop/Nokia31/'):
    if('dctlogfile' in file):
        ltd.getTimeDiffs(file,'True')
