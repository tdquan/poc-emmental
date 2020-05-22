import urllib.parse
import os
import requests

AIRTABLE_API_URL = 'https://api.airtable.com/v0'
AIRTABLE_TOKEN = os.environ.get('AIRTABLE_TOKEN')


def request_airtable_rows(
        base_id,
        table_name,
        filter_by_formula=None,
        max_records=None,
        token=AIRTABLE_TOKEN
):
    url = '{}/{}/{}?view=Grid%20view'.format(
        AIRTABLE_API_URL,
        base_id,
        urllib.parse.quote(table_name, safe='')
    )

    if filter_by_formula:
        url = '{}&filterByFormula={}'.format(
            url,
            urllib.parse.quote(filter_by_formula)
        )

    if max_records:
        url = '{}&maxRecords={}'.format(url, max_records)

    headers = {'Authorization': 'Bearer {}'.format(token)}

    result = requests.get(url, headers=headers).json()
    records = result['records']
    offset = result.get('offset')
    while offset:
        url_with_offset = '{}&offset={}'.format(url, offset)
        result = requests.get(url_with_offset, headers=headers).json()
        offset = result.get('offset')
        records += result['records']

    return [
        {'airtableId': record['id'], **record['fields']}
        for (index, record) in enumerate(records)
    ]
