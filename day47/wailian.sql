CREATE TABLE ClassCharger(

       id TINYINT PRIMARY KEY auto_increment,
       name VARCHAR (20),
       age INT ,
       is_marriged boolean  -- show create table ClassCharger: tinyint(1)

);

create table student(
  id integer primary key auto_increment,
  name varchar(20),
  charge_id INT
) ENGINE=INNODB;