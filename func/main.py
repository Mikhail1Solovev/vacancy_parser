import json

def load_data():
    with open('../operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def mask_card(operation):
    if 'from' in operation:
        operation["from"] = operation["from"].split()[-1][:4] + ' **** **** ' + operation["from"][-4:]
    return operation

def mask_account_number(operation):
    if 'to' in operation:
        operation["to"] = operation["to"].split()[-1][:4] + ' **** **** ' + operation["to"][-4:]
    return operation

def print_operation(operation):
    operation_date = operation.get('date', '')
    from_account = operation.get('from', '') or operation.get('description', '')
    to_account = operation.get('to', '')
    amount = operation['operationAmount'].get('amount', '')
    currency = operation['operationAmount']['currency'].get('name', '')



    return f"{operation_date}\n{from_account} -> {to_account}\n{amount} {currency}"

def process_operation(operation):
    operation = mask_card(operation)
    operation = mask_account_number(operation)
    return operation

data = load_data()

formatted_operations = map(print_operation,
                           filter(lambda x: x.get("state", "") == "EXECUTED",
                                  map(process_operation,
                                      filter(lambda x: 'date' in x,
                                             sorted(data, reverse=True, key=lambda x: x.get("date", "")))
                                  )
                           )
                       )

print("\n\n".join(list(formatted_operations)[:5]))