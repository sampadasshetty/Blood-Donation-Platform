-- =====================================
-- BLOOD REQUEST AND DONATION PLATFORM
-- Complete SQL Implementation
-- =====================================

USE mini_project;



CREATE TABLE Donor (
    D_id INT AUTO_INCREMENT PRIMARY KEY,
    Address VARCHAR(255),
    First_Name VARCHAR(100),
    Last_Name VARCHAR(100),
    Age INT,
    Gender VARCHAR(10)
);

CREATE TABLE Donor_Contact (
    Contact VARCHAR(50),
    D_id INT,
    FOREIGN KEY (D_id) REFERENCES Donor(D_id)
);

CREATE TABLE Hospital (
    H_id INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(255),
    City VARCHAR(100),
    State VARCHAR(100),
    Pincode VARCHAR(20)
);

CREATE TABLE Hospital_Contact (
    Contact VARCHAR(50),
    H_id INT,
    FOREIGN KEY (H_id) REFERENCES Hospital(H_id)
);

CREATE TABLE Blood_Request (
    Request_Id INT AUTO_INCREMENT PRIMARY KEY,
    Blood_type VARCHAR(10),
    Quantity INT,
    Request_date DATE,
    Status VARCHAR(50),
    H_id INT,
    FOREIGN KEY (H_id) REFERENCES Hospital(H_id)
);

CREATE TABLE Donation (
    Donation_id INT AUTO_INCREMENT PRIMARY KEY,
    D_id INT,
    Donation_date DATE,
    H_id INT,
    Quantity INT,
    FOREIGN KEY (D_id) REFERENCES Donor(D_id),
    FOREIGN KEY (H_id) REFERENCES Hospital(H_id)
);

CREATE TABLE Patient (
    Patient_Id INT AUTO_INCREMENT PRIMARY KEY,
    First_Name VARCHAR(100),
    Last_Name VARCHAR(100),
    Age INT,
    Disease VARCHAR(255),
    H_id INT,
    Request_bloodtype VARCHAR(10),
    FOREIGN KEY (H_id) REFERENCES Hospital(H_id)
);

CREATE TABLE Register (
    Last_donation_date DATE,
    Status VARCHAR(50),
    Register_date DATE,
    H_id INT,
    D_id INT,
    PRIMARY KEY (H_id, D_id),
    FOREIGN KEY (H_id) REFERENCES Hospital(H_id),
    FOREIGN KEY (D_id) REFERENCES Donor(D_id)
);

-- ================
-- INSERT 10 RECORDS PER TABLE
-- ================

-- Donor
INSERT INTO Donor VALUES
(1, '123 Main St', 'John', 'Doe', 30, 'Male'),
(2, '456 Lake Rd', 'Jane', 'Smith', 25, 'Female'),
(3, '789 Hill Ave', 'Robert', 'Johnson', 40, 'Male'),
(4, '12 Oak St', 'Emily', 'Davis', 29, 'Female'),
(5, '34 Pine Rd', 'Michael', 'Miller', 35, 'Male'),
(6, '56 Maple St', 'Sarah', 'Wilson', 28, 'Female'),
(7, '78 Cedar St', 'David', 'Anderson', 32, 'Male'),
(8, '90 Birch Rd', 'Laura', 'Thomas', 27, 'Female'),
(9, '11 Elm St', 'James', 'Jackson', 31, 'Male'),
(10, '22 Walnut St', 'Linda', 'White', 26, 'Female');

-- Donor_Contact
INSERT INTO Donor_Contact VALUES
('9876543210', 1),
('8765432109', 2),
('7654321098', 3),
('6543210987', 4),
('5432109876', 5),
('4321098765', 6),
('3210987654', 7),
('2109876543', 8),
('1098765432', 9),
('0198765432', 10);

-- Hospital
INSERT INTO Hospital VALUES
(101, 'City Hospital', 'New York', 'NY', '10001'),
(102, 'Green Valley Hospital', 'Chicago', 'IL', '60601'),
(103, 'Sunrise Hospital', 'Los Angeles', 'CA', '90001'),
(104, 'Lakeside Medical', 'Houston', 'TX', '77001'),
(105, 'Metro Health', 'Miami', 'FL', '33101'),
(106, 'Riverfront Hospital', 'Seattle', 'WA', '98101'),
(107, 'Central Hospital', 'Denver', 'CO', '80201'),
(108, 'Northside Clinic', 'Boston', 'MA', '02101'),
(109, 'Eastview Hospital', 'Atlanta', 'GA', '30301'),
(110, 'Westend Health', 'San Diego', 'CA', '92101');

-- Hospital_Contact
INSERT INTO Hospital_Contact VALUES
('212-555-1001', 101),
('312-555-2002', 102),
('213-555-3003', 103),
('713-555-4004', 104),
('305-555-5005', 105),
('206-555-6006', 106),
('303-555-7007', 107),
('617-555-8008', 108),
('404-555-9009', 109),
('619-555-1010', 110);

-- Blood_Request
INSERT INTO Blood_Request VALUES
(1001, 'A+', 2, '2025-09-10', 'Pending', 101),
(1002, 'O-', 1, '2025-09-11', 'Approved', 102),
(1003, 'B+', 3, '2025-09-12', 'Pending', 103),
(1004, 'AB-', 2, '2025-09-13', 'Pending', 104),
(1005, 'O+', 1, '2025-09-14', 'Approved', 105),
(1006, 'A-', 4, '2025-09-15', 'Pending', 106),
(1007, 'B-', 2, '2025-09-16', 'Pending', 107),
(1008, 'AB+', 3, '2025-09-17', 'Approved', 108),
(1009, 'A+', 1, '2025-09-18', 'Pending', 109),
(1010, 'O-', 2, '2025-09-19', 'Approved', 110);

-- Donation
INSERT INTO Donation VALUES
(5001, 1, '2025-09-05', 101, 1),
(5002, 2, '2025-09-07', 102, 2),
(5003, 3, '2025-09-08', 103, 1),
(5004, 4, '2025-09-09', 104, 2),
(5005, 5, '2025-09-10', 105, 1),
(5006, 6, '2025-09-11', 106, 3),
(5007, 7, '2025-09-12', 107, 2),
(5008, 8, '2025-09-13', 108, 1),
(5009, 9, '2025-09-14', 109, 2),
(5010, 10, '2025-09-15', 110, 1);

-- Patient
INSERT INTO Patient VALUES
(2001, 'Michael', 'Brown', 45, 'Surgery', 101, 'A+'),
(2002, 'Emily', 'Clark', 32, 'Accident', 102, 'O-'),
(2003, 'Sarah', 'Lee', 29, 'Cancer', 103, 'B+'),
(2004, 'James', 'Lopez', 55, 'Heart Attack', 104, 'AB-'),
(2005, 'Robert', 'Hall', 38, 'Surgery', 105, 'O+'),
(2006, 'Linda', 'Young', 47, 'Anemia', 106, 'A-'),
(2007, 'David', 'King', 36, 'Accident', 107, 'B-'),
(2008, 'Laura', 'Scott', 41, 'Cancer', 108, 'AB+'),
(2009, 'John', 'Adams', 30, 'Surgery', 109, 'A+'),
(2010, 'Jane', 'Baker', 28, 'Accident', 110, 'O-');

-- Register
INSERT INTO Register VALUES
('2025-06-15', 'Active', '2025-07-01', 101, 1),
('2025-07-20', 'Inactive', '2025-08-01', 102, 2),
('2025-06-10', 'Active', '2025-07-05', 103, 3),
('2025-07-22', 'Active', '2025-08-02', 104, 4),
('2025-05-30', 'Inactive', '2025-06-15', 105, 5),
('2025-07-18', 'Active', '2025-08-03', 106, 6),
('2025-06-25', 'Active', '2025-07-15', 107, 7),
('2025-07-19', 'Inactive', '2025-08-04', 108, 8),
('2025-06-28', 'Active', '2025-07-20', 109, 9),
('2025-07-21', 'Active', '2025-08-05', 110, 10);

-- =====================================
-- SECTION 2: TRIGGERS (6 Triggers)
-- =====================================

DELIMITER //

-- Trigger 1: Auto-update Blood Request status after donation
CREATE TRIGGER trg_update_request_status
AFTER INSERT ON Donation
FOR EACH ROW
BEGIN
    UPDATE Blood_Request 
    SET Status = 'Fulfilled'
    WHERE H_id = NEW.H_id 
    AND Status = 'Approved'
    AND Request_date <= NEW.Donation_date
    LIMIT 1;
END//

-- Trigger 2: Validate donor age before registration
CREATE TRIGGER trg_validate_donor_age
BEFORE INSERT ON Donor
FOR EACH ROW
BEGIN
    IF NEW.Age < 18 OR NEW.Age > 65 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Donor age must be between 18 and 65';
    END IF;
END//

-- Trigger 3: Update register status after donation
CREATE TRIGGER trg_update_register_after_donation
AFTER INSERT ON Donation
FOR EACH ROW
BEGIN
    UPDATE Register
    SET Last_donation_date = NEW.Donation_date,
        Status = 'Active'
    WHERE D_id = NEW.D_id AND H_id = NEW.H_id;
END//

-- Trigger 4: Check donation eligibility (90 days gap)
CREATE TRIGGER trg_check_donation_eligibility
BEFORE INSERT ON Donation
FOR EACH ROW
BEGIN
    DECLARE last_date DATE;
    SELECT MAX(Donation_date) INTO last_date
    FROM Donation
    WHERE D_id = NEW.D_id;
    
    IF last_date IS NOT NULL AND DATEDIFF(NEW.Donation_date, last_date) < 90 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Minimum 90 days gap required between donations';
    END IF;
END//

-- Trigger 5: Auto-create register entry for new donor
CREATE TRIGGER trg_auto_register_donor
AFTER INSERT ON Donor
FOR EACH ROW
BEGIN
    INSERT INTO Register (Last_donation_date, Status, Register_date, H_id, D_id)
    VALUES (NULL, 'Inactive', CURDATE(), 101, NEW.D_id);
END//

-- Trigger 6: Log blood request changes
CREATE TABLE Blood_Request_Log (
    Log_id INT AUTO_INCREMENT PRIMARY KEY,
    Request_Id INT,
    Old_Status VARCHAR(50),
    New_Status VARCHAR(50),
    Change_date DATETIME
);

CREATE TRIGGER trg_log_request_changes
AFTER UPDATE ON Blood_Request
FOR EACH ROW
BEGIN
    IF OLD.Status != NEW.Status THEN
        INSERT INTO Blood_Request_Log (Request_Id, Old_Status, New_Status, Change_date)
        VALUES (NEW.Request_Id, OLD.Status, NEW.Status, NOW());
    END IF;
END//

DELIMITER ;

-- =====================================
-- SECTION 3: PROCEDURES (6 Procedures)
-- =====================================

DELIMITER //

-- Procedure 1: Add new donor with contact
CREATE PROCEDURE sp_add_donor(
    IN p_address VARCHAR(255),
    IN p_first_name VARCHAR(100),
    IN p_last_name VARCHAR(100),
    IN p_age INT,
    IN p_gender VARCHAR(10),
    IN p_contact VARCHAR(50)
)
BEGIN
    DECLARE new_donor_id INT;
    
    INSERT INTO Donor (Address, First_Name, Last_Name, Age, Gender)
    VALUES (p_address, p_first_name, p_last_name, p_age, p_gender);
    
    SET new_donor_id = LAST_INSERT_ID();
    
    INSERT INTO Donor_Contact (Contact, D_id)
    VALUES (p_contact, new_donor_id);
    
    SELECT new_donor_id AS Donor_ID, 'Donor added successfully' AS Message;
END//

-- Procedure 2: Process blood request
CREATE PROCEDURE sp_process_blood_request(
    IN p_blood_type VARCHAR(10),
    IN p_quantity INT,
    IN p_h_id INT
)
BEGIN
    INSERT INTO Blood_Request (Blood_type, Quantity, Request_date, Status, H_id)
    VALUES (p_blood_type, p_quantity, CURDATE(), 'Pending', p_h_id);
    
    SELECT LAST_INSERT_ID() AS Request_ID, 'Blood request created' AS Message;
END//

-- Procedure 3: Record donation
CREATE PROCEDURE sp_record_donation(
    IN p_d_id INT,
    IN p_h_id INT,
    IN p_quantity INT
)
BEGIN
    DECLARE donor_name VARCHAR(200);
    
    SELECT CONCAT(First_Name, ' ', Last_Name) INTO donor_name
    FROM Donor WHERE D_id = p_d_id;
    
    INSERT INTO Donation (D_id, Donation_date, H_id, Quantity)
    VALUES (p_d_id, CURDATE(), p_h_id, p_quantity);
    
    SELECT LAST_INSERT_ID() AS Donation_ID, donor_name AS Donor_Name, 
           'Donation recorded successfully' AS Message;
END//

-- Procedure 4: Get available donors by blood type
CREATE PROCEDURE sp_get_available_donors(
    IN p_blood_type VARCHAR(10),
    IN p_h_id INT
)
BEGIN
    SELECT d.D_id, d.First_Name, d.Last_Name, d.Age, d.Gender, 
           dc.Contact, r.Last_donation_date
    FROM Donor d
    JOIN Donor_Contact dc ON d.D_id = dc.D_id
    JOIN Register r ON d.D_id = r.D_id AND r.H_id = p_h_id
    WHERE r.Status = 'Active'
    AND (r.Last_donation_date IS NULL OR 
         DATEDIFF(CURDATE(), r.Last_donation_date) >= 90);
END//

-- Procedure 5: Update blood request status
CREATE PROCEDURE sp_update_request_status(
    IN p_request_id INT,
    IN p_new_status VARCHAR(50)
)
BEGIN
    UPDATE Blood_Request
    SET Status = p_new_status
    WHERE Request_Id = p_request_id;
    
    SELECT p_request_id AS Request_ID, p_new_status AS New_Status,
           'Status updated successfully' AS Message;
END//

-- Procedure 6: Generate hospital donation report
CREATE PROCEDURE sp_hospital_donation_report(
    IN p_h_id INT,
    IN p_start_date DATE,
    IN p_end_date DATE
)
BEGIN
    SELECT h.Name AS Hospital_Name,
           COUNT(DISTINCT don.D_id) AS Total_Donors,
           COUNT(don.Donation_id) AS Total_Donations,
           SUM(don.Quantity) AS Total_Units_Collected,
           MIN(don.Donation_date) AS First_Donation,
           MAX(don.Donation_date) AS Last_Donation
    FROM Hospital h
    LEFT JOIN Donation don ON h.H_id = don.H_id
    WHERE h.H_id = p_h_id
    AND don.Donation_date BETWEEN p_start_date AND p_end_date
    GROUP BY h.H_id, h.Name;
END//

DELIMITER ;

-- =====================================
-- SECTION 4: FUNCTIONS (6 Functions)
-- =====================================

DELIMITER //

-- Function 1: Calculate donor age eligibility
CREATE FUNCTION fn_check_donor_eligibility(p_age INT)
RETURNS VARCHAR(20)
DETERMINISTIC
BEGIN
    IF p_age < 18 THEN
        RETURN 'Too Young';
    ELSEIF p_age > 65 THEN
        RETURN 'Too Old';
    ELSE
        RETURN 'Eligible';
    END IF;
END//

-- Function 2: Get total donations by donor
CREATE FUNCTION fn_get_donor_total_donations(p_d_id INT)
RETURNS INT
DETERMINISTIC
READS SQL DATA
BEGIN
    DECLARE total INT;
    SELECT COUNT(*) INTO total
    FROM Donation
    WHERE D_id = p_d_id;
    RETURN total;
END//

-- Function 3: Get days since last donation
CREATE FUNCTION fn_days_since_last_donation(p_d_id INT)
RETURNS INT
READS SQL DATA
DETERMINISTIC
BEGIN
    DECLARE last_date DATE;
    DECLARE days INT;
    
    SELECT MAX(Donation_date) INTO last_date
    FROM Donation
    WHERE D_id = p_d_id;
    
    IF last_date IS NULL THEN
        RETURN 999;
    ELSE
        SET days = DATEDIFF(CURDATE(), last_date);
        RETURN days;
    END IF;
END//

-- Function 4: Calculate hospital total blood units
CREATE FUNCTION fn_hospital_total_units(p_h_id INT)
RETURNS INT
READS SQL DATA
DETERMINISTIC
BEGIN
    DECLARE total INT;
    SELECT COALESCE(SUM(Quantity), 0) INTO total
    FROM Donation
    WHERE H_id = p_h_id;
    RETURN total;
END//

-- Function 5: Get pending requests count
CREATE FUNCTION fn_pending_requests_count(p_h_id INT)
RETURNS INT
READS SQL DATA
DETERMINISTIC
BEGIN
    DECLARE pending INT;
    SELECT COUNT(*) INTO pending
    FROM Blood_Request
    WHERE H_id = p_h_id AND Status = 'Pending';
    RETURN pending;
END//

-- Function 6: Get donor status
CREATE FUNCTION fn_get_donor_status(p_d_id INT)
RETURNS VARCHAR(50)
READS SQL DATA
DETERMINISTIC
BEGIN
    DECLARE days_since INT;
    SET days_since = fn_days_since_last_donation(p_d_id);
    
    IF days_since >= 90 THEN
        RETURN 'Available for Donation';
    ELSE
        RETURN CONCAT('Not Eligible (', 90 - days_since, ' days remaining)');
    END IF;
END//

DELIMITER ;

-- =====================================
-- SECTION 5: CRUD OPERATIONS
-- =====================================

-- CREATE Operations
-- Already covered in procedures: sp_add_donor, sp_process_blood_request, sp_record_donation

-- READ Operations (Sample Queries)
-- 1. Get all active donors
SELECT d.*, dc.Contact, r.Status, r.Last_donation_date
FROM Donor d
JOIN Donor_Contact dc ON d.D_id = dc.D_id
JOIN Register r ON d.D_id = r.D_id
WHERE r.Status = 'Active';

-- 2. Get all pending blood requests
SELECT br.*, h.Name AS Hospital_Name, h.City
FROM Blood_Request br
JOIN Hospital h ON br.H_id = h.H_id
WHERE br.Status = 'Pending'
ORDER BY br.Request_date;

-- UPDATE Operations
-- 1. Update donor information
UPDATE Donor
SET Address = '999 New Address St', Age = 31
WHERE D_id = 1;

-- 2. Update blood request status
UPDATE Blood_Request
SET Status = 'Approved'
WHERE Request_Id = 1001;

-- DELETE Operations
-- 1. Delete a donation record (with care)
DELETE FROM Donation WHERE Donation_id = 5001;

-- 2. Delete a blood request
DELETE FROM Blood_Request WHERE Request_Id = 1001;

-- =====================================
-- SECTION 6: NESTED QUERIES (6 Queries)
-- =====================================

-- Nested Query 1: Find donors who have donated more than average
SELECT d.D_id, d.First_Name, d.Last_Name, COUNT(don.Donation_id) AS Total_Donations
FROM Donor d
JOIN Donation don ON d.D_id = don.D_id
GROUP BY d.D_id, d.First_Name, d.Last_Name
HAVING COUNT(don.Donation_id) > (
    SELECT AVG(donation_count)
    FROM (
        SELECT COUNT(*) AS donation_count
        FROM Donation
        GROUP BY D_id
    ) AS avg_donations
);

-- Nested Query 2: Find hospitals with pending requests
SELECT h.H_id, h.Name, h.City
FROM Hospital h
WHERE h.H_id IN (
    SELECT DISTINCT H_id
    FROM Blood_Request
    WHERE Status = 'Pending'
);

-- Nested Query 3: Find donors eligible for next donation
SELECT d.D_id, d.First_Name, d.Last_Name, d.Age
FROM Donor d
WHERE d.D_id IN (
    SELECT D_id
    FROM Donation
    GROUP BY D_id
    HAVING MAX(Donation_date) < DATE_SUB(CURDATE(), INTERVAL 90 DAY)
);

-- Nested Query 4: Find patients in hospitals with approved blood requests
SELECT p.Patient_Id, p.First_Name, p.Last_Name, p.Disease
FROM Patient p
WHERE p.H_id IN (
    SELECT H_id
    FROM Blood_Request
    WHERE Status = 'Approved'
);

-- Nested Query 5: Find donors who haven't donated yet
SELECT d.D_id, d.First_Name, d.Last_Name
FROM Donor d
WHERE d.D_id NOT IN (
    SELECT DISTINCT D_id
    FROM Donation
);

-- Nested Query 6: Find hospitals requesting blood types matching active donors
SELECT DISTINCT h.Name, br.Blood_type, br.Quantity
FROM Hospital h
JOIN Blood_Request br ON h.H_id = br.H_id
WHERE br.Blood_type IN (
    SELECT DISTINCT Request_bloodtype
    FROM Patient
    WHERE H_id = br.H_id
);

-- =====================================
-- SECTION 7: JOIN QUERIES (6 Queries)
-- =====================================

-- Join Query 1: Complete donor information with contacts and registration
SELECT d.D_id, d.First_Name, d.Last_Name, d.Age, d.Gender, d.Address,
       dc.Contact, r.Status, r.Register_date, r.Last_donation_date
FROM Donor d
INNER JOIN Donor_Contact dc ON d.D_id = dc.D_id
INNER JOIN Register r ON d.D_id = r.D_id;

-- Join Query 2: Hospital blood requests with hospital details
SELECT h.Name AS Hospital_Name, h.City, h.State,
       br.Request_Id, br.Blood_type, br.Quantity, br.Request_date, br.Status
FROM Hospital h
INNER JOIN Blood_Request br ON h.H_id = br.H_id
ORDER BY br.Request_date DESC;

-- Join Query 3: Donation history with donor and hospital information
SELECT don.Donation_id, don.Donation_date, don.Quantity,
       d.First_Name AS Donor_FirstName, d.Last_Name AS Donor_LastName,
       h.Name AS Hospital_Name, h.City
FROM Donation don
INNER JOIN Donor d ON don.D_id = d.D_id
INNER JOIN Hospital h ON don.H_id = h.H_id
ORDER BY don.Donation_date DESC;

-- Join Query 4: Patients with hospital and blood request matching
SELECT p.Patient_Id, p.First_Name, p.Last_Name, p.Age, p.Disease, 
       p.Request_bloodtype, h.Name AS Hospital_Name,
       br.Status AS Request_Status, br.Request_date
FROM Patient p
INNER JOIN Hospital h ON p.H_id = h.H_id
LEFT JOIN Blood_Request br ON p.H_id = br.H_id 
       AND p.Request_bloodtype = br.Blood_type;

-- Join Query 5: Complete register information with donor and hospital
SELECT r.Register_date, r.Last_donation_date, r.Status,
       d.First_Name, d.Last_Name, d.Age,
       h.Name AS Hospital_Name, h.City
FROM Register r
INNER JOIN Donor d ON r.D_id = d.D_id
INNER JOIN Hospital h ON r.H_id = h.H_id
WHERE r.Status = 'Active';

-- Join Query 6: Multi-table join - Complete donation ecosystem
SELECT don.Donation_id, don.Donation_date, don.Quantity,
       CONCAT(d.First_Name, ' ', d.Last_Name) AS Donor_Name,
       dc.Contact AS Donor_Contact,
       h.Name AS Hospital_Name, hc.Contact AS Hospital_Contact,
       r.Status AS Registration_Status
FROM Donation don
INNER JOIN Donor d ON don.D_id = d.D_id
INNER JOIN Donor_Contact dc ON d.D_id = dc.D_id
INNER JOIN Hospital h ON don.H_id = h.H_id
INNER JOIN Hospital_Contact hc ON h.H_id = hc.H_id
INNER JOIN Register r ON d.D_id = r.D_id AND h.H_id = r.H_id;

-- =====================================
-- SECTION 8: AGGREGATE QUERIES (6 Queries)
-- =====================================

-- Aggregate Query 1: Total donations and units by hospital
SELECT h.Name AS Hospital_Name, h.City,
       COUNT(don.Donation_id) AS Total_Donations,
       SUM(don.Quantity) AS Total_Units_Collected,
       AVG(don.Quantity) AS Avg_Units_Per_Donation
FROM Hospital h
LEFT JOIN Donation don ON h.H_id = don.H_id
GROUP BY h.H_id, h.Name, h.City
ORDER BY Total_Units_Collected DESC;

-- Aggregate Query 2: Donor statistics with donation count
SELECT d.D_id, CONCAT(d.First_Name, ' ', d.Last_Name) AS Donor_Name,
       d.Age, d.Gender,
       COUNT(don.Donation_id) AS Total_Donations,
       SUM(don.Quantity) AS Total_Units_Donated,
       MAX(don.Donation_date) AS Last_Donation_Date,
       MIN(don.Donation_date) AS First_Donation_Date
FROM Donor d
LEFT JOIN Donation don ON d.D_id = don.D_id
GROUP BY d.D_id, d.First_Name, d.Last_Name, d.Age, d.Gender
ORDER BY Total_Units_Donated DESC;

-- Aggregate Query 3: Blood request statistics by status
SELECT Status, COUNT(*) AS Request_Count,
       SUM(Quantity) AS Total_Units_Requested,
       AVG(Quantity) AS Avg_Units_Per_Request
FROM Blood_Request
GROUP BY Status;

-- Aggregate Query 4: Blood type demand analysis
SELECT Blood_type,
       COUNT(*) AS Total_Requests,
       SUM(Quantity) AS Total_Units_Requested,
       AVG(Quantity) AS Avg_Units_Per_Request,
       SUM(CASE WHEN Status = 'Approved' THEN 1 ELSE 0 END) AS Approved_Requests,
       SUM(CASE WHEN Status = 'Pending' THEN 1 ELSE 0 END) AS Pending_Requests
FROM Blood_Request
GROUP BY Blood_type
ORDER BY Total_Units_Requested DESC;

-- Aggregate Query 5: Monthly donation trends
SELECT YEAR(Donation_date) AS Year,
       MONTH(Donation_date) AS Month,
       COUNT(*) AS Total_Donations,
       SUM(Quantity) AS Total_Units,
       COUNT(DISTINCT D_id) AS Unique_Donors,
       COUNT(DISTINCT H_id) AS Unique_Hospitals
FROM Donation
GROUP BY YEAR(Donation_date), MONTH(Donation_date)
ORDER BY Year DESC, Month DESC;

-- Aggregate Query 6: Hospital-wise patient and request analysis
SELECT h.Name AS Hospital_Name,
       COUNT(DISTINCT p.Patient_Id) AS Total_Patients,
       COUNT(DISTINCT br.Request_Id) AS Total_Requests,
       COUNT(DISTINCT don.Donation_id) AS Total_Donations,
       SUM(don.Quantity) AS Total_Blood_Units
FROM Hospital h
LEFT JOIN Patient p ON h.H_id = p.H_id
LEFT JOIN Blood_Request br ON h.H_id = br.H_id
LEFT JOIN Donation don ON h.H_id = don.H_id
GROUP BY h.H_id, h.Name
ORDER BY Total_Blood_Units DESC;

-- =====================================
-- SECTION 9: TESTING FUNCTIONS
-- =====================================

-- Test Function 1: Check donor eligibility
SELECT D_id, First_Name, Last_Name, Age, 
       fn_check_donor_eligibility(Age) AS Eligibility_Status
FROM Donor;

-- Test Function 2: Get donor donation count
SELECT D_id, First_Name, Last_Name,
       fn_get_donor_total_donations(D_id) AS Total_Donations
FROM Donor;

-- Test Function 3: Days since last donation
SELECT D_id, First_Name, Last_Name,
       fn_days_since_last_donation(D_id) AS Days_Since_Last_Donation,
       fn_get_donor_status(D_id) AS Donation_Status
FROM Donor;

-- Test Function 4: Hospital blood units
SELECT H_id, Name, 
       fn_hospital_total_units(H_id) AS Total_Units_Collected
FROM Hospital;

-- Test Function 5: Pending requests
SELECT H_id, Name,
       fn_pending_requests_count(H_id) AS Pending_Requests
FROM Hospital;

-- =====================================
-- END OF SQL FILE
-- =====================================
