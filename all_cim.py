import pywbem, json

# Make connection

conn = pywbem.WBEMConnection('https://10.32.16.15',     # url
                             ('superuser', 'passw0rd'), 'root/ibm')  # credentials
conn.no_verification = "true"
# Get all CIM_OperatingSystem instances

names = conn.EnumerateInstanceNames('IBMTSSVC_Cluster')

# Call GetInstance on returned instances
f = open('text.txt', 'w')
for n in names:
    
    os = conn.GetInstance(n)
    
    
    for key, value in os.items():
        print '%s = %s' % (key, value)

        # f.write(('%s = %s' % (key, value)) + '\n')
    

