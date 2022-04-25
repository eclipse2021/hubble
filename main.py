import csv

c = 299792458 #[m/s]

rawdata = open("COMBO17.csv",'r') #Mcz = col6 ;vmag=col12;; 571fs = col38
rdr = csv.reader(rawdata)

data = open("COMBO17modified.csv", 'w', newline = '')
wrt = csv.writer(data)

#
for obj in rdr:
    ID = obj[0]
    if ID == "Nr":
        continue
    m = float(obj[37])
    M = float(obj[13])
    Mcz = float(obj[5])
    #distance = np.power(10, ((m - M)/5) + 1) * 0.000001 #[Mpc]
    distance = (10 ** ((m - M)/5 + 1)) * 0.00001
    speed = Mcz * c * 0.001# [km/s]
    print (ID,';DIST',distance,';SPEED',speed,';H',speed/distance)
    input()

#

data.close()
rawdata.close()
