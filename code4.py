
resources = [
    {"id": "R001", "name": "Laptop", "category": "Electronics", "total": 10, "available": 10},
    {"id": "R002", "name": "Keyboard", "category": "Accessories", "total": 5, "available": 5},
    {"id": "R003", "name": "Headset", "category": "Accessories", "total": 3, "available": 3}
]

fellows = {"F001": "Ada", "F002": "John", "F003": "Grace"}
borrow_records = []


def find_resource(resource_id):
    for resource in resources:
        if resource["id"] == resource_id:
            return resource
    return None


def add_resource(resource_id, name, category, total):
    if find_resource(resource_id):
        print("Error: Resource ID already exists.")
        return False

    if total <= 0:
        print("Error: Total units must be positive.")
        return False

    resources.append({
        "id": resource_id,
        "name": name,
        "category": category,
        "total": total,
        "available": total
    })

    print("Resource added successfully.")
    return True


def list_resources():
    for resource in resources:
        print(
            f'{resource["id"]}: {resource["name"]} | '
            f'{resource["category"]} | '
            f'Total: {resource["total"]} | '
            f'Available: {resource["available"]}'
        )


def borrow_resource(fellow_id, resource_id, quantity):
    if fellow_id not in fellows:
        print("Rejected: Invalid fellow ID.")
        return False

    resource = find_resource(resource_id)

    if resource is None:
        print("Rejected: Invalid resource ID.")
        return False

    if not isinstance(quantity, int) or isinstance(quantity, bool) or quantity <= 0:
        print("Rejected: Quantity must be a positive integer.")
        return False

    if quantity > resource["available"]:
        print("Rejected: Not enough stock.")
        return False

    resource["available"] -= quantity

    borrow_records.append({
        "fellow_id": fellow_id,
        "resource_id": resource_id,
        "quantity": quantity
    })

    print(
        f"Success: {fellows[fellow_id]} borrowed "
        f"{quantity} {resource['name']}(s)."
    )

    return True


def return_resource(fellow_id, resource_id, quantity):
    if fellow_id not in fellows:
        print("Rejected: Invalid fellow ID.")
        return False

    resource = find_resource(resource_id)

    if resource is None:
        print("Rejected: Invalid resource ID.")
        return False

    if not isinstance(quantity, int) or isinstance(quantity, bool) or quantity <= 0:
        print("Rejected: Quantity must be a positive integer.")
        return False

    borrowed = 0

    for record in borrow_records:
        if (
            record["fellow_id"] == fellow_id
            and record["resource_id"] == resource_id
        ):
            borrowed += record["quantity"]

    if quantity > borrowed:
        print("Rejected: Fellow does not have that many units on loan.")
        return False

    remaining = quantity

    for record in borrow_records:
        if remaining == 0:
            break

        if (
            record["fellow_id"] == fellow_id
            and record["resource_id"] == resource_id
        ):
            amount = min(record["quantity"], remaining)
            record["quantity"] -= amount
            remaining -= amount

    borrow_records[:] = [
        record for record in borrow_records
        if record["quantity"] > 0
    ]

    resource["available"] += quantity

    print(
        f"Success: {fellows[fellow_id]} returned "
        f"{quantity} {resource['name']}(s)."
    )

    return True


def search_resources(name):
    matches = [
        resource for resource in resources
        if name.lower() in resource["name"].lower()
    ]

    if matches:
        for resource in matches:
            print(f'Found: {resource["name"]} ({resource["id"]})')
    else:
        print("No matching resources found.")


def filter_by_category(category):
    matches = [
        resource for resource in resources
        if resource["category"].lower() == category.lower()
    ]

    if matches:
        for resource in matches:
            print(f'{resource["name"]} ({resource["id"]})')
    else:
        print("No resources found in this category.")


def report():
    total_units = sum(resource["total"] for resource in resources)
    available_units = sum(resource["available"] for resource in resources)
    borrowed_units = total_units - available_units

    low_stock = [
        resource["name"]
        for resource in resources
        if resource["available"] < 3
    ]

    borrowed_by_resource = {}

    for record in borrow_records:
        borrowed_by_resource[record["resource_id"]] = (
            borrowed_by_resource.get(record["resource_id"], 0)
            + record["quantity"]
        )

    max_borrowed = max(borrowed_by_resource.values(), default=0)

    leaders = [
        resource["name"]
        for resource in resources
        if borrowed_by_resource.get(resource["id"], 0) == max_borrowed
        and max_borrowed > 0
    ]

    print("\n--- REPORT ---")
    print(f"Overall units: {total_units}")
    print(f"Available units: {available_units}")
    print(f"Borrowed units: {borrowed_units}")
    print(
        f"Low stock (<3): "
        f"{', '.join(low_stock) if low_stock else 'None'}"
    )
    print(
        f"Most borrowed: {', '.join(leaders)} "
        f"({max_borrowed} units)"
    )


def main():
    while True:
        print("\n1. Add resource")
        print("2. List resources")
        print("3. Borrow resource")
        print("4. Return resource")
        print("5. Search resource")
        print("6. Filter by category")
        print("7. Generate report")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            resource_id = input("Resource ID: ")
            name = input("Name: ")
            category = input("Category: ")

            try:
                total = int(input("Total units: "))
                add_resource(resource_id, name, category, total)
            except ValueError:
                print("Error: Total units must be a number.")

        elif choice == "2":
            list_resources()

        elif choice == "3":
            fellow_id = input("Fellow ID: ")
            resource_id = input("Resource ID: ")

            try:
                quantity = int(input("Quantity: "))
                borrow_resource(fellow_id, resource_id, quantity)
            except ValueError:
                print("Rejected: Quantity must be a positive integer.")

        elif choice == "4":
            fellow_id = input("Fellow ID: ")
            resource_id = input("Resource ID: ")

            try:
                quantity = int(input("Quantity: "))
                return_resource(fellow_id, resource_id, quantity)
            except ValueError:
                print("Rejected: Quantity must be a positive integer.")

        elif choice == "5":
            name = input("Search name: ")
            search_resources(name)

        elif choice == "6":
            category = input("Category: ")
            filter_by_category(category)

        elif choice == "7":
            report()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose from the menu.")


if __name__ == "__main__":
    main()