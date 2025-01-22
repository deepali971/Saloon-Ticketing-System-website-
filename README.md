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
Add screenshots here to visually represent the GUI (e.g., login page, service selection, ticket generation).

## Future Enhancements
- Add dynamic service management (add/update/delete services).
- Implement advanced reporting and analytics.
- Enhance security with hashed passwords and role-based access.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
