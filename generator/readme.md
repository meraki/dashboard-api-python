# Generating the Meraki Dashboard API Python Library

Most users don't need this: just `pip install --upgrade meraki`, or a [published beta
release](https://github.com/meraki/dashboard-api-python#releases) for early-access operations.

Generate the library yourself only when you need it matched to your own org's spec. Follow along below.

> **NB:** The generator requires Python 3.11 or later.

1. Clone this repo locally.
2. Open a terminal in this `generator` folder.
3. Install dependencies using [uv](https://docs.astral.sh/uv/):

   ```shell
   uv sync --group generator
   ```

4. *Optional:* To work with beta operations, first [review the warnings and opt one of your orgs into the Early API
   Access program](https://community.meraki.com/t5/Developers-APIs/UPDATED-Beta-testing-with-the-Meraki-Developer-Early-Access/m-p/145344#M5808).
5. Run the generator:

   ```shell
   uv run --group generator python generate_library.py -v locally_generated -o YOUR_ORG_ID -k YOUR_API_KEY
   ```

   Making these replacements:
   * Replace `YOUR_ORG_ID` with the org ID you want to use as reference. Use the one opted into Early API access if you
     want the beta operations.
   * Replace `YOUR_API_KEY` with an API key that has org admin privileges on that org.
   * NB: Your local system may require minor syntax tweaks (e.g. Windows may require you prepend `generate_library.py`
     with `.\`)

6. You now have a `meraki` module folder inside `generator`. Copy it into any project that needs it.
7. If the official `meraki` package is also installed, your scripts may import it instead, and early-access calls will
   fail. Uninstall the official package (or replace it with the one you generated) to avoid this.
