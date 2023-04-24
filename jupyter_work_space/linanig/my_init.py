import numpy as np
import pandas as pd
import scipy as sp
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn.datasets import load_digits
from matplotlib import font_manager
from matplotlib import gridspec
from scipy import misc
from sklearn.datasets import fetch_olivetti_faces



# import warnings
# warnings.filterwarnings('ignore')

font_fname = 'C:/Windows/Fonts/malgun.ttf'
font_family = font_manager.FontProperties(fname=font_fname).get_name()

plt.rcParams["font.family"] = font_family
plt.rcParams["axes.unicode_minus"] = False


%matplotlib inline