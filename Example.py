import Proteus as Pt
import numpy as np
import matplotlib.pyplot as plt


system = Pt.Signal(10,0.0001)
system.Add_PWM(low_voltage=0,high_voltage=5,pulse_width=50,period=2)
system.Add_Sinusoidal(Amplitud=5,Frecuency=60,noise=0.05)
system.Add_Sinusoidal(Amplitud=2,Frecuency=135,noise=0.15)
system.Generate_File("signal1")


X = system.t
Y = system.signal

plt.plot(X,Y)
plt.grid()
plt.show()

