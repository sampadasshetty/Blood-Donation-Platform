# 🩸 Blood Donation & Request Management Platform

A comprehensive desktop application for managing blood donations, requests, and hospital operations built with Python and MySQL.

## 📋 Table of Contents
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Database Setup](#database-setup)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Database Schema](#database-schema)
- [Screenshots](#screenshots)
- [Contributors](#contributors)
- [License](#license)

## ✨ Features

### Core Functionality
- **Donor Management**: Add, update, view, and delete donor records
- **Hospital Management**: Manage hospital information and contacts
- **Blood Request System**: Create and track blood requests with status management
- **Donation Tracking**: Record and monitor blood donations
- **Patient Management**: Maintain patient records and blood requirements
- **Reports & Analytics**: Generate comprehensive reports and statistics
- **Advanced Queries**: Execute complex queries for data analysis

### Database Features
- **6 Triggers**: Automated validation and status updates
- **6 Stored Procedures**: Streamlined data operations
- **6 Functions**: Utility functions for calculations
- **CRUD Operations**: Complete Create, Read, Update, Delete functionality
- **Nested Queries**: Complex data retrieval
- **Join Operations**: Multi-table data relationships
- **Aggregate Functions**: Statistical analysis

## 🛠️ Technology Stack

- **Frontend**: Python Tkinter with ttkthemes
- **Backend**: MySQL 8.0+
- **Database Connector**: mysql-connector-python
- **GUI Framework**: Tkinter, TTK
- **Theme**: Arc theme (modern UI)

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- MySQL 8.0 or higher
- pip (Python package manager)

### Step 1: Clone the Repository
```bash
git clone https://github.com/sampadasshetty/Blood-Donation-Platform.git
cd Blood-Donation-Platform
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Database Setup
1. Start your MySQL server
2. Open MySQL Workbench or command line client
3. Create database:
```sql
CREATE DATABASE mini_project;
USE mini_project;
```
4. Import the SQL file:
```bash
mysql -u root -p mini_project < src/PES2UG23CS522_PES2UG23CS467_H_Blood_Request_Platform.sql
```

### Step 4: Configure Database Connection
Edit the database credentials in `src/PES2UG23CS522_PES2UG23CS467_H_Blood_Request_Platform.py`:
```python
self.db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",  # Change this
    database="mini_project"
)
```

### Step 5: Run the Application
```bash
python src/PES2UG23CS522_PES2UG23CS467_H_Blood_Request_Platform.py
```

## 🗄️ Database Setup

### Database Schema
The platform uses 8 main tables:
- **Donor**: Donor personal information
- **Donor_Contact**: Donor contact details
- **Hospital**: Hospital information
- **Hospital_Contact**: Hospital contact details
- **Blood_Request**: Blood request records
- **Donation**: Donation transaction records
- **Patient**: Patient information
- **Register**: Donor-Hospital registration mapping

### Key Database Components

#### Triggers
1. Auto-update blood request status after donation
2. Validate donor age before registration
3. Update register status after donation
4. Check donation eligibility (90 days gap)
5. Auto-create register entry for new donor
6. Log blood request status changes

#### Stored Procedures
1. `sp_add_donor`: Add new donor with contact
2. `sp_process_blood_request`: Create blood request
3. `sp_record_donation`: Record donation
4. `sp_get_available_donors`: Get eligible donors
5. `sp_update_request_status`: Update request status
6. `sp_hospital_donation_report`: Generate reports

#### Functions
1. `fn_check_donor_eligibility`: Validate donor age
2. `fn_get_donor_total_donations`: Count donations
3. `fn_days_since_last_donation`: Calculate days
4. `fn_hospital_total_units`: Sum blood units
5. `fn_pending_requests_count`: Count pending requests
6. `fn_get_donor_status`: Get donation eligibility

## 📁 Project Structure

```
Blood-Donation-Platform/
│
├── src/
│   ├── PES2UG23CS522_PES2UG23CS467_H_Blood_Request_Platform.py  # Main application
│   └── PES2UG23CS522_PES2UG23CS467_H_Blood_Request_Platform.sql # Database schema
│
├── docs/
│   └── documentation.pdf
│
├── screenshots/
│   ├── dashboard.png
│   ├── donor_management.png
│   └── reports.png
│
├── .gitignore
├── requirements.txt
├── README.md
├── setup.py
└── LICENSE
```

## 🎯 Usage

### Main Menu Options

1. **Donor Management**
   - Add new donors with validation
   - View all registered donors
   - Update donor information
   - Delete donor records

2. **Hospital Management**
   - Register new hospitals
   - View hospital list
   - Update hospital details

3. **Blood Requests**
   - Create new blood requests
   - View pending/approved requests
   - Update request status

4. **Donations**
   - Record new donations
   - View donation history
   - Track donor contributions

5. **Patient Management**
   - Add patient records
   - View patient information
   - Track blood requirements

6. **Reports**
   - Hospital donation reports
   - Aggregate statistics
   - Blood type demand analysis

7. **Advanced Queries**
   - Execute predefined complex queries
   - View nested query results
   - Analyze donation trends

8. **Procedures/Functions**
   - Test stored procedures
   - Execute database functions
   - View function outputs

## 🔧 Configuration

### Database Configuration
Update credentials in the Python file:
```python
host="localhost"
user="root"
password="YOUR_PASSWORD"
database="mini_project"
```

### GUI Theme
The application uses the Arc theme. To change:
```python
root = ThemedTk(theme="arc")  # Options: arc, breeze, radiance, etc.
```

## 📊 Sample Data

The SQL file includes 10 sample records for each table:
- 10 Donors
- 10 Hospitals
- 10 Blood Requests
- 10 Donations
- 10 Patients
- 10 Registration records

## 🐛 Troubleshooting

### Common Issues

**Database Connection Error**
```
Solution: Check MySQL service is running and credentials are correct
```

**Module Import Error**
```bash
pip install --upgrade mysql-connector-python ttkthemes
```

**Trigger/Procedure Not Found**
```
Solution: Re-import the SQL file to create all database objects
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 👥 Contributors

- **PES2UG23CS522** - Developer
- **PES2UG23CS467** - Developer

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Contact

For queries and support:
- Create an issue on GitHub
- Email: sampadasam3003@gmail.com

## 🙏 Acknowledgments

- MySQL Documentation
- Python Tkinter Documentation
- TTKThemes Library
- PES University

---

⭐ **Star this repository if you find it helpful!**

Made with ❤️ by PESU Students
