[![Gitter chat](https://img.shields.io/badge/gitter-join%20chat-brightgreen.svg)](https://gitter.im/CiscoSecurity/Threat-Grid "Gitter chat")

### Threat Grid API Basics:

This collection of scripts cover the basics of interacting with the Threat Grid API. Each script covers one API endpoint. These are intented to show the bare minimum required to interact with the API endpoint.

### Before using you must update the following:
- api_key

### Usage:
```
python 01_authentication.py
```

### Example script output:
```
{'api_version': 3, 'id': 5510618, 'data': {'role': 'user', 'properties': {}, 'integration_id': 'h7od', 'email': 'jdoe@example.com', 'organization_id': 1, 'name': 'John Doe', 'login': 'jdoe', 'title': 'SOC Analyst', 'api_key': 'asdf1234asdf1234asdf1234', 'device': False}}
```
