import matplotlib.pyplot
import numpy as np

xAxis = np.arange(0, 7)
yAxis = np.linspace(0, 100, 7)
matplotlib.pyplot.plot(xAxis, yAxis)
matplotlib.pyplot.show(block=False)

matplotlib.pyplot.figure()

# adjusts the width and height of the padding between subplots
matplotlib.pyplot.subplots_adjust(wspace=0.2, hspace=0.5)

# Choosing the first two spots of the 3x2 plot figure
matplotlib.pyplot.subplot(3, 2, (1, 2))

matplotlib.pyplot.plot(xAxis, yAxis)
matplotlib.pyplot.xlabel("Input")  # adds a label on the X axis
matplotlib.pyplot.ylabel("Output")  # adds a label on the Y axis
matplotlib.pyplot.title("My plot")  # sets the plot title

# makes the graph show the data points with a dot,
# have dashed line rather than solid
# with red color which could alternatively
# be written as 'r' or (255, 0, 0) or (255, 0, 0, 255)
# uses RGB/RGBA case sensitive notation
matplotlib.pyplot.subplot(3, 2, 3)
matplotlib.pyplot.plot(xAxis, yAxis, marker='o', linestyle="--", color="#ff0000")
matplotlib.pyplot.subplot(3, 2, 4)
matplotlib.pyplot.stem(xAxis, yAxis)

matplotlib.pyplot.subplot(3, 2, 5)
# 50 random data. each with dimensionality 2
# using the Gaussian distribution
X = np.randon.randn(50, 2)
matplotlib.pyplot.scatter(X[:, 0], X[:, 1])

matplotlib.pyplot.subplot(3, 2, 6)
X = np.random.randn(10_000)
# histogram of a normal distribution PRNG
matplotlib.pyplot.hist(X, bins=50)
matplotlib.pyplot.show()
