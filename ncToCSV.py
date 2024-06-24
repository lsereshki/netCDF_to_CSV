 #in a netcdf file, dates are written as numeric.
 # we want to write the values of a varible e.g. 'fwi' and their corresponded dates in a CSV file.

import netCDF4 as nc
import pandas as pd

# Open the NetCDF file

nc_file = 'FWI_FENZ_NOV2022-MAY2023.nc'

#dataset = nc.Dataset(nc_file, 'r')
dataset = nc.Dataset(nc_file)

# Assume the time variable is named 'time' and the variable that we want to have its values is named 'fwi'
time_var = dataset.variables['time']
FWI = dataset.variables['fwi']

# Get the units and calendar of the time variable
time_units = time_var.units  # e.g., 'days since 2000-01-01 00:00:00'
time_calendar = time_var.calendar if hasattr(time_var, 'calendar') else 'gregorian'

# Convert the numeric time values to datetime objects
dates = nc.num2date(time_var[:], units=time_units, calendar=time_calendar)

# Create a DataFrame with the dates and the corresponding variable values
df = pd.DataFrame({
    'Date': dates,
    'Value': FWI[:]
})

# Sort the DataFrame by the 'Date' column
df_sorted = df.sort_values(by='Date')

# Write the sorted DataFrame to a CSV file
output_csv_path = 'sorted_data.csv'
df_sorted.to_csv(output_csv_path, index=False)

# Close the dataset
dataset.close()

print(f"Sorted data has been saved to {output_csv_path}")