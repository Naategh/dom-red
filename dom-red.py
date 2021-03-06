#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import sys
import urllib3
import argparse 

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

RED = "\033[91m"
BLUE = "\033[36m"
WHITE = '\033[37m'
END = "\033[0m"

def banner():
    print("""
________                       ________     _________
___  __ \____________ ___      ___  __ \__________  /
__  / / /  __ \_  __ `__ \     __  /_/ /  _ \  __  / 
_  /_/ // /_/ /  / / / / /     _  _, _//  __/ /_/ /  
/_____/ \____//_/ /_/ /_/      /_/ |_| \___/\__,_/   
                
                Author {}::{} Naategh                                                     
""".format(RED, END))


def main():

    with open(file) as f:
        print("")
        
        for line in f:
            with open(payloads) as p:
                for payload in p:
                    try:
                        line2 = line.strip()

                        if 'http://' in line2:
                            pass
                        elif 'https://' in line2:
                            pass
                        else:
                            line2 = 'http://' + line2

                        if args.include:
                            URL = line2 + "/" + payload
                        else:
                            URL = line2 + payload

                        response = requests.get(URL, verify=False, timeout=5)
                        if args.verbose:                     
                            print(URL.replace("\n", "") + RED + " ++> " + str(response.status_code) + "\n" + END)
                        else:
                            pass

                        try:
                            if response.history and not str(response.url).startswith(line2):

                                for resp in response.history:

                                    print("Redirect Found: " + WHITE +  resp.url + END)
                                    
                                print("Final Destination: " + BLUE + response.url + "\n" + END)
                                if output:
                                    res.write(resp.url + " ++> " + response.url + "\n\n")
                            else:
                                pass
                        except Exception as e:
                            print("Connection Error: ", e)

                    except requests.exceptions.RequestException:
                        print(RED + "Requests error: " + URL + "\nContinue...\n" + END)
                        continue

                    except KeyboardInterrupt:
                        print(RED + "Shutdown..." + END)
                        exit(0)

if __name__ == '__main__':
    banner()
    parser = argparse.ArgumentParser()

    parser.add_argument('-d', '--domain', help='Path of domains list', required=True)
    parser.add_argument('-p', '--payload', help='Path of payloads list', required=True)
    parser.add_argument('-i', '--include', help="Include a slash at end of URLs", action='store_true')
    parser.add_argument('-v', '--verbose', help="Show more results", action="store_true")
    parser.add_argument('-o', '--output', help="Output file, ex: res.txt")
    
    args = parser.parse_args()
    file = args.domain
    payloads = args.payload
    output = args.output
    if output:
        res = open(output, "a+")
    
    main()


