from max30100 import MAX30100
import time
import csv
from scipy.signal import butter, lfilter

sensor = MAX30100()

sensor.enable_spo2()

filename = "ppg_data.csv"

with open(filename, "w") as csv_file:
    writer = csv.writer(csv_file, delimiter=",")
    writer.writerow(["Red", "IR"])

    while True:
        red, ir = sensor.read_sequential()
        
        # Filter the PPG signals
        lowcut = 0.5  # Lower cutoff frequency (Hz)
        highcut = 10.0  # Upper cutoff frequency (Hz)
        fs = 100.0  # Sampling rate (Hz)
        nyquist = 0.5 * fs
        low = lowcut / nyquist
        high = highcut / nyquist
        order = 2
        b, a = butter(order, [low, high], btype="band")
        red_filtered = lfilter(b, a, red)
        ir_filtered = lfilter(b, a, ir)
        
        print("Red: {0}, IR: {1}".format(red_filtered, ir_filtered))
        writer.writerow([red_filtered, ir_filtered])
        time.sleep(0.1)
