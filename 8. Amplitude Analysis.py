import parselmouth
import matplotlib.pyplot as plt
import seaborn as sns


sns.set()  #Use seaborn's default style to make attractive graphs
plt.rcParams['figure.dpi'] = 100 #Show nicely large images in this notebook

snd = parselmouth.Sound("WilhelmScream.wav")

plt.figure()
plt.plot(snd.xs(), snd.values.T)

plt.xlim([snd.xmin, snd.xmax])
plt.xlabel("time [s]")
plt.ylabel("amplitude")
plt.show()