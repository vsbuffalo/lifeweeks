from datetime import date, timedelta
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.collections import PatchCollection

mean_le = math.ceil(78.54) # for men in US
birthday = (1986, 12, 19)
deathday = (mean_le + birthday[0], 12, 19)
birthday = date(*birthday)
deathday = date(*deathday)

life = deathday - birthday
days_left = deathday - date.today()
print(f'Assuming a life expectancy of {mean_le} years, your life is {round(100 * (1 - (days_left / life)), 2)}% through.')

# approximation; ignores leap years
total_years = int(life.days / 365)
total_weeks = int(total_years * 52)
now_week = (date.today() - birthday).days / 7

shape = (total_years, 52)
mat = np.full(shape, 0)
rows, cols = map(lambda x: x.flatten(), np.indices(shape))

fig, ax = plt.subplots()

ax.set_xlim(0, 52)
ax.set_ylim(total_years, 0)
ax.set_ylabel('year')
ax.set_xlabel('week')
fig.set_size_inches(8.5, 11)

for week_i, (x, y) in enumerate(zip(cols, rows)):
    col = 'black' if week_i < now_week else 'lightgrey'
    ax.add_patch(Rectangle(xy = (x, y), width=0.9, height=0.9, facecolor = col))

plt.tight_layout()
fig.savefig('life.pdf')

