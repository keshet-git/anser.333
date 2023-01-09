import matplotlib.pyplot as plt
import numpy as np
year = np.arange(1951,2020,1)
population  = np.array([2.583816786,2.630584384,2.677230358,2.724302468,2.772242535,2.821383444,2.871952278,
                        2.924081243,2.977824686,3.033212527,3.090305279,3.149244245,3.210271352,3.273670772,
                        3.339592688,3.408121405,3.479053821,3.5518807,3.625905514,3.70057765,3.7757909,
                        3.851545181,3.927538695,4.003448151,4.079087198,4.154287594,4.229201257,4.304377112,4.380585755,
                        4.458411534,4.537845777,4.618776168,4.701530843,4.786483862,4.873781796,4.963633228,
                        5.055636132,5.148556956,5.240735117,5.33094346,5.418758803,5.504401149,5.588094837,
                        5.670319703,5.751474416,5.83156502,5.910566295,5.988846103,6.066867391,6.145006989,
                        6.223412158,6.302149639,6.381408987,6.461370865,6.542159383,6.623847913,6.706418593,
                        6.789771253,6.873741054,6.958169159,7.043008586,7.128176935,7.213426452,7.298453033,
                        7.38300882,7.46696428,7.550262101,7.632819325,7.714576923])

#plt.yticks([0,1,2], ["one","two","three"])
#plt.plot(year,population)

# Definition of tick_val and tick_lab
#tick_val = [2, 3, 4, 5, 6, 7, 8]
#tick_lab = ['2b', '3b','4b','5b','6b','7b','8b']

# Adapt the ticks on the x-axis
#plt.yticks(tick_val,tick_lab)

# After customizing, display the plot
#plt.show()
#///////////////
x_data = np.arange(0,10)
y_data = np.array([2, 2.5, 3, 2.2 ,4 ,6, 5.5, 8, 7.7, 10])

#plt.scatter(x_data,y_data)

# display the plot
#plt.show()

s = np.array([20, 100, 200, 400, 70, 500, 800, 1500, 300, 900])

# Make a scatter plot:
#plt.scatter(x_data,y_data,2*s)

# display the plot
#
# plt.show()

cols = ['red','green','blue','yellow','pink','red','green','blue','yellow','pink']

# Make a scatter plot :
plt.scatter(x_data,y_data,4*s, c = cols, alpha = 0.8) # Alpha defines transparency

# display the plot
plt.show()