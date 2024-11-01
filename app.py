# app.py
from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    output = ""
    if request.method == 'POST':
        user_input = request.form['input_text']
        try:
            # Execute the PowerShell script with the user input as a parameter
            result = subprocess.run(
                ['powershell', '-ExecutionPolicy', 'Bypass', '-File', 'echoscript.ps1', '-InputText', user_input],
                capture_output=True,
                text=True
            )
            output = result.stdout
        except Exception as e:
            output = f"An error occurred: {str(e)}"
    return render_template('index.html', output=output)

if __name__ == '__main__':
    app.run(debug=True)
