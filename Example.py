import Proteus as Pt

system = Pt.Signal(10,0.0001)

system.Add_PWM(low_voltage=0,high_voltage=5,pulse_width=75,period=2)
system.Generate_Graph()
system.Generate_File("signal PWM")

system.Clear_Signal()
system.Add_Sinusoidal(Amplitud=5,Frecuency=60)
system.Add_Sinusoidal(Amplitud=2,Frecuency=25)
system.Add_Sinusoidal(Amplitud=3,Frecuency=100,start_time=1/60)
system.Generate_Graph(min_x=0,max_x=3/60)
system.Generate_File("signalSenosidal")

system.Clear_Signal()
system.Generate_AM_Signal(amplitud=5,frecuency1=500,frecuency2=10)
system.Generate_Graph(min_x=0,max_x=0.2)
system.Generate_File("signalAM")

system.Clear_Signal()
system.Generate_FM_Signal(amplitud=5,frecuency1=60,frecuency2=130,period=0.05)
system.Generate_Graph(min_x=0,max_x=0.2)
system.Generate_File("signalFM")