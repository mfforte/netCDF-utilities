import matplotlib.pyplot as plt
import netCDF4 as nc
import pandas as pd
import numpy as np
import windrose
from windrose import WindroseAxes


csa02 = nc.Dataset("http://134.164.129.55/thredds/dodsC/FRF/oceanography/waterlevel/CS02-Waterlog/CS02-Waterlog.ncml")
cstime = csa02['time'][:]
csnewtime = nc.num2date(csa02['time'][:],csa02['time'].units)
cswlevel = csa02["waterLevelHeight"][:]
cswlevel_ft = cswlevel * 3.2808


csa01Waves = nc.Dataset("https://chlthredds.erdc.dren.mil/thredds/dodsC/frf/oceanography/waves/waverider-17m/waverider-17m.ncml")
csa01WaveTime = csa01Waves['time'][:]
csa01WaveTimePlotTime = nc.num2date(csa01Waves['time'][:],csa01Waves['time'].units)
csa01Waves_ht = csa01Waves['waveHs'][:]
csa01Waves_ht_Ft = csa01Waves_ht * 3.2808

csa01Winds = nc.Dataset("http://134.164.129.55/thredds/dodsC/FRF/meteorology/wind/CS01-Wind1/CS01-Wind1.ncml")
csa01WindTime = csa01Winds['time'][:]
csa01WindTimePlot = nc.num2date(csa01Winds['time'][:],csa01Winds['time'].units)
csa01WindSpeed_kts = csa01Winds['windSpeed'][:] * 2.23694
csa01WindDirection = csa01Winds['windDirection'][:]


# waves = pd.DataFrame({"HSft": csa03Waves_ht_Ft, "Time": csa03WaveTimePlotTime})
# waves.to_pickle('C:\\temp\\CSA03_waves')
#
# waterLevels = pd.DataFrame({"WaterLevel Ft": cswlevel_ft, "Time": csnewtime})
# waterLevels.to_pickle('C:\\temp\\CSA03_waterlevels')


plt.figure()
plt.plot(csnewtime,cswlevel_ft)
plt.savefig('soundplot.png')
f = plt.figure(figsize=(40,10))
plt.figure()
f, axarr = plt.subplots(3, sharex=True)
axarr[0].plot(csnewtime, cswlevel_ft)
axarr[0].set_title('CSA02 - Water Level')
axarr[0].set_ylabel('NAVD88 Feet')
axarr[1].plot(csa02WaveTimePlotTime, csa02Waves_ht_Ft)
axarr[1].set_title('CSA02 - Wave Height')
axarr[1].set_ylabel('Feet')
axarr[2].set_title('CSA01 - Wind Speed')
axarr[2].plot(csa01WindTimePlot,csa01WindSpeed_kts)
axarr[2].set_ylabel('MPH')
print 'done'
plt.savefig('soundplot.png')
