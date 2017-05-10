import urllib2
import base64
import logging
import os

__author__ = 'abitran'


def get_ip_address():

    ''' This function calls os command ifconfig and finds the ip address
    of the external interface '''
    command = os.popen("/sbin/ifconfig")  #  we call ifconfing and store it in command
    line1 = command.read()   # we read the lines as string in line1
    st1 = line1.find('eth1')  # we search for eth1
    subline = line1[st1:]   # we create a substring from eth1 up to end of file
    st2 = subline.find(' addr')  # we search for addr with a space in front
    subline1 = subline[st2+6:st2+20]   # we create a substring from subline starting from addr
    return subline1.rstrip()   # we store in myip the string that matches the ip


def run_no_ip():
    host = "put your host here"
    username = 'put your no-ip username here'
    password = "put your no-ip password here"
    ip = get_ip_address()    # we store in myip the string that matches the ip
    print "IP ADDRESS: " + ip + "\n"
    urlbase = "https://dynupdate.no-ip.com/nic/update?hostname={0}&myip={1}"
    url = urlbase.format(host,ip)
    userdata = "Basic "+(username+":"+password).encode("base64").rstrip()
    req = urllib2.Request(url)
    version = "Megatron/" + "1.0 " + "root@megatron.kdelinux.net"
    req.add_header("Authorization", userdata)
    req.add_header("User-Agent", version)

    try:
        res = urllib2.urlopen(req)
    except urllib2.HTTPError:
        logging.error(" authentication error")
        exit(2)
    print "Result:", res.read()


run_no_ip()
