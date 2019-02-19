
import argparse
import sys
import calendar
from datetime import datetime
import matplotlib.pyplot as pl
import os, sys
class HiddenPrints:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout

def main(argv):

    parser = argparse.ArgumentParser(description="Does stuff")
    parser.add_argument("-f", "--filename", dest='filename',default= '', required=True,help='filenamo')
    parser.add_argument("-p","--plot", dest="plot",default=False,required=True,help='PLOOTT')
    parser.add_argument("-v","--verbose", dest="verbose",default=False,required=False,help='print everything')
    args = parser.parse_args(argv)
    if args.verbose == 'False' or args.verbose == 'false':
        with HiddenPrints():
            getTimeDiffs(args.filename,args.plot)
    else:
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
                splitlines = line.split(' : ')
                try:
                    date = datetime.strptime(splitlines[0],'%H:%M:%S:%f')
                    times.append(splitlines[0])
                    current_time =calendar.timegm(date.utctimetuple())
                    if(count > 0):
                        timediffs.append((abs((current_time-last_time))))
                    last_time = current_time
                    count += 1
                except ValueError:
                    print('Didn\'t find timestamp on line:\t',count)
                #count += 1
                line = file.readline()

            if(count > 0):
                print('Max. time difference [min]:\t',max(timediffs)/60,' @ ',timediffs.index(max(timediffs)))
                print('Before:\t\t\t\t',times[timediffs.index(max(timediffs))])
                print('After:\t\t\t\t',times[timediffs.index(max(timediffs))+1])
                #print('Plotting time differences:\t', shouldPlot)
                if shouldPlot == 'True' or shouldPlot == 'true':
                    print('Plotting ',filename,'\'s time differences')
                    pl.plot(timediffs)
                    pl.xlabel('Samples [n]')
                    pl.ylabel('Time difference [min]')
                    pl.title(filename)
                    pl.xlim(0,count)
                    pl.ylim(0,30)
                    pl.show()
    except FileNotFoundError:
        print('File not found')



if __name__ == '__main__':
    import sys
    main(sys.argv[1:])