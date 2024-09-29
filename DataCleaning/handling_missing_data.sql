SELECT
    IFNULL(start_station_name, 'Unknown Station') AS start_station_name,
    IFNULL(end_station_name, 'Unknown Station') AS end_station_name,
    *
FROM 
    `inner-nuance-436720-u7.last_12_months_trip_data1.tripdata_202406`;