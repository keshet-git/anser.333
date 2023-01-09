import matplotlib.pyplot as plt
import numpy as np
Data = np.random.randn(1000)
#plt.hist(Data)

#========
#plt.hist(Data,5)

# Show and clean up plot
#plt.show()
#plt.clf()
#====
# Change the line plot below to a scatter plot
plt.hist(Data,20)

# Show and clean up again
plt.show()
plt.clf()