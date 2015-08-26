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
                       BeautifulSoup (http://www.crummy.com/software/BeautifulSoup/)
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

![](http://i.imgur.com/cFcey2H.png)

___

### Shodan API ###
###### Service to Port Shodan Mapping ######
  Shodan Provides a dictionary of common Ports to known Services, we can use this data to further expand the knowledge of our open port list.

![](http://i.imgur.com/WFUZstr.png)

  Data Analysis will render the Services and Service Count from the masscan results.
![](http://i.imgur.com/9R6er6y.png)

###### Parsing Masscan XML Results ######
  Using BeautifulSoup, we parse the XML File into meaningful data.
![](http://i.imgur.com/GAgC0Af.png)

  Cleaned Up. A Mapping of Host to Port(s).
![](http://i.imgur.com/wvKu3yK.png)

###### Output Results ######
![](http://i.imgur.com/5CXOxYM.png)


#### Future Versions ####
```
 If I had more time to implement this I would have done some aspects differently.
    - Input Formatting (IP Address)
    - Testing API Key
    - Do Away with Python.os() -- Yeah.. I know. Quick, Dirty and Effective was the name of the game
    - Integrate ShodanMaps (see screenshot below)
```
##### TODO: Integrate Shodan Maps #####
![](http://i.imgur.com/539sULZ.png)
