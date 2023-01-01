from flask import Flask,render_template,request
from cartoon1 import display
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/uploader',methods=['POST','GET'])
def getValue():
    if request.method=='POST' :
        f = request.files['infile']
        f.save(secure_filename(f.filename))
        #print(f.filename)
        display(f)
        return render_template("index2.html") 
    

if __name__ == "__main__":
    app.run(debug=True)