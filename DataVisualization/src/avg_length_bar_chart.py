import pandas as pd
import matplotlib.pyplot as plt

# Ensure file is read
combined_df = pd.read_csv('202406-divvy-tripdata.csv')

# Convert 'started_at' and 'ended_at' to datetime
combined_df['started_at'] = pd.to_datetime(combined_df['started_at'])
combined_df['ended_at'] = pd.to_datetime(combined_df['ended_at'])

combined_df['ride_length'] = (combined_df['ended_at'] - combined_df['started_at']).dt.total_seconds() / 60
avg_ride_length = combined_df.groupby('member_casual')['ride_length'].mean()

# Plotting the bar chart
avg_ride_length.plot(kind='bar', color=['blue', 'orange'])

plt.title('Average Ride Length by Rider Type')
plt.xlabel('Rider Type')
plt.ylabel('Average Ride Length (minutes)')
plt.xticks(rotation=0)
plt.show()