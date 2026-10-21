import json

ticket = [
    {"id": "1", "name": "favour", "tittle": "wifi", "status": "open"},
    {"id": "2", "name": "dorcas", "tittle": "keyboard", "status": "in_progress"},
    {"id": "3", "name": "juliet", "tittle": "server", "status": "resolved"},
]

with open("ticket.json", "w") as f:
    json.dump(ticket, f, indent=2)