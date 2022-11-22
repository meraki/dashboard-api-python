# Generating the Meraki Dashboard API Python Library

1. Clone this repo locally.
2. Open a terminal in this `generator` folder.
3. [Review the warnings, then opt one of your orgs into the Early API Access program](https://community.meraki.com/t5/Developers-APIs/UPDATED-Beta-testing-with-the-Meraki-Developer-Early-Access/m-p/145344#M5808). 
4. Run `python generate_library.py -v locally_generated_beta -o YOUR_BETA_ORG_ID -k YOUR_API_KEY` making these replacements:
* Replace `YOUR_BETA_ORG_ID` with the org ID you opted into Early API access
* Replace `YOUR_API_KEY` with an API key that has org admin privileges on that beta org.
* NB: Your local system may require minor syntax tweaks (e.g. Windows may require you prepend `generate_library.py` with `.\`)
5. You will now have a `meraki` module folder inside `generator`, which you can locally reference in your scripts. Simply copy the `meraki` folder to those projects which require it.
6. In some cases, if you've already installed the official library, your scripts may prefer that one over the local folder. If that happens, then calls to early access endpoints will fail. So, if necessary, uninstall any instances of the meraki package that may have been installed in your venv or system, or replace the version installed in your venv with that which you generated here.
