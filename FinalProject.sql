create database MurphysburgMS;

use MurphysburgMS;

# Student Table Create command
Create Table Students ( 
StudentID varchar(4) NOT NULL,
FirstName varchar(30) NOT NULL,
LastName varchar(30) NOT NULL,
DATEofBIRTH DATE,
Address varchar(50),
PhoneNumber varchar(15),
SchoolEmail varchar(30),
constraint Students_StudentID_PK PRIMARY KEY (StudentID)
);

# Teacher Table Create command 
Create Table Teachers ( 
TeacherID varchar(4) NOT NULL, 
FirstName varchar(30) NOT NULL,
LastName varchar(30) NOT NULL,
Department varchar(30),
constraint Teachers_TeacherID_PK PRIMARY KEY (TeacherID)
);

#Classes Table Create command 
Create Table Classes (
ClassID varchar(4) NOT NULL,
ClassName varchar(40) NOT NULL,
TeacherID varchar(4),
constraint Classes_ClassID_PK PRIMARY KEY (ClassID),
constraint Classes_TeacherID_FK FOREIGN KEY (TeacherID) references Teachers(TeacherID)
);

#Enrollments Table Create command
CREATE TABLE Enrollments (
EnrollmentID VARCHAR(4) NOT NULL,
StudentID VARCHAR(4),
ClassID VARCHAR(4),
EnrollmentDate DATE,
Grade DECIMAL(5, 2),
Status VARCHAR(20),
CONSTRAINT Enrollments_EnrollmentID_PK PRIMARY KEY (EnrollmentID),
CONSTRAINT Enrollments_StudentID_FK FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
CONSTRAINT Enrollments_ClassID_FK FOREIGN KEY (ClassID) REFERENCES Classes(ClassID)
);


#Student Table DATA insert command
INSERT INTO Students (StudentID, FirstName, LastName, DATEofBIRTH, Address, PhoneNumber, SchoolEmail)
VALUES
('S001', 'John', 'Doe', '2005-01-15', '123 Maple St', '249-555-1234', 'johndoe@school.edu'),
('S002', 'Mitch', 'Black', '2004-07-18', '4928 Grassroot LN', '872-122-9273', 'MitchBlack@school.edu'),
('S003', 'Ronny', 'Bruce', '2005-01-07', '14 Happy St', '555-492-1432', 'RonnyBruce@school.edu'),
('S004', 'Craig', 'Green', '2005-06-08', '1382 Cat Court', '438-535-1963', 'CraigGreen@school.edu'),
('S005', 'Jane', 'Doe', '2005-01-15', '123 Maple St', '249-555-1235', 'JaneDoe@school.edu'),
('S006', 'Jackson', 'Dean', '2006-03-23', '762 Blue Road', '765-827-3245', 'JacksonDead@school.edu'),
('S007', 'Alix', 'Skillman', '2005-02-12', '1414 Rock St', '982-555-3287', 'AlixSkillman@school.edu'),
('S008', 'Sheral', 'Poster', '2005-03-17', '82 Yellow Lane', '762-135-5790', 'SheralPoster@school.edu'),
('S009', 'Bob', 'Track', '2005-05-11', '1 Public Court', '625-325-9234', 'BobTrack@school.edu'),
('S010', 'Sally', 'Brown', '2005-04-27', '167 Sad St', '827-2555-1264', 'SallyBrown@school.edu'),
('S011', 'Robert', 'Jones', '2004-01-12', '134 Craggle Road', '762-458-2983', 'RobertJones@school.edu'),
('S012', 'Carrie', 'Smith', '2005-03-19', '16523 South LN', '918-123-3812', 'CarrieSmith@school.edu'),
('S013', 'Jagger', 'TheGreat', '2001-01-07', '1492 King St', '317-535-4387', 'JaggerRULES@school.edu'),
('S014', 'Mallory', 'Cabrone', '2004-04-25', '92 South St', '827-455-8721', 'MalloryCabrone@school.edu'),
('S015', 'Stuart', 'Grubler', '2005-01-23', '123 Morres Court', '317-563-1234', 'StuartGruber@school.edu'),
('S016', 'Gandolf', 'Azeras', '2004-04-11', '192 Magic Road', '462-555-348', 'GandolfAzeras@school.edu'),
('S017', 'Bibo', 'Baggins', '2005-07-23', '827 Shire Street', '928-235-9284', 'BilboBaggins@school.edu'),
('S018', 'Riley', 'Seeless', '2006-07-08', '480 Space Court', '327-723-4283', 'RileySeeless@school.edu'),
('S019', 'Archer', 'Blackson', '2004-08-15', '12 Alabaster St', '236-165-9621', 'ArcherBlackson@school.edu'),
('S020', 'Gimley', 'Collins', '2005-04-12', '3 Shire Street', '921-253-1234', 'GimleyCollins@school.edu'),
('S021', 'Jill', 'Williams', '2005-06-23', '18 Pearl St', '317-242-1234', 'JillWilliams@school.edu'),
('S022', 'Tim', 'Taylor', '2006-04-18', '999 Cedar Court', '827-542-4211', 'TimTaylor@school.edu'),
('S023', 'Michale', 'Anthony', '2004-06-23', '92 Colunm Court', '855-726-1234', 'MichaleAnthony@school.edu'),
('S024', 'Trysten', 'Beachwood', '2005-07-25', '1 Park St', '317-429-2952', 'TrystenBeachwood@school.edu'),
('S025', 'Bee', 'Honeycomb', '2006-03-18', '45 Hive Hill LN', '427-926-4343', 'BeeHoney@school.edu'),
('S026', 'Polly', 'Porkle', '2005-07-4', '143 Short St', '923-552-1234', 'PolyPorkle@school.edu'),
('S027', 'Butters', 'Berkhart', '2006-02-18', '482 Shovel St', '348-825-8235', 'ButtersBerkhart@school.edu'),
('S028', 'William', 'Swift', '2006-04-20', '19 Duck Drive', '231-355-1456', 'WilliamSwift@school.edu'),
('S029', 'Joe', 'Brown', '2004-05-28', '125 Tree Road', '521-142-9287', 'JoeBrown@school.edu'),
('S030', 'Martin', 'Funk', '2005-05-28', '1 Funk Street Lane', '317-235-3412', 'MartinFunk@school.edu');


 
#Teachers Table DATA insert command
INSERT INTO Teachers (TeacherID, FirstName, LastName, Department)
 VALUES
 ('T001', 'Alice', 'Cooper', 'Math'),
 ('T002', 'Bob', 'Marley', 'Science'),
 ('T003', 'Charlie', 'Browm', 'History'),
 ('T004', 'David', 'Bowie', 'Art'),
 ('T005', 'Eve', 'Adams', 'Pysical Education'),
 ('T006', 'Dave', 'Perara', 'Economics'),
 ('T007', 'Ron', 'Roberts', 'Math'),
 ('T008', 'Cartment', 'Red', 'Science'),
 ('T009', 'Taylor', 'Smith', 'History'),
 ('T010', 'Alice', 'Cooper', 'Science'),
 ('T011', 'Rita', 'Smith', 'Psychology'),
 ('T012', 'Fiona', 'Trest', 'Math'),
 ('T013', 'William', 'Williamson', 'Physical Education'),
 ('T014', 'James', 'Taylor', 'History'),
 ('T015', 'Anthony', 'Smith', 'Horticulture'),
 ('T016', 'Charlie', 'Brown', 'Physical Education'),
 ('T017', 'Snoopy', 'White', 'Math'),
 ('T018', 'Grima', 'Wormtower', 'Economics'),
 ('T019', 'Benjamin', 'Button', 'Science'),
 ('T020', 'Cooper', 'Cup', 'History'),
 ('T021', 'Jonnah', 'Hill', 'Theater'),
 ('T022', 'Makel', 'Smithson', 'Economics'),
 ('T023', 'Taylor', 'Smith', 'Math'),
 ('T024', 'Theodred', 'Maxwell', 'Science'),
 ('T025', 'Barnibus', 'Groblet', 'History'),
 ('T026', 'Kurt', 'Cobain', 'Math'),
 ('T027', 'Morgen', 'Wallen', 'Art'),
 ('T028', 'Post', 'Malone', 'Music'),
 ('T029', 'Benson', 'Boone', 'History'),
 ('T030', 'Noah', 'Kahan', 'Science');
 
 

 #Classes Table DATA insert command
 INSERT INTO Classes (ClassID, ClassName, TeacherID) 
 VALUES
 ('C001', 'Algebra I', 'T001'),
 ('C002', 'Biology', 'T002'),
 ('C003', 'World History', 'T003'),
 ('C004', 'Art History', 'T004'),
 ('C005', 'PE 101', 'T005'),
 ('C006', 'Econ 101', 'T006'),
 ('C007', 'Geometry', 'T007'),
 ('C008', 'Anatomy', 'T008'),
 ('C009', 'AP World History', 'T009'),
 ('C010', 'Physics', 'T010'),
 ('C011', 'Pysch 101', 'T011'),
 ('C012', 'Algebra 2', 'T012'),
 ('C013', 'Weight Lifting', 'T013'),
 ('C014', 'US History', 'T014'),
 ('C015', 'Gardening', 'T015'),
 ('C016', 'Health and Fitness', 'T016'),
 ('C017', 'Pre-Calculus', 'T017'),
 ('C018', 'AP Econ', 'T018'),
 ('C019', 'Astrology', 'T019'),
 ('C020', 'AP US History', 'T020'),
 ('C021', 'Music and Theater', 'T021'),
 ('C022', 'Accounting', 'T022'),
 ('C023', 'Calulus', 'T023'),
 ('C024', 'Earth Science', 'T024'),
 ('C025', 'Geo-Political Studies', 'T025'),
 ('C026', 'Triginometry', 'T026'),
 ('C027', 'Sculpting', 'T027'),
 ('C028', 'Band', 'T028'),
 ('C029', 'Earths History', 'T029'),
 ('C030', 'Chemistry', 'T030');
 
 
 #Enrollments Table DATA insert command 
INSERT INTO Enrollments (EnrollmentID, StudentID, ClassID, EnrollmentDate, Grade, Status)
 VALUES 
('E001', 'S001', 'C001', '2023-01-01', 85.5, 'Enrolled'), 
('E002', 'S002', 'C002', '2023-01-02', 90.0, 'Enrolled'),
 ('E003', 'S003', 'C003', '2023-01-03', 88.0, 'Enrolled'),
 ('E004', 'S004', 'C004', '2023-01-04', 92.0, 'Enrolled'),
 ('E005', 'S005', 'C005', '2023-01-05', 98.0, 'Enrolled'),
 ('E006', 'S006', 'C006', '2023-01-06', 80.0, 'Enrolled'),
 ('E007', 'S007', 'C007', '2023-01-07', 83.0, 'Enrolled'),
 ('E008', 'S008', 'C008', '2023-01-08', 95.0, 'Enrolled'),
 ('E009', 'S009', 'C009', '2023-01-09', 89.0, 'Enrolled'),
 ('E010', 'S010', 'C010', '2023-01-10', 75.0, 'Enrolled'),
 ('E011', 'S011', 'C011', '2023-01-11', 92.0, 'Enrolled'),
 ('E012', 'S012', 'C012', '2023-01-12', 95.0, 'Enrolled'),
 ('E013', 'S013', 'C013', '2023-01-13', 90.0, 'Enrolled'), 
 ('E014', 'S014', 'C014', '2023-01-14', 80.0, 'Enrolled'),
 ('E015', 'S015', 'C015', '2023-01-15', 99.0, 'Enrolled'),
 ('E016', 'S016', 'C016', '2023-01-16', 94.0, 'Enrolled'),
 ('E017', 'S017', 'C017', '2023-01-17', 68.0, 'Enrolled'),
 ('E018', 'S018', 'C018', '2023-01-18', 97.0, 'Enrolled'),
 ('E019', 'S019', 'C019', '2023-01-19', 76.0, 'Enrolled'), 
 ('E020', 'S020', 'C020', '2023-01-20', 91.0, 'Enrolled'), 
 ('E021', 'S021', 'C021', '2023-01-21', 84.0, 'Enrolled'), 
 ('E022', 'S022', 'C022', '2023-01-22', 87.0, 'Enrolled'), 
 ('E023', 'S023', 'C023', '2023-01-23', 94.0, 'Enrolled'), 
 ('E024', 'S024', 'C024', '2023-01-24', 92.0, 'Enrolled'), 
 ('E025', 'S025', 'C025', '2023-01-25', 82.0, 'Enrolled'), 
 ('E026', 'S026', 'C026', '2023-01-26', 95.0, 'Enrolled'), 
 ('E027', 'S027', 'C027', '2023-01-27', 98.0, 'Enrolled'),
 ('E029', 'S029', 'C029', '2023-01-29', 81.0, 'Enrolled'), 
 ('E030', 'S030', 'C030', '2023-01-30', 81.0, 'Enrolled');

 
 #Queries for part B  
 
#Question 1: What are the first and last names of students born after April 1, 2005?
#Query 1 
SELECT FirstName, LastName
FROM Students
WHERE DATEofBIRTH > '2005-04-01';

#Question 2: What are the first and last names of students living on Maple St or Elm St?
#Query 2
SELECT FirstName, LastName
FROM Students
WHERE Address LIKE '%Maple St%' OR Address LIKE '%Park St%';

#Question 3: What are the names of teachers whose first name starts with 'A'?
#Query 3
SELECT FirstName, LastName
FROM Teachers
WHERE FirstName LIKE 'A%';

#Question 4: What are the names of classes taught by teachers in the Math or Science departments?
#Query 4
SELECT ClassName
FROM Classes
WHERE TeacherID IN (SELECT TeacherID FROM Teachers WHERE Department IN ('Math', 'Science'));
 
#Question 5: What is the average grade for the Biology class?
#Query 5
SELECT AVG(Grade) AS AverageGrade
FROM Enrollments
WHERE ClassID = 'C002';

#Question 6: What is the average grade for each class?
#Query 6
SELECT ClassID, AVG(Grade) AS AverageGrade
FROM Enrollments
GROUP BY ClassID;

#Question 7: What are the names of students and the classes they are enrolled in?
#Query 7
SELECT s.FirstName, s.LastName, c.ClassName
FROM Students s
JOIN Enrollments e ON s.StudentID = e.StudentID
JOIN Classes c ON e.ClassID = c.ClassID;

#Question 8: What are the names of students enrolled in classes taught by teachers in the Art department?
#Query 8
SELECT FirstName, LastName
FROM Students
WHERE StudentID IN (
SELECT e.StudentID
FROM Enrollments e
JOIN Classes c ON e.ClassID = c.ClassID
WHERE c.TeacherID IN (SELECT TeacherID FROM Teachers WHERE Department = 'Art')
);

#Question 9: What are the names of students enrolled in the class with the highest average grade?
#Query 9
SELECT FirstName, LastName
FROM Students
WHERE StudentID IN (
SELECT StudentID
FROM Enrollments
WHERE ClassID = (
SELECT ClassID
FROM Enrollments
GROUP BY ClassID
ORDER BY AVG(Grade) DESC
LIMIT 1
    )
);

#Question 10: What are the names of teachers and the classes they teach?
#Query 10
SELECT t.FirstName, t.LastName, c.ClassName
FROM Teachers t
INNER JOIN Classes c ON t.TeacherID = c.TeacherID;

#Question 11:  What are the names of students who have a grade below 70 in any of their classes?
#Query 11
SELECT FirstName, LastName
FROM Students
WHERE StudentID = ANY (
SELECT StudentID
FROM Enrollments
WHERE Grade < 70
);
