# License
'''
Code by Pranjal Singh
April 14,2020
Released under GNU GPL
'''

#Bode plot using scipy in python
from scipy import signal
import matplotlib.pyplot as plt
from pylab import*
from control.matlab import *

#Defining the transfer function 
s1 = signal.lti([1, 0.5],[1,2,1,0.5])
sys = tf([1, 0.5],[1,2,1,0.5])

#signal.bode takes transfer function as input and returns frequency,magnitude and phase arrays
w,mag,phase = signal.bode(s1)
gm, pm, wg, wp = margin(sys)
print("The Phase margin is:",pm)
print("The Gain Margin is:", gm)  #printing the phase margin of the system
subplot(2,1,1)
#plt.xlabel('Frequency(rad/s)')
plt.ylabel('Mag(deg)')
plt.title('Magnitude plot')
plt.semilogx(w, mag,'b')        # Bode Magnitude plot
plt.grid() 

subplot(2,1,2)
plt.xlabel('Frequency(rad/s)')
plt.ylabel('Phase(deg)')
plt.title('Phase plot')
plt.semilogx(w,phase)          # Bode phase plot
plt.grid() 




plt.show()
