# Generating the Meraki Dashboard API Python Library

Generally speaking, you will not need to generate this yourself. Simply use the official PyPI package
via `pip install --update meraki`.

However, if you participate in Early Access features, you may want to generate a library to match your org's spec. In
which case, follow along.

> **NB:** The generator requires Python 3.10 or later.

1. Clone this repo locally.
2. Open a terminal in this `generator` folder.
3. *Optional:* If you want to work with beta endpoints, then
   first [review the warnings, and then opt one of your orgs into the Early API Access program](https://community.meraki.com/t5/Developers-APIs/UPDATED-Beta-testing-with-the-Meraki-Developer-Early-Access/m-p/145344#M5808).
4. Run `python generate_library.py -v locally_generated -o YOUR_ORG_ID -k YOUR_API_KEY` making these replacements:

* Replace `YOUR_ORG_ID` with the org ID you want to use as reference. Use the one opted into Early API access if you
  want the beta endpoints.
* Replace `YOUR_API_KEY` with an API key that has org admin privileges on that org.
* NB: Your local system may require minor syntax tweaks (e.g. Windows may require you prepend `generate_library.py`
  with `.\`)

5. You will now have a `meraki` module folder inside `generator`, which you can locally reference in your scripts.
   Simply copy the `meraki` folder to those projects which require it.
6. In some cases, if you've already installed the official library, your scripts may prefer that one over the local
   folder. If that happens, then calls to early access endpoints will fail. So, if necessary, uninstall any instances of
   the meraki package that may have been installed in your venv or system, or replace the version installed in your venv
   with that which you generated here.
