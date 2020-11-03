
CREATE TABLE line1seq (
  id SERIAL PRIMARY KEY,
  NR varchar (50),
  PONO varchar(50),
  MODEL varchar(50),
  Country varchar(50),
  Trim_Level varchar(50),
  AFD_AFF varchar(50),
  SEQ_NO varchar(50),
  DEST varchar(50),
  Emission varchar(50),
  Engin varchar(50),
  TRAN varchar(50),
  Body_Color varchar(50),
  FRT_B varchar(50),
  RR_B varchar(50),
  ABS varchar(50),
  WHEEL varchar(50),
  Spoiler varchar(50),
  REDEC varchar(50),
  date_added timestamp default NULL
  );

CREATE TABLE line2seq (
  id SERIAL PRIMARY KEY,
  NR varchar (50),
  PONO varchar(50),
  MODEL varchar(50),
  Country varchar(50),
  Trim_Level varchar(50),
  AFD_AFF varchar(50),
  SEQ_NO varchar(50),
  DEST varchar(50),
  Emission varchar(50),
  Engin varchar(50),
  TRAN varchar(50),
  Body_Color varchar(50),
  FRT_B varchar(50),
  RR_B varchar(50),
  Spoiler varchar(50),
  REDEC varchar(50),
  date_added timestamp default NULL
  );

