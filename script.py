from bs4 import BeautifulSoup

import requests

import time
global start_time
start_time = time.time()


import threading
global i,urls
i=0
urls = [
"http://www.ffiec.gov/cybersecurity.htm",
"https://www.openssl.org/docs/",
"https://www.first.org",
"https://securityblog.redhat.com/",
"https://threatpost.com/",
"http://www.sophos.com/en-us/security-news-trends",
"https://blogs.rsa.com/",
"https://apwg.org/",
"http://www.cybersecurity.alabama.gov/",
"http://www.symantec.com/connect/blogs/discover?community-id=691",
"http://www.digitalthreat.net/2010/05/information-security-models-for-confidentiality-and-integrity/",
"http://www.itsecurity.com/dictionary/all/",
"https://www.schneier.com/cryptography.html",
"http://www.iplocation.net/",
"http://www.iso.org/iso/home/standards/management-standards/iso27001.htm",
"https://www.kuppingercole.com/blog/kuppinger/information-rights-management-microsoft-gives-it-a-new-push-just-in-time-to-succeed",
"http://www.cisco.com/c/en/us/td/docs/ios/sec_data_plane/configuration/guide/12_4/sec_data_plane_12_4_book.html",
"https://www.freebsd.org/doc/handbook/index.html",
"http://www.cgisecurity.com/owasp/html/index.html",
"http://csrc.nist.gov/",
"http://disa.mil/Network-Services/Data",
"http://wiki.openssl.org/",
"http://www.isg.rhul.ac.uk/tls/",
"http://www.cryptographyworld.com/",
"http://www.w3.org/TR/xmlsec-algorithms/",
"http://niccs.us-cert.gov/glossary",
"https://www.schneier.com/essays/",
"http://securitywatch.pcmag.com/",
"https://www.torproject.org/",
"http://resources.infosecinstitute.com",
"http://www.esslsecurity.com/",
"http://stackoverflow.com/questions/tagged/security",
"http://docs.saltstack.com/en/latest/",
"https://saltthepass.com/#help-about",
"http://crypto.stackexchange.com/",
"http://www.biometrics.gov/",
"http://www.biometricsinstitute.org/pages/types-of-biometrics.html",
"http://support.microsoft.com/en-us/kb/246071",
"http://www.garykessler.net/library/fsc_stego.html",
"https://technet.microsoft.com/en-us/library/cc179103.aspx",
"http://cs.stanford.edu/people/eroberts/courses/soco/projects/2000-01/risc/whatis/",
"http://www.gammassl.co.uk/research/chinesewall.php",
"http://www.softpanorama.org/Access_control/Security_models/",
"http://www.openpgp.org/",
"http://www.quadibloc.com/crypto/jscrypt.htm",
"http://search.cpan.org/dist/Crypt-Loki97/Loki97.pm",
"https://www.fastmail.com/help/technical/ssltlsstarttls.html",
"http://www.ietf.org/rfc/rfc4880.txt",
"https://tools.ietf.org/html/rfc2595",
"http://www.pcmag.com/article2/0,2817,2407168,00.asp",
"http://www.pcmag.com/article2/0,2817,2372364,00.asp",
"https://technet.microsoft.com/en-us/library/hh994558%28v=ws.10%29.aspx",
"https://technet.microsoft.com/en-us/library/hh994561(v=ws.10).aspx",
"https://technet.microsoft.com/en-us/library/dd883248(v=ws.10).aspx",
"https://technet.microsoft.com/en-us/library/cc755284(v=ws.10).aspx",
"https://technet.microsoft.com/en-us/library/cc731416(v=ws.10).aspx",
"https://technet.microsoft.com/en-us/library/ee706526(v=ws.10).aspx",
"https://technet.microsoft.com/en-us/library/cc731004(v=ws.10).aspx",
"https://technet.microsoft.com/en-us/library/cc731515(v=ws.10).aspx",
"https://technet.microsoft.com/en-us/library/cc771395(v=ws.10).aspx",
"https://technet.microsoft.com/en-us/library/jj865680(v=ws.10).aspx",
"https://technet.microsoft.com/en-us/library/ff641731(v=ws.10).aspx",
"https://technet.microsoft.com/en-us/library/cc753173(v=ws.10).aspx",
"https://technet.microsoft.com/en-us/library/cc721923(v=ws.10).aspx",
"https://technet.microsoft.com/en-us/library/cc731549(v=ws.10).aspx",
"https://technet.microsoft.com/en-us/library/cc732077(v=ws.10).aspx",
"https://technet.microsoft.com/en-us/library/cc772066(v=ws.10).aspx",
"https://twitter.com/bruce_schneier",
"http://www.isaccouncil.org/memberisacs.html",
"https://tools.ietf.org/",
"http://www.sqlsecurity.co",
"https://technet.microsoft.com/en-us/library/security/dn610807.aspx",
"http://searchsecurity.techtarget.in/",
"http://www.bmc.com/support/security/",
"https://portal.reisac.org/SitePages/Index.aspx",
"http://www.infosecisland.com/",
"http://www.infosecblog.org/",
"https://isc.sans.edu/",
"http://www.northropgrumman.com",
"https://ics-cert.us-cert.gov/Standards-and-References",
"http://www.information-age.com/",
"https://europaysolutions.com/fraud-risk-management/fraud-prevention-suite/",
"http://www.idrbt.ac.in/",
"https://cve.mitre.org/",
"http://www.ibm.com/developerworks/websphere/zones/was/security/",
"https://cryptoworks21.uwaterloo.ca/cryptography",
"http://www.fortinet.com",
"https://crackstation.net/hashing-security.htm",
"http://www.enterprisedb.com/docs/en/9.3/pg/sql-security-label.html",
"http://www.arubanetworks.com/products/security/",
"http://cyfy.org/tag/security/",
"https://access.redhat.com/security/cve/",
"http://www.crypto.com",
"http://www2.schneider-electric.com/sites/corporate/en/support/cybersecurity/cybersecurity.page",
"http://www.govinfosecurity.com",
"http://www.wisegeek.com/what-is-tls.htm",
"http://www.governmentsecurity.org/",
"http://www.wired.com/category/threatlevel",
"http://www.austinfosec.com",
"http://www.wired.com/2014/11/hacker-lexicon-whats-dark-web/",
]

def crawler(threadName):
    global urls,i,start_time
    while (time.time() - start_time )< (60*5):
        # print urls
        url = urls[i]
        print "Started", i
        i+=1
        if url!="" and not ( url.startswith('http://') or url.startswith('https://') ):
            print "Nope"
        else:
            r  = requests.get(url)

            data = r.text
            filename = url.split("/")[-1] + '.html'
            with open(filename, 'wb') as f:
                f.write(data.encode('utf-8'))
            pass


            soup = BeautifulSoup(data,"lxml")

            for link in soup.find_all('a'):
                # if i>1:
                #     print(link.get('href'))
                links = link.get('href')
                urls.append(links)

class myThread (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        crawler(self.name)

for i in range(20):
    thread = myThread(1, i)
    thread.start()

# for i in range(20):
#     thread[i].start()
# thread2.start()
# try:
#    thread.start_new_thread( crawler, ("Thread-1", ) )
#    thread.start_new_thread( crawler, ("Thread-2",) )
# except:
#    print "Error: unable to start thread"

# while 1:
#    pass
