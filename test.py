from flask import Flask, request, render_template_string
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    output = ""
    if request.method == 'POST':
        command = request.form.get('command', '')
        
        # Directly executing the command without a whitelist (dangerous)
        try:
            output = subprocess.check_output(command, shell=True, text=True)
        except Exception as e:
            output = f"Error: {str(e)}"

    # HTML template as a string
    html = '''
    <!doctype html>
    <html>
        <head>
            <title>Command Executor</title>
        </head>
        <body>
            <h1>Execute Command</h1>
            <form method="post">
                <input type="text" name="command" placeholder="Enter command" required>
                <input type="submit" value="Execute">
            </form>
            <h2>Output:</h2>
            <pre>{{output}}</pre>
        </body>
    </html>
    '''
    return render_template_string(html, output=output)

if __name__ == '__main__':
    app.run(debug=True)
