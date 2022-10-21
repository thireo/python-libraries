import math


def chu_harrington_calc(freq, radius):
    print("Frequency:\t%.2f MHz"%(freq/1e6))
    print("Radius:\t\t"+str(radius)+"m")
    c = 300e6
    la = c/freq
    k = (2*math.pi)/(la)
    gmax = (k*radius)*(k*radius)+2*k*radius
    gdbi = 10*math.log10(gmax)
    print("Max gain:\t%.2f"%gmax)
    print("Max gain:\t%.2f dB"%gdbi)

if __name__ == '__main__':
    import sys
    import argparse
    parser = argparse.ArgumentParser(description="Calculates Chu Harrington limit for antenna with frequence [f] and minimum volume radius [r]")
    parser.add_argument("-f", "--frequency", dest='freq',default='1', required=True,help='Frequency [Hz]')
    parser.add_argument("-r","--radius", dest="radius",default=1,required=True,help='Radius of smallest volume that contains entire antenna [m]')
    args = parser.parse_args(sys.argv[1:])
    chu_harrington_calc(float(args.freq),float(args.radius))