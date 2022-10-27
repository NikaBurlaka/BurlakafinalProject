import requests
import json

def test_authorization_check():
  url = "https://dev.ddso-spot.quantori.com/api/authorization/me"
  payload = {}
  headers = { 'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJkOGEwNTM4YmEwMTQzYjBkMGRlZDNmZjYyZTExYjY5NjExZmRiZDFiMjZkNjNjNjFlYzRhM2IzNmVkMGFmM2RkIiwiaWF0IjoxNjY0ODExMDU1LCJuYmYiOjE2NjQ4MTEwNTUsImp0aSI6ImU2MTQyNWEyLTgxN2QtNDliZC04YTU3LWVlNTBlMWUzNzcwMiIsImV4cCI6MTY2NDgzOTg1NSwidHlwZSI6ImFjY2VzcyIsImZyZXNoIjpmYWxzZSwiY3NyZiI6IjBlMjE3YTY3LTQzZDgtNDk0NC04NmNmLTcwMDVjMWUxYzllMSJ9.nK2Y04liUvPpbPPHiGXy67L2U0XxTYRuBswAmjdc7X4	',
              'X-CSRF-REFRESH-TOKEN': '174dc936-dc6c-41e2-939f-cf2f19bbe732'

  }
  response = requests.request("GET", url, headers=headers, data=payload)
  assert response.status_code == 200

def test_get_user_guide_has_pdf_format():

  url = "https://dev.ddso-spot.quantori.com/api/static/user-guide"
  payload = {}
  headers = {
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJkOGEwNTM4YmEwMTQzYjBkMGRlZDNmZjYyZTExYjY5NjExZmRiZDFiMjZkNjNjNjFlYzRhM2IzNmVkMGFmM2RkIiwiaWF0IjoxNjY1Njc3NzY0LCJuYmYiOjE2NjU2Nzc3NjQsImp0aSI6ImU5ZjJhOGUxLTA4YTUtNDJhYy04YmViLWRiMDBiMjQ1MjI3NSIsImV4cCI6MTY2NTcwNjU2NCwidHlwZSI6ImFjY2VzcyIsImZyZXNoIjpmYWxzZSwiY3NyZiI6ImY4ODIyNWE1LWIyNWItNDIwZC1iODFlLTczMmE2M2VmMzFlNiJ9.qmFKvaeDlWYi3uDG-4zcg9YNzjjHZNTzKmDIy0lK3EY'
  }

  response = requests.request("GET", url, headers=headers, data=payload)
  assert response.headers['Content-type'] == 'application/pdf'




