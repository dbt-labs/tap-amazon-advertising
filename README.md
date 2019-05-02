# tap-amazon-advertising

Author: Drew Banin (drew@fishtownanalytics.com)

This is a [Singer](http://singer.io) tap that produces JSON-formatted data following the [Singer spec](https://github.com/singer-io/getting-started/blob/master/SPEC.md).

It:

- Generates a catalog of available data in the Amazon Advertising API
- Extracts the following resources:
    - portfolios
    - profiles
    - ad groups
    - ad groups: biddable keywords
    - ad groups: negative keywords
    - campaigns:
    - campaigns: negative keywords
    - product ads
    - sponsored products report: product ads
    - sponsored brands report: ad groups
    - sponsored brands report: campaigns
    - sponsored brands report: keywords

### Quick Start

1. Install

```bash
git clone git@github.com:fishtown-analytics/tap-amazon-advertising.git
cd tap-amazon-advertising
pip install .
```

2. Get credentials from Amazon

In addition to a client id and secret, you'll also need to obtain a refresh token for an authorized amazon advertising user. This can be accomplished by
running the `get_refresh_token.py` script located in the root of this repository.

3. Create the config file.

There is a template you can use at `config.json.example`, just copy it to `config.json` in the repo root and insert your credentials.

4. Run the application to generate a catalog.

```bash
tap-amazon-advertising -c config.json --discover > catalog.json
```

5. Select the tables you'd like to replicate

Step 4 a file called `catalog.json` that specifies all the available endpoints and fields. You'll need to open the file and select the ones you'd like to replicate. See the [Singer guide on Catalog Format](https://github.com/singer-io/getting-started/blob/c3de2a10e10164689ddd6f24fee7289184682c1f/BEST_PRACTICES.md#catalog-format) for more information on how tables are selected.

6. Run it!

```bash
tap-amazon-advertising -c config.json --catalog catalog.json
```

Copyright &copy; 2019 Fishtown Analytics
