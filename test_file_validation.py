import requests
import json

def test_file_upload_after_receiving_credetials():
    url = "https://dev.ddso-spot.quantori.com/api/upload/datasets/upload_params?filename=1compound.csv"
    payload = {}
    headers = {
            'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJkOGEwNTM4YmEwMTQzYjBkMGRlZDNmZjYyZTExYjY5NjExZmRiZDFiMjZkNjNjNjFlYzRhM2IzNmVkMGFmM2RkIiwiaWF0IjoxNjY1Njc3NzY0LCJuYmYiOjE2NjU2Nzc3NjQsImp0aSI6ImU5ZjJhOGUxLTA4YTUtNDJhYy04YmViLWRiMDBiMjQ1MjI3NSIsImV4cCI6MTY2NTcwNjU2NCwidHlwZSI6ImFjY2VzcyIsImZyZXNoIjpmYWxzZSwiY3NyZiI6ImY4ODIyNWE1LWIyNWItNDIwZC1iODFlLTczMmE2M2VmMzFlNiJ9.qmFKvaeDlWYi3uDG-4zcg9YNzjjHZNTzKmDIy0lK3EY',
            'X-CSRF-REFRESH-TOKEN': '8a5b7507-33d3-4b2c-8fd7-855ecc803434'
        }
    response = requests.request("GET", url, headers=headers, data=payload)
    received_response_creds = json.loads(response.text)
    amazon_url = received_response_creds['data']['url']
    key = received_response_creds['data']['fields']['key']
    amazon_algorithm = received_response_creds['data']['fields']['x-amz-algorithm']
    amazon_credential = received_response_creds['data']['fields']['x-amz-credential']
    amazon_date = received_response_creds['data']['fields']['x-amz-date']
    policy = received_response_creds['data']['fields']['policy']
    amazon_signature = received_response_creds['data']['fields']['x-amz-signature']
    print(amazon_url, amazon_credential)
    payload_for_upload = {"key":key, "x-amz-algorithm": amazon_algorithm, "x-amz-credential":amazon_credential,"x-amz-date":amazon_date,"policy": policy, "X-amz-signature":amazon_signature}
    my_file = open('venv/test_files/1compound.csv', 'rb')
    files = {'file': ('1compound.csv', my_file, "text/csv")}
    upload = requests.post(amazon_url, data=payload_for_upload, files = files)
    assert upload.status_code == 204

