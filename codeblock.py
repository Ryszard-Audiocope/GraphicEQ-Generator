import numpy as np

# Load the data from the base and target files
base_data = np.loadtxt('target.txt', skiprows=1)
target_data = np.loadtxt('base.txt', skiprows=1)

# Define the target frequency points
target_freq_points = [20, 21, 22, 23, 24, 26, 27, 29, 30, 32, 34, 36, 38, 40, 43, 45, 48, 50, 53, 56, 59, 63, 66, 70, 74, 78, 83, 87, 92, 97, 103, 109, 115, 121, 128, 136, 143, 151, 160, 169, 178, 188, 199, 210, 222, 235, 248, 262, 277, 292, 309, 326, 345, 364, 385, 406, 429, 453, 479, 506, 534, 565, 596, 630, 665, 703, 743, 784, 829, 875, 924, 977, 1032, 1090, 1151, 1216, 1284, 1357, 1433, 1514, 1599, 1689, 1784, 1885, 1991, 2103, 2221, 2347, 2479, 2618, 2766, 2921, 3086, 3260, 3443, 3637, 3842, 4058, 4287, 4528, 4783, 5052, 5337, 5637, 5955, 6290, 6644, 7018, 7414, 7831, 8272, 8738, 9230, 9749, 10298, 10878, 11490, 12137, 12821, 13543, 14305, 15110, 15961, 16860, 17809, 18812, 19871]

# Extract the frequency and amplitude columns from the base and target data
base_freq = base_data[:, 0]
base_amp = base_data[:, 1]
target_freq = target_data[:, 0]
target_amp = target_data[:, 1]

# Calculate the required dB value of each frequency in the base file based on the closest frequencies in the target file
req_db = np.interp(target_freq_points, base_freq, base_amp) - np.interp(target_freq_points, target_freq, target_amp)

# Normalize the required dB values to prevent clipping and make them audible
max_db = np.max(np.abs(req_db))
norm_db = np.clip(req_db / max_db, -1.0, 1.0) * 20.0
norm_db -= np.max(norm_db) # Subtract the maximum value to make it 0dB

# Write the normalized dB values to a text file
with open('output.txt', 'w') as f:
    f.write('GraphicEQ: ')
    for i, freq in enumerate(target_freq_points):
        f.write(f'{int(freq)} {norm_db[i]:.1f}; ')
    f.write('\n')
