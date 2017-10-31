Python 3.6 module providing all current Meraki [Dashboard API](https://dashboard.meraki.com/api_docs) calls to interface with the Cisco Meraki cloud-managed IT solutions.
Also available via [PIP](https://pypi.python.org/pypi/meraki/).


## Initial Setup
* Enable APIs in your Meraki dashboard and obtain an APIKey: [Instructions](https://documentation.meraki.com/zGeneral_Administration/Other_Topics/The_Cisco_Meraki_Dashboard_API) 
  * Keep your APIKey safe and secure.  It is similar to a password for your dashboard.  If publishing your Python programs to a wider audience, please research secure handling of APIKeys.
* Although the Meraki API can be accessed in various ways, this module uses Python3.  [Get started with Python](https://wiki.python.org/moin/BeginnersGuide/NonProgrammers)
* After Python is installed, prepare your environment:
  * Use pip (or alternative such as easy_install) to install required packages:
    * pip install requests
  * Download merakiapi.py above and place it in your desired folder
* You are now ready to create your first script:
  * create a new file and name it with python extension, e.g., meraki_hello_world.py
  * import the meraki api into your script, e.g.,  import merakiapi as m
  * use the meraki API to interact with your dashboard
  
## Example

```python
import merakiapi as m

apikey = "jkhsfsdhk32424******example*****jlasdfsdfl3245345"
myOrgs = m.myorgaccess(apikey)
print(myOrgs)
```

## Useful API calls to get started

```python
myNetworks = m.getnetworklist(apikey, orgid)
deviceList = m.getnetworkdevices(apikey, networkid)
clientList = m.getclients(apikey,serialnum)
```
