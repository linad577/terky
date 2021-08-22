import os,sys,time

a = "\e[34m"
b = "\e[91m"

os.system("clear")
os.system("figlet Terky | lolcat")
logo =  """

	[✓] Authour : Linad577
	TOMBOL TAMBAHAN TERMUX
	=====================

	"""
print (logo)
print ('\033[34m silakan tunggu sebentar')
time.sleep(2)

print ('\033[34m Mengambil File Default Termux')
try:
      os.mkdir('/data/data/com.termux/files/home/.termux')
except:
      pass
print ('\033[34mSuccess !')
print ('\033[34m menambahkan File Tambahan..')


key = "extra-keys = [['ESC' , '/' , '-' , 'HOME' , 'UP' , 'END' , 'PGUP']  ,  ['TAB' , 'CTRL' , 'ALT' , 'LEFT' , 'DOWN' , 'RIGHT' , 'PGDN']]"
kontol = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
kontol.write(key)
kontol.close()
print ('\033[34m Memproses  !')
print ("\033[37m Berhasil ")
os.system('termux-reload-settings')

