#numpy version
import numpy as np
import serial, sys, time
import matplotlib.pyplot as plt

ser=serial.Serial(sys.argv[1], sys.argv[2])
print("connected to: " + ser.portstr)
time.sleep(1)
i=0
d1=np.empty(0)
d2=np.empty(0)
while True:
  line = ser.readline()
  line2=line.strip().decode('utf-8')
  data = [str(val) for val in line2.split(",")]
#  print(line2)
  if i<100 and len(data)==2 and data[0]!="" and data[1]!="":
    d1=np.append(d1,np.float(data[0]))
    d2=np.append(d2,np.float(data[1]))
    i=i+1
  else:
    print("i=100")
    print(len(d1))
    print(len(d2))
    x=range(len(d1)) #plot array
    plt.plot(x,d1)
    plt.show()
    plt.plot(x,d2)
    plt.show()
    c=1.0/(np.linalg.norm(d1)*np.linalg.norm(d2))   # added on 16.Sep.2021
    corr=np.empty(0)   #make nd.array of length zero
    corr=np.append(corr,np.dot(d1,d2)*c)  # the first element of corr, modified on 16.Sep.2021
    for i in range(len(d1)):
      d2=np.roll(d2,-1)  # shift 1 to the left
      corr=np.append(corr,np.dot(d1,d2)*c)   # cross correlation, modified on 16.Sep.2021
    mx=np.amax(corr)
    print(mx)
    for i in range(len(corr)):
      if corr[i]==mx:
        ix=i
        break
    print(ix)
    x=range(len(corr)) #plot array
    plt.plot(x,corr)
    plt.show()
    d1=np.empty(0)
    d2=np.empty(0)
    corr=np.empty(0)
    i=0
#    ser.close()
#    break

#m=np.loadtxt(sys.argv[1],delimiter=',')  # convert a csv file to a matrix from file sys.argv[1]
#mt=m.T #transpose matrix

#computing cross-correlation
#v1=mt[1][12000:15000];v2=mt[2][12000:15000]
#c=np.linalg.norm(v1)*np.linalg.norm(v2)   # added on 16.Sep.2021
#corr=np.empty(0)   #make nd.array of length zero
#corr=np.append(corr,np.dot(v1,v2)*c)  # the first element of corr, modified on 16.Sep.2021
#for i in range(len(v1)):
#  v2=np.roll(v2,-1)  # shift 1 to the left
#  corr=np.append(corr,np.dot(v1,v2)*c)   # cross correlation, modified on 16.Sep.2021

# find index of maximum element of corr
#mx=np.amax(corr)
#print(mx)
#for i in range(len(corr)):
#  if corr[i]==mx:
#    ix=i
#    break
#print(ix)

#output the result to file sys.argv[2]
#f = open(sys.argv[2], 'w') 
#st=str(corr[0])
#for i in range(1,len(corr)):
#  if i!=(len(corr)-1):
#    st=st+","+str(corr[i])
#  else:
#    st=st+str(corr[i])+"\n"
#f.write(st)
#f.write(str(ix))
#f.close()
#
## plot the result
#x=range(len(corr)) #plot array
#plt.plot(x,corr)
#plt.show()
