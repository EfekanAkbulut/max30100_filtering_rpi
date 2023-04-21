# max30100_filtering_rpi

In this script, the PPG signals are filtered using a bandpass filter with a lower cutoff frequency of 0.5 Hz and an upper cutoff frequency of 10.0 Hz. The sampling rate is set to 100 Hz, which is the default sampling rate for the MAX30100 sensor. The filter coefficients are calculated using the butter function from the scipy.signal library, and the filtered signals are computed using the lfilter function.

Inside the while loop, the filtered PPG signals are printed to the console and written to the CSV file. The script waits for 100 milliseconds between each reading to avoid overwhelming the sensor.

When you run this modified script, it will continuously read PPG data from the sensor, filter the signals, and save the filtered signals to the "ppg_data.csv" file in the same directory as the script. The filtered signals can be visualized and analyzed in a spreadsheet program like Microsoft Excel.
