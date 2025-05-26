use newdb;
create table quiz_questions (
		Questions_No INT primary key auto_increment,
        Questions VARCHAR(100),
        Answers VARCHAR(70));
insert into quiz_questions (Questions,Answers) Values 
("What does CPU stands for? ","Central Processing Unit"),
("What does GPS stands for? ","Global Positioning System"),
("What does API stands for? ","Application Programming Interface"),
("what does IDE stands for? ","Integrated Development Enviroment"),
("What does SQL stands for ?","Structured Query Language"),
("what SQL statement used to extract data from a database? ","Select"),
("Write a correct file extension for python files? ",".py");


select * from quiz_questions;
