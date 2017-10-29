#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# LINE 2 SEQ
#
#
#
#
#


import os
import re
import datetime
import psycopg2 #emerge psycopg
date = datetime.datetime.now().strftime( "%Y-%m-%d %H:%M:%S" )





attachments = "/home/openkasnet/Documents/Programming/Python/sequence/attachments/"
file_convert = "/home/openkasnet/Documents/Programming/Python/sequence/result/convert/"
line1seq = "line1seq/"
line2seq = "line2seq/"
bum1line = 'bum1line/'
bum2line = "bum2line/"
stljit = 'stljit/'
ndljit = 'ndljit/'






try:
	conn = psycopg2.connect(database="testdb", user="kasim", password="1212", host="127.0.0.1", port="5432")
except:
	conn = 'Err'
	f=open('err.log', 'a')
	f.write('%s No connected db;\n' %(date))
	f.close()
a= []





bad_str = [] # Strokda probel, yoki hato bo'lsa shu joyga qo'shiladi

#f = open("/home/openkasnet/Documents/Programming/Python/sequence/result/convert/line1seq/2-LINE1SEQ.xls", 'r')
#result = f.readlines()


for top, dirs, files in os.walk(file_convert+line2seq):
        for nm in files:
        	lsresult = os.path.join(nm)
        	##print lsresult
        	f_result = open(file_convert+line2seq+lsresult)
        	for i in f_result:
				##print i
				res = re.findall(r'^\d', i)
				if res:
					##print i
					NR_SQL =  i[0:4]

					#----------PONO------------------

					PONO_SQL = i[6:12]

					#----------Model-----------------

					Model_SQL = i[15:20]

					#---------Country-------------

					Country_SQL = i[23:26]

					#--------Trim_Level----------

					Trim_Level_SQL = i[32:35]

					#---------AFD AFF -----------

					AFD_AFF_SQL = i[44:47]

					#----------SEQ NO-------------

					SEQ_NO_SQL = i[52:59]

					#----------DEST --------------

					DEST_SQL = i[62:70]

					#---------- Emission ----------

					Emission_SQL = i[73:76]


					#-----------Engin----------------

					Engin_SQL = i[83:86]

					#------------TRAN----------------

					TRAN_SQL = i[90:93]

					#------------Body_Color----------

					Body_Color_SQL =i[96:99]

					#------------FRT_B---------------
					FRT_B_SQL = i[107:115]

					#------------RR_B-----------------

					RR_B_SQL = i[117:125]

					#--------------Spoiler--------------

					Spoiler_SQL = i[127:135]

					#---------------REDEC---------------

					REDEC_SQL = i[137:138]

					#---------------Time Date-----------------


					SEQ_HOUR_SQL = i[144:149]

					SEQ_DAY_SQL = i[158:160]

					SEQ_MOUNTH_SQL = i[156:158]

					SEQ_YEAR_SQL = i[154:156]

					Time_Date_SQL = '20'+SEQ_YEAR_SQL+'-'+SEQ_MOUNTH_SQL+'-'+SEQ_DAY_SQL+' '+SEQ_HOUR_SQL

					ls2 = "\'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\'" % (NR_SQL, PONO_SQL, Model_SQL, Country_SQL, Trim_Level_SQL, AFD_AFF_SQL, SEQ_NO_SQL, DEST_SQL,\
		 					Emission_SQL, Engin_SQL, TRAN_SQL, Body_Color_SQL, FRT_B_SQL, RR_B_SQL, Spoiler_SQL, REDEC_SQL, Time_Date_SQL)

					#ls2 = "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (NR_SQL, PONO_SQL, Model_SQL, Country_SQL, Trim_Level_SQL, AFD_AFF_SQL, SEQ_NO_SQL, DEST_SQL,\
		 			#		Emission_SQL, Engin_SQL, TRAN_SQL, Body_Color_SQL, FRT_B_SQL, RR_B_SQL, Spoiler_SQL, REDEC_SQL, Time_Date_SQL)


					if ls2:
						#print ls2 , 'LS2'
						if 'Err' != conn:
							cur = conn.cursor()
							cur.execute(""" SELECT * FROM line2seq WHERE seq_no = '%s' """ % (SEQ_NO_SQL))
							tmp = cur.fetchall()
							if not tmp:
								cur.execute(""" INSERT INTO line2seq (nr, pono, model, country, trim_level, afd_aff, seq_no, dest, emission,  engin, tran, body_color, frt_b, rr_b, spoiler, redec, date_added) VALUES (%s) """ % (ls2))
								conn.commit()
								continue
							get_SEQ_NO = tmp[0][7]
							##print get_SEQ_NO ,'Seq_NO'
							if get_SEQ_NO == SEQ_NO_SQL:
								pass
							else:
								cur.execute(""" INSERT INTO line2seq (nr, pono, model, country, trim_level, afd_aff, seq_no, dest, emission,  engin, tran, body_color, frt_b, rr_b, spoiler, redec, date_added) VALUES (%s) """ % (ls2))
								conn.commit()



		f_result.close()
		os.remove(file_convert+line2seq+lsresult)
		##print 'Faylni o\'chiramiz -', file_convert+line2seq+lsresult
conn.close()
