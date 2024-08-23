import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

NUM_LEVELS = 8
band_structure = []
energy_band = [ [] for _ in range(NUM_LEVELS) ]
print(energy_band)

with open('silicon.bands.out') as input_data:
    # Skips text before the beginning of the interesting block:
    for line in input_data:
        if line.strip() == 'End of band structure calculation':  # Or whatever test is needed
            break
    # Reads text until the end of the block:
    for line in input_data:  # This keeps reading the file
        if 'Writing all to output data dir' in line.strip():
            break
        stripped = line.strip()
        if((stripped != '') and (not stripped.startswith('k ='))):
            energy_levels = np.asarray(stripped.split(), dtype=float) 
            for i in range(len(energy_levels)):
                energy_band[i].append(energy_levels[i])
for i in range(NUM_LEVELS):
    plt.plot(energy_band[i])
plt.ylabel('eV')
plt.show()
                