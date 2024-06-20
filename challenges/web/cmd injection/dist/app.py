import subprocess
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cmd', methods=['POST'])
def cmd():
    # Remove all spaces from the command
    command = request.form.get('cmd', '').replace(' ', '')
    not_allowed_commands = ['cat', 'rm']  # Example blocked commands
    if any(disallowed_cmd in command for disallowed_cmd in not_allowed_commands):
        return "Command not allowed!", 400

    try:
        # Using shell=True to illustrate a risky but common vulnerability
        result = subprocess.run(
            command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout or result.stderr, 200
    except Exception as e:
        return f"Error executing command: {str(e)}", 500


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
