from flask import *
import os
from emotion import *

app=Flask(__name__)
app.config['SECRET_KEY']='emotion'
app.config['UPLOAD_FOLDER']="E:\PEDA\CAPTURED SHOTS"

@app.route('/',methods=['GET','POST'])
def homepage():
    if request.method=='POST':
        file=request.files['file']
        file_loc=os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_loc)
        out=detect_properties(file_loc)
        if out=='':
            return render_template('result.html',data=['Not a Face'],image=file_loc)
        else:
            return render_template('result.html',data=out,image=file_loc)
    return render_template('image_sentiment.html')
