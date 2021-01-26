import numpy as np
from scipy.io import wavfile

seed=8
np.random.seed(seed)
sample_rate = 44100

sweep = []
cycles = 100
freq_sweep = np.arange(20,22050,0.1)
rand_freq = 82 + 250*np.random.normal(0,1,1000)
rand_duration = (np.random.rand(1000)*0 + 1)/10
bpm=115
fixed_duration = 4*(60/bpm)*(1/16)
for i, f in enumerate(rand_freq):
    #x = np.linspace(0,cycles*2*np.pi,int(cycles*44100/f))
    #t = np.arange(0,cycles/f,1/sample_rate)
    t = np.arange(0,fixed_duration,1/sample_rate)
    #tried to replicate a fat bass tone using pure sine waves.
    sweep.append((np.sin(2*np.pi*f*t)+0.1*np.sin((5/4)*2*np.pi*f*t)+np.sin(1.5*2*np.pi*f*t)+np.sin(2*2*np.pi*f*t))**5 \
                 +0.5*(np.sin(2*np.pi*f*t)+0.1*np.sin((5/4)*2*np.pi*f*t)+np.sin(1.5*2*np.pi*f*t)-np.sin(2*2*np.pi*f*t))**5)
    #sweep.append(np.zeros(sample_rate//100))
sweep = np.concatenate(tuple(sweep))
wavfile.write('random_riff_'+str(seed)+'.wav', sample_rate, sweep/np.max(sweep))