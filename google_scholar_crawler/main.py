from scholarly import scholarly
import jsonpickle
import json
from datetime import datetime
import os

print("Step 1: starting...", flush=True)

scholar_id = os.environ['GOOGLE_SCHOLAR_ID']
print(f"Step 2: GOOGLE_SCHOLAR_ID loaded: {scholar_id}", flush=True)

print("Step 3: search_author_id starting...", flush=True)
author: dict = scholarly.search_author_id(scholar_id)
print("Step 4: search_author_id finished", flush=True)

print("Step 5: scholarly.fill starting...", flush=True)
scholarly.fill(
    author,
    sections=['basics', 'indices', 'counts', 'publications']
)
print("Step 6: scholarly.fill finished", flush=True)

name = author['name']
author['updated'] = str(datetime.now())
author['publications'] = {
    v['author_pub_id']: v for v in author['publications']
}

print(json.dumps(author, indent=2), flush=True)

os.makedirs('results', exist_ok=True)

with open('results/gs_data.json', 'w') as outfile:
    json.dump(author, outfile, ensure_ascii=False)

shieldio_data = {
    "schemaVersion": 1,
    "label": "citations",
    "message": f"{author['citedby']}",
}

with open('results/gs_data_shieldsio.json', 'w') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)

print("Done!", flush=True)
