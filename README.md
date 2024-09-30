# Cyclistic Rider Analysis

## Overview
**Cyclistic Rider Analysis** is a case study from the Google Data Analytics Specialization Capstone, It serves as a data analysis project that examines the usage patterns of Cyclistic's bike-share service in Chicago. The project aims to understand how casual riders and annual members use Cyclistic bikes differently, providing data-driven insights to help convert casual riders into annual members. This analysis follows a structured process including data cleaning, analysis, visualization, and recommendations.

## Highlights
- Conducted data cleaning and transformation using SQL to prepare Cyclistic's 12-month trip data for analysis, ensuring data integrity by addressing missing values and inconsistencies.
- Analyzed key metrics such as ride duration, rider types, usage by day of the week, and station popularity.
- Created data visualizations using Python to identify trends and communicate findings effectively, including histograms of ride lengths, line charts of weekly usage, and bar charts of average ride durations.
- Provided recommendations to support marketing strategies aimed at converting casual riders to annual members, focusing on engagement based on identified behavioral patterns.

## Technologies Used
- **Python (pandas, matplotlib)**: Data manipulation and visualization.
- **SQL (MySQL)**: Data cleaning, aggregation, and extraction.
- **Google BigQuery**: Cloud-based SQL for managing large datasets.

## Data Analysis Workflow

1. **Data Cleaning**:
   - Addressed missing values in critical columns (e.g., station names and coordinates) using SQL queries to ensure data completeness.
   - Removed outliers and verified consistency in rider types (`casual` vs. `member`) to maintain data quality.

2. **Data Analysis**:
   - Used SQL and Python to explore key metrics such as average ride duration, number of rides by day of the week, and differences between casual and member riders.
   - Aggregated data and created new fields (e.g., ride duration) for detailed analysis.

3. **Data Visualization**:
   - Created visualizations in Python with matplotlib:
     - **Histogram** to compare ride durations between casual and member riders.
     - **Line Chart** to analyze the number of rides throughout the week for both rider types.
     - **Bar Chart** to compare average ride durations between casual and member riders.

4. **Recommendations**:
   - Suggested targeted marketing campaigns focusing on weekends to convert casual riders to members.
   - Proposed tailored membership plans for longer ride durations to match the behavior of casual riders.
   - Recommended personalized digital engagement strategies to drive conversion based on usage patterns.

## Key Insights
- **Histogram of Ride Lengths**: Casual riders tend to have longer ride durations compared to annual members, suggesting potential marketing opportunities focused on offering incentives for long-duration rides.
- **Line Chart for Weekly Usage**: Both casual riders and members have higher ridership on weekends, with casual riders showing a more significant increase, indicating that weekend promotions may be effective.
- **Bar Chart for Average Ride Length**: The average ride duration is consistently longer for casual riders, indicating that they may benefit from membership plans tailored for long-duration rides.


## Presentation
A detailed presentation of the Cyclistic Rider Analysis, including key insights, visualizations, and recommendations, can be found here:
- **[Cyclistic Rider Analysis Presentation (PDF)](https://docs.google.com/presentation/d/1BLcbv_KQcrIheA77xXCgILxiNkxDbeG_9IV564l-XNg/edit?usp=drive_link)**

## Data Source
The data used in this analysis was sourced from Cyclistic's historical trip data in the last 12 months. The dataset includes information such as trip duration, start and end times, and rider types, allowing for a comprehensive analysis of user behavior. The data was provided under an open license and prepared for analysis using Google BigQuery.

## Conclusion
The **Cyclistic Rider Analysis** provides an in-depth understanding of how casual riders and annual members use the bike-share service. The findings reveal key differences in behavior, such as ride duration and peak riding times, which can be leveraged to drive conversions from casual riders to annual members. By targeting casual riders on weekends, offering customized membership options for longer rides, and improving digital engagement, Cyclistic can effectively increase customer retention and boost revenue. The insights derived from this project offer actionable steps that can significantly enhance Cyclistic's marketing strategies and overall user experience.
