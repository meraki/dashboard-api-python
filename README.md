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

## Usage
1. Export your API key as an [environment variable](https://www.twilio.com/blog/2017/01/how-to-set-environment-variables.html), for example:

    `export MERAKI_DASHBOARD_API_KEY=093b24e85df15a3e66f1fc359f4c48493eaa1b73`

2. Alternatively, define your API key as a variable in your source code; this method is not recommended due to its inherent insecurity.

3. Single line of code to import and use the library goes at the top of your script:

    `import meraki`

4. Instantiate the client (API consumer class), optionally specifying any of the parameters available to set:

    `dashboard = meraki.DashboardAPI()`

5. Make dashboard API calls in your source code, using the format _client.section.operation_, where _client_ is the name you defined in the previous step (**dashboard** above), _section_ is the corresponding group (or tag from the OpenAPI spec) from the [API docs](https://developer.cisco.com/meraki/api/#/rest), and _operation_ is the name (or operation ID from OpenAPI) of the API endpoint. For example, to make a call to get the list of organizations accessible by the API key defined in step 1, use this function call:

    `my_orgs = dashboard.organizations.getOrganizations()`


For a full working script that demos this library, please see and run the **org_wide_clients.py** file included (in **examples** folder). That code collects the clients of all networks, in all orgs to which the key has access. No changes are made, since only GET endpoints are called, and the data is written to local CSV output files.
