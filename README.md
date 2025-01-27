# Saloon-Ticketing-System(website)

The Saloon Ticketing System is a Python-based application designed to simplify the customer management and billing process for saloons. This project features a user-friendly graphical interface built with Tkinter and a robust backend powered by an SQL database, enabling real-time updates and efficient ticket generation.

## Features
- Secure Login: Shop owner authentication with basic username and password verification.
- Service Selection: A clean interface displaying predefined services (Hair Cut, Spa, Facial) and their corresponding prices.
- Ticket Generation: Automatic generation of a unique ticket ID with:
  - Selected services and their prices.
  - The total amount to be paid.
- Database Integration: Real-time storage of ticket details in an SQL database, including:
  - Customer Name
  - Ticket ID
  - Services Selected
  - Total Amount
- CSV Export: Generates a CSV file for each ticket, allowing easy record-keeping and printing.

## Technologies Used
- Python: Core programming language.
- Tkinter: For designing the graphical user interface.
- SQLite: For backend database management.
- CSV Module: For exporting ticket details.

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/deepali971/Saloon-Ticketing-System2.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Saloon-Ticketing-System2
   ```
3. Install required dependencies (if any).
4. Run the application:
   ```bash
   python gui.py
   ```

## Screenshots
- Screenshots to visually represent the GUI
- Login Page
- <img src="![step1-login](https://github.com/user-attachments/assets/a414b046-af47-4542-99db-ae7139848893)" alt="Alt Text" style="width:50%; height:auto;">
<img src="![step1-login](https://github.com/user-attachments/assets/a414b046-af47-4542-99db-ae7139848893)" alt="Alt Text" width="300" height="200">
- Service Selection
- <img src="![step2-generating ticket](https://github.com/user-attachments/assets/d8ddc0ba-dfb6-4119-b654-4786b3e8dc1b)" alt="Alt Text" style="width:50%; height:auto;">
- <img src=" ![step2-generating ticket](https://github.com/user-attachments/assets/d8ddc0ba-dfb6-4119-b654-4786b3e8dc1b)" alt="Alt Text" width="300" height="200">
- Ticket Generation
- <img src="![step3-ticket generated](https://github.com/user-attachments/assets/d94acbbd-67e7-4b71-bdf4-4f42c771e1e0)" alt="Alt Text" style="width:50%; height:auto;">
- <img src="![step3-ticket generated](https://github.com/user-attachments/assets/d94acbbd-67e7-4b71-bdf4-4f42c771e1e0)" alt="Alt Text" width="300" height="200">

## Future Enhancements
- Add dynamic service management (add/update/delete services).
- Implement advanced reporting and analytics.
- Enhance security with hashed passwords and role-based access.


