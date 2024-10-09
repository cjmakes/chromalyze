import matplotlib.pyplot as plt
import numpy as np
import sys

from chromalyze import chromalyze

num_bins=85

bgrs = chromalyze.get_colors(sys.argv[1], samplerate=0.1)
clrs = ['blue','green','red']
bottom = np.zeros(num_bins)

plt.hist(bgrs, num_bins, color=clrs, stacked=True)
plt.title('histogram of average color of frame')
plt.legend(clrs)
plt.savefig('hist.png')
