create database library;

create table books(
    Book_Code int(10),
    Book_Name varchar(40),
    Author_Name varchar(40),
    Total_Books int(25)
);

create table issue(
    Name varchar(40),
    RegNo int(20),
    Book_Code int(10),
    Return_Date date
);

create table return_book(
    Name varchar(40),
    RegNo int(20),
    Book_Code int(10),
    Return_Date date
);

