import numpy as np


def PWM(t,low_voltage,high_voltage,pulse_width,periodo=0,frecuency=0,sample_time=0,end_time=0):
    operacion = lambda x, min, max: np.logical_and(x > min, x < max)
    if periodo == 0 and frecuency!= 0:
        periodo = 1/frecuency

    if end_time == 0:
        end_time = float(max(t))

    space = periodo * (pulse_width / 100)
    signal = np.zeros([t.shape[0],1])

    num_periodos = round(end_time/periodo)
    print(num_periodos)


    for i in range(num_periodos):
        start = sample_time + periodo * i
        stop = sample_time + periodo * i + space
        if stop>end_time:
            stop = end_time
        signal = np.logical_or(signal, operacion(t, start, stop))

    signal = signal*1

    signal[signal == 0] = low_voltage
    signal[signal == 1] = high_voltage

    #Eliminate DC gain
    dc_gain = np.zeros([t.shape[0],1])

    dc_gain = np.logical_or(dc_gain,operacion(t,-1,sample_time))
    dc_gain = np.logical_or(dc_gain,operacion(t,end_time,float(max(t))+1))

    dc_gain = low_voltage*dc_gain

    signal-= dc_gain

    return signal















#












