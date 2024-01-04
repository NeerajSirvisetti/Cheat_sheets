from flask import Flask # Import Flask Class
app = Flask(__name__) # Create an Instance

@app.route('/<var>') # Route the Function
def main(var): # Run the function with an arg 'var'
    return var # Returns var

app.run(host='0.0.0.0', port=5000, debug=True) # Run the Application (in debug mode)