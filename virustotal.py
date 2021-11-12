from hashlib import md5
from virus_total_apis import PublicApi

def total(args):
    API_KEY = "0b0ee841de83cfe9a05232f3a7d820e724babb33283ac182567cf988fad4bd99"
    api = PublicApi(API_KEY)
    with open(str(args.x), "rb") as f:
        file_hash = md5(f.read()).hexdigest()
    response = api.get_file_report(file_hash)
    response1= api.scan_file(args.x)

    if response["response_code"] == 200:
        if response["results"]["positives"] > 0:
            print("Archivo malicioso.")
        else:
            print("Archivo seguro.")
    else:
        print("No ha podido obtenerse el análisis del archivo.")