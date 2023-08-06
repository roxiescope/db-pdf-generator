from flask import Flask, render_template, request, jsonify
import psycopg2
import config_reader

app = Flask(__name__)

app.secret_key = "caircocoders-ednalan"


@app.route('/')
def index():
    conn = psycopg2.connect(database='postgres',
                            user=config_reader.getXML('user'),
                            host=config_reader.getXML('host'),
                            password=config_reader.getXML('password'),
                            port=config_reader.getXML('port'))
    cur = conn.cursor()
    cur.execute("SELECT * FROM dragdrop ORDER BY listorder ASC")
    dragdrop = cur.fetchall()
    print(dragdrop)
    return render_template('index.html', dragdrop=dragdrop)


@app.route("/updateList", methods=["POST", "GET"])
def updateList():
    conn = psycopg2.connect(database='postgres',
                            user=config_reader.getXML('user'),
                            host=config_reader.getXML('host'),
                            password=config_reader.getXML('password'),
                            port=config_reader.getXML('port'))
    cur = conn.cursor()
    if request.method == 'POST':
        cur.execute("SELECT * FROM dragdrop")
        number_of_rows = cur.fetchall()
        print(number_of_rows)
        getorder = request.form['order']
        print(getorder)
        order = getorder.split(",", len(number_of_rows))
        count = 0
        for value in number_of_rows:
            count += 1
            print(count)
            cur.execute("UPDATE dragdrop SET listorder = %s WHERE id = %s ", [count, value[0]])
            cur.connection.commit()
        cur.close()
    return jsonify('Successfully Updated')


if __name__ == "__main__":
    app.run(debug=True)
