import Proteus as Pt

system = Pt.Signal(10,0.0001)
system.Generate_AM_Signal(amplitud=5,frecuency1=500,frecuency2=10)
system.Generate_Graph(min_x=0,max_x=0.2)
system.Generate_File("signal1")
