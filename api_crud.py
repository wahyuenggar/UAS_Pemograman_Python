import requests
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="db_akademik_0495"
)
	
def write_db_api():
	newdict = { }
	url = 'https://api.abcfdab.cfd/students'
	response = requests.get(url)
	data = response.json()
	cursor = mydb.cursor()
	sql = '''INSERT INTO tbl_students_0495
			(id,nim,nama,jk,jurusan,alamat) VALUES 
			(%s, %s, %s, %s, %s, %s )'''

	for row in data['data'] :
		val = (row['id'],row['nim'], row['nama'] ,row['jk'], row['jurusan'], row['alamat'])		
		cursor.execute(sql,val)
		mydb.commit()	

def tampil_semua():
	mycursor = mydb.cursor()
	mycursor.execute("SELECT * FROM tbl_students_0495")
	myresult = mycursor.fetchall()
	for x in myresult:
  		print(x)

def tampil_limit():
	baris = input("\nBerapa limitnya : ")
	mycursor = mydb.cursor()
	sql = ("SELECT * FROM tbl_students_0495 limit ")
	mycursor.execute(sql + baris)
	myresult = mycursor.fetchall()
	for x in myresult:
  		print(x)

def tampil_nim():
	petik = "'"
	nim = input('Masukkan NIM : ')
	mycursor = mydb.cursor()
	sql = (" SELECT * FROM `tbl_students_0495` WHERE nim = ")
	mycursor.execute(sql + petik + nim + petik )
	myresult = mycursor.fetchone()
	print(myresult)

if __name__ == '__main__':
	#write_db_api()
	while True:
		print("\n________Program API________\n")
		print("1. Tampilkan semua data ")
		print("2. Tampilkan data berdasarkan limit ")
		print("3. Cari data berdasarkan NIM ")
		print("0. Exit\n")
		menu = int(input("Masukkan menu : "))
		if menu == 1 :
			tampil_semua()
		if menu == 2 :
			tampil_limit()
		if menu == 3 :
			tampil_nim()
		if menu == 0 :
			break
		else :
			print('Masukkan salah !!!')
		
