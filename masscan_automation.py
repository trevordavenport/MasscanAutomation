import os
import subprocess
import requests
import optparse
import shodan
from bs4 import BeautifulSoup

def print_results(host_info, service_summary):
    try:
        output = open('Masscan_Summary.txt', 'wb')
        output.write('MASSCAN AUTOMATION RESULTS\n__________________________\n')
        output.write('\n[*] Service Count\n')
        output.write('---------------------------------------\n')

        for k,v in service_summary.iteritems():
            output.write(k + ": ")
            output.write(str(v) + '\n')

        output.write('\n[*] Host Port Mapping\n')
        output.write('---------------------------------------\n')

        for k in host_dict.iterkeys():
            output.write("IP: " + k)
            output.write(" Ports: " + str(host_dict[k]) + '\n')    
        output.close()

    except Exception as e:
        print e

def vuln_management(results, api):
    try:
        #A dictionary containing the ports/ service_dict that Shodan crawls for.
        #Format: {'Port': service}
        service_dict  = api.service_dict()
        host_dict     = {} 
        service_count = {}
        soup          = BeautifulSoup(results, "lxml")

        #Convert Shodan's Unicode results to String
        service_dict = { str(key):value for key,value in service_dict.items() }

        #Collect Host Information
        for addr in soup.findAll('host'):
            host = str(addr.find('address')).split("\"")[1]
            port = str(addr.find('port')).split("\"")[1]
            temp_port_list = []
            temp_port_list.append(port)
            if host not in host_dict:
                host_dict[host] = temp_port_list
            else:
                host_dict[host] += temp_port_list

        #Keeping Count of Port & Service Instances
        for elems in host_dict.itervalues():
            port_list_len = len(elems)
            if port_list_len > 1:
                for vals in elems:
                    if str(vals) in service_dict:
                        service = service_dict[vals]
                        if service not in service_count:
                            service_count[str(service)] = 1
                        else:
                            service_count[str(service)] += 1
                    else:
                        if vals not in service_count:
                            service_count[str('Port ' + vals)] = 1
                        else:
                            service_count[str('Port ' + vals)] += 1
            elif elems[0] in service_dict:
                service = service_dict[elems[0]]
                if service not in service_count:
                    service_count[str(service)] = 1
                else:
                    service_count[str(service)] += 1
            else:
                if elems not in service_count:
                    service_count[str('Port ' + elems[0])] = 1
                else:
                    service_count[str('Port ' + elems[0]] += 1  
        if (host_dict and service_count):
            print_results(host_dict, service_count)

    except Exception as e:
        print e

def run_mass_scan(ip_address, API_KEY):
    try:
        MASS_SCAN = "./masscan " + ip_address + " -p 0-65535 --output-filename results.xml --rate 5000000"
        api       = shodan.Shodan(API_KEY)
        print "[*] Running Masscan "
        print "[+]" + "\" " + MASS_SCAN + "\""
        p = subprocess.Popen(MASS_SCAN, shell=True, stderr=subprocess.PIPE) #Improper/Insecure way to run this, time is not my friend, this hacky way will work
        (output, err) = p.communicate()

        if output:
            results = open('results.xml', 'r')
            if results:
                print "[*] ----- Scan Complete ----- "
                CURL = "curl -F nmap_xml=@results.xml \"https://scanhub.shodan.io/repository/upload/masscanautomation?key=" + API_KEY
                RET  = os.system(CURL)
                if (RET == 0):
                    print "[*] Pushing results.xml to scanhub.shodan.io/repo"
                else:
                    print "[+] Failed to Push results.xml onto scanhub. Check Stack Trace."
                vuln_management(results, api)
                results.close()
    except Exception as e:
        print e

def main():
    try:
        parser = optparse.OptionParser(usage='Usage: %prog [arguments]', version='%prog 1.0')
        parser.add_option('-i', '--ip', help='Argument Takes IP Address as Input')
        parser.add_option('-k', '--key', help='Argument Takes a Shodan API Key as Input')
        (options, args) = parser.parse_args()
        
        if options.ip != None and options.key != None:
            ip_addr = options.ip
            api_key = options.key
            run_mass_scan(ip_addr, api_key)

        elif options.ip == None or options.key == None:
            print "Error: Must provide two arguments."
            print "IP Address is in format: XXX.XXX.XXX.XXX/XX(optional) and also provide valid Shodan Key"
            parser.print_help()
    except Exception as e:
        print e

if __name__ == '__main__':
    main()
