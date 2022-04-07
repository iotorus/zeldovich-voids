import numpy as np
import pynbody
import matplotlib.pyplot as plt

# Load the snapshots
s = pynbody.load('snapshot_data/snapshot_001') # Snapshot at z=0
h = s.halos()
m = []
for i in range(1,len(h)):
    m.append(h[i]['mass'].sum())
plt.hist(m, bins=50, log=True)
plt.savefig('histogram.pdf')
