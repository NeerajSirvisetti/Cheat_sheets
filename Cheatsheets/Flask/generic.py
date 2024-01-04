from flask import Flask, render_template # Import Flask Class, and render_template
app = Flask(__name__) # Create an Instance

@app.route('/') # Route the Function
def main(): # Run the function
    return render_template('index.html') # Render the template

app.run(host='0.0.0.0', port=5000, debug=True) # Run the Application (in debug mode)