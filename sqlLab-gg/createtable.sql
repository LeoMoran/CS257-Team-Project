

DROP TABLE IF EXISTS earthquakes;
CREATE TABLE earthquakes (
  time datetime,
  latitude real,
  longitude real,
  quakedepth real,
  mag real,
  nst real,
  gap real,
  dmin real,
  rms real,
  id text,
  updated datetime,
  place text,
  horizontalError real,
  depthError real,
  curstatus text,
  locationSource text
);