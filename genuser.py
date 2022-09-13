#!/usr/bin/python3
import sys
import os

def genuser(x):
	x = x.lower()
	fname = x.split(" ")[0]
	lname = x.split(" ")[1]

	print(f'''{fname}
{fname}{lname}
{fname}.{lname}
{fname}_{lname}
{fname}-{lname}
{fname[0]}{lname}
{fname[0]}.{lname}
{fname[0]}_{lname}
{lname}{fname[0]}
{fname[0:3]}{lname[0:3]}
''',end='')


	with open("usernames.txt","a") as f:
		f.write(f'''{fname}
{fname}{lname}
{fname}.{lname}
{fname}_{lname}
{fname}-{lname}
{fname[0]}{lname}
{fname[0]}.{lname}
{fname[0]}_{lname}
{lname}{fname[0]}
{fname[0:3]}{lname[0:3]}
'''
)

if __name__ == "__main__":
	try:
		inputfile = sys.argv[1]
			
		with open(inputfile) as f:
			line = f.readline().strip()
			while line:
				genuser(line)
				line = f.readline().strip()
		print()
		print(f"Saved to {os.path.dirname(__file__)}/usernames.txt")
	except:
		print("Usage: python3 usernames.py [full-names].txt")
