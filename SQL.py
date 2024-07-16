
Transation 

Cust_Id , Product_Id, Cat_Id, Transaction_amount, Tran_timestamp 
1       , 123       , 1     ,  100              , 2023-10-10: 10:20:30
2       , 123       , 1     ,  200              , 2023-10-10: 10:21:30
1       , 123       , 3    ,   300              , 2023-10-10: 10:22:30
3       , 123       , 1     ,  400              , 2023-10-10: 10:23:30



Dim_customer , 
Dim_Product
Dim_Category

Category_name , month_of_year, totoal_sales, total_cumulative_sales

with cte as (
Select 
    c.Category_name,
    extract('Month' from t.Tran_timestamp) as  month_of_year, 
    extract('Year' from t.Tran_timestamp) as  year, 
    sum(Transaction_amount) as totoal_sales
    From 
        Transation t 
        Join  Dim_Category c on 
            t.Cat_Id = c.Dim_Category
    group by 1,2,3
)
    select Category_name , month_of_year, year, totoal_sales , sum(totoal_sales) over (Order by year, month_of_year ) as total_cumulative_sales
        from cte 
            group by Category_name , month_of_year, year, totoal_sales



=============
cust_name , phone_no , Type
A , 123, Home                 
A, 456 , Office
B, 123, Home

phone.a

A {123 :office ,456:home}
B (123)
    
Cust_Details 
Cust_name , phone_no_home, phone_no_office
A, 456    , 123

{
   
}

1. Staging_a 
    
insert into Cust_Details values()
    
with cte_home as  (
    select cust_name,phone_no  from Cust_Details where type = 'Home'
), 
 cte_office as
 (    select cust_name,phone_no  from Cust_Details where type = 'Office'
 )   

select a.cust_name, b.phone_no as phone_no_home , c.phone_no as phone_no_office 
    from cte_home join a cte_office b 

    

    select cust_name,phone_no  from Cust_Details where type = 'Home'

    select cust_name,phone_no  from Cust_Details where type = 'Office'


Cust_phone_history
cust_name , phone_no ,
A , 123
A, 456
B, 123
    
