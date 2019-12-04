DROP TABLE IF EXISTS leads;
DROP TABLE IF EXISTS high_priority;

CREATE DATABASE leadsdb
  WITH OWNER = postgres
       ENCODING = 'UTF8'
       TABLESPACE = pg_default
       LC_COLLATE = 'en_US.UTF-8'
       LC_CTYPE = 'en_US.UTF-8'
       CONNECTION LIMIT = -1;


CREATE TABLE leads ( 

  registration_dttm varchar, 
  id varchar, 
  first_name varchar, 
  last_name varchar, 
  email varchar, 
  gender varchar, 
  ip_address varchar, 
  cc varchar, 
  country varchar, 
  birthdate varchar, 
  salary varchar, 
  title varchar, 
  comments varchar); 

CREATE TABLE high_priority ( 

  registration_dttm varchar, 
  id varchar, 
  first_name varchar, 
  last_name varchar, 
  email varchar, 
  gender varchar, 
  ip_address varchar, 
  cc varchar, 
  country varchar, 
  birthdate varchar, 
  salary varchar, 
  title varchar, 
  comments varchar); 





