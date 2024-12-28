from flask import Flask, redirect, render_template, url_for, request
import psycopg2

app = Flask(__name__)

DB_URL = 'postgresql://postgres:1234@localhost:5432/disha_student_data'

def connect_to_db():
    conn = psycopg2.connect(DB_URL)
    return conn

connect_to_db()

#daily login page for here 

def create__DaliyLogin_table():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS student_login (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            course VARCHAR(255) NOT NULL,
            current_language VARCHAR(255) NOT NULL,
            current_topic VARCHAR(255) NOT NULL,
            login_date DATE DEFAULT CURRENT_DATE,
            in_time VARCHAR(255) NOT NULL,
            out_time VARCHAR(255) NOT NULL
        );
    ''')
    conn.commit()
    cursor.close()
    conn.close()

create__DaliyLogin_table()

@app.route('/DailyLogin', methods=['GET', 'POST'])
def Daily_login():  
    if request.method == 'POST':
        name = request.form['name']
        course = request.form['course']
        current_language = request.form['current_language']
        current_topic = request.form['current_topic']
        in_time = request.form['in_time']
        out_time = request.form['out_time']
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute(
            '''
            INSERT INTO student_login (name, course, current_language, current_topic, in_time, out_time)
            VALUES (%s, %s, %s, %s, %s, %s)
            ''', (name, course, current_language, current_topic, in_time, out_time)
        )
        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for('Daily_Login'))

    return render_template('DailyLogin.html')

#register user page form here

def create_register_table():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS student_data (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            mobile VARCHAR(255) NOT NULL,
            course VARCHAR(255) NOT NULL,
            batchtime VARCHAR(255) NOT NULL
        );
    ''')
    conn.commit()
    cursor.close()
    conn.close()

create_register_table() 

@app.route('/register', methods=['GET', 'POST'])
def register():  
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        mobile = request.form['mobile']
        course = request.form['course']
        batch_time = request.form['batchtime']
        
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute(
            '''
            INSERT INTO student_data (name, email, mobile, course, batchtime)
            VALUES (%s, %s, %s, %s, %s)
            ''', (name, email, mobile, course, batch_time)
        )
        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for('register'))

    return render_template('register.html')

# making a home page

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)