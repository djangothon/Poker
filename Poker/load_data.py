# Full path and name to your csv file
csv_filepathname="F:/Hacks/Django/Poker/sample.csv"
# Full path to your django project directory
your_djangoproject_home="F:/Hacks/Django/Poker"

import sys,os
sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django
django.setup()

from contacts.models import contacts

import csv
dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')



for record in dataReader:
	print(record[0].split(",")) 
	print(">>>")
	print(record[0]) 
	x = record[0].split(",")
	if x[0] != 'phased_out_age': # Ignore the header record, import everything else
		recordset = contacts()
		recordset.contact_phasedout_age = x[0]
		recordset.contact_name = x[1]
		recordset.contact_ph_num = x[2]
		recordset.contact_emailid = x[3]
		recordset.contact_last_contacted = x[4]
		recordset.save()
		
		print(recordset) 
		
		
