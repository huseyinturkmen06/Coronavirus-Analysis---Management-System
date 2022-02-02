from os import replace
from MySQLdb.cursors import Cursor
from flask import Flask,render_template,flash,redirect,url_for,session,logging,request
from flask_mysqldb import MySQL
from wtforms import Form,StringField,TextAreaField,PasswordField,validators
from passlib.hash import sha256_crypt 
from functools import wraps

#giriş kontrolü decoratörü
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            flash("Bu sayfayı görüntülemek için lütfen giriş yapın.","danger")
            return redirect(url_for("login"))           #giriş yapılmamışsa login sayfasına geri gönderiliyor
    return decorated_function


#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
app=Flask(__name__)  
app.secret_key="veritabani2"    #burayı flash mesajı hata vermesin diye yaptık
#MYSQL ayarlarını yapıyoruz
app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]=""
app.config["MYSQL_DB"]="veritabani2"
app.config["MYSQL_CURSORCLASS"]="DictCursor"
mysql=MySQL(app)  
#mysql diye bir nesne oluşturduk ve bunun üzerinde flusk ile MYSQL arası ilişkiyi kurduk
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



@app.route("/")
def index():
    return render_template("index.html")  #anasayfa



@app.route("/index")
def index2():
    return render_template("index.html")  #anasayfa
    

@app.route("/dashboard")    #tüm seçenekler ve veriler burada
@login_required
def dashboard():
    return render_template("dashboard.html")

    
#404 error hatası
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404error.html'), 404

###############################################################################################################################

# Kayıt Olma ekranı
@app.route("/register",methods = ["GET", "POST"])
def register():
    
    if request.method == "POST" :          # register ekranındaki formdan gelen bilgileri aldık
        name = request.form.get('name')
        email = request.form.get('eposta')
        username = request.form.get('username')
        password = sha256_crypt.encrypt(request.form.get('password'))
        
        cursor = mysql.connection.cursor()
        sorgu = "Insert into users(name,email,username,password) VALUES(%s,%s,%s,%s)"  #form bilgilerini database e yolladık
        cursor.execute(sorgu,(name,email,username,password))
        mysql.connection.commit()
        cursor.close()
        
        flash("Başarılı bir şekilde kayıt oldunuz","success")
        return redirect(url_for("login"))                   
    else:                                                   #post yapılmayacaksa tekrar aynı sayfaya dön
        return render_template("register.html")


#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# Login erkanı
@app.route("/login",methods = ["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password_entered= request.form.get('password')

        cursor = mysql.connection.cursor()                  

        sorgu = "Select * From users where username = %s"
        result = cursor.execute(sorgu,(username,))          # BUNU DEMET OLARAK VERMEK GEREKTİĞİ İÇİN usernamedeen sonra virgül(,) gelmelidir.
        #insert kullanılmayan yerlerde commit yapılmaz
        

        if result > 0:
            data = cursor.fetchone()                      
            real_password = data["password"]            #parolayı aldık
            if(sha256_crypt.verify(password_entered,real_password)):
                flash("Başarılı bir şekilde giriş yaptınız.","success")
                session["logged_in"] = True
                session["username"] = username
                return redirect(url_for("index"))
            else:
                flash("Parolayı yanlış girdiniz","danger")
                return redirect(url_for("login"))
        else:
            flash("Böyle bir kullanıcı bulunmuyor...","danger")
            return redirect(url_for("login"))
    return render_template("login.html")

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Logout İşlemi
@app.route("/logout")
def logout():
    session.clear()                         #session u sıfırlayarak erişim iznini kaldırdık
    flash("Çıkış yapıldı","danger")                      
    return redirect(url_for("login"))



#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#  ÇALIŞAN TABLOSU İŞLEMLERİ

# Çalışan Ekleme
@app.route("/calisanekle",methods = ["GET","POST"])
def istatistik1():
    if request.method == "POST":
        tcno = request.form.get('tc')
        isim = request.form.get('isim')
        soyisim = request.form.get('soyad')
        kangrubu = request.form.get('kan_grubu')
        sehir = request.form.get('dogdugu_sehir')
        pozisyon = request.form.get('pozisyon')
        maas = request.form.get('maas')
        lisans = request.form.get('lisans')
        yukseklisans = request.form.get('yuksek_lisans')
        doktora = request.form.get('doktora')
        asidurumu = request.form.get('asi_durumu')

        cursor = mysql.connection.cursor()

        sorgu = "Insert into calisanlar(tc,isim,soyad,kan_grubu,dogdugu_sehir,pozisyon,maas,lisans,yuksek_lisans,doktora,asi_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sorgu,(tcno,isim,soyisim,kangrubu,sehir,pozisyon,maas,lisans,yukseklisans,doktora,asidurumu))

        mysql.connection.commit()
        cursor.close()
        flash("Çalışan başarıyla kaydedildi","success")
        return redirect(url_for("istatistik2"))
    else:
        return render_template("calisanekle.html")


# Calisan Silme
@app.route("/calisansil")
def istatistik2():
    cursor = mysql.connection.cursor()
    sorgu = "Select * From calisanlar"
    result = cursor.execute(sorgu)
    if result > 0:
        calisanlar = cursor.fetchall()   #tablodaki tüm verileri calisansil.html e for döngüsü ile vermek üzere aldık
        return render_template("calisansil.html",calisanlar = calisanlar)
    else:
        return render_template("calisansil.html")

    #burası sadece html sayfasına calisanlar tablosunu göstermek için
    

@app.route("/calisansil/delete/<string:id>")
@login_required
def delete(id): 
    cursor = mysql.connection.cursor()
    sorgu = "Select * from calisanlar where calisanlar_id = %s"
    result = cursor.execute(sorgu,(id,))

    if result > 0:
        sorgu2 = "Delete from calisanlar where calisanlar_id = %s"
        cursor.execute(sorgu2,(id,))
        mysql.connection.commit()
        flash("Çalışan silindi","danger")
        return redirect(url_for("istatistik2"))
    else:
        flash("Bu numaralı id'de eleman bulunmamaktadır.")
        return redirect(url_for("index"))



#çalışan güncelleme
@app.route("/calisanguncelle/edit/<string:id>",methods=["GET","POST"])
@login_required
def edit(id):
    if request.method == "GET":
        cursor = mysql.connection.cursor()
        sorgu = "SELECT * FROM calisanlar WHERE calisanlar_id = %s"
        result = cursor.execute(sorgu,(id,))
        data = cursor.fetchall()
        cursor.close()
        print(data[0])
        return render_template("calisanguncelle.html",calisanlar=data[0])   #calisanlar yaz
    else:
        newtcno = request.form['tc']
        newisim = request.form['isim']
        newsoyisim = request.form['soyad']
        newkangrubu = request.form['kan_grubu']
        newdogumyeri = request.form['sehir']
        newpozisyon = request.form['pozisyon']
        newmaas = request.form['maas']
        newlisans = request.form['lisans']
        newyukseklisans = request.form['yuksek_lisans']
        newdoktora = request.form['doktora']
        newasidurumu = request.form['asi_id']
        cursor = mysql.connection.cursor()
        sorgu = "UPDATE calisanlar SET tc = %s, isim = %s, soyad = %s, kan_grubu = %s, dogdugu_sehir = %s, pozisyon = %s, maas = %s, lisans = %s, yuksek_lisans = %s,doktora = %s,asi_id = %s WHERE calisanlar_id = %s"
        result = cursor.execute(sorgu,(newtcno,newisim,newsoyisim,newkangrubu,newdogumyeri,newpozisyon,newmaas,newlisans,newyukseklisans,newdoktora,newasidurumu,id))
        mysql.connection.commit()
        if result > 0:
            flash("Çalışan başarılı bir şekilde güncellendi","success")
            return redirect(url_for("istatistik2"))
        else:
            flash("Bir hata ile karşılaşıldı. Lütfen tekrar deneyiniz.","danger")
            return redirect(url_for("istatistik2"))





#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


#  HASTALIK TABLOSU İŞLEMLERİ

#hastalık tablosu bilgileri gösterme
@app.route("/hastaliktablo")
def hastaliktablo():
    cursor = mysql.connection.cursor()
    sorgu = "Select * From hastalik_tablo"
    result = cursor.execute(sorgu)
    if result > 0:
        hastalik_tablo = cursor.fetchall()   #tablodaki tüm verileri html e for döngüsü ile vermek üzere aldık
        return render_template("hastaliktablo.html",hastalik_tablo=hastalik_tablo)
    else:
        return render_template("hastaliktablo.html")

#hastalik tablosu silme işlemleri
@app.route("/hastaliksil/delete/<string:id>")
@login_required
def hastaliksil(id): 
    cursor = mysql.connection.cursor()
    sorgu = "Select * from hastalik_tablo where hastalik_id = %s"
    result = cursor.execute(sorgu,(id,))

    if result > 0:
        sorgu2 = "Delete from hastalik_tablo where hastalik_id = %s"
        cursor.execute(sorgu2,(id,))
        mysql.connection.commit()
        flash("Çalışan silindi","danger")
        return redirect(url_for("hastaliktablo"))
    else:
        flash("Bu numaralı id'de silinecek eleman bulunmamaktadır.")
        return redirect(url_for("index"))


#Hastalık Tablosuna Yeni Kayıt Girme
@app.route("/hastalikekle",methods = ["GET","POST"])
def hastalikekle():
    if request.method == "POST":
        tc = request.form.get('tc')
        hastalik_ismi = request.form.get('hastalik_ismi')
        hastalik_tarihi = request.form.get('hastalik_tarihi')
        hastalik_tarihiTrue = hastalik_tarihi.replace(".","-")
        ilac = request.form.get('ilac')
        doz = request.form.get('doz')
        semptom = request.form.get('semptom')
        

        cursor = mysql.connection.cursor()

        sorgu = "Insert into hastalik_tablo(tc,hastalik_adi,hastalik_tarihi,ilac,doz,semptomlar) VALUES(%s,%s,%s,%s,%s,%s)"
        cursor.execute(sorgu,(tc,hastalik_ismi,hastalik_tarihiTrue,ilac,doz,semptom))

        mysql.connection.commit()
        cursor.close()
        flash("Yeni hastalık kaydı yapıldı","success")
        return redirect(url_for("hastaliktablo"))
    else:
        return render_template("hastalikekle.html")


#hastalikguncelle
@app.route("/hastalikguncelle/edit/<string:id>",methods=["GET","POST"])
@login_required
def hastalik_guncelle(id):
    if request.method == "GET":
        cursor = mysql.connection.cursor()
        sorgu = "SELECT * FROM hastalik_tablo WHERE hastalik_id = %s"
        result = cursor.execute(sorgu,(id,))
        data = cursor.fetchall()
        cursor.close()
        return render_template("hastalikguncelle.html",hastaliklar=data[0])   #calisanlar yaz
    else:
        newtcno = request.form['tc']
        new_hastalik_ismi = request.form['hastalik_adi']
        new_hastalik_tarihi = request.form['hastalik_tarihi']
        new_hastalik_tarihiTrue= new_hastalik_tarihi.replace(".","-")
        new_kullanşlan_ilac = request.form['ilac']
        new_doz = request.form['doz']
        new_semptom = request.form['semptomlar']
        
        cursor = mysql.connection.cursor()
        sorgu = "UPDATE hastalik_tablo SET tc = %s, hastalik_adi = %s, hastalik_tarihi = %s, ilac = %s, doz = %s, semptomlar = %s WHERE hastalik_id = %s"
        result = cursor.execute(sorgu,(newtcno,new_hastalik_ismi,new_hastalik_tarihiTrue,new_kullanşlan_ilac,new_doz,new_semptom,id))
        mysql.connection.commit()
        if result > 0:
            flash("Hastalık kaydı başarılı bir şekilde güncellendi","success")
            return redirect(url_for("hastaliktablo"))
        else:
            flash("Bir hata ile karşılaşıldı. Lütfen tekrar deneyiniz.","danger")
            return redirect(url_for("hastalik_guncelle"))



#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#calisma_sureleri tablosu işlemleri


# Çalışma Süreleri Gösterme

@app.route("/calismasuresigoruntule")
def calismasuresigoruntule():
    cursor = mysql.connection.cursor()
    sorgu = "Select * From calisma_sureleri"
    result = cursor.execute(sorgu)
    if result > 0:
        calisma_tablo = cursor.fetchall()   #tablodaki tüm verileri html e for döngüsü ile vermek üzere aldık
        return render_template("calismasuresigoruntule.html",calisma_tablo=calisma_tablo)
    else:
        return render_template("calismasuresigoruntule.html")



# Çalışma Süresi tablosu yeni kayıt ekleme
@app.route("/calismasuresiekle",methods = ["GET","POST"])
def calismasuresiekle():
    if request.method == "POST":
        tc = request.form.get('tc')
        haftaicigiris = request.form.get('haftaicigiris')
        haftaicicikis = request.form.get('haftaicicikis')
        cumartesigiris = request.form.get('cumartesigiris')
        cumartesicikis = request.form.get('cumartesicikis')
        pazargiris = request.form.get('pazargiris')
        pazarcikis = request.form.get('pazarcikis')
        cursor = mysql.connection.cursor()
        sorgu = "Insert into calisma_sureleri(tc,haftaicigiris,haftaicicikis,cumartesigiris,cumartesicikis,pazargiris,pazarcikis) VALUES(%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sorgu,(tc,haftaicigiris,haftaicicikis,cumartesigiris,cumartesicikis,pazargiris,pazarcikis))
        mysql.connection.commit()
        cursor.close()

        flash("Yeni çalışma süresi kaydı yapıldı","success")
        return redirect(url_for("calismasuresiekle"))
    else:
        return render_template("calismasuresiekle.html")



# Çalışma Süresi tablosu kayıt silme
@app.route("/calismasuresi/delete/<string:id>")
@login_required
def calismasuresisil(id): 
    cursor = mysql.connection.cursor()
    sorgu = "Select * from calisma_sureleri where id = %s"
    result = cursor.execute(sorgu,(id,))

    if result > 0:
        sorgu2 = "Delete from calisma_sureleri where id = %s"
        cursor.execute(sorgu2,(id,))
        mysql.connection.commit()
        flash("Covid kaydı silindi","danger")
        return redirect(url_for("calismasuresigoruntule"))
    else:
        flash("Bu numaralı id'de silinecek eleman bulunmamaktadır.")
        return redirect(url_for("calismasuresigoruntule"))


# Çalışma Süresi tablosu kayıt güncelleme
@app.route("/calismasuresi/edit/<string:id>",methods=["GET","POST"])
@login_required
def calismasuresiguncelle(id):
    if request.method == "GET":
        cursor = mysql.connection.cursor()
        sorgu = "SELECT * FROM calisma_sureleri WHERE id = %s"
        result = cursor.execute(sorgu,(id,))
        sure = cursor.fetchall()
        cursor.close()
        return render_template("calismasuresiguncelle.html",sure=sure[0])   #tablodaki 1. kaydı alır   ###########
    else:
        new_tcno = request.form['tcno']
        new_haftaicigiris = request.form['haftaicigiris']
        new_haftaicicikis = request.form['haftaicicikis']
        new_cumartesigiris = request.form['cumartesigiris']
        new_cumartesicikis = request.form['cumartesicikis']
        new_pazargiris = request.form['pazargiris']
        new_pazarcikis = request.form['pazarcikis']   
        cursor = mysql.connection.cursor()
        sorgu = "UPDATE calisma_sureleri SET tc = %s, haftaicigiris = %s, haftaicicikis = %s, cumartesigiris = %s, cumartesicikis = %s, pazargiris= %s, pazarcikis= %s  WHERE id = %s"
        result = cursor.execute(sorgu,(new_tcno,new_haftaicigiris,new_haftaicicikis,new_cumartesigiris,new_cumartesicikis,new_pazargiris,new_pazarcikis,id))
        mysql.connection.commit()
        if result > 0:
            flash("Çalışma süresi kaydı başarılı bir şekilde güncellendi","success")
            return redirect(url_for("calismasuresigoruntule"))
        else:
            flash("Bir hata ile karşılaşıldı. Lütfen tekrar deneyiniz.","danger")
            return redirect(url_for("calismasuresigoruntule"))



#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#  COVİD TABLOSU İŞLEMLERİ

#covid tablosu bilgileri gösterme
@app.route("/covidtablosu")
def covidtablosu():
    cursor = mysql.connection.cursor()
    sorgu = "Select * From covid_tablosu"
    result = cursor.execute(sorgu)
    if result > 0:
        covid_tablosu = cursor.fetchall()   #tablodaki tüm verileri html e for döngüsü ile vermek üzere aldık
        return render_template("covidtablosu.html",covid_tablosu=covid_tablosu)
    else:
        return render_template("covidtablosu.html")


#Covid Tablosuna Yeni Kayıt Girme
@app.route("/covidekle",methods = ["GET","POST"])
def covidekle():
    if request.method == "POST":
        tc = request.form.get('tc')
        pozitif_tarihi = request.form.get('pozitif_tarihi')
        negatif_tarihi = request.form.get('negatif_tarihi')
        asi_id = request.form.get('asi_id')

        cursor = mysql.connection.cursor()
        sorgu = "Insert into covid_tablosu(tc,pozitif_tarihi,negatif_tarihi,asi_id) VALUES(%s,%s,%s,%s)"
        cursor.execute(sorgu,(tc,pozitif_tarihi,negatif_tarihi,asi_id))
        mysql.connection.commit()
        cursor.close()

        flash("Yeni covid kaydı yapıldı","success")
        return redirect(url_for("covidtablosu"))
    else:
        return render_template("covidekle.html")


#covid tablosu silme işlemleri
@app.route("/covidsil/delete/<string:id>")
@login_required
def covidsil(id): 
    cursor = mysql.connection.cursor()
    sorgu = "Select * from covid_tablosu where covid_id = %s"
    result = cursor.execute(sorgu,(id,))

    if result > 0:
        sorgu2 = "Delete from covid_tablosu where covid_id = %s"
        cursor.execute(sorgu2,(id,))
        mysql.connection.commit()
        flash("Covid kaydı silindi","danger")
        return redirect(url_for("covidtablosu"))
    else:
        flash("Bu numaralı id'de silinecek eleman bulunmamaktadır.")
        return redirect(url_for("index"))


#covidguncelle
@app.route("/covidguncelle/edit/<string:id>",methods=["GET","POST"])
@login_required
def covidguncelle(id):
    if request.method == "GET":
        cursor = mysql.connection.cursor()
        sorgu = "SELECT * FROM covid_tablosu WHERE covid_id = %s"
        result = cursor.execute(sorgu,(id,))
        data = cursor.fetchall()
        cursor.close()
        return render_template("covidguncelle.html",covid=data[0])   
    else:
        new_tcno = request.form['tc']
        new_pozitif_tarihi = request.form['pozitif_tarihi']
        new_negatif_tarihi = request.form['negatif_tarihi']
        #new_belirtiler = request.form['belirtiler']
        #new_temasli_tc = request.form['temasli_tc']
        new_asi_id = request.form['asi_id']
        #new_kronik_hastalik = request.form['kronik_hastalik']
        
        new_pozitif_tarihiTrue = new_pozitif_tarihi.replace(".","-")   #html time ile mysql time arası farkı düzelttik
        new_negatif_tarihiTrue = new_negatif_tarihi.replace(".","-")
        
        cursor = mysql.connection.cursor()
        sorgu = "UPDATE covid_tablosu SET tc = %s, pozitif_tarihi = %s, negatif_tarihi = %s, asi_id = %s WHERE covid_id = %s"
        result = cursor.execute(sorgu,(new_tcno,new_pozitif_tarihiTrue,new_negatif_tarihiTrue,new_asi_id,id))
        mysql.connection.commit()
        if result > 0:
            flash("Covid kaydı başarılı bir şekilde güncellendi","success")
            return redirect(url_for("covidtablosu"))
        else:
            flash("Bir hata ile karşılaşıldı. Lütfen tekrar deneyiniz.","danger")
            return redirect(url_for("covidguncelle"))



#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#  HOBİ TABLOSU İŞLEMLERİ

#hobi tablosu bilgileri gösterme
@app.route("/hobilertablosu")
def hobilertablosu():
    cursor = mysql.connection.cursor()
    sorgu = "Select * From hobiler_tablosu"
    result = cursor.execute(sorgu)
    if result > 0:
        hobiler_tablosu = cursor.fetchall()   #tablodaki tüm verileri html e for döngüsü ile vermek üzere aldık
        return render_template("hobilertablosu.html",hobiler_tablosu=hobiler_tablosu)
    else:
        return render_template("hobilertablosu.html")


#Hobi Tablosuna Yeni Kayıt Girme
@app.route("/hobiekle",methods = ["GET","POST"])
def hobiekle():
    if request.method == "POST":
        tc = request.form.get('tc')
        hobi_ismi = request.form.get('hobi_ismi')
        
        cursor = mysql.connection.cursor()
        sorgu = "Insert into hobiler_tablosu(tc,hobi_ismi) VALUES(%s,%s)"
        cursor.execute(sorgu,(tc,hobi_ismi))
        mysql.connection.commit()
        cursor.close()

        flash("Yeni hobi kaydı yapıldı","success")
        return redirect(url_for("hobilertablosu"))
    else:   
        return render_template("hobiekle.html")


#hobi tablosu silme işlemleri
@app.route("/hobisil/delete/<string:id>")
@login_required
def hobisil(id): 
    cursor = mysql.connection.cursor()
    sorgu = "Select * from hobiler_tablosu where hobi_id = %s"
    result = cursor.execute(sorgu,(id,))

    if result > 0:
        sorgu2 = "Delete from hobiler_tablosu where hobi_id = %s"
        cursor.execute(sorgu2,(id,))
        mysql.connection.commit()
        flash("Hobi kaydı silindi","danger")
        return redirect(url_for("hobilertablosu"))
    else:
        flash("Bu numaralı id'de silinecek eleman bulunmamaktadır.")
        return redirect(url_for("index"))








#hobi güncelle
@app.route("/hobiguncelle/edit/<string:id>",methods=["GET","POST"])
@login_required
def hobiguncelle(id):
    if request.method == "GET":
        cursor = mysql.connection.cursor()
        sorgu = "SELECT * FROM hobiler_tablosu WHERE hobi_id = %s"
        result = cursor.execute(sorgu,(id,))
        data = cursor.fetchall()
        cursor.close()
        return render_template("hobiguncelle.html",hobi=data[0])   
    else:
        new_tcno = request.form['tc']
        new_hobi_ismi = request.form['hobi_ismi']
        cursor = mysql.connection.cursor()
        sorgu = "UPDATE hobiler_tablosu SET tc = %s, hobi_ismi = %s WHERE hobi_id = %s"
        result = cursor.execute(sorgu,(new_tcno,new_hobi_ismi,id))
        mysql.connection.commit()
        if result > 0:
            flash("Hobi kaydı başarılı bir şekilde güncellendi","success")
            return redirect(url_for("hobilertablosu"))
        else:
            flash("Bir hata ile karşılaşıldı. Lütfen tekrar deneyiniz.","danger")
            return redirect(url_for("hobilertablosu"))




#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#asi tablosu bilgileri gösterme
@app.route("/asitablosu")
def asi_tablosu():
    cursor = mysql.connection.cursor()
    sorgu = "Select * From asi_tablosu"
    result = cursor.execute(sorgu)
    if result > 0:
        asi_tablosu = cursor.fetchall()   #tablodaki tüm verileri html e for döngüsü ile vermek üzere aldık
        return render_template("asitablosu.html",asi_tablosu=asi_tablosu)
    else:
        return render_template("asitablosu.html")


#not: bu tablo yalnızca backend de kullanılıyor, gösterilmese de olur ama yine de gösterdik

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

# 3 YENİ TABLO BAŞLANGIÇ

##############################covid tablosu ek işlemler başlıyor


# Kronik hastalık bilgisi ekleme
@app.route("/kronikekle",methods=["GET", "POST"])
def kronikekle():
    if request.method == "POST":
        tcno = request.form.get('tcno')
        kronik = request.form.get('kronik')
        cursor = mysql.connection.cursor()
        sorgu = "Insert into kronik_hastalik_tablo(tc,kronik_hastalik_ismi) VALUES(%s,%s)"
        cursor.execute(sorgu,(tcno,kronik))
        mysql.connection.commit()
        cursor.close()
        flash("Kronik hastalık bilgisi başarılı bir şekilde kaydedildi","success")
        return redirect(url_for("kronikekle"))
    else:
        return render_template("kronikekle.html")



# Kronik hastalık bilgisini güncelleme ve silme
@app.route("/kronikgoruntule")
def kronikgoruntule():
    cursor = mysql.connection.cursor()
    sorgu = "Select * From kronik_hastalik_tablo"
    result = cursor.execute(sorgu)
    if result > 0:
        kronik = cursor.fetchall()
        return render_template("kronikgoruntule.html",kronik = kronik)
    else:
        return render_template("kronikgoruntule.html")


@app.route("/kronikgoruntule/delete/<string:id>")
@login_required
def kroniksil(id):
    cursor = mysql.connection.cursor()
    sorgu = "Select * from kronik_hastalik_tablo where kronik_hastalik_id = %s"
    result = cursor.execute(sorgu,(id,))
    if result > 0:
        sorgu2 = "Delete from kronik_hastalik_tablo where kronik_hastalik_id = %s"
        cursor.execute(sorgu2,(id,))
        mysql.connection.commit()
        return redirect(url_for("kronikgoruntule"))
    else:
        flash("Herhangi bir bilgi bulunmamaktadır.")
        return redirect(url_for("kronikgoruntule"))


@app.route("/kronikgoruntule/edit/<string:id>",methods=["GET","POST"])
@login_required
def kronikduzenle(id):
    if request.method == "GET":
        cursor = mysql.connection.cursor()
        sorgu = "SELECT * FROM kronik_hastalik_tablo WHERE kronik_hastalik_id = %s"
        result = cursor.execute(sorgu,(id,))
        data = cursor.fetchall()
        cursor.close()
        return render_template('kronikguncelle.html',kronik=data[0])
    else:
        newtcno = request.form['tcno']
        newkronik = request.form['kronik']
        cursor = mysql.connection.cursor()
        sorgu = "UPDATE kronik_hastalik_tablo SET tc = %s, kronik_hastalik_ismi = %s WHERE kronik_hastalik_id = %s"
        result = cursor.execute(sorgu,(newtcno,newkronik,id))
        mysql.connection.commit()
        if result > 0:
            flash("Kronik hastalık bilgisi başarılı bir şekilde güncellendi","success")
            return redirect(url_for("kronikgoruntule"))
        else:
            flash("Bir hata ile karşılaşıldı. Lütfen tekrar deneyiniz.","danger")
            return redirect(url_for("kronikgoruntule"))


##############################covid tablosu ek işlemler bitti

















# Kronik hastalık bilgisi ekleme
@app.route("/belirtiekle",methods=["GET", "POST"])
def belirtiekle():
    if request.method == "POST":
        tcno = request.form.get('tcno')
        belirti = request.form.get('belirti')
        cursor = mysql.connection.cursor()
        sorgu = "Insert into belirtiler_tablo(tc,belirti_ismi) VALUES(%s,%s)"
        cursor.execute(sorgu,(tcno,belirti))
        mysql.connection.commit()
        cursor.close()
        flash("Belirti bilgisi başarılı bir şekilde kaydedildi","success")
        return redirect(url_for("belirtiekle"))
    else:
        return render_template("belirtiekle.html")



# Kronik hastalık bilgisini güncelleme ve silme
@app.route("/belirtigoruntule")
def belirtigoruntule():
    cursor = mysql.connection.cursor()
    sorgu = "Select * From belirtiler_tablo"
    result = cursor.execute(sorgu)
    if result > 0:
        belirti = cursor.fetchall()
        return render_template("belirtigoruntule.html",belirti = belirti)
    else:
        return render_template("belirtigoruntule.html")


@app.route("/belirtigoruntule/delete/<string:id>")
@login_required
def belirtisil(id):
    cursor = mysql.connection.cursor()
    sorgu = "Select * from belirtiler_tablo where belirti_id = %s"
    result = cursor.execute(sorgu,(id,))
    if result > 0:
        sorgu2 = "Delete from belirtiler_tablo where belirti_id = %s"
        cursor.execute(sorgu2,(id,))
        mysql.connection.commit()
        return redirect(url_for("belirtigoruntule"))
    else:
        flash("Herhangi bir bilgi bulunmamaktadır.")
        return redirect(url_for("belirtigoruntule"))


@app.route("/belirtigoruntule/edit/<string:id>",methods=["GET","POST"])
@login_required
def belirtiguncelle(id):
    if request.method == "GET":
        cursor = mysql.connection.cursor()
        sorgu = "SELECT * FROM belirtiler_tablo WHERE belirti_id = %s"
        result = cursor.execute(sorgu,(id,))
        data = cursor.fetchall()
        cursor.close()
        return render_template('belirtiguncelle.html',belirti=data[0])
    else:
        newtcno = request.form['tcno']
        newbelirti = request.form['belirti']
        cursor = mysql.connection.cursor()
        sorgu = "UPDATE belirtiler_tablo SET tc = %s, belirti_ismi = %s WHERE belirti_id = %s"
        result = cursor.execute(sorgu,(newtcno,newbelirti,id))
        mysql.connection.commit()
        if result > 0:
            flash("Belirti bilgisi başarılı bir şekilde güncellendi","success")
            return redirect(url_for("belirtigoruntule"))
        else:
            flash("Bir hata ile karşılaşıldı. Lütfen tekrar deneyiniz.","danger")
            return redirect(url_for("belirtigoruntule"))


##############################belirti ek işlemler bitti










# Temaslı çalışan bilgisi ekleme
@app.route("/temasliekle",methods=["GET", "POST"])
def temasliekle():
    if request.method == "POST":
        tcno = request.form.get('tcno')
        temasli = request.form.get('temasli')
        cursor = mysql.connection.cursor()
        sorgu = "Insert into temasli_calisanlar_tablo(tc,temasli_tc) VALUES(%s,%s)"
        cursor.execute(sorgu,(tcno,temasli))
        mysql.connection.commit()
        cursor.close()
        flash("Temaslı bilgisi başarılı bir şekilde kaydedildi","success")
        return redirect(url_for("temasliekle"))
    else:
        return render_template("temasliekle.html")



# Temaslı çalışan bilgisini güncelleme ve silme
@app.route("/temasligoruntule")
def temasligoruntule():
    cursor = mysql.connection.cursor()
    sorgu = "Select * From temasli_calisanlar_tablo"
    result = cursor.execute(sorgu)
    if result > 0:
        temasli = cursor.fetchall()
        return render_template("temasligoruntule.html",temasli = temasli)
    else:
        return render_template("temasligoruntule.html")


@app.route("/temasligoruntule/delete/<string:id>")
@login_required
def temaslisil(id):
    cursor = mysql.connection.cursor()
    sorgu = "Select * from temasli_calisanlar_tablo where temasli_id = %s"
    result = cursor.execute(sorgu,(id,))
    if result > 0:
        sorgu2 = "Delete from temasli_calisanlar_tablo where temasli_id = %s"
        cursor.execute(sorgu2,(id,))
        mysql.connection.commit()
        return redirect(url_for("temasligoruntule"))
    else:
        flash("Herhangi bir bilgi bulunmamaktadır.")
        return redirect(url_for("temasligoruntule"))


@app.route("/temasligoruntule/edit/<string:id>",methods=["GET","POST"])
@login_required
def temasliguncelle(id):
    if request.method == "GET":
        cursor = mysql.connection.cursor()
        sorgu = "SELECT * FROM temasli_calisanlar_tablo WHERE temasli_id = %s"
        result = cursor.execute(sorgu,(id,))
        data = cursor.fetchall()
        cursor.close()
        return render_template('temasliguncelle.html',temasli=data[0])
    else:
        newtcno = request.form['tcno']
        newtemasli = request.form['temasli']
        cursor = mysql.connection.cursor()
        sorgu = "UPDATE temasli_calisanlar_tablo SET tc = %s, temasli_Tc = %s WHERE temasli_id = %s"
        result = cursor.execute(sorgu,(newtcno,newtemasli,id))
        mysql.connection.commit()
        if result > 0:
            flash("Belirti bilgisi başarılı bir şekilde güncellendi","success")
            return redirect(url_for("temasligoruntule"))
        else:
            flash("Bir hata ile karşılaşıldı. Lütfen tekrar deneyiniz.","danger")
            return redirect(url_for("temasligoruntule"))


##############################Temaslı çalışan ek işlemler bitti
# 3 YENİ TABLO BİTİŞ












#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Eğitim durumu ve COVID arasındaki istatistiki bilgi (1)
@app.route("/egitimcorona")
def egitimcorona():
    cursor = mysql.connection.cursor()
    cursor2 = mysql.connection.cursor()
    cursor3 = mysql.connection.cursor()
    sorgu = "select DISTINCT ca.* from calisanlar ca, covid_tablosu c where doktora = '0' and yuksek_lisans = '0' and ca.tc in (Select c.tc from covid_tablosu);" #Lisans
    sorgu2 = "select DISTINCT ca.* from calisanlar ca, covid_tablosu c where doktora = '0' and yuksek_lisans <> '0' and ca.tc in (Select c.tc from covid_tablosu);" #Yüksek Lisans
    sorgu3 = "select DISTINCT ca.* from calisanlar ca, covid_tablosu c where doktora <> '0' and ca.tc in (Select c.tc from covid_tablosu);" # Doktora
    result = cursor.execute(sorgu)
    result2 = cursor2.execute(sorgu2)
    result3 = cursor3.execute(sorgu3)
    if result or result2 or result3 > 0:
        lisans = cursor.fetchall()
        ylisans = cursor2.fetchall()
        doktora = cursor3.fetchall()
        lisansadet = len(lisans)
        ylisansadet = len(ylisans)
        doktoraadet = len(doktora)
        return render_template("egitimcorona.html",lisans = lisans, ylisans = ylisans, doktora = doktora, ylisansadet = ylisansadet, lisansadet = lisansadet, doktoraadet = doktoraadet)
    else:
        return render_template("egitimcorona.html")

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#Elemanlar arasında görülen en yaygın üç hastalık türü ve o hastalığa sahip olan elemanların listesi  (2.sorgu)
@app.route("/top3hastalik", methods=["GET","POST"])
def deneme32():
    if request.method == "GET" or request.method == "POST":
        cursor = mysql.connection.cursor() 
        cursor0 = mysql.connection.cursor()  
        cursor1 = mysql.connection.cursor()
        cursor2 = mysql.connection.cursor()
        #hastalık tablosunda en çok tekrar eden 3 hastalığı al   
        sorgu = "SELECT hastalik_adi, COUNT(hastalik_adi) AS hastaliklar FROM hastalik_tablo GROUP BY hastalik_adi ORDER BY hastaliklar DESC LIMIT 3;"       
        result = cursor.execute(sorgu) 
        if result > 0:
            data = cursor.fetchall()  
            hastalik_adi0 = data[0]['hastalik_adi']  #1.kaydın hastalık adı
            hastalik_adi1 = data[1]['hastalik_adi']  #2.kaydın hastalık adı
            hastalik_adi2 = data[2]['hastalik_adi']  #3.kaydın hastalık adı
            print(data)

            #çalışanlar tablosunda tc,isim,soyad attribute lerini çek, 
            # sonrahastalık tablosundaki hastalık adı en çok tekrar eden 3 hastalıkla eşleşen tc leri de çek, bu tc leri eşitle
            sorgu0 = "SELECT DISTINCT c.tc, c.isim, c.soyad from calisanlar c, hastalik_tablo h where c.tc in (SELECT DISTINCT tc from hastalik_tablo where hastalik_adi= '" + hastalik_adi0 + "');"
            sorgu1 = "SELECT DISTINCT c.tc, c.isim, c.soyad from calisanlar c, hastalik_tablo h where c.tc in (SELECT DISTINCT tc from hastalik_tablo where hastalik_adi= '" + hastalik_adi1 + "');"
            sorgu2 = "SELECT DISTINCT c.tc, c.isim, c.soyad from calisanlar c, hastalik_tablo h where c.tc in (SELECT DISTINCT tc from hastalik_tablo where hastalik_adi= '" + hastalik_adi2 + "');"
            result0 = cursor0.execute(sorgu0)
            result1 = cursor1.execute(sorgu1)
            result2 = cursor2.execute(sorgu2)
            if result0 or result1 or result2 > 0:
                data0 = cursor0.fetchall()     
                data1 = cursor1.fetchall()        
                data2 = cursor2.fetchall()
                bir = len(data0)
                iki = len(data1)
                uc = len(data2)
                return render_template("top3hastalik.html", data=data, data0=data0, data1= data1, data2= data2, bir=bir, iki= iki, uc=uc)
            else:
                flash("Henüz herhangi bir veri yok","danger")
                return redirect(url_for("index"))
        else:
            flash("Heniz bir veri bulunmamaktadır","danger")
            return render_template("top3hastalik.html")

@app.route("/den")
def den():
    return render_template("den.html")

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

@app.route("/sehirhastalik", methods=["GET","POST"])
def istatistik18():
    if request.method == "POST":
        sehiradi = request.form.get('sehiradi')
        cursor = mysql.connection.cursor()
        sorgu = "SELECT h.hastalik_adi, COUNT(hastalik_adi) as hastaliklar from calisanlar c, hastalik_tablo h where h.tc in (Select c.tc from calisanlar where c.dogdugu_sehir= '"+ str(sehiradi) +"') GROUP BY hastalik_adi order by hastaliklar desc limit 3;"
        #üst satira bir bak
        result = cursor.execute(sorgu)
        if result == 0:
            flash("Aranan şehire ait bir hastalık bulunamadı...","warning")
            return render_template("sehirhastalik.html")
        else:
            data = cursor.fetchall()
            return render_template("sehirhastalik.html",data = data, sehiradi=sehiradi)
    else:
        return render_template("sehirhastalik.html") ###########



@app.route("/calisanilac",methods= ["GET","POST"])
def istatistik19():
    if request.method == "GET" or request.method == "POST":
        cursor = mysql.connection.cursor() 
        cursor0 = mysql.connection.cursor()  
        cursor1 = mysql.connection.cursor()
        cursor2 = mysql.connection.cursor()   
        sorgu = "select ilac, COUNT(ilac) as adet_sayisi from hastalik_tablo GROUP BY ilac ORDER BY adet_sayisi desc LIMIT 3;"       
        result = cursor.execute(sorgu) 
        if result > 0:
            data = cursor.fetchall()  
            ilac_adi0 = data[0]['ilac']   #key alır
            ilac_adi1 = data[1]['ilac']
            ilac_adi2 = data[2]['ilac']
            print(data)
            sorgu0 = "Select e.tc, e.isim, e.soyad, c.pozitif_tarihi, c.negatif_tarihi, h.ilac from calisanlar e, covid_tablosu c, hastalik_tablo h where e.tc in (Select c.tc from covid_tablosu where c.tc in (Select h.tc from hastalik_tablo where h.ilac = '"+ ilac_adi0+"'))"
            sorgu1 = "Select e.tc, e.isim, e.soyad, c.pozitif_tarihi, c.negatif_tarihi, h.ilac from calisanlar e, covid_tablosu c, hastalik_tablo h where e.tc in (Select c.tc from covid_tablosu where c.tc in (Select h.tc from hastalik_tablo where h.ilac = '"+ ilac_adi1+"'))"
            sorgu2 = "Select e.tc, e.isim, e.soyad, c.pozitif_tarihi, c.negatif_tarihi, h.ilac from calisanlar e, covid_tablosu c, hastalik_tablo h where e.tc in (Select c.tc from covid_tablosu where c.tc in (Select h.tc from hastalik_tablo where h.ilac = '"+ ilac_adi2+"'))"
            result0 = cursor0.execute(sorgu0)
            result1 = cursor1.execute(sorgu1)
            result2 = cursor2.execute(sorgu2)
            if result0 or result1 or result2 > 0:
                data0 = cursor0.fetchall()     
                data1 = cursor1.fetchall()        
                data2 = cursor2.fetchall()
                bir = len(data0)
                iki = len(data1)
                uc = len(data2)
                return render_template("calisanilac.html", data=data, data0=data0, data1= data1, data2= data2,bir = bir, iki= iki, uc=uc)
            else:
                
                return render_template("calisanilac.html",data=data)
        else:
            flash("Bu sayfada henüz veri bulunmamaktadır","danger")
            return render_template("calisanilac.html")




#belirli ilaca göre covid sorgusu
@app.route("/covidilac",methods=["GET","POST"])
def covidilac():
    if request.method == "POST":
        ilacismi = request.form.get('ilacismi')
        cursor = mysql.connection.cursor()
        sorgu = "select DISTINCT c.tc, c.pozitif_tarihi, c.negatif_tarihi, h.ilac from covid_tablosu c, hastalik_tablo h where c.tc in (Select h.tc from hastalik_tablo where h.ilac = '"+ilacismi+"');"
        result = cursor.execute(sorgu)
        if result == 0:
            flash("Bu ilacı kullanıp korona olan çalışan bulunmamaktadır","warning")
            return render_template("covidilac.html")
        else:
            data = cursor.fetchall()
            return render_template("covidilac.html",data = data, ilacismi=ilacismi)
    else:
        return render_template("covidilac.html") 


#aşı vurulma durumuna göre covid hastalığına yakalanma durumu/// burayı tekrar et, önemli
@app.route("/asicovid")
def asicovid():
    cursor = mysql.connection.cursor()
    cursor2 = mysql.connection.cursor()
    cursor3 = mysql.connection.cursor()
    sorgu = "select c.tc, c.isim, c.soyad, co.pozitif_tarihi,co.negatif_tarihi,co.asi_id from covid_tablosu co, calisanlar c where c.tc in (Select DISTINCT co.tc from covid_tablosu where co.asi_id = '1' GROUP BY tc)" #Aşı olmayıp korona olanlar
    sorgu2 = "select c.tc, c.isim, c.soyad, co.pozitif_tarihi,co.negatif_tarihi,co.asi_id from covid_tablosu co, calisanlar c where c.tc in (Select DISTINCT co.tc from covid_tablosu where co.asi_id = '2' GROUP BY tc)" #Sinovac aşısı olup korona olanlar
    sorgu3 = "select c.tc, c.isim, c.soyad, co.pozitif_tarihi,co.negatif_tarihi,co.asi_id from covid_tablosu co, calisanlar c where c.tc in (Select DISTINCT co.tc from covid_tablosu where co.asi_id = '3' GROUP BY tc)" #Biontech aşısı olup korona olanlar
    result = cursor.execute(sorgu)
    result2 = cursor2.execute(sorgu2)
    result3 = cursor3.execute(sorgu3)
    if result or result2 or result3 > 0:
        asi_olmayan = cursor.fetchall()
        sinovac = cursor2.fetchall()
        biontech = cursor3.fetchall()
        bir = len(asi_olmayan)
        iki = len(sinovac)
        uc = len(biontech)
        return render_template("asicovid.html",asi_olmayan = asi_olmayan, sinovac = sinovac, biontech = biontech,bir=bir,iki=iki,uc=uc)
    else:
        flash("Bir hata oluştu","danger")
        return render_template("asicovid.html")


# Belirli bir kronik hastalığa göre koronanın geçme süresini gösteren sorgu
@app.route("/kronikcorona",methods=["GET","POST"])
def kronikcorona():
    if request.method == "POST":
        hastalikadi = request.form.get('hastalikadi')
        cursor = mysql.connection.cursor()
        sorgu=  "Select c.tc,c.pozitif_tarihi,c.negatif_tarihi,TIMESTAMPDIFF(DAY,c.pozitif_tarihi,c.negatif_tarihi) as gecen_sure ,k.kronik_hastalik_ismi from covid_tablosu c, kronik_hastalik_tablo k where c.tc in (SELECT k.tc from kronik_hastalik_tablo where k.kronik_hastalik_ismi = '"+ str(hastalikadi) +"');"
        result = cursor.execute(sorgu)
        if result == 0:
            flash("Bu hastalığa sahip korona geçirmiş çalışan bulunmamaktadır","warning")
            return render_template("kronikcorona.html")
        else:
            data = cursor.fetchall()
            return render_template("kronikcorona.html",data = data, hastalikadi=hastalikadi)
    else:
        return render_template("kronikcorona.html") 



#Kan grubuna göre covide yakalanma durumu ve oranı
@app.route("/kangrubucovid")
def kangrubucovid():
    cursor = mysql.connection.cursor()  #A-
    cursor2 = mysql.connection.cursor() #A+
    cursor3 = mysql.connection.cursor() #B-
    cursor4 = mysql.connection.cursor() #B+
    cursor5 = mysql.connection.cursor() #AB-
    cursor6 = mysql.connection.cursor() #AB+
    cursor7 = mysql.connection.cursor() #0-
    cursor8 = mysql.connection.cursor() #0+
    sorgu =  "select c.tc, c.isim, c.soyad, c.kan_grubu, co.pozitif_tarihi,co.negatif_tarihi from calisanlar c, covid_tablosu co where co.tc in (Select c.tc from calisanlar where c.kan_grubu = 'A-')"
    sorgu2 = "select c.tc, c.isim, c.soyad, c.kan_grubu, co.pozitif_tarihi,co.negatif_tarihi from calisanlar c, covid_tablosu co where co.tc in (Select c.tc from calisanlar where c.kan_grubu = 'A+')"
    sorgu3 = "select c.tc, c.isim, c.soyad, c.kan_grubu, co.pozitif_tarihi,co.negatif_tarihi from calisanlar c, covid_tablosu co where co.tc in (Select c.tc from calisanlar where c.kan_grubu = 'B-')"
    sorgu4 = "select c.tc, c.isim, c.soyad, c.kan_grubu, co.pozitif_tarihi,co.negatif_tarihi from calisanlar c, covid_tablosu co where co.tc in (Select c.tc from calisanlar where c.kan_grubu = 'B+')"
    sorgu5 = "select c.tc, c.isim, c.soyad, c.kan_grubu, co.pozitif_tarihi,co.negatif_tarihi from calisanlar c, covid_tablosu co where co.tc in (Select c.tc from calisanlar where c.kan_grubu = 'AB-')"
    sorgu6 = "select c.tc, c.isim, c.soyad, c.kan_grubu, co.pozitif_tarihi,co.negatif_tarihi from calisanlar c, covid_tablosu co where co.tc in (Select c.tc from calisanlar where c.kan_grubu = 'AB+')"
    sorgu7 = "select c.tc, c.isim, c.soyad, c.kan_grubu, co.pozitif_tarihi,co.negatif_tarihi from calisanlar c, covid_tablosu co where co.tc in (Select c.tc from calisanlar where c.kan_grubu = '0-')"
    sorgu8 = "select c.tc, c.isim, c.soyad, c.kan_grubu, co.pozitif_tarihi,co.negatif_tarihi from calisanlar c, covid_tablosu co where co.tc in (Select c.tc from calisanlar where c.kan_grubu = '0+')"
    result = cursor.execute(sorgu)      #A-
    result2 = cursor2.execute(sorgu2)   #A+
    result3 = cursor3.execute(sorgu3)   #B-
    result4 = cursor4.execute(sorgu4)   #B+
    result5 = cursor5.execute(sorgu5)   #AB-
    result6 = cursor6.execute(sorgu6)   #AB+
    result7 = cursor7.execute(sorgu7)   #0-
    result8 = cursor8.execute(sorgu8)   #0+
    if result or result2 or result3 or result4 or result5 or result6 or result7 or result8 > 0:
        a1 = cursor.fetchall()
        a2 = cursor2.fetchall()
        b1 = cursor3.fetchall()
        b2 = cursor4.fetchall()
        ab1 = cursor5.fetchall()
        ab2 = cursor6.fetchall()
        sıfır1 = cursor7.fetchall()
        sıfır2 = cursor8.fetchall()
        ua1 = len(a1)
        ua2 = len(a2)
        ub1 = len(b1)
        ub2 = len(b2)
        uab1 = len(ab1)
        uab2 = len(ab2)
        usıfır1 = len(sıfır1)
        usıfır2 = len(sıfır2)
        return render_template("kangrubucovid.html",a1 = a1, a2= a2, b1 = b1, b2 = b2, ab1= ab1, ab2= ab2, sıfır1 = sıfır1, sıfır2 = sıfır2, ua1= ua1, ua2=ua2, ub1=ub1,ub2=ub2, uab1=uab1,uab2=uab2,usıfır1=usıfır1,usıfır2=usıfır2)
    else:
        flash("Bir hata oluştu","danger")
        return render_template("kangrubucovid.html")




# COVID'e yakalananlar arasında en sık görülen 3 belirti ve o belirtiye sahip olan çalışanlar
@app.route("/top3belirti", methods=["GET","POST"])
def top3belirti():
    if request.method == "GET" or request.method == "POST":
        cursor = mysql.connection.cursor() 
        cursor0 = mysql.connection.cursor()  
        cursor1 = mysql.connection.cursor()
        cursor2 = mysql.connection.cursor()   
        sorgu = "Select belirti_ismi, COUNT(belirti_ismi) as gorulme_sayisi from belirtiler_tablo GROUP BY belirti_ismi ORDER BY gorulme_sayisi desc LIMIT 3;"       
        result = cursor.execute(sorgu) 
        if result > 0:
            data = cursor.fetchall()  
            belirti_adi0 = data[0]['belirti_ismi']
            belirti_adi1 = data[1]['belirti_ismi']
            belirti_adi2 = data[2]['belirti_ismi']
            print(data)
            sorgu0 = "Select DISTINCT c.tc, c.isim, c.soyad, b.belirti_ismi from calisanlar c, belirtiler_tablo b where c.tc in (Select b.tc where b.belirti_ismi = '" + belirti_adi0 + "');"
            sorgu1 = "Select DISTINCT c.tc, c.isim, c.soyad, b.belirti_ismi from calisanlar c, belirtiler_tablo b where c.tc in (Select b.tc where b.belirti_ismi = '" + belirti_adi1 + "');"
            sorgu2 = "Select DISTINCT c.tc, c.isim, c.soyad, b.belirti_ismi from calisanlar c, belirtiler_tablo b where c.tc in (Select b.tc where b.belirti_ismi = '" + belirti_adi2 + "');"
            result0 = cursor0.execute(sorgu0)
            result1 = cursor1.execute(sorgu1)
            result2 = cursor2.execute(sorgu2)
            if result0 and result1 and result2 > 0:
                data0 = cursor0.fetchall()     
                data1 = cursor1.fetchall()        
                data2 = cursor2.fetchall()
                bir = len(data0)
                iki = len(data1)
                uc = len(data2)
                return render_template("top3belirti.html", data=data, data0=data0, data1= data1, data2= data2,bir=bir, iki = iki,uc = uc)
            else:
                flash("Bu sayfada henüz herhangi bir veri bulunmamaktadır","danger")
                return redirect(url_for("dashboard"))



#/////////////////////////////////////////////////////////////////////////////////
#covid olup sağlıklı kişilere temas edenler
@app.route("/covidtemas")
def covidtemas():
    cursor = mysql.connection.cursor()
    cursor2 = mysql.connection.cursor()
    sorgu = "SELECT tc,isim,soyad FROM bulastiran_covidliler GROUP by tc order by count(tc) DESC LIMIT 3;"
    sorgu2 = "select temas_eden_tc,isim,soyad from covidliye_dokunanlar GROUP by temas_eden_tc order by count(temas_eden_tc) desc limit 3;"
    #view dan sorgu yaptık
    result = cursor.execute(sorgu)
    result2 = cursor2.execute(sorgu2)
    if result or result2> 0:
        data = cursor.fetchall()
        data2 = cursor2.fetchall()
        return render_template("covidtemas.html",data = data, data2= data2)
    else:
        flash("Bir hata oluştur","danger")
        return render_template("covidtemas.html")

#view oluşturma kodlarım
#create view bulastiren_covidliler as Select c.tc, c.isim, c.soyad, t.temasli_tc from calisanlar c, temasli_calisanlar_tablo t where c.tc in (SELECT t.tc from temasli_calisanlar_tablo);

#create view covidliye_dokunanlar as select c.tc as temas_eden_tc, c.isim,c.soyad,t.tc as koronali from calisanlar c, temasli_calisanlar_tablo t where c.tc in (Select t.temasli_tc from temasli_calisanlar_tablo);

#////////////////////////////////////////////////////////////////////////////////



# Aşı türüne ve durumuna göre covidi kaç günde atlatma bilgisi
@app.route("/asiturucovidatlatma")
def asiturucovidatlatma():
    cursor = mysql.connection.cursor()
    cursor2 = mysql.connection.cursor()
    cursor3 = mysql.connection.cursor()
    sorgu = "Select DISTINCT c.tc, c.isim, c.soyad, TIMESTAMPDIFF(DAY,co.pozitif_tarihi,co.negatif_tarihi) as fark, co.asi_id from covid_tablosu co, calisanlar c where c.tc in (SELECT co.tc from covid_tablosu where co.asi_id = '1');" #Aşı olmayanlar
    sorgu2 = "Select DISTINCT c.tc, c.isim, c.soyad, TIMESTAMPDIFF(DAY,co.pozitif_tarihi,co.negatif_tarihi) as fark, co.asi_id from covid_tablosu co, calisanlar c where c.tc in (SELECT co.tc from covid_tablosu where co.asi_id = '2');" #Sinovac aşısı olanlar
    sorgu3 = "Select DISTINCT c.tc, c.isim, c.soyad, TIMESTAMPDIFF(DAY,co.pozitif_tarihi,co.negatif_tarihi) as fark, co.asi_id from covid_tablosu co, calisanlar c where c.tc in (SELECT co.tc from covid_tablosu where co.asi_id = '3');" #Biontech aşısı olanlar
    result = cursor.execute(sorgu)
    result2 = cursor2.execute(sorgu2)
    result3 = cursor3.execute(sorgu3)
    if result or result2 or result3 > 0:
        asisiz = cursor.fetchall()
        sinovac = cursor2.fetchall()
        biontech = cursor3.fetchall()
        return render_template("asiturucovidatlatma.html",asisiz = asisiz, sinovac = sinovac, biontech = biontech)
    else:
        flash("Bir hata oluştur","danger")
        return render_template("asiturucovidatlatma.html")



# En sık hasta olan ilk 10 kişinin son bir ay içerisinde COVID'e yakalanma durumunu listeleyen kod
@app.route("/encokhastaolanson1aycovid")
def encokhastaolanson1aycovid():
    cursor = mysql.connection.cursor()
    sorgu = "select DISTINCT c.tc,c.isim, c.soyad,co.pozitif_tarihi,co.negatif_tarihi from calisanlar c, hastalik_tablo h, covid_tablosu co where c.tc in (select co.tc from covid_tablosu where co.tc in (SELECT tc from hastalik_tablo GROUP BY tc ORDER BY COUNT(tc) desc) and timestampdiff(month,co.negatif_tarihi,curdate())<=1);"
    result = cursor.execute(sorgu)
    if result > 0:
        data = cursor.fetchall()
        return render_template("encokhastaolanson1aycovid.html",data = data)
    else:
        flash("Bir hata oluştur","danger")
        return render_template("encokhastaolanson1aycovid.html")



#Biontech aşısı olan ve belirli bir hastalığı önceden geçirmiş olan çalışanlardan COVID'e yakalananların listesi
  
@app.route("/biontechhastalik", methods=["GET","POST"])
def biontechhastalik():
    if request.method == "POST":
        hastalikadi = request.form.get('hastalikadi')
        cursor = mysql.connection.cursor()
        sorgu = "select c.tc, c.isim, c.soyad, co.pozitif_tarihi, co.negatif_tarihi,h.hastalik_adi, co.asi_id  from calisanlar c, covid_tablosu co, hastalik_tablo h where c.tc in (Select co.tc from covid_tablosu where co.asi_id = '3' and co.tc in (Select h.tc from hastalik_tablo where h.hastalik_adi = '"+hastalikadi+"')) order by c.tc"
        result = cursor.execute(sorgu)
        if result == 0:
            flash("Aranan hastalığa ait bir veri bulunamadı...","warning")
            return render_template("biontechhastalik.html")
        else:
            data = cursor.fetchall()
            return render_template("biontechhastalik.html",data = data, hastalikadi=hastalikadi)
    else:
        return render_template("biontechhastalik.html") 




# Haftasonu çalışıp korona olanların listesi
@app.route("/haftasonucorona")
def haftasonucorona():
    cursor = mysql.connection.cursor()
    cursor2 = mysql.connection.cursor()
    sorgu = "Select c.tc, c.isim, c.soyad, co.pozitif_tarihi, co.negatif_tarihi, cs.cumartesigiris,cs.cumartesicikis,cs.pazargiris, cs.pazarcikis from calisanlar c, covid_tablosu co, calisma_sureleri cs where c.tc in (Select co.tc from covid_tablosu where co.tc in (Select cs.tc from calisma_sureleri where cs.cumartesigiris <> '0:00:00' or  cs.cumartesicikis <> '0:00:00' or cs.pazargiris <> '0:00:00' or cs.pazarcikis <> '0:00:00'))"
    sorgu2 = "Select * from calisma_sureleri where cumartesigiris <> '0:00:00' or  cumartesicikis <> '0:00:00' or pazargiris <> '0:00:00' or pazarcikis <> '0:00:00';"
    result = cursor.execute(sorgu)
    result2 = cursor2.execute(sorgu2)
    if result or result2> 0:
        data = cursor.fetchall()
        data2 = cursor2.fetchall() 
        korona_olan = len(data)
        toplamkisisayisi = len(data2)
        #korona_olmayan = toplamkisisayisi - korona_olan
        return render_template("haftasonucorona.html",data = data,korona_olan=korona_olan,toplamkisisayisi=toplamkisisayisi)
    else:
        flash("Bir hata oluştur","danger")
        return render_template("haftasonucorona.html")














#####################################################################################
#######################################################################################
if __name__ == "__main__":                    ##########################################
    app.run(debug=True)                       ###########################################
    #local host çalıştırılmış oldu            ##########################################
#######################################################################################
######################################################################################