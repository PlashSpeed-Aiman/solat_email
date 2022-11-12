import json
from dbInterface import insert_to_db, search_db
from emailModule import send_email
from parserModule import parse_today
import datetime
from fetcher import fetcher
from zone import Times,SolatZone
from typing import Optional
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Server Works!'

@app.route('/send-time/<string:email>')
def send_time(email:str):
	pass
@app.route('/api/<string:zone>')
def say_hello(zone : str):
	msg = ""
	date_time = datetime.datetime.today()
	print(date_time.strftime("%d %b %Y"))
	result = search_db(date_time.strftime("%d %b %Y"),zone,'salatdb.db')
	#THIS SUCKS,NEED BETTER LOGIC
	if result is not None:
		msg = return_msg(result)
	else:
		solat_times = parse_today(fetcher(zone))
		if solat_times is not None:
			insert_to_db('salatdb.db',solat_times)
			msg = return_msg(solat_times)
		msg = return_msg(solat_times)

	return msg
    
def return_msg(result:Optional[Times]):
	msg =""
	if result is not None:
		msg = f"""
		<html>
			<body>
			<h1>Solat Time</h1>
			<p>{result.to_string()}</p>
			</body>
		</html>
		"""
	else:
		msg = f"""
		<html>
			<body>
			<h1>Solat Time</h1>
			<p>No Data Received</p>
			</body>
		</html>
		"""
	return msg

# def main()->None:
#     a = parse_today(fetcher(SolatZone.JOHOR01))
#     b = parse_today({})

#     if a is not None:
#         print(a.to_string())
#         send_email(a.to_string())
#     # print(json.dumps(a))
# if __name__ == '__main__':
#     main()