#!/usr/bin/env python
#-*-coding: utf-8 -*-
# Something in lines of http://stackoverflow.com/questions/348630/how-can-i-download-all-emails-with-attachments-from-gmail

import email
import imaplib
import os
import sys
import datetime
import uu
import re
import shutil
import socket

detach_dir = '.'
if 'attachments' not in os.listdir(detach_dir):
    os.mkdir('attachments')

attachments = "/home/openkasnet/Documents/Programming/Python/sequence/attachments/"
file_convert = "/home/openkasnet/Documents/Programming/Python/sequence/result/convert/"
line1seq = "line1seq/"
line2seq = "line2seq/"
bum1line = 'bum1line/'
bum2line = "bum2line/"
stljit = 'stljit/'
ndljit = 'ndljit/'

date = datetime.datetime.now().strftime( "%d-%m-%Y-%H:%M:%S" )
lines = '-'

def GetMail(imap_host, userName, passwd):
    ##print 'Oy'
    socket.setdefaulttimeout(100)
    imapSession = imaplib.IMAP4_SSL(imap_host)
    typ, accountDetails = imapSession.login(userName, passwd)

    if typ != 'OK':
        #print 'Not able to sign in!'
        raise

    imapSession.select('INBOX')
    typ, data = imapSession.search(None, '(UNSEEN)')
    if typ != 'OK':
        #print 'Error searching Inbox.'
        raise

    # Iterating over all emails
    for msgId in data[0].split():
        typ, messageParts = imapSession.fetch(msgId, '(RFC822)')
        if typ != 'OK':
            #print 'Error fetching mail.'
            raise

        ##print messageParts[0][1]
        #Begin 644
        status, count = imapSession.fetch(msgId, '(UID BODY[TEXT])')
        mip = '%s\n' % (count[0][1])
        ##print mip
        if 'begin 644' in mip:
            #print 'Ok'
            k = re.search(r'(begin.*)', '%s' % (mip)).group(0)
            Subj = k[10:-1]
            #print Subj
            print mip
            f = open(attachments+msgId+lines+Subj, 'w')
            f.write(mip)
            f.close()

        emailBody = messageParts[0][1]
        mail = email.message_from_string(emailBody)
        for part in mail.walk():
            if part.get_content_maintype() == 'multipart':
                # #print part.as_string()
                continue
            if part.get('Content-Disposition') is None:
                # #print part.as_string()
                continue
            fileName = part.get_filename()

            if bool(fileName):
                filePath = os.path.join(detach_dir, 'attachments', fileName)
                if not os.path.isfile(filePath) :
                    #print fileName
                    fp = open(filePath, 'w')
                    fp.write(part.get_payload(decode=True))
                    fp.close()
    imapSession.close()
    imapSession.logout()

#else:
    #print 'Not able to download all attachments.'
#    pass

#Bu joyda attch file ni o'qiladigan holatda olsa db ga ko'chiradigan papkaga o'tkazamiz
for top, dirs, files in os.walk(attachments):
        for nm in files:
            ##print os.path.join(nm)
            lsresult = os.path.join(nm)
            ##print lsresult
            if 'LINE1SEQ' in lsresult:
                #print lsresult
                f = open(attachments+lsresult)
                hb = f.readline()
                f.close()
                ##print d
                if 'begin 644' in hb:
                    #print 'begin 644'
                    f = open(attachments+lsresult)
                    pd = uu.decode(f, file_convert+line1seq+lsresult)
                    f.close()
                    os.remove(attachments+lsresult)
                    #print 'Remove file %s' % (lsresult)
                elif 'LINE1SEQ' == hb[0:8]:
                    shutil.move(attachments+lsresult, file_convert+line1seq+lsresult)
                    #print 'Copied file %s' % (lsresult)
                else:
                    os.remove(attachments+lsresult)
                    #print 'Remove file %s' % (lsresult)

            #-----------------LINE2SEQ--------------
            if 'LINE2SEQ' in lsresult:
                print lsresult
                f = open(attachments+lsresult)
                hb = f.readline()
                f.close()
                if 'begin 644' in hb:
                    f = open(attachments+lsresult)
                    pd = uu.decode(f, file_convert+line2seq+lsresult)
                    f.close()
                    os.remove(attachments+lsresult)
                    #print 'Remove file %s' % (lsresult)
                elif 'LINE2SEQ' == hb[0:8]:
                    shutil.move(attachments+lsresult, file_convert+line2seq+lsresult)
                    #print 'Copied file %s' % (lsresult)
                else:
                    #os.remove(attachments+lsresult)
                    #print 'Remove file %s' % (lsresult)
                    pass

            #----------BUM1LINE----------
            if 'BUM1LINE' in lsresult:
                #print lsresult
                f = open(attachments+lsresult)
                hb = f.readline()
                f.close()
                print attachments+lsresult
                if 'begin 644' in hb:
                    f = open(attachments+lsresult)
                    pd = uu.decode(f, file_convert+bum1line+lsresult)
                    f.close()
                    os.remove(attachments+lsresult)
                    #print 'Remove file %s' % (lsresult)
                elif 'BUM1LINE' == hb[0:8]:
                    shutil.move(attachments+lsresult, file_convert+bum1line+lsresult)
                    #print 'Copied file %s' % (lsresult)
                else:
                    os.remove(attachments+lsresult)
                    #print 'Remove file %s' % (lsresult)

            #----------BUM2LINE----------
            if 'BUM2LINE' in lsresult:
                #print lsresult
                f = open(attachments+lsresult)
                hb = f.readline()
                f.close()
                print attachments+lsresult
                if 'begin 644' in hb:
                    f = open(attachments+lsresult)
                    pd = uu.decode(f, file_convert+bum2line+lsresult)
                    f.close()
                    os.remove(attachments+lsresult)
                    #print 'Remove file %s' % (lsresult)
                elif 'BUM2LINE' == hb[0:8]:
                    shutil.move(attachments+lsresult, file_convert+bum2line+lsresult)
                    #print 'Copied file %s' % (lsresult)
                else:
                    os.remove(attachments+lsresult)
                    #print 'Remove file %s' % (lsresult)

            #---------------1STLNJIT-------------
            if '1STLNJIT' in lsresult:
                #print lsresult
                f = open(attachments+lsresult)
                hb = f.readline()
                f.close()
                ##print d
                if 'begin 644' in hb:
                    f = open(attachments+lsresult)
                    pd = uu.decode(f, file_convert+stljit+lsresult)
                    f.close()
                    os.remove(attachments+lsresult)
                    #print 'Copied file %s' % (lsresult)
                elif '1STLNJIT' == hb[0:8]:
                    shutil.move(attachments+lsresult, file_convert+stljit+lsresult)
                    #print 'Copied file %s' % (lsresult)
                else:
                    os.remove(attachments+lsresult)
                    #print 'Remove file %s' % (lsresult)

            #---------------2NDLNJIT-------------
            if '2NDLNJIT' in lsresult:
                #print lsresult
                f = open(attachments+lsresult)
                hb = f.readline()
                f.close()
                ##print d
                if 'begin 644' in hb:
                    f = open(attachments+lsresult)
                    pd = uu.decode(f, file_convert+ndljit+lsresult)
                    f.close()
                    os.remove(attachments+lsresult)
                    #print 'Copied file %s' % (lsresult)
                elif '2NDLNJIT' == hb[0:8]:
                    shutil.move(attachments+lsresult, file_convert+ndljit+lsresult)
                    #print 'Copied file %s' % (lsresult)
                else:
                    os.remove(attachments+lsresult)
                    #print 'Remove file %s' % (lsresult)


import line1seq
import line2seq


<<<<<<< HEAD
GetMail(imap_host = 'host', userName = 'user', passwd = 'pass')
=======
GetMail(imap_host = 'mail.uzkoram.uz', userName = 'user', passwd = 'pass')
>>>>>>> abb32364bd7cf648936408886bffdfb7eb71a90a

