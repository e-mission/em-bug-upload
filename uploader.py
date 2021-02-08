from flask import Flask, request, redirect, abort
from flask_cors import CORS, cross_origin
from flask_limiter import Limiter, util
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from werkzeug.utils import secure_filename
from datetime import datetime

app = Flask(__name__)

cors = CORS(app)

limiter = Limiter(
    app,
    key_func=util.get_remote_address,
    default_limits=["1000 per hour"]
)

OUTDIR="/phonelogs/"

patch_request_class(app, 1024 * 1024 * 1024) # 1G

@app.route('/phonelogs', methods=['POST'])
def uploader():
    # print(request)
    # print(request.files)
    # print(request.data)
    # print(request.form)
    if 'rawFile' not in request.form:
        print('No Files')
        abort(400)
    else:
        reason = request.form['reason']
        rawFileData = request.form['rawFile']
        filename = datetime.today().isoformat()+"_"+secure_filename(reason)
        f = open(OUTDIR+filename, "w")
        f.write(rawFileData)
        return 'file data of length %s written to %s' % (len(rawFileData), filename)
