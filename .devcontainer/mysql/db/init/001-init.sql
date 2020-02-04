-- CREATE DATABASE stock_price_project CHARACTER SET utf8mb4;;
use stock_price_project;

create table stock_info (
    stock_name varchar(10) not null,
    stock_date date not null,
    high double,
    low double,
    open double,
    close double,
    volume double,
    adj_close double,
    primary key(stock_name, stock_date)
);

GRANT ALL ON `stock_price_project`.* TO 'dbuser'@'%';
FLUSH PRIVILEGES;
