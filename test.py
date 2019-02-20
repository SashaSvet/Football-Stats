import pandas as pd
import numpy as np
import glob
import warnings
from scipy.stats import norm
from IPython.display import display, HTML
import scipy
warnings.filterwarnings("ignore")
import seaborn as sns
pd.options.display.float_format = '{:.2f}'.format
sns.set()
from datetime import datetime as dt
import matplotlib.pyplot as plt
from IPython.display import Markdown, display
def printmd(string):
    display(Markdown(string))
# %config InlineBackend.figure_format = 'svg'


results = pd.read_csv('epl/results.csv')

results.groupby('home_team').agg({'home_goals':'sum'}).plot(kind='bar')
plt.show()