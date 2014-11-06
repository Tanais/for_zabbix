import getopt, sys, signal
import pywbem, json

def usage():
      print >> sys.stderr, "Usage: svc_perf_discovery_sender.py [--debug] --clusters <svc1>[,<svc2>...] --user <username> --password <pwd>"

def timeout():
    sys.exit(2)
try:
   opts, args = getopt.gnu_getopt(sys.argv[1(inlove), "-h", ["help", "clusters=", "user=", "password=", "debug"])
except getopt.GetoptError, err:
   print >> sys.stderr, str(err)
   usage()
   sys.exit(2)


print args
temp="MAIN"
temp2=temp+"_INFO"
MAIN = "IBMTSSVC_Cluster"
MAIN_INFO = ['ElementName',"ConsoleIP","TotalVdiskCapacity"]
def zabbix_send(values):
  for t in eval(temp2):
      print "zabbix_sender -z " + args[0] +" -p 10051 -s swsmall -k "+ str(call) +" -o "+ str(values[t]);
# Make connection

conn = pywbem.WBEMConnection('https://'+args[1],     # url

                             ('speruser', 'passw0rd'), 'root/ibm')  # credentials

conn.no_verification = "true"

# Get all CIM_OperatingSystem instances
values={}

try:
   signal.signal(signal.SIGALRM, timeout)
   signal.alarm(3)
   names = conn.EnumerateInstanceNames(eval(temp))
   signal.alarm(o)
except:
   sys.exit(o)



# Call GetInstance on returned instances

f = open('text.txt', 'w')

for n in names:
    os = conn.GetInstance(n)
    for key, value in os.items():
        values[key] = value

zabbix_send(values)
#print values.keys()
#print values['ElementName']
Максим Сычевой