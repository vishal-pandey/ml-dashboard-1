from flask import Flask,request, render_template
# from flask_cors import CORS
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import json
from werkzeug import secure_filename

# from cStringIO import StringIO
import base64


app = Flask(__name__)
# CORS(app)

@app.route('/',methods=['GET' , 'POST'])
def index():

  if request.method == 'POST':
      f = request.files['file']
      f.save("dataset/"+secure_filename(f.filename))

      if f.filename.split('.')[-1] == 'csv':
        df = pd.read_csv("dataset/"+secure_filename(f.filename))
        df.plot()
        plt.savefig('static/describe')

      return render_template('dashboard.html', table = df[:100].to_html())
      # return df[:100].to_html()

  if request.method == 'GET':
      return render_template('upload.html')
  
    



if __name__ == "__main__":
  app.run(threaded=False)