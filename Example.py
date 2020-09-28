import Proteus as Pt
import numpy as np
import matplotlib.pyplot as plt

Ts = 0.0001
Tsimu = 3/60

t = np.arange(0,Tsimu+Ts,Ts)
t = t[:,np.newaxis]

low_voltage = -4 #[V]
high_voltage = 4 #[V]
pulse_width = 70 #[%]
frecuency = 60 #[Hz]
#periodo = 1 #[s]
sample_time = 0
#


signal = Pt.PWM(t,low_voltage,high_voltage,pulse_width,frecuency = 60,sample_time = 0.01,end_time=0.03)



plt.plot(t,signal)
plt.show()





