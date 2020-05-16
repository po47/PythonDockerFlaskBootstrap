from typing import List, Dict
import simplejson as json
from flask import Flask, request, Response, redirect
from flask import render_template
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor

app = Flask(__name__)
mysql = MySQL(cursorclass=DictCursor)

app.config['MYSQL_DATABASE_HOST'] = 'db'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_DB'] = 'bioData'
mysql.init_app(app)


@app.route('/', methods=['GET'])
def index():
    user = {'username': 'Bio Stats'}
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM biostats')
    result = cursor.fetchall()
    return render_template('index.html', title='Home', user=user, biostats=result)


@app.route('/view/<int:biostat_id>', methods=['GET'])
def record_view(biostat_id):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM biostats WHERE id=%s', biostat_id)
    result = cursor.fetchall()
    return render_template('view.html', title='View Form', biostat=result[0])


@app.route('/edit/<int:biostat_id>', methods=['GET'])
def form_edit_get(biostat_id):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM biostats WHERE id=%s', biostat_id)
    result = cursor.fetchall()
    return render_template('edit.html', title='Edit Form', biostat=result[0])


@app.route('/edit/<int:biostat_id>', methods=['POST'])
def form_update_post(biostat_id):
    cursor = mysql.get_db().cursor()
    inputData = (request.form.get('YourName'), request.form.get('YourSex'), request.form.get('YourAge'),
                 request.form.get('YourHeight'), request.form.get('YourWeight'), biostat_id)
    sql_update_query = """UPDATE biostats t SET t.YourName = %s, t.Sex = %s, t.Age = %s, t.Height_in = %s, t.Weight_lbs = %s WHERE t.id = %s """
    cursor.execute(sql_update_query, inputData)
    mysql.get_db().commit()
    return redirect("/", code=302)


@app.route('/biostats/new', methods=['GET'])
def form_insert_get():
    return render_template('new.html', title='New Biostat Form')


@app.route('/biostats/new', methods=['POST'])
def form_insert_post():
    cursor = mysql.get_db().cursor()
    inputData = (request.form.get('YourName'), request.form.get('Sex'), request.form.get('Age'),
                 request.form.get('Height_in'), request.form.get('Weight_lbs'))
    sql_insert_query = """INSERT INTO biostats (YourName,Sex,Age,Height_in,Weight_lbs) VALUES (%s, %s, %s, %s, %s) """
    cursor.execute(sql_insert_query, inputData)
    mysql.get_db().commit()
    return redirect("/", code=302)


@app.route('/delete/<int:biostat_id>', methods=['POST'])
def form_delete_post(biostat_id):
    cursor = mysql.get_db().cursor()
    sql_delete_query = """DELETE FROM biostats WHERE id = %s """
    cursor.execute(sql_delete_query, biostat_id)
    mysql.get_db().commit()
    return redirect("/", code=302)


@app.route('/api/v1/biostats', methods=['GET'])
def api_browse() -> str:
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM biostats')
    result = cursor.fetchall()
    json_result = json.dumps(result);
    resp = Response(json_result, status=200, mimetype='application/json')
    return resp


@app.route('/api/v1/biostats/<int:biostat_id>', methods=['GET'])
def api_retrieve(biostat_id) -> str:
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM biostats WHERE id=%s', biostat_id)
    result = cursor.fetchall()
    json_result = json.dumps(result);
    resp = Response(json_result, status=200, mimetype='application/json')
    return resp


@app.route('/api/v1/biostats/', methods=['POST'])
def api_add() -> str:
    resp = Response(status=201, mimetype='application/json')
    return resp


@app.route('/api/v1/biostats/<int:biostat_id>', methods=['PUT'])
def api_edit(biostat_id) -> str:
    resp = Response(status=201, mimetype='application/json')
    return resp


@app.route('/api/biostats/<int:biostat_id>', methods=['DELETE'])
def api_delete(biostat_id) -> str:
    resp = Response(status=210, mimetype='application/json')
    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
