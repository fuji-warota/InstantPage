import os, json
from flask import Flask, render_template, request, session, redirect, url_for,jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__, static_folder='./templates', static_url_path='')
app.config["JSON_AS_ASCII"] = False


#@app.route('/')
#def index():
 #   return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def upload_file():
  if request.method == 'POST':
    
    file = request.files['file']
    file_name = secure_filename(file.filename)
    file.save(os.path.join('download_file',file_name))

    with open("download_file/" + str(file_name)) as f:
      data = json.load(f)
      section = []
      item = []
      url = []
      for key in data.keys():
        section.append(key)
      #app.logger.debug(section)

      for i in section:
        app.logger.debug(type(i))
        for j in range(len(data[i])):
          item.append(data[i][j]['item'])
          url.append(data[i][j]['url'])

          #app.logger.debug(item)
    return render_template('instant_page.html', html_section=section,html_data=zip(item,url))
  return render_template('index.html')

app.run(host="0.0.0.0", port=8080, debug=True, threaded=True)
