#!/usr/bin/env python
# a stacked bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt


# Transitional probabilities away from IV in CCLI-2011

N = 7
medians = (0.64, 0.00, 0.00, 0.00, 0.21, 0.00, 0.00)
confidenceIntervals = (0.12, 0.02, 0.00, 0.02, 0.12, 0.03, 0.00)
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, medians, width, color='#ddddff', yerr=confidenceIntervals)

plt.ylabel('Median probability')
plt.xticks(ind+width/2., ('IV-I', 'IV-II', 'IV-III', 'IV-IV', 'IV-V', 'IV-VI', 'IV-bVII') )
plt.yticks(np.arange(0,1,0.1))

plt.show()



# Transitional probabilities away from I in CCLI-2011

N = 7
medians = (0.00, 0.00, 0.00, 0.35, 0.33, 0.00, 0.00)
confidenceIntervals = (0.04, 0.03, 0.00, 0.12, 0.13, 0.08, 0.00)
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, medians, width, color='#ddddff', yerr=confidenceIntervals)

plt.ylabel('Median probability')
plt.xticks(ind+width/2., ('I-I', 'I-II', 'I-III', 'I-IV', 'I-V', 'I-VI', 'I-bVII') )
plt.yticks(np.arange(0,1,0.1))

plt.show()



# Transitional probabilities away from V in CCLI-2011

N = 7
medians = (0.25, 0.00, 0.00, 0.22, 0.00, 0.24, 0.00)
confidenceIntervals = (0.12, 0.06, 0.00, 0.11, 0.02, 0.12, 0.08)
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, medians, width, color='#ddddff', yerr=confidenceIntervals)

plt.ylabel('Median probability')
plt.xticks(ind+width/2., ('V-I', 'V-II', 'V-III', 'V-IV', 'V-V', 'V-VI', 'V-bVII') )
plt.yticks(np.arange(0,1,0.1))

plt.show()



# Transitional probabilities away from V in CCLI-2011 Cluster 0

N = 7
medians = (0.43, 0.03, 0.00, 0.24, 0.00, 0.20, 0.00)
confidenceIntervals = (0.17, 0.10, 0.00, 0.04, 0.10, 0.28, 0.00)
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, medians, width, color='#ddddff', yerr=confidenceIntervals)

plt.ylabel('Median probability')
plt.xticks(ind+width/2., ('V-I', 'V-II', 'V-III', 'V-IV', 'V-V', 'V-VI', 'V-bVII') )
plt.yticks(np.arange(0,1,0.1))

plt.show()


# Transitional probabilities away from V in CCLI-2011 Cluster 2

N = 7
medians = (0.08, 0.00, 0.00, 0.38, 0.00, 0.48, 0.00)
confidenceIntervals = (0.07, 0.03, 0.00, 0.15, 0.01, 0.21, 0.00)
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, medians, width, color='#ddddff', yerr=confidenceIntervals)

plt.ylabel('Median probability')
plt.xticks(ind+width/2., ('V-I', 'V-II', 'V-III', 'V-IV', 'V-V', 'V-VI', 'V-bVII') )
plt.yticks(np.arange(0,1,0.1))

plt.show()



# Transitional probabilities away from V in CCLI-2011 Cluster 3

N = 7
medians = (0.45, 0.00, 0.00, 0.02, 0.00, 0.29, 0.00)
confidenceIntervals = (0.16, 0.18, 0.00, 0.09, 0.02, 0.16, 0.02)
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, medians, width, color='#ddddff', yerr=confidenceIntervals)

plt.ylabel('Median probability')
plt.xticks(ind+width/2., ('V-I', 'V-II', 'V-III', 'V-IV', 'V-V', 'V-VI', 'V-bVII') )
plt.yticks(np.arange(0,1,0.1))

plt.show()


# Transitional probabilities away from V in CCLI-2011 Cluster 4

N = 7
medians = (0.25, 0.00, 0.00, 0.63, 0.00, 0.00, 0.00)
confidenceIntervals = (0.40, 0.04, 0.00, 0.42, 0.00, 0.05, 0.00)
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, medians, width, color='#ddddff', yerr=confidenceIntervals)

plt.ylabel('Median probability')
plt.xticks(ind+width/2., ('V-I', 'V-II', 'V-III', 'V-IV', 'V-V', 'V-VI', 'V-bVII') )
plt.yticks(np.arange(0,1,0.1))

plt.show()

