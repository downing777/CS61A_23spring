.read data.sql


CREATE TABLE bluedog AS
  SELECT color, pet from students WHERE color = 'blue' and pet = 'dog';

CREATE TABLE bluedog_songs AS
  SELECT color, pet, song from students WHERE color = 'blue' and pet = 'dog';


CREATE TABLE smallest_int_having AS
  SELECT time, smallest from students group by smallest HAVING COUNT(*) = 1;


CREATE TABLE matchmaker AS
  SELECT a.pet, a.song, a.color, b.color from students as a, students as b 
        where a.time < b.time and a.pet = b.pet and a.song = b.song;


CREATE TABLE sevens AS
  SELECT seven from students, numbers where students.time = numbers.time and students.number = 7 and numbers.'7' = 'True';
 


CREATE TABLE average_prices AS
  SELECT category as category, AVG(MSRP) as average_price from products group by category;


CREATE TABLE lowest_prices AS
  SELECT store, item, min(price) from inventory group by item;

CREATE TABLE best_deal AS
  SELECT name, min(MSRP/rating) from products group by category;

CREATE TABLE shopping_list AS
  SELECT name, store from best_deal, lowest_prices where name = item;


CREATE TABLE total_bandwidth AS
  SELECT sum(Mbs) from shopping_list, stores where shopping_list.store = stores.store;

