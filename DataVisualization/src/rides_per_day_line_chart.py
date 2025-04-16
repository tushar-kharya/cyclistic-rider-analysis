import pandas as pd
import matplotlib.pyplot as plt

combined_df = pd.read_csv('202406-divvy-tripdata.csv')

combined_df['started_at'] = pd.to_datetime(combined_df['started_at'])
combined_df['day_of_week'] = combined_df['started_at'].dt.dayofweek + 1

day_of_week_counts = combined_df.groupby(['day_of_week', 'member_casual']).size().unstack()
day_of_week_counts.plot(kind='line', marker='o')

plt.title('Rides by Day of the Week')
plt.xlabel('Day of the Week (1=Monday, 7=Sunday)')
plt.ylabel('Number of Rides')
plt.legend(title='Rider Type')
plt.grid(True)
plt.show()
