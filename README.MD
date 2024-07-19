Python version = 3.11.4
macOS = Ventura 13.4

I used a virtual ennviornment for this exerise. To start it, run the following from the root folder;

```
source venv/bin/activate
```

To run the code, ensure you have python 3 installed. Version 3.11.5 is the version this project was developed on.

Next, ensure flask is installed on your local machine. You can run the following command to install it. Note: future required packages such as for security will be added here:

```
pip install -r requirements.txt
```

To run the flask application from the root folder, you may have to add a temporary variable in your current terminal. To do this run:

```
export FLASK_APP=api.py
```

You can then start the flask application using:

```
flask run
```

To initialize the database, please run:

```
python initDB.py
```

Finally, once this is up and running, you can verifiy that the create user endpoint works by running:

```
curl --location 'http://127.0.0.1:5000/player' \
--header 'Content-Type: application/json' \
--data '{ "name": "testName" }'
```

And verifying that the database has updated. I used "DB Browser for SQLite" to view the database.

Further to this, the file `testing_script.py` can be run to verify the operation of the battle engine as the fully operational endpoint to show this has not been implemented yet.

