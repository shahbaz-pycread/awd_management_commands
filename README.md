# AWD Management Commands 
AWD Management Commandsis a custom Django management commands package that automates 
various tasks like greeting, inserting data into the database, and importing data from CSV files into specific tables. 
These commands can simplify repetitive tasks during Django development and data handling.

# Features
- Greeting Command: Outputs a greeting message.
- InsertData Command: Inserts data into the Django database programmatically.
- ImportData Command: Imports data from a CSV file into the Django database.
- ImportDataInTable Command: Allows importing CSV data into any specific table.
  
## Installation
 - Clone the repository to your local machine:
 - git clone https://github.com/yourusername/awd_management_commands.git
 - Navigate to the project directory:

 - cd awd_management_commands
 - Install the necessary dependencies (if any):

``pip install -r requirements.txt``

- Add the awd_management_commands app to your Django project’s INSTALLED_APPS in settings.py:
``
INSTALLED_APPS = [
    ...,
    'awd_management_commands',
]``

### Usage
#### Greeting Command
 - This command outputs a simple greeting message. You can run the command using:

``python manage.py greeting``
#### InsertData Command
 - Use the insertdata command to insert data into your Django database. The command will automatically insert pre-defined data.

``python manage.py insertdata``

#### ImportData Command
 - This command allows importing data from a CSV file into the Django database. You need to specify the path to the CSV file.

``python manage.py importdata --file=<path_to_csv_file>``

#### ImportDataInTable Command
 - You can import data from a CSV file to a specific table in your database using this command. Specify the file path and table name.

``python manage.py importdataintable --file=<path_to_csv_file> --model=<model_name>``

Command Options
--file: Path to the CSV file you want to import.
--model: Name of the model where you want to insert data (applicable for importdataintable command).
Example
Here's an example to import data from a CSV file called data.csv into the my_table table:

``python manage.py importdata_to_table --file=data.csv --model=my_model``

Contributing
Feel free to open an issue or submit a pull request if you'd like to contribute to this project. Contributions are welcome!
