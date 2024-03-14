
-- Write a SQL script that loads CSV data into a table.

-- create table ipl_matches with proper column names
CREATE TABLE ipl_matches (
  id SERIAL PRIMARY KEY,
  season INTEGER,
  city TEXT,
  date DATE,
  team1 TEXT,
  team2 TEXT,
  toss_winner TEXT,
  toss_decision TEXT,
  result TEXT,
  dl_applied BOOLEAN,
  winner TEXT,
  win_by_runs INTEGER,
  win_by_wickets INTEGER,
  player_of_match TEXT,
  venue TEXT,
  umpire1 TEXT,
  umpire2 TEXT,
  umpire3 TEXT
);

-- fetch the ipl_matches data from matches.csv
\copy ipl_matches from 'DataFiles/matches.csv' DELIMITER  ',' CSV HEADER;

-- create table ipl_deliveries with proper column names
CREATE TABLE ipl_deliveries (
  match_id INTEGER,
  inning INTEGER,
  batting_team TEXT,
  bowling_team TEXT,
  over INTEGER,
  ball INTEGER,
  batsman TEXT,
  non_striker TEXT,
  bowler TEXT,
  is_super_over BOOLEAN,
  wide_runs INTEGER,
  bye_runs INTEGER,
  legbye_runs INTEGER,
  noball_runs INTEGER,
  penalty_runs INTEGER,
  batsman_runs INTEGER,
  extra_runs INTEGER,
  total_runs INTEGER,
  player_dismissed TEXT,
  dismissal_kind TEXT,
  fielder TEXT
);

-- fetch the ipl_deliveries data from deliveries.csv
\copy ipl_deliveries from 'DataFiles/deliveries.csv' DELIMITER  ',' CSV HEADER;

-- create table ipl_umpires with proper column names
CREATE TABLE ipl_umpires (
    umpire TEXT,
    country TEXT
);

-- fetch the umpires data from umpires.csv
\copy ipl_umpires from 'DataFiles/umpires.csv' DELIMITER  ',' CSV HEADER;