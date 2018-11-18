
from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from pathlib import Path
from datetime import datetime
from hashlib import sha256
application = Flask(__name__)
CORS(application)
@application.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

@application.route("/log",  methods=['GET', 'POST'])
def log():
	content = request.json	
	print(content)
	now = datetime.now()
	content['log_timestamp'] = now.strftime('%Y-%m-%d %H:%M:%S')
	year, month, day, hour = now.year, now.month, now.day, now.hour
	Path(f'/logs/{year}/{month}/{day}/{hour}').mkdir(parents=True, exist_ok=True)
	ser = json.dumps(content, indent=2, ensure_ascii=False)
	hashed = sha256(bytes(ser,'utf8')).hexdigest()
	with open(f'/logs/{year}/{month}/{day}/{hour}/{hashed}.json', 'w') as fp:
		fp.write(ser)
	return f"<h1 style='color:blue'>OK</h1>"

if __name__ == "__main__":
    application.run(host='0.0.0.0')
