-- Question1 : write a sql to find min and max value of continuous sequence in each group

create table min_max_group(group_name varchar, id int);

insert into min_max_group values ('A',1);
insert into min_max_group values ('A',2);
insert into min_max_group values ('A',3);
insert into min_max_group values ('A',5);
insert into min_max_group values ('A',6);
insert into min_max_group values ('A',7);
insert into min_max_group values ('A',9);
insert into min_max_group values ('A',11);
insert into min_max_group values ('B',1);
insert into min_max_group values ('C',1);
insert into min_max_group values ('C',2);
insert into min_max_group values ('C',3);

with cte as (select  group_name , id , row_number() Over(partition by group_name order by id asc )rk,
(id - row_number() Over(partition by group_name order by id asc ) )group_split
from min_max_group)

select group_name,min(id), max(id) from cte group by group_name , group_split  order by group_name

