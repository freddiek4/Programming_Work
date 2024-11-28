import requests
import lxml.html as lx
import re
import time
import nltk
import numpy as np

import matplotlib.pyplot as plt # or your favorite alternative

from sklearn.preprocessing import normalize
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
