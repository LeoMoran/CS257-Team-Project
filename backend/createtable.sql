DROP TABLE IF EXISTS gradratetable;
CREATE TABLE gradratetable(
    stateName varchar(35),
    districtName varchar(100),
    category varchar(5),
    cohortSize real,
    givenRate varchar(10),
    convertedRate real
)
