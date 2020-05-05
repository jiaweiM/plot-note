import plotly.express as px
import xarray as xr

airtemps = xr.tutorial.open_dataset('air_temperature').air.isel(time=500)
colorbar_title = airtemps.attrs['var_desc'] + '<br>(%s)' % airtemps.attrs['units']
fig = px.imshow(airtemps, color_continuous_scale='RdBu_r', aspect='equal')
fig.show()
