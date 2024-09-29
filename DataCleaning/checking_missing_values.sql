
-- Check for missing values in start_station_name
SELECT 
    COUNT(*) AS missing_start_station_name
FROM 
    `inner-nuance-436720-u7.last_12_months_trip_data1.tripdata_202406`
WHERE 
    start_station_name IS NULL;

-- Check for missing values in end_station_name
SELECT 
    COUNT(*) AS missing_end_station_name
FROM 
    `inner-nuance-436720-u7.last_12_months_trip_data1.tripdata_202406`
WHERE 
    end_station_name IS NULL;

-- Check for missing values in end_lat and end_lng
SELECT 
    COUNT(*) AS missing_end_lat,
    COUNT(*) AS missing_end_lng
FROM 
    `inner-nuance-436720-u7.last_12_months_trip_data1.tripdata_202406`
WHERE 
    end_lat IS NULL
    OR end_lng IS NULL;