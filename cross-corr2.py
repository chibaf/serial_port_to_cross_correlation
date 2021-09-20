#numpy version
import numpy as np
import serial, sys, time
import matplotlib.pyplot as plt

ser=serial.Serial(sys.argv[1],19200)  # sys.argv[1]=serial port
print("connected to: " + ser.portstr)
time.sleep(2)
i=0
d1=np.empty(0)
d2=np.empty(0)
f = open(sys.argv[2], "w")
while True:
  try:
	  line = ser.readline()
	  line2=line.strip().decode('utf-8')
	  data = [str(val) for val in line2.split(",")]
	#  print(line2)
	  if i<100 and len(data)==2 and data[0]!="" and data[1]!="":
	    d1=np.append(d1,np.float(data[0]))
	    d2=np.append(d2,np.float(data[1]))
	    i=i+1
	  else:
	#    x=range(len(d1)) #plot array
	#    plt.plot(x,d1)
	#    plt.show()
	#    plt.plot(x,d2)
	#    plt.show()
	    c=1.0/(np.linalg.norm(d1)*np.linalg.norm(d2))   # added on 16.Sep.2021
	    corr=np.empty(0)   #make nd.array of length zero
	    corr=np.append(corr,np.dot(d1,d2)*c)  # the first element of corr, modified on 16.Sep.2021
	    for i in range(len(d1)):
	      d2=np.roll(d2,-1)  # shift 1 to the left
	      corr=np.append(corr,np.dot(d1,d2)*c)   # cross correlation, modified on 16.Sep.2021
	    mx=np.amax(corr)
	    for i in range(len(corr)):
	      if corr[i]==mx:
	        ix=i
	        break
	    print(ix*0.1);f.write(str(0.1*ix)+"\n")
	#    x=range(len(corr)) #plot array
	#    plt.plot(x,corr)
	#    plt.show()
	    d1=np.empty(0)
	    d2=np.empty(0)
	    corr=np.empty(0)
	    i=0
  except KeyboardInterrupt:
    print ('exiting')
    f.close()
    break
