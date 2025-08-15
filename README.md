# Python Inventory Tracker

A simple desktop application for managing tools and spare parts inventory, built with Python, Tkinter, and SQLite. This project is designed as a straightforward tool for small workshops, garages, or maintenance departments to keep track of their assets.

![Application Screenshot](screenshot.png)

## Features

-   **Add, Update, & Delete:** Perform full CRUD (Create, Read, Update, Delete) operations on inventory items.
-   **Dynamic Search:** Instantly search for items by name, part number, or supplier.
-   **Stock Level Alerts:** Items with a quantity below their specified minimum are highlighted in orange for easy identification. Out-of-stock items are highlighted in red.
-   **Data Persistence:** All data is stored locally in a single-file SQLite database (`inventory.db`).
-   **Input Validation:** Prevents crashes by ensuring that quantity and price fields only accept numeric input.
-   **User-Friendly Interface:** Built with Python's native Tkinter library for a lightweight and responsive experience.

## Technologies Used

-   **Python 3**
-   **Tkinter** (for the Graphical User Interface)
-   **SQLite3** (for the database)

## Getting Started

To run this application on your local machine, follow these simple steps.

### Prerequisites

You need to have Python 3 installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Installation & Running

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/YourUsername/Python-Inventory-Tracker.git
    ```

2.  **Navigate to the project directory:**
    ```bash
    cd Python-Inventory-Tracker
    ```

3.  **Run the application:**
    No external libraries are needed as Tkinter and SQLite3 are part of the Python standard library.
    ```bash
    python app.py
    ```
    (On some systems, you might need to use `python3` or `py` instead of `python`).

## How to Use

1.  Launch the application by running `app.py`.
2.  The main window will appear. The application will automatically create an `inventory.db` file in the project folder if one does not exist.
3.  **To add an item:** Fill in the details in the form at the top and click the "Add Item" button.
4.  **To update an item:** Click on any item in the list. Its details will load into the form. Make your changes and click "Update Selected".
5.  **To delete an item:** Select an item from the list and click "Delete Selected".
6.  **To find an item:** Type a keyword into the search bar and click "Search". Click "Show All" to clear the search filter.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
