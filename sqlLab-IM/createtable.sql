-- time,latitude,longitude,depth,mag,magType,net,id,updated,place,depthError,status,locationSource,magSource
-- time,latitude,longitude,mag

-- REPLACE TABLE IF EXISTS earthquakes;
CREATE TABLE OR REPLACE TABLE earthquakes(
  quakedate date,
  quaketime time with time zone,
  latitude real,
  longitude real,
  mag real
);