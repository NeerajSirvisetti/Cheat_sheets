from flask import Flask # Import Flask Class
app = Flask(__name__) # Create an Instance

@app.route('/') # Route the Function
def main(): # Run the function
   x = 'String' # Set x to 'String'
   return render_template('index.html', x=x) # Render the template with a variable

app.run(host='0.0.0.0', port=5000, debug=True) # Run the Application (in debug mode)