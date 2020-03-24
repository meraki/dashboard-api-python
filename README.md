# Meraki Dashboard API Python Library

The new Meraki Dashboard API Python library provides all current Meraki [Dashboard API](https://api.meraki.com/api_docs) calls to interface with the Cisco Meraki cloud-managed platform. The library is supported on Python 3.6 or above, and you can install it via [PyPI](https://pypi.org/project/meraki/):

    pip install meraki

## Features

This library's goal is to refresh and supplant the legacy module (this repository versions 0.34 and prior) as well as the now-deprecated [SDK](https://github.com/meraki/meraki-python-sdk). Here are some of the features in this revamped library:

* Support for all API endpoints, as it uses the [OpenAPI specification](https://api.meraki.com/api/v0/openapiSpec) to generate source code
* Log all API requests made to a local file as well as on-screen console
* Automatic retries upon 429 rate limit errors, using the [`Retry-After` field](https://developer.cisco.com/meraki/api/#/rest/guides/rate-limit-errors) within response headers
* Get all (or a specified number of) pages of data with built-in pagination control
* Tweak settings such as the default base URL (for example, to use with V1 and/or mega-proxy)
* Simulate POST/PUT/DELETE calls to preview first, so that network configuration does not get changed
* Includes the legacy module's functions for backward compatibility

## Setup

1. Enable API access in your Meraki dashboard organization and obtain an API key ([instructions](https://documentation.meraki.com/zGeneral_Administration/Other_Topics/The_Cisco_Meraki_Dashboard_API))

2. Keep your API key safe and secure, as it is similar to a password for your dashboard. If publishing your Python code to a wider audience, please research secure handling of API keys.

3. Although the Meraki dashboard API, as a REST API, can be accessed in various ways, this library uses Python 3.6+. ([get started with Python](https://wiki.python.org/moin/BeginnersGuide/NonProgrammers))

4. After Python 3 is installed, use _pip_ (or an alternative such as _easy_install_) to install the library:
    * `pip install meraki`
    * If you have both Python3 and Python2 installed, you may need to use `pip3 install meraki`
    * If _meraki_ was previously installed, you can upgrade with `pip install --upgrade meraki` or `pip3 install --upgrade meraki`

## Usage
1. Export your API key as an [environment variable](https://www.twilio.com/blog/2017/01/how-to-set-environment-variables.html), for example:

    ```shell
    export MERAKI_DASHBOARD_API_KEY=093b24e85df15a3e66f1fc359f4c48493eaa1b73
    ```

2. Alternatively, define your API key as a variable in your source code; this method is not recommended due to its inherent insecurity.

3. Single line of code to import and use the library goes at the top of your script:

    ```python
    import meraki
    ```

4. Instantiate the client (API consumer class), optionally specifying any of the parameters available to set:

    ```python
    dashboard = meraki.DashboardAPI()
    ```

5. Make dashboard API calls in your source code, using the format _client.section.operation_, where _client_ is the name you defined in the previous step (**dashboard** above), _section_ is the corresponding group (or tag from the OpenAPI spec) from the [API docs](https://developer.cisco.com/meraki/api/#/rest), and _operation_ is the name (or operation ID from OpenAPI) of the API endpoint. For example, to make a call to get the list of organizations accessible by the API key defined in step 1, use this function call:

    ```python
    my_orgs = dashboard.organizations.getOrganizations()
    ```

6. If you were using this module versions 0.34 and prior, that file's functions are included in the _legacy.py_ file, and you can adapt your existing scripts by replacing their `from meraki import meraki` line to `import meraki`

### Examples
You can find fully working example scripts in the **examples** folder.

| Script              | Purpose                                                                                                                                                                                               |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **org_wide_clients.py** | That code collects the clients of all networks, in all orgs to which the key has access. No changes are made, since only GET endpoints are called, and the data is written to local CSV output files. |

## AsyncIO
**asyncio** is a library to write concurrent code using the **async/await** syntax. Special thanks to Heimo Stieg ([@coreGreenberet](https://github.com/coreGreenberet)) who has ported the API to asyncio.

The usage is similiar to the sequential version above. However it has has some differences.

1. Export your API key as an [environment variable](https://www.twilio.com/blog/2017/01/how-to-set-environment-variables.html), for example:

    ```shell
    export MERAKI_DASHBOARD_API_KEY=093b24e85df15a3e66f1fc359f4c48493eaa1b73
    ```

2. Alternatively, define your API key as a variable in your source code; this method is not recommended due to its inherent insecurity.

3. Single line of code to import and use the library goes at the top of your script:

    ```python
    import meraki.aio
    ```

4. Instantiate the client (API consumer class), optionally specifying any of the parameters available to set:

    ```python
    async with meraki.aio.AsyncDashboardAPI() as aiomeraki:
    ```
    The **async with** statement is important here to make sure, that the client sessions will be closed after using the api.

5. Make dashboard API calls in your source code, using the format await _client.section.operation_, where _client_ is the name you defined in the previous step (**aiomeraki** above), _section_ is the corresponding group (or tag from the OpenAPI spec) from the [API docs](https://developer.cisco.com/meraki/api/#/rest), and _operation_ is the name (or operation ID from OpenAPI) of the API endpoint. For example, to make a call to get the list of organizations accessible by the API key defined in step 1, use this function call:

    ```python
    my_orgs = await aiomeraki.organizations.getOrganizations()
    ```
6. Run everything inside an event loop.
```python
import asyncio

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(my_async_entry_point())
    
    # if you are using Python 3.7+ you can also simply 
    # use the following line instead of the two lines above
    asyncio.run(my_async_entry_point())
```


### Examples
You can find fully working example scripts in the **examples** folder.
| Script                  | Purpose                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **aio_org_wide_clients.py** | That code is a asyncio port from org_wide_clients.py and collects the clients of all networks, in all orgs to which the key has access. No changes are made, since only GET endpoints are called, and the data is written to local CSV output files.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **aio_ips2firewall.py**     |  That code will collect the source IP of security events and creates L7 firewall rules to block them. `usage: aio_ips2firewall.py [-h] -o ORGANIZATIONS [ORGANIZATIONS ...] [-f FILTER] [-s] [-d DAYS]` |
