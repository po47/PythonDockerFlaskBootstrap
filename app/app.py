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
app.config['MYSQL_DATABASE_DB'] = 'homeData'
mysql.init_app(app)


@app.route('/', methods=['GET'])
def index():
    user = {'username': 'Home Stats'}
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM homestats')
    result = cursor.fetchall()
    return render_template('index.html', title='Home', user=user, homestats=result)


@app.route('/view/<int:homestat_id>', methods=['GET'])
def record_view(homestat_id):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM homestats WHERE id=%s', homestat_id)
    result = cursor.fetchall()
    return render_template('view.html', title='View Form', homestat=result[0])


@app.route('/edit/<int:homestat_id>', methods=['GET'])
def form_edit_get(homestat_id):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM homestats WHERE id=%s', homestat_id)
    result = cursor.fetchall()
    return render_template('edit.html', title='Edit Form', homestat=result[0])


@app.route('/edit/<int:homestat_id>', methods=['POST'])
def form_update_post(homestat_id):
    cursor = mysql.get_db().cursor()
    inputData = (request.form.get('Street'), request.form.get('City'), request.form.get('Zip_Code'),
                 request.form.get('Selling_Price'), request.form.get('Listing_Price'), request.form.get('Sq_ft'),
                 request.form.get('Rooms'),
                 request.form.get('Baths'), request.form.get('Age_of_House'), homestat_id)
    sql_update_query = """UPDATE homestats t SET t.Street = %s, t.City = %s, t.Zip_Code = %s, t.Selling_Price_in = %s,
    t.Listing_Price = %s, t.Sq_ft = %s,t.Rooms = %s,t.Baths = %s,t.Age_of_House = %s, WHERE t.id = %s """
    cursor.execute(sql_update_query, inputData)
    mysql.get_db().commit()
    return redirect("/", code=302)


@app.route('/homestats/new', methods=['GET'])
def form_insert_get():
    return render_template('new.html', title='New Homestat Form')


@app.route('/homestats/new', methods=['POST'])
def form_insert_post():
    cursor = mysql.get_db().cursor()
    inputData = (request.form.get('Street'), request.form.get('City'), request.form.get('Zip_Code'),
                 request.form.get('Selling_Price'), request.form.get('Listing_Price'),
                 request.form.get('Listing_Price'), request.form.get('Sq_ft'), request.form.get('Rooms'),
                 request.form.get('Baths'), request.form.get('Age_of_House'))
    sql_insert_query = """INSERT INTO homestats (Street, City, Zip_Code, Selling_Price, Listing_Price, Sq_ft, Rooms, 
    Baths, Age_of_House) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) """
    cursor.execute(sql_insert_query, inputData)
    mysql.get_db().commit()
    return redirect("/", code=302)


@app.route('/delete/<int:homestat_id>', methods=['POST'])
def form_delete_post(homestat_id):
    cursor = mysql.get_db().cursor()
    sql_delete_query = """DELETE FROM homestats WHERE id = %s """
    cursor.execute(sql_delete_query, homestat_id)
    mysql.get_db().commit()
    return redirect("/", code=302)


@app.route('/api/v1/homestats', methods=['GET'])
def api_browse() -> str:
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM homestats')
    result = cursor.fetchall()
    json_result = json.dumps(result);
    resp = Response(json_result, status=200, mimetype='application/json')
    return resp


@app.route('/api/v1/homestats/<int:homestat_id>', methods=['GET'])
def api_retrieve(homestat_id) -> str:
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM homestats WHERE id=%s', homestat_id)
    result = cursor.fetchall()
    json_result = json.dumps(result);
    resp = Response(json_result, status=200, mimetype='application/json')
    return resp


@app.route('/api/v1/homestats/', methods=['POST'])
def api_add() -> str:
    resp = Response(status=201, mimetype='application/json')
    return resp


@app.route('/api/v1/homestats/<int:homestat_id>', methods=['PUT'])
def api_edit(homestat_id) -> str:
    resp = Response(status=201, mimetype='application/json')
    return resp


@app.route('/api/homestats/<int:homestat_id>', methods=['DELETE'])
def api_delete(homestat_id) -> str:
    resp = Response(status=210, mimetype='application/json')
    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
