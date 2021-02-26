import pymysql
import json
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request
import time 
from elasticsearch import Elasticsearch
from datetime import datetime



@app.route("/")
def index():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT 1")
		empRows = cursor.fetchall()
		respone = jsonify(empRows)
		respone.status_code = 200
		return """
		App: [  Ok  ] <br>
		Db :  [  Ok  ]
		"""
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

#Get all Breeds
@app.route('/breeds')
def breeds():
	try:
		#get initial time function
		start = time.time()
		#mysql block code
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM cats")
		empRows = cursor.fetchall()
		respone = jsonify(empRows) 		
		#get end time execution
		end = time.time() - start
		#format output timestamp
		timestamp = get_current_timestamp_formated()
		#send data to audit elastic
		audit_es(respone.status_code, 'GET', empRows, end, timestamp)
		return respone
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

#Get a specify Breed
@app.route('/breeds/<name>')
def breed(name):
	try:
		#get initial time function
		start = time.time()
		#mysql block code
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM cats WHERE name = %s", name)
		empRow = cursor.fetchone()
		if empRow:
			respone = jsonify(empRow)
		else:
			respone = jsonify(message="{} Not Found".format(name))
		#get end time execution
		end = time.time() - start
		#format output timestamp
		timestamp = get_current_timestamp_formated()
		#send data to audit elastic
		audit_es(respone.status_code, 'GET', empRow, end, timestamp)
		return respone
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

#Get Breed with temperament equals <temperament>
@app.route('/temperament')
def temperaments():
	try:
		#get initial time function
		start = time.time()
		#mysql block code
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT temperament FROM cats")
		empRows = cursor.fetchall()
		respone = jsonify(empRows)
		#get end time execution
		end = time.time() - start
		#format output timestamp
		timestamp = get_current_timestamp_formated()
		#send data to audit elastic
		audit_es(respone.status_code, 'GET', empRows, end, timestamp)
		return respone
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

#Get Breed with temperament equals <temperament>
@app.route('/temperament/<temperament>')
def temperament(temperament):
	try:
		#get initial time function
		start = time.time()
		#mysql block code
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT name FROM cats WHERE temperament LIKE %s", ('%' + temperament + '%'))
		empRow = cursor.fetchall()
		respone = jsonify(empRow)
		if empRow:
			respone = jsonify(empRow)
		else:
			respone = jsonify(message="{} Not Found".format(name))
		#get end time execution
		end = time.time() - start
		#format output timestamp
		timestamp = get_current_timestamp_formated()
		#send data to audit elastic
		audit_es(respone.status_code, 'GET', empRow, end, timestamp)
		return respone
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

#Get all Origin
@app.route('/origin')
def origins():
	try:
		#get initial time function
		start = time.time()
		#mysql block code
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT origin FROM cats")
		empRows = cursor.fetchall()
		respone = jsonify(empRows)
		#get end time execution
		end = time.time() - start
		#format output timestamp
		timestamp = get_current_timestamp_formated()
		#send data to audit elastic
		audit_es(respone.status_code, 'GET', empRows, end, timestamp)
		return respone
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

#Get Breed with origin equals <origin>
@app.route('/origin/<origin>')
def origin(origin):
	try:
		#get initial time function
		start = time.time()
		#mysql block code
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT name FROM cats WHERE origin LIKE %s", ("%" + origin + "%"))
		empRow = cursor.fetchall()
		respone = jsonify(empRow)
		if empRow:
			respone = jsonify(empRow)
		else:
			respone = jsonify(message="{} Not Found".format(name))
		#get end time execution
		end = time.time() - start
		#format output timestamp
		timestamp = get_current_timestamp_formated()
		#send data to audit elastic
		audit_es(respone.status_code, 'GET', empRow, end, timestamp)
		return respone
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

#Get Breed with origin equals <origin>
@app.route('/hat')
def hat():
	try:
		#get initial time function
		start = time.time()
		#mysql block code
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM cats WHERE id_api LIKE %s", "%hat%")
		empRow = cursor.fetchall()
		respone = jsonify(empRows)
		#get end time execution
		end = time.time() - start
		#format output timestamp
		timestamp = get_current_timestamp_formated()
		#send data to audit elastic
		audit_es(respone.status_code, 'GET', empRows, end, timestamp)
		return respone
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

#Get Breed with origin equals <origin>
@app.route('/glasses')
def glasses():
	try:
		#get initial time function
		start = time.time()
		#mysql block code
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM cats WHERE id_api LIKE %s", "%glasses%")
		empRow = cursor.fetchall()
		respone = jsonify(empRow)
		#get end time execution
		end = time.time() - start
		#format output timestamp
		timestamp = get_current_timestamp_formated()
		#send data to audit elastic
		audit_es(respone.status_code, 'GET', empRows, end, timestamp)
		return respone
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

@app.errorhandler(404)
def not_found(error=None):
	#get initial time function
	start = time.time()
	#return block
	message = {
			'status_code': 404,
			'message': 'Record not found: ' + request.full_path,
	}
	respone = jsonify(message)
	#get end time execution
	end = time.time() - start
	#format output timestamp
	timestamp = get_current_timestamp_formated()
	#send data to audit elastic
#	audit_es(respone.status_code, 'GET', 'Not values', end, timestamp)
	return respone

@app.errorhandler(500)
def bad_request(error=None):
	#get initial time function
	start = time.time()
	#return block
	message = {
			'status_code': 500,
			'message': 'It was not possible to interpret the request ' + request.full_path,
	}
	respone = jsonify(message)
	#get end time execution
	end = time.time() - start
	#format output timestamp
	timestamp = get_current_timestamp_formated()
	#send data to audit elastic
#	audit_es(respone.status_code, 'GET', 'Not values', end, timestamp)
	return respone

def get_current_timestamp_formated():
    dateTimeObj = datetime.now()
    return str(dateTimeObj.strftime("%d/%m/%Y %H:%M:%S"))

def audit_es(status_code, method, response, end, timestamp):
	if status_code == 200:
		httpc = 'SUCCESS'
	elif status_code == 404:
		httpc = 'INFO'
	elif status_code == 500:
		httpc = 'ERROR'
	else:
		httpc = status_code

	#get IP
	ip = request.remote_addr

	es=Elasticsearch("elasticsearch")
	audit = {}
	audit.update({"@timestamp" : timestamp})
	audit.update({"type" : httpc})
	audit.update({"http_code" : status_code})
	audit.update({"method" : method})
	audit.update({"IP" : ip})
	audit.update({"url" : request.full_path})
	audit.update({"execution_time" : end})
	audit.update({"response_payload" : response})
	body = json.dumps(audit)
	audit =  es.index(index='audit-py',doc_type='_doc',body=body)

	end2 = str(end)

	print("{} : {} [{}] : {} from {}, execution time: {}s in {} ".format(timestamp, httpc, status_code, method, ip, end2[:5], request.path))
	return audit

if __name__ == "__main__":
  app.run(host='0.0.0.0')