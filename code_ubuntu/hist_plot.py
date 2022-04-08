import numpy as np
import pynbody
import matplotlib.pyplot as plt

# Load the snapshots
s = pynbody.load('snapshot_data/snapshot_001') # Snapshot at z=0
h = s.halos()
m = []
for i in tqdm(range(1,len(h)),desc='Collecting masses...'):
    m.append(h[i]['mass'].sum())
n, bins, patches = plt.hist(m, bins=8, log=True, alpha=0.75, density=True, facecolor='green')
plt.xlabel('Number of halos with this Mass')
plt.ylabel('Probability')
plt.title('Halo counts ')
plt.grid(True)
plt.show()
plt.savefig('histogram.pdf')
