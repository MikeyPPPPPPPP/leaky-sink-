
import sys, json

#search a list of domains for leaked config files and admin logins
#Note: after httpx to use FFUF to bruteforce the data=

class low_hanging_fruit:
	def __init__(self, hosts: str):
		self.temp_directory = hosts + "_temp"
		os.mkdir(self.temp_directory)
		self.hosts: list[str] = hosts
		self.found: dict[str:dict[str:str]] = {}
		self.__format_data()


	def __format_data(self) -> None:
		"""Unpacke the files, They should be pretty small"""

		#the hosts
		with open(self.hosts, "r") as host:
			self.hosts = [hos.strip() for hos in host.readlines]


	def FFUF(self, host: str) -> None: #hosts should look like https://www.google.com
		"""Make a temp directory, write indiviudal output files from it."""
		#os.system()

		#run the command
		dirSafeHost = host.split("://")[-1]# th
		command = f"/opt/tools/ffuf/ffuf -u {host}/FUZZ -w $wordlists/Bug-Bounty-Wordlists-main/all-files-leaked.txt -o {self.temp_directory}/{dirSafeHost}.output"
		os.system(command)

		#parse the file: status code, url
		with open(f'{self.temp_directory}/{dirSafeHost}.output','r') as file:
			data = json.loads(file.read())

		#add statusecodes and url to the hosts variable.
		for x in data["results"]:
			self.hosts[host] = {x["status"], x["url"]}

def chaching(hosts):
	#thread ripper~~!!
	shoot = low_hanging_fruit(hosts)
	with open()
		with concurrent.futures.ThreadPoolExecutor(max_worker = 2) as executor:
			futures = [executor.submit(shoot.FFUF, hos) for hos in shoot.hosts]

	if len(shoot.found) != 0:
		with open("leaky.output", "w") as log:
			json.dumps(shoot.found)

	if not os.is_file("leaky.output"):
		os.system(f"rm -rf {shoot.temp_directory}/")
	else:
		print("Failed >:P")


def main():
	hostsfile = sys.argv[1]
	chaching(hostsfile)




if __name__ == "__main__":
	main()

"""
Log: grep by status code


grep 200 log.txt


200, 303, 404,402, 430, 203 http://www.google.com
200 http://www.google.com/ds
200 http://www.google.com/fdsa

200, 303, 404,402, 430, 203 http://wdwdw.google.com
200 http://wdwdw.google.com/dsds.fpfd
200 http://wdwdw.google.com/.git

200, 303, 404,402, 430, 203 http://sub.google.com
203 http://sub.google.com/dsdfsa/index.php
203 http://sub.google.com/fdsafsdf.php

All Ports: 200, 303, 404,402, 430, 203, 324, 321, 532, 533
"""
