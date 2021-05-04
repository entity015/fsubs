#!/usr/bin/python3
#entity015 ~ https://t.me/rzeee
from bs4 import BeautifulSoup
import requests,re,os

class Oploverz:
	def __init__(self):
		self.url = "https://oploverz.bz"
	def latest(self):
		content = soup(self.url)
		data = {"titles":[],"links":[]}
		for _ in content.find_all("article",class_="stylesix"):
			data["titles"].append(_.h2.a.text)
			data["links"].append(_.h2.a["href"])
		return data
	def search(self,query):
		self.url += "/?s=" + query
		content = soup(self.url)
		data = {"titles":[],"links":[]}
		for _ in content.find_all("article",class_="bs"):
			data["titles"].append(_.a["title"])
			data["links"].append(_.a["href"])
		return data
	def anime(self,url):
		content = soup(url).find("div",class_="eplister")
		data = {"titles":[],"links":[]}
		for _ in content.find_all("li"):
			t = "Episode " + _.find("div",class_="epl-num").text
			data["titles"].append(t)
			data["links"].append(_.a["href"])
		data["titles"] = data["titles"][::-1]
		data["links"] = data["links"][::-1]
		return data
	def go(self,url):
		try:
			content = soup(url).find("div",class_="mctnx")
			for _ in content.find_all("div",class_="soraddlx soradlg"):
				print(f"{SKY}{_.h3.text}{END}")
				for urls in _.find_all("div",class_="soraurlx"):
					print(f"{SKY}{urls.strong.text}{END}")
					for u in urls.find_all("a"):
						print(f"[x] {u['href']}")
				print("")
		except Exception:
			print("Link not available")

class Anitoki:
	def __init__(self):
		self.url = "http://anitoki.com"
	def latest(self):
		content = soup(self.url)
		data = {"titles":[],"links":[]}
		for _ in content.find_all("div",class_="content"):
			data["titles"].append(_.h2.a.text.replace("Subtitle Indonesia",""))
			data["links"].append(_.h2.a["href"])
		return data
	def search(self,query):
		self.url += "/?s=" + query + "&post_type=anime"
		content = soup(self.url)
		data = {"titles":[],"links":[]}
		for _ in content.find_all("div",class_="content"):
			data["titles"].append(_.h2.a.text)
			data["links"].append(_.h2.a["href"])
		return data
	def anime(self,url):
		content = soup(url).find_all("div",class_="sinopc")[1]
		data = {"titles":[],"links":[]}
		for _ in content.find_all("li"):
			data["titles"].append(_.a.text.strip())
			data["links"].append(_.a["href"])
		data["titles"] = data["titles"][::-1]
		data["links"] = data["links"][::-1]
		return data
	def go(self,url):
		content = soup(url)
		for _ in content.find_all("div",class_="smokeddl"):
			for title in _.find_all("div",class_="smokettl"):
				print(f"{SKY}{title.text}{END}")
				for url in _.find_all("div","smokeurl"):
					for quality in url.find_all("strong"):
						print(f"{SKY}{quality.text}{END}")
					for links in url.find_all("a",attrs={'href':re.compile("https://")}):
						print(f"[x] {links['href']}")
				print("")

class Kusonime:
	def __init__(self):
		self.url = "https://kusonime.com"
	def search(self,query):
		self.url += "/?s=" + query + "&post_type=post"
		content = soup(self.url)
		data = {"titles":[],"links":[]}
		for _ in content.find_all("div",class_="content"):
			data["titles"].append(_.a.text)
			data["links"].append(_.a["href"])
		return data
	def go(self,url):
		content = soup(url)
		for _ in content.find_all("div",class_="smokeddl"):
			for title in _.find_all("div",class_="smokettl"):
				print(f"{SKY}{title.text}{END}")
				for url in _.find_all("div","smokeurl"):
					for quality in url.find_all("strong"):
						print(f"{SKY}{quality.text}{END}")
					for links in url.find_all("a",attrs={'href':re.compile("https://")}):
						print(f"[x] {links['href']}")
				print("")

class Otakudesu:
	def __init__(self):
		self.url = "https://otakudesu.moe"
	def search(self,query):
		self.url += "/?s=" + query + "&post_type=anime"
		content = soup(self.url).find("ul",class_="chivsrc")
		data = {"titles":[],"links":[]}
		for _ in content.find_all("li"):
			data["titles"].append(_.h2.a.text)
			data["links"].append(_.h2.a["href"])
		return data
	def anime(self,url):
		content = soup(url).find("div",class_="venser")
		data = {"titles":[],"links":[]}
		print(f"{SKY}{content.find('div',class_='smokelister').text.replace('Batch','')}List{END}")
		for _ in content.find_all("div",class_="episodelist")[:2]:
			urls = _.find_all("li")
			for i in urls:
				data["titles"].append(i.a.text)
				data["links"].append(i.a["href"])
		data["titles"] = data["titles"][::-1]
		data["links"] = data["links"][::-1]
		return data
	def go(self,url):
		content = soup(url).find("div",class_="download")
		print(f"{SKY}{content.h4.text}{END}")
		for _ in content.find_all("li"):
			print(f"{SKY}{_.strong.text}{END}")
			for l in _.find_all("a"):
				print(f"[x] {l['href']}")
			print("")

class Maxnime:
	def __init__(self):
		self.url = "https://maxnime.com"
	def search(self,query):
		self.url += "/?s=" + query
		content = soup(self.url).find("div",class_="white").find("ul")
		data = {"titles":[],"links":[]}
		for _ in content.find_all("div",class_="dtl"):
			data["titles"].append(_.a.text)
			data["links"].append(_.a["href"])
		return data
	def go(self,url):
		content = soup(url)
		for _ in content.find_all("div",class_="boxdl"):
			title = _.find("div",class_="boxtitle").text
			print(f"{SKY}{title}{END}")
			for urls in _.find_all("div",class_="boxurl"):
				resolution = urls.find("strong").text
				print(f"{SKY}{resolution}{END}")
				for url in urls.find_all("a"):
					print(f"[x] {url['href']}")
			print("")

class Drivenime:
	def __init__(self):
		self.url = "https://drivenime.com"
	def search(self,query):
		self.url += "/?s=" + query
		content = soup(self.url).find("article",class_="article")
		data = {"titles":[],"links":[]}
		for _ in content.find_all("div",class_="post"):
			data["titles"].append(_.h2.a.text)
			data["links"].append(_.h2.a["href"])
		return data
	def go(self,url,alternative=None):
		content = soup(url).find("div",class_="post-single-content box mark-links")
		alter = content.find("div",class_="su-accordion su-u-trim")
		if alter:
			alternative = BeautifulSoup("</p>".join(re.findall("<p><a.*",str(alter))),'html.parser')
			alter.extract()
		filters = BeautifulSoup("</p>".join(re.findall("<p><a.*",str(content))),'html.parser')
		print(f"{SKY}Google Drive{END}")
		for x in filters.find_all("p"):
			print(f"[x] {x.text}\n{x.a['href']}\n")
		if alternative:
			print(f"{SKY}Google Drive Mirror (Alternative){END}")
			for y in alternative.find_all("p"):
				print(f"[x] {y.text}\n{y.a['href']}\n")

def oploverz():
	op = Oploverz()
	print(f" 1. Latest Update")
	print(f" 2. Search Anime\n")
	x = input("−−$ ")
	if x == "1":
		data = op.latest()
		show(data)
		link = int(input("−−$ "))
		op.go(data["links"][link])
	elif x == "2":
		data1 = op.search(input("Search: "))
		show(data1)
		link1 = int(input("−−$ "))
		data2 = op.anime(data1["links"][link1])
		show(data2)
		link2 = int(input("−−$ "))
		op.go(data2["links"][link2])

def anitoki():
	at = Anitoki()
	print(f" 1. Latest Update")
	print(f" 2. Search Anime\n")
	x = input("−−$ ")
	if x == "1":
		data = at.latest()
		show(data)
		link = int(input("−−$ "))
		at.go(data["links"][link])
	elif x == "2":
		data1 = at.search(input("Search: "))
		show(data1)
		link1 = int(input("−−$ "))
		data2 = at.anime(data1["links"][link1])
		show(data2)
		link2 = int(input("−−$ "))
		at.go(data2["links"][link2])

def kusonime():
	kn = Kusonime()
	data = kn.search(input("Search: "))
	show(data)
	link = int(input("−−$ "))
	kn.go(data["links"][link])

def drivenime():
	dn = Drivenime()
	data = dn.search(input("Search: "))
	show(data)
	link = int(input("−−$ "))
	dn.go(data["links"][link])

def otakudesu():
	od = Otakudesu()
	data1 = od.search(input("Search: "))
	show(data1)
	link1 = int(input("−−$ "))
	data2 = od.anime(data1["links"][link1])
	show(data2)
	link2 = int(input("−−$ "))
	od.go(data2["links"][link2])

def maxnime():
	mn = Maxnime()
	data = mn.search(input("Search: "))
	show(data)
	link = int(input("−−$ "))
	mn.go(data["links"][link])

def soup(url):
	respons = requests.get(url,headers=header,timeout=15)
	content = BeautifulSoup(respons.text,'html.parser')
	return content
def show(data):
	titles = data["titles"]
	for i,title in enumerate(titles):
		print(f" {i}. {title}")
	print("")

def main():
	try:
		os.system("clear" if os.name=="posix" else "cls")
		print(banner)
		o = input("−−$ ")
		if o=="1":oploverz()
		elif o=="2":anitoki()
		elif o=="3":kusonime()
		elif o=="4":drivenime()
		elif o=="5":otakudesu()
		elif o=="6":maxnime()
		elif o=="0":exit("Exit.")
		else:exit("Wrong input")
	except KeyboardInterrupt:
		exit("\nExit.")

ICE = "\033[1;37m"
TEA = "\033[1;32m"
RED = "\033[1;31m"
SKY = "\033[1;34m"
SUN = "\033[1;33m"
END = "\033[0;00m"
banner = f"""{RED}
     ___________       __        
    / ____/ ___/__  __/ /_  _____
   / /_   \__ \/ / / / __ \/ ___/
  / __/  ___/ / /_/ / /_/ (__  ) 
 /_/    /____/\__,_/_.___/____/ {SUN}

 ｢ Fansub & Fanshare Urls Grabber ｣
            Entity015 ♥
{TEA}
 1. Oploverz
 2. Anitoki
 3. Kusonime
 4. Drivenime
 5. Otakudesu
 6. Maxnime 
 0. Exit
{END}"""
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0"}
main()
