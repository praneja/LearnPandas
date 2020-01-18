import matplotlib.pyplot as plt
import numpy as np

# plt.plot([1,2,3,4,5])
# plt.xlabel("Keys")
# plt.ylabel("Some Numbers")
# plt.show()

# plt.plot([1,2,3,4,5],[1,4,9,16,25])
# plt.xlabel("Keys")
# plt.ylabel("Some Numbers")
# plt.show()

# plt.plot([1,2,3,4,5],[1,4,9,16,25],"ro")
# plt.axis([0,6,0,20])
# plt.ylabel("Some Numbers")
# plt.show()

arr = np.arange(0.0,5.0,0.2)
plt.plot(arr,arr,"r--",arr,arr**2,"bs",arr,arr**3,"g^")
plt.show()