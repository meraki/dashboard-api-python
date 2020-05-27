# Meraki Dashboard API Python Library

The Meraki Dashboard API Python library provides all current Meraki [Dashboard API](https://developer.cisco.com/docs/meraki-api-v1) calls to interface with the Cisco Meraki cloud-managed platform. The library is supported on Python 3.6 or above, and you can install it via [PyPI](https://pypi.org/project/meraki/):

    pip install meraki

## Features

While you can make direct HTTP requests to dashboard API in any programming language or REST API client, using a client library can make it easier for you to focus on your specific use case, without the overhead of having to write functions to handle the dashboard API calls. The Python library can also take care of error handling, logging, retries, and other convenient processes and options for you automatically.

* Support for all API endpoints, as it uses the [OpenAPI specification](https://api.meraki.com/api/v1/openapiSpec) to generate source code
* Log all API requests made to a local file as well as on-screen console
* Automatic retries upon 429 rate limit errors, using the [`Retry-After` field](https://developer.cisco.com/docs/meraki-api-v1/#!rate-limit) within response headers
* Get all (or a specified number of) pages of data with built-in pagination control
* Tweak settings such as maximum retries, certificate path, suppress logging, and other options
* Simulate POST/PUT/DELETE calls to preview first, so that network configuration does not get changed
* Includes the legacy module's (version 0.34 and prior) functions for backward compatibility

## Setup

1. Enable API access in your Meraki dashboard organization and obtain an API key ([instructions](https://documentation.meraki.com/zGeneral_Administration/Other_Topics/The_Cisco_Meraki_Dashboard_API))

2. Keep your API key safe and secure, as it is similar to a password for your dashboard. If publishing your Python code to a wider audience, please research secure handling of API keys.

3. Install the latest version of [Python 3](ttps://wiki.python.org/moin/BeginnersGuide/NonProgrammers)

4. Use _pip_ (or an alternative such as _easy_install_) to install the library from the Python [Package Index](https://pypi.org/project/meraki/):
    * `pip install meraki`
    * If you have both Python3 and Python2 installed, you may need to use `pip3` (so `pip3 install meraki`) along with `python3` on your system
    * If _meraki_ was previously installed, you can upgrade to the latest stable (non-beta) release with `pip install --upgrade meraki`

5. Meraki dashboard API v1 is currently in beta, so if you clone this repository and want to use v1 locally, rename the folder _meraki_v1_ to _meraki_, replacing the v0 contents there. You can also specify the version of the library when installing with _pip_:
    * See the full [release history](https://pypi.org/project/meraki/#history) to pick the version you want, or use `pip install meraki==` without including a version number to display the list of available versions
    * v0 versions of the Python library begin with _0_ (0.**x**.**y**), and v1 versions begin with _1_ (1.0.0b**z** for beta)
    * Specify the version you want with the install command; for example: `pip install meraki==0.x.y` for v0 or `pip install meraki==1.0.0bz` for v1 beta
    * You can also upgrade to the latest non-beta version with `pip install meraki --upgrade`

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

5. Make dashboard API calls in your source code, using the format _client.scope.operation_, where _client_ is the name you defined in the previous step (**dashboard** above), _scope_ is the corresponding scope that represents the first tag from the OpenAPI spec, and _operation_ is the operation of the API endpoint. For example, to make a call to get the list of organizations accessible by the API key defined in step 1, use this function call:

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
