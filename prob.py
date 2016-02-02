import scipy.stats as stats
import matplotlib.pyplot as plt
import collections

x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]

count=collections.Counter(x)
for item in count:
	print item,"has a frequency of",count[item]


plt.boxplot(x)
plt.xlabel("Data Set")
plt.ylabel("Numbers")
plt.title("Box and Whisker Plot")
plt.savefig("BoxWhiskerPlot.png")

plt.hist(x,histtype="bar")
plt.xlabel("Numbers")
plt.ylabel("Frequency")
plt.title("Frequency of Numbers in Data Set")
plt.savefig("Histogram.png")


stats.probplot(x, dist="norm", plot=plt)
plt.savefig("QQplot.png")