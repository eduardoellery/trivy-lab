from flask import Flask, request, render_template_string
import pickle
import base64
import os

app = Flask(__name__)

# Vulnerabilidade: Template Injection
TEMPLATE = '''
<h1>Hello {{name}}!</h1>
<p>Your input: {{user_input|safe}}</p>
'''

@app.route('/')
def home():
    return '<h1>Vulnerable App</h1><a href="/greet?name=World">Greet</a>'

@app.route('/greet')
def greet():
    name = request.args.get('name', 'Anonymous')
    user_input = request.args.get('input', '')
    
    # Vulnerabilidade: Server-Side Template Injection
    return render_template_string(TEMPLATE, name=name, user_input=user_input)

@app.route('/deserialize')
def deserialize():
    data = request.args.get('data')
    if data:
        # Vulnerabilidade: Insecure Deserialization
        try:
            decoded = base64.b64decode(data)
            obj = pickle.loads(decoded)
            return f"Deserialized: {obj}"
        except:
            return "Error deserializing"
    return "Provide data parameter"

@app.route('/cmd')
def cmd():
    command = request.args.get('cmd')
    if command:
        # Vulnerabilidade: Command Injection
        result = os.system(command)
        return f"Command executed: {command}"
    return "Provide cmd parameter"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
