import numpy as np


to_delete = range(0, 22) + range(27, 75)
angles_to_print = []
angles = np.loadtxt('charges.txt')
for i, line in enumerate(angles):
    if i not in to_delete:
        angles_to_print.append(line)


np.savetxt('charges-new.txt', np.asarray(angles_to_print), fmt='%.4f')
