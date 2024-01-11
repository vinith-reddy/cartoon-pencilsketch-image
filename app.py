# Import necessary libraries
from flask import Flask, render_template, request
from cartoon import display
from werkzeug.utils import secure_filename
import os

# Create a Flask application
app = Flask(__name__)

# Set the upload folder
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'uploads')
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Define the route for the home page
@app.route('/')
def index():
    return render_template('index1.html')

# Define the route for file upload
@app.route('/uploader', methods=['POST', 'GET'])
def getValue():
    if request.method == 'POST':
        f = request.files['infile']
        filename = secure_filename(f.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        f.save(filepath)

        # Call the display function with the file path
        image_paths = display(filepath)

        # Pass the processed image paths to the template
        return render_template("index2.html", image_paths=image_paths)

# Run the application if executed as the main script
if __name__ == "__main__":
    app.run(debug=True, port=5001)
