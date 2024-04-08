import pandas as pd

# Read the CSV file
df = pd.read_csv('dataset.csv')
def get_features(lat,lon):
    filtered_data = df[(df['latitude'] == lat) & (df['longitude'] == lon)]

    # Retrieve tmin, tmax, and prcp values
    tmin_values = filtered_data['tmin']
    tmax_values = filtered_data['tmax']
    prcp_values = filtered_data['prcp']
    return tmin_values,tmax_values,prcp_values
