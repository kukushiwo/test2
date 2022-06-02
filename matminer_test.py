import matminer
import pymatgen
import numpy as mp
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pymatgen.core.composition import Composition
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
from matminer.featurizers.composition import ElementFraction


ds_PF_ZT = pd.read_csv('./PF_ZT.csv')
X = ds_PF_ZT.iloc[:, 0:3]
y = ds_PF_ZT.iloc[:, -1]

Comp = []
for value in ds_PF_ZT['Formula']:
  Comp.append(Composition(value))

ds_PF_ZT['Composition'] = Comp

ef = ElementFraction()

ds_PF_ZT = ef.featurize_dataframe(ds_PF_ZT, 'Composition')

ds_PF_ZT = ds_PF_ZT.loc[:, (ds_PF_ZT != 0).any(axis=0)]

ds_PF_ZT.to_csv('./PF_ZT_processed.csv')










