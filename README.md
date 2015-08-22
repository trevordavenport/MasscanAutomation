Masscan + Shodan Automation
===========================
> Integrating Masscan port scanner with Shodan API using Python

```
Author: Trevor Davenport
```

#### Background ####
```
  Masscan Port Scanner: https://github.com/robertdavidgraham/masscan
  Masscan Man Page:     http://manpages.ubuntu.com/manpages/vivid/man8/masscan.8.html
  
  Python Dependencies: Requests (http://www.python-requests.org/en/latest/)
                       Simplejson (https://simplejson.readthedocs.org/en/latest/)
                       Shodan API (https://shodan.readthedocs.org/en/latest/)
```
___

#### Overview ####
```
 1  [*] Masscan initiates port scan
 2   [*] Results are generated in XML output
 3    [*] Output is pushed to scanhub.shodan.io/repo
 4     [*] Data Analysis for Security/Vulnerability Management
```
___

#### Usage ####

![](http://i.imgur.com/ixgwvDW.png)
