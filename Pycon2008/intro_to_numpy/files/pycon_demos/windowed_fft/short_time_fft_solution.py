# Short-time Fourier Transform
#   
#   The short-time Fourier Transform is implemented
#      by multiplying a segment of the data by some kind
#      of window function (boxcar, triangular, hamming, hanning, 
#      blackman, etc.) and then taking the Fourier transform.
#      This process is repeated on a shifted segment of the data
#      until all the data has been processed. 
#
#   In this excercise you will:
#  
#      1.  Read audio data from scale.wav (it takes the filename as 
#            input and returns the sample rate (in samples/sec) and 
#            waveform data as output.
#      2.  Perform the short-time Fourier transform on every 50 ms
#            of data.
#      3.  Create an image showing the frequency on the horizontal 
#            axis and the center-point window time on the 
#            vertical axis. 
#      4.  (Bonus):  Label the axes with correct units and labels.
#

# Import the required functions
from scipy.io.wavfile import read
from scipy.fftpack import fft, fftfreq, fftshift
from scipy.signal import get_window
from math import ceil
from pylab import figure, imshow, clf, gray, xlabel, ylabel

# Read in a wav file 
#   returns sample rate (samples / sec) and data
rate, data = read('scale.wav')

# Define the sample spacing and window size.
dT = 1.0/rate
T_window = 50e-3
N_window = int(T_window * rate)
N_data = len(data)

# 1. Get the window profile
window = get_window('hamming', N_window)

# 2. Set up the FFT
result = []
start = 0
while (start < N_data - N_window):
    end = start + N_window
    result.append(fftshift(fft(window*data[start:end])))
    start = end

result.append(fftshift(fft(window*data[-N_window:])))
result = array(result,result[0].dtype)

# Display results
freqscale = fftshift(fftfreq(N_window,dT))[150:-150]/1e3
figure(1)
clf()
imshow(abs(result[:,150:-150]),extent=(freqscale[-1],freqscale[0],(N_data*dT-T_window/2.0),T_window/2.0))
xlabel('Frequency (kHz)')
ylabel('Time (sec.)')
gray()




