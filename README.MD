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