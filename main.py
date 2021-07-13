import fastf1 as ff1
from fastf1 import plotting
from matplotlib import pyplot as plt

plotting.setup_mpl()


race = ff1.get_session(2020, 'Turkish Grand Prix', 'R')
laps = race.load_laps()

lec = laps.pick_driver('LEC')
ham = laps.pick_driver('HAM')

fig, ax = plt.subplots()
ax.plot(lec['LapNumber'], lec['LapTime'], color='red')
ax.plot(ham['LapNumber'], ham['LapTime'], color='cyan')
ax.set_title("LEC vs HAM")
ax.set_xlabel("Lap Number")
ax.set_ylabel("Lap Time")
plt.show()
