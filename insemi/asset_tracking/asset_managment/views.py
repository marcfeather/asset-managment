from django.http import HttpResponse
from django.shortcuts import render
import sqlite3

def index(request):
    en = ""
    er = ""

    p = {'e_n': en, 'e_r': er}
    #return render(request,'index.html',p)

    return render(request,'index.html',p)

def coordinates(rr1,rr2,rr3):
    # RSSI TO DISTANCE and distance of 3 gatways to point location of the beacon
    x1 = 0
    x2 = 0
    x3 = 20
    y1 = 0
    y2 = 20
    y3 = 10
    r1 = 10 ** ((-59 - (rr1)) / 20)
    r2 = 10 ** ((-59 - (rr2)) / 20)
    r3 = 10 ** ((-59 - (rr3)) / 20)

    y = (((x2 - x3) * ((x2 * x2 - x1 * x1) + (y2 * y2 - y1 * y1) + (r1 * r1 - r2 * r2)) - (x1 - x2) * (
                (x3 * x3 - x2 * x2) + (y3 * y3 - y2 * y2) + (r2 * r2 - r3 * r3))) / (
                     2 * ((y1 - y2) * (x2 - x3) - (y2 - y3) * (x1 - x2))))

    x = (((y2 - y3) * ((y2 * y2 - y1 * y1) + (x2 * x2 - x1 * x1) + (r1 * r1 - r2 * r2)) - (y1 - y2) * (
                (y3 * y3 - y2 * y2) + (x3 * x3 - x2 * x2) + (r2 * r2 - r3 * r3))) / (
                     2 * ((x1 - x2) * (y2 - y3) - (x2 - x3) * (y1 - y2))))

    return([-1*(x),-1*(y)])


def analyze(request):
    #Get the text
    djtn = request.GET.get('tn', 'default')
    djtr = request.GET.get('tr', 'default')

    en=""
    er=""

    if(djtn != 'admin'):
        en=en+"invalid username"
    #print(en)
    if(djtr != 'admin'):
        er="incorrect password"

    # p={'e_n':en}
    p = {'e_n': en, 'e_r': er}

    if (len(en + er) < 0):  # |||| need to be > 0 |||||||
        return render(request, 'index.html', p)


    cord = [[-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1],[-1, -1]]  # a dictionary to store the co-ordinates
    rss1 = [-12,-34,-53]        # RSSI values from gateway 1 of all 5 devices
    rss2 = [-23, -54, -13]   # RSSI values from gateway 2 of all 5 devices
    rss3 = [-92, -24, -73]    #RSSI values from gateway 3 to all 5 devices

    for i in range(0,3,1):
        d=coordinates(rss1[i],rss2[i],rss3[i])
        cord[i]=d

    cor={'x0':cord[0][0],'x1':cord[1][0],'x2':cord[2][0],'x3':cord[3][0],'x4':cord[4][0],'x5':cord[5][0],'x6':cord[6][0],'x7':cord[7][0],'x8':cord[8][0],'x9':cord[9][0],'y0':cord[0][1],'y1':cord[1][1],'y2':cord[2][1],'y3':cord[3][1],'y4':cord[4][1],'y5':cord[5][1],'y6':cord[6][1],'y7':cord[7][1],'y8':cord[8][1],'y9':cord[9][1]}
    print(cor)

    return render(request,'analyze.html',cor)

def gateway_1(request):

    cord=[0 for _ in range(10)]

    rss1 = [-12, -34, -53]

    for i in range(len(rss1)):

        cord[i] = 10 ** ((-59 - (rss1[i])) / 20)

    cor = {'x0': cord[0], 'x1': cord[1], 'x2': cord[2], 'x3': cord[3], 'x4': cord[4], 'x5': cord[5],
           'x6': cord[6], 'x7': cord[7], 'x8': cord[8], 'x9': cord[9]}
    print(cor)

    return render(request,'gateway_1.html',cor)





