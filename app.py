from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management and flash messages

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    # You can process the data here (e.g., save to a database, perform calculations, etc.)
    flash(f'Hello, {name}! Your form has been submitted successfully.')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
    