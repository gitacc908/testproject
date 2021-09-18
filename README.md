### Setup
1. Create a folder and put all the files inside it.
2. Create a virtual environtment - `virtualenv env`
3. Activate VirtualENV - `source env/bin/activate`
5. Run requirements.txt - `pip3 install -r requirements.txt`
6. Run migrations - `python3 manage.py migrate`
7. Create superuser - `python3 manage.py createsuperuser`
8. Run the Application - `python3 manage.py runserver`
9. Go to - http://localhost:8000/


### DB Setup
You can connect to SQLite while specifying a new database file (one that doesn’t already exist):

sqlite3 Store2.db
By specifying a database file that doesn’t exist, SQLite will create a blank database.

Now that you’re in SQLite, you can read the contents of the backup file:

.read 'NameOfTheFile'.sql
That’s all there is to it. The database has been reconstructed from the .sql file. All tables have been created and all data has been inserted.