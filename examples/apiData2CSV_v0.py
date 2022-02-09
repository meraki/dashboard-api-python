import csv
from datetime import datetime
import os
import json
import argparse
import sys

import meraki

import urllib.parse
import platform

# This example pulls API calls from the passed in org_id from the last timespan
# seconds, where the default timespan is 900 (hint 24 hours = 3600 seconds) and
# generates a CSV file with the data.
#
# Either input your API key below by uncommenting line 10 and changing line 16 to api_key=API_KEY,
# or set an environment variable (preferred) to define your API key. The former is insecure and not recommended.
# For example, in Linux/macOS:  export MERAKI_DASHBOARD_API_KEY=093b24e85df15a3e66f1fc359f4c48493eaa1b73
# API_KEY = '093b24e85df15a3e66f1fc359f4c48493eaa1b73'
#
# Optionally, Cisco partners can set their BE GEO ID by using export BE_GEO_ID=XXXXXX
# where XXXXX is a valid BE GEO ID.  This is used for metrics collection.
#
# Optionally, a calling application can be set by using export MERAKI_PYTHON_SDK_CALLER=YYYYY
# where YYYYY is a string identifying the application, script, or whatever piece of code
# is callig the Meraki Python SDK


def main(org_id, timespan):
    # Instantiate a Meraki dashboard API session
    dashboard = meraki.DashboardAPI(
        base_url='https://api.meraki.com/api/v0/',
        print_console=False,
        output_log=False,
    )

    # Get list of API usage data and start the output csv string
    apiUsage = dashboard.api_usage.getOrganizationApiRequests(org_id, timespan=timespan, total_pages=-1)
    csvString = 'method,host,path,queryString,tsDate,tsTime,responseCode,sourceIp,userAgent,'
    csvString += 'implementation,implementationVersion,distro,distroVersion,system,systemRelease,'
    csvString += 'cpu,be_geo_id,caller\r\n'
    cumulativeAPIcalls = 0;
    for use in apiUsage:
        csvString += use['method'] + ','
        csvString += use['host'] + ','
        csvString += use['path'] + ','
        csvString += use['queryString'] + ','
        csvString += use['ts'].split('T')[0] + ','
        csvString += use['ts'].split('T')[1].replace('Z','') + ','
        csvString += str(use['responseCode']) + ','
        csvString += use['sourceIp'] + ','

        # Special  User-Agent processing
        if 'python-meraki' in use['userAgent']:
            print(use['userAgent'])
            userAgent = use['userAgent'].split(' ')
            csvString += userAgent[0] + ','
            if len(userAgent) > 1:
                if "implementation" in userAgent[1]:
                    userAgentDict = json.loads(urllib.parse.unquote(userAgent[1]))
                    if "implementation" in userAgentDict:
                        csvString += userAgentDict['implementation']['name'] + ','
                        csvString += userAgentDict['implementation']['version'] + ','
                    else:
                        csvString += ',,'
                    if "distro" in userAgentDict:
                        csvString += userAgentDict['distro']['name'] + ','
                        csvString += userAgentDict['distro']['version'] + ','
                    else:
                        csvString += ',,'
                    if "system" in userAgentDict:
                        csvString += userAgentDict['system']['name'] + ','
                        csvString += userAgentDict['system']['release'] + ','
                    else:
                        csvString += ',,'
                    if "cpu" in userAgentDict:
                        csvString += userAgentDict['cpu'] + ','
                    else:
                        csvString += ','
                    if "be_geo_id" in userAgentDict:
                        csvString += userAgentDict['be_geo_id'] + ','
                    else:
                        csvString += ','
                    if "application" in userAgentDict:
                        csvString += userAgentDict['application'] + ','
                    elif "caller" in userAgentDict:
                        csvString += userAgentDict['caller'] + ','
                    else:
                        csvString += ','
                else:
                    csvString += ',,,,,,,,,'
            else:
                csvString += ',,,,,,,,,'
        else:
            csvString += use['userAgent']+ ','
            csvString += ',,,,,,,,,'

        csvString += '\r\n'

    # Output the file
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d_%H-%M-%S")
    filename = org_id + '_' + str(timespan) + '_' + dt_string + '.csv'
    file = open(filename, 'w')
    file.write(csvString)
    file.close()
    print('Results written to ' + filename)

if __name__ == '__main__':
    # First check for API key
    if "MERAKI_DASHBOARD_API_KEY" not in os.environ:
        print('You must set the MERAKI_DASHBOARD_API_KEY variable')
        sys.exit()

    # Now check arguments
    parser = argparse.ArgumentParser(description='Generate a CSV file of Meraki API activity for an organization.')
    parser.add_argument('org_id', help='Organization id to pull API activity from')
    parser.add_argument('--timespan', type=int, default=900,
                        help='The timespan (in seconds) for which the information will be fetched.  Default = 900 (15 mins)')
    args = parser.parse_args()
    print('About to run with org_id: ' + args.org_id + ' and timespan: ' + str(args.timespan))

    # Finally, let's roll
    start_time = datetime.now()
    main(args.org_id, args.timespan)
    end_time = datetime.now()
    print(f'\nScript complete, total runtime {end_time - start_time}')
