import pandas as pd
import io
import re
import csv
from contextlib import redirect_stdout
import numpy as np
from posydon.grids.psygrid import PSyGrid
from scipy.interpolate import interp1d
single_grid = PSyGrid("/home/jovyan/data/POSYDON_GRIDS/POSYDON_data/single_HMS/1e+00_Zsun.h5")
def find_single_star(m):
    m_zams = []
    index_grid = []
    for i in range(len(single_grid)):
        m_zams.append(pd.DataFrame(single_grid[i].history1).star_mass[0])
        index_grid.append(i)
    m_zams = np.array(m_zams)
    index_grid = np.array(index_grid)
    i = index_grid[(np.abs(m_zams - m)).argmin()]
    return pd.DataFrame(single_grid[i].history1)[['star_age','star_mass','log_R']]

def secondary_radius(time, m):
    history = find_single_star(m)
    log_R = history['log_R']
    star_ages = history['star_age'].values
    interpolator_log_R = interp1d(star_ages, log_R, kind='nearest', fill_value="extrapolate")
    interpolated_log_R = interpolator_log_R(time)
    return float(interpolated_log_R)

