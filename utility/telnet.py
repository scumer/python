#encoding=utf-8

import socket 
import time 

def main():   
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
    sk.settimeout(100)    

    ip = '180.168.156.226'
    port = 30025
    try:    
        start = time.time()		
        sk.connect((ip,port))  
        end = time.time()
        print end-start
        print('Server %s port %d OK!' % (ip,port))    
    except Exception, e:    
        print('Server %s port %d is not connected!' % (ip,port))
        print e
    sk.close()    
        
if __name__ == '__main__':    
    main()