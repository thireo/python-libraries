import calendar
from datetime import datetime
import matplotlib.pyplot as pl
import argparse
import sys

def main(argv):
    parser = argparse.ArgumentParser(description="Does stuff")
    parser.add_argument("-f", "--filename", dest='filename',default= '', required=True,help='filenamo')
    parser.add_argument("-p","--plot", dest="plot",default=False,required=True,help='PLOOTT')
    #parser.add_argument("-q", "--quiet",action="store_false", dest="verbose", default=True,help="don't print status messages to stdout")
    #for arg in argv:
    args = parser.parse_args(argv)
    getTimeDiffs(args.filename,args.plot)

def getTimeDiffs(filename,shouldPlot):
    try:
        with open(filename,'r') as file:
            line = file.readline()
            count = 0
            last_time = 0
            timediffs = []
            times = []
            while line:
                #print(str(count))
                splitlines = line.split(' : ')
                try:
                    date = datetime.strptime(splitlines[0],'%H:%M:%S:%f')
                    times.append(splitlines[0])
                    current_time =calendar.timegm(date.utctimetuple())
                    #print((current_time-last_time))
                    if(count > 0):
                        timediffs.append((abs((current_time-last_time))))
                    last_time = current_time
                except ValueError:
                    print('Found non-timestamp on line:\t',count)
                count += 1
                line = file.readline()
        print('Max. time difference [min]:\t',max(timediffs)/60,' @ ',timediffs.index(max(timediffs)))
        print('Before:\t\t\t\t',times[timediffs.index(max(timediffs))])
        print('After:\t\t\t\t',times[timediffs.index(max(timediffs))+1])
        print('Plotting time differences:\t', shouldPlot)
        if shouldPlot == 'True' or shouldPlot == 'true':
            pl.plot(timediffs)
            pl.show()
    except FileNotFoundError:
        print('File not found')



if __name__ == '__main__':
    import sys
    main(sys.argv[1:])