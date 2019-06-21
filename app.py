from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL, MySQLdb
import datetime

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'smoking_test'
mysql = MySQL(app)

@app.route('/login', methods=['POST','GET'])
def login():
    return render_template('layout_log.html')

@app.route('/')
@app.route('/home')
def home(): 
    return render_template('utama.html')
    
@app.route('/kepala')
def kepala():
    #Pertanyaan Kepala
    ask = [
        "1.Apakah anda merasa sakit saat menghirup atau menghembuskan Nafas?.",
        "2.Apakah kepala terasa sakit mencengkram?.",
        "3.Apakah terjadi pembengkakan pada wajah?.",
        "4.Bercak kemerahan atau putih dalam mulut?.",
        "5.Apakah kesulitan dalam mengunyah?.",
        "6.Sakit kepala yang tiba-tiba.",
        "7.Tiba-tiba kehilangan kesadaran, keseimbangan, koordinasi, kontrol tubuh, dan bicara tidak jelas."
        ]
    return render_template('kepala.html', result = ask)
@app.route('/cek_kepala', methods = ['POST','GET'])
def cek_kepala():
    #Penyakit Kepala
    p01 = [5,5,5,5,5,0,0]
    p02 = [0,0,0,0,0,5,5]
    result = dict(request.form)
    key = list(result.values())
    data = list(map(float, key))
    hasil = []
   
    n1 = 0
    for j1 in range(0,5):
        
            n1 += data[j1]   
        
    n2 = 0
    for j2 in range(5,7):
        
            n2 += data[j2]

    hasil.append(round(n1/sum(p01)*100,2))
    hasil.append(round(n2/sum(p02)*100,2))

    penyakit = ['Kanker Mulut','Stroke']

    akhir = dict(zip(penyakit, hasil))  

    return render_template('cek_kepala.html', result = akhir)

@app.route('/tenggorokan')
def tenggorokan():
    ask = [
        '1. Perubahan suara serta sulit atau rasa sakit saat menelan serta mengunyah',
        '2. Pembengkakan pada wajah dan leher',
        '3. Batuk kronis serta telinga terasa sakit dan berdengung',
        '4. Timbul benjolan yang muncul di sekitar mata, rahang, leher, atau tenggorokan',
        '5. Pembengkakan kelenjar getah bening',
        '6. Tiba-tiba kehilangan kesadaran, keseimbangan, koordinasi, kontrol tubuh, dan bicara tidak jelas'
    ]
    return render_template('tenggorokan.html', result=ask)

@app.route('/cek_tenggorokan', methods=['GET','POST'])
def cek_tenggorokan():
    p01 = [5,5,5,5,5,5]
    
    result = dict(request.form)
    key = list(result.values())
    data = list(map(float, key))
    hasil = []
    n1 = 0
    for j1 in range(0,6):
        
            n1 += data[j1]
    hasil.append(round(n1/sum(p01)*100,2))
    penyakit = ['Kanker Tenggorokan']

    akhir = dict(zip(penyakit, hasil))
    return render_template('cek_tenggorokan.html', result = akhir)

@app.route('/dada')
def dada():
    ask = [
        '1. Pembengkakan kelenjar getah bening',
        '2. Dada sesak, nyeri, dan berat',
        '3. Batuk berdahak disertai bercak darah',
        '4. Penyakit infeksi saluran pernapasan (flu atau pilek)',
        '5. Keluar lendir dari rongga hidung terus menerus yang berwarna kemerahan',
        '6. Pembengkakan pada pergelangan kaki, kaki, dan tungkai kiri serta kanan'
    ]
    return render_template('dada.html', result=ask)

@app.route('/cek_dada', methods=['GET','POST'])
def cek_dada():
    p01 = [5,5,5,0,0,0]
    p02 = [0,0,0,5,5,5]
    
    result = dict(request.form)
    key = list(result.values())
    data = list(map(float, key))
    hasil = []
    n1 = 0
    for j1 in range(0,3): 
            n1 += data[j1]
    n2 = 0
    for j2 in range(3,6): 
            n2 += data[j2]

    hasil.append(round(n1/sum(p01)*100,2))
    hasil.append(round(n2/sum(p02)*100,2))
    penyakit = ['Kanker Paru-Paru','Bronkitis']

    akhir = dict(zip(penyakit, hasil))
    return render_template('cek_dada.html', result=akhir)

@app.route('/perut')
def perut():
    ask = [
        '1. Apakah anda merasakan sensasi perih dan panas pada uluhati',
        '2. Apakah anda serih muntah asam'
    ]
    return render_template('perut.html', result=ask)

@app.route('/cek_perut', methods=['GET','POST'])
def cek_perut():
    p01 = [5,5]
    
    result = dict(request.form)
    key = list(result.values())
    data = list(map(float, key))
    hasil = []
    n1 = 0
    for j1 in range(0,2):
        n1 += data[j1]

    hasil.append(round(n1/sum(p01)*100,2))
    penyakit = ['Asam Lambung']

    akhir = dict(zip(penyakit, hasil))

    return render_template('cek_perut.html', result=akhir)

@app.route('/kemaluan')
def kemaluan():
    ask = [
        '1. Frekuensi buang air kecil semakin sering, tapi jumlah urine yang dikeluarkan hanya sedikit, serta warna urin keruh atau kuning kemerahan',
        '2. Kandung kemih terasa tegang, penuh, keras dan nyeri pada perut bagian bawah, serta nyeri atau perih kertika buang air kecil',
        '3. Terlalu cepat ejakulasi',
        '4. Kesulitan memulai dan mempertahankan ereksi'
    ]
    return render_template('kemaluan.html', result=ask)

@app.route('/cek_kemaluan', methods=['GET','POST'])
def cek_kemaluan():
    p01 = [5,5,0,0]
    p02 = [0,0,5,5]
    
    result = dict(request.form)
    key = list(result.values())
    data = list(map(float, key))
    hasil = []
    n1 = 0
    for j1 in range(0,2): 
            n1 += data[j1]
    n2 = 0
    for j2 in range(2,4): 
            n2 += data[j2]

    hasil.append(round(n1/sum(p01)*100,2))
    hasil.append(round(n2/sum(p02)*100,2))
    penyakit = ['Kanker Kandung Kemih','Impotensi']

    akhir = dict(zip(penyakit, hasil))
    return render_template('cek_kemaluan.html', result=akhir)

@app.route('/record', methods=['GET','POST'])
def record():
    anatomy = request.form['anatomy']
    hasil = request.form['hasil']
    diagnosa = request.form['diagnosa']
    solusi = request.form['solusi']
    waktu = datetime.datetime.now()
    cur = mysql.connection.cursor()
    cur.execute("INSERT into result (anatomy,hasil,diagnosa,solusi,waktu) values(%s,%s,%s,%s,%s)", (anatomy,hasil,diagnosa,solusi,waktu))
    mysql.connection.commit()
    cur.close()

    return redirect(url_for('data'))

@app.route('/data')
def data():

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM result ORDER by waktu DESC")
    data = cur.fetchall()
    cur.close()
  
    return render_template('data.html', result=data)

@app.route('/hapus/<id>', methods=['GET'])
def delete(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM result WHERE id=%s", (id,))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('data'))

@app.route('/reset')
def reset():
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM result")
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('data'))

if __name__ == '__main__':
    app.run(debug=True)