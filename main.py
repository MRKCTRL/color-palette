from flask import flask,  render_template, request
import numpy as np
from scipy import misc
from PIL import image
from werkzeug.utils import secure_filename
import os


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/Users/jabu/home'
app.config['MAX_CONTENT_PATH'] = 10000000

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/post', methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)

        if len(filename) > 1:
            f_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            f.save(fullpath)
            pallete_hex, pallete_rgb = get_color(fullpath)
            return_render('index.html', hex_success=True, pallete_hex=palette_hex)
        return render_template('index.html')


def drop_image():
    file_name = input('drop image below')
    my_img = Image.open(file_name)
    img = misc.face()
    img_arr = nnp.array(img)
    plt.show(img)

# TODO: function to get the colors
# TODO: get the image as input



if __name__ == '__main__':
    app.run(debug=True)
