import json

tickets = []

title = input("Enter ticket title: ")
description = input("Enter ticket description: ")

if title.strip() == "" or description.strip() == "":
    print("Title and description cannot be empty.")
else:
    ticket = {
        "id": "T001",
        "title": title,
        "description": description
    }

    tickets.append(ticket)

    with open("tickets.json", "w") as file:
        json.dump(tickets, file, indent=4)

    print("Ticket created successfully!")