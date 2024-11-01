# win-script-runner
A WebUI that broadcasts locally and uses inputs for running custom scripts on Windows. 

# Prerequisites
Python Installation: Ensure you have Python installed on your Windows machine. You can download it from python.org.

## Install Required Python Packages. 
Use an admin process if possible:
```bash
pip install Flask
```

# Usage
Create your custom script, reference it as appropriate in your repo, and run the Flask App:
```bash
python app.py
```

Example output with `...` substituted for further input and GET/POST requests:
```bash
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!

...
127.0.0.1 - - [01/Nov/2024 00:00:00] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Nov/2024 00:00:04] "POST / HTTP/1.1" 200 -
```