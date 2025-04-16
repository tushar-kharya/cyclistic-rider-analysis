import pandas as pd
import matplotlib.pyplot as plt

combined_df = pd.read_csv('202406-divvy-tripdata.csv')

print(combined_df.columns)

combined_df['started_at'] = pd.to_datetime(combined_df['started_at'])
combined_df['ended_at'] = pd.to_datetime(combined_df['ended_at'])
combined_df['ride_length'] = (combined_df['ended_at'] - combined_df['started_at']).dt.total_seconds() / 60

# Plot
plt.hist([combined_df['ride_length'][combined_df['member_casual'] == 'member'], 
          combined_df['ride_length'][combined_df['member_casual'] == 'casual']], 
         bins=50, label=['Member', 'Casual'], color=['blue', 'orange'], alpha=0.7)

plt.title('Distribution of Ride Lengths')
plt.xlabel('Ride Length (minutes)')
plt.ylabel('Frequency')
plt.legend()
plt.show()

