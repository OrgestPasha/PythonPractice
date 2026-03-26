accounts = {}


def create_account(name: str, initial_balance: float) -> dict:
    if name in accounts:
        raise ValueError("Name already exists")
    if not initial_balance > 0:
        raise ValueError("Initial balance needs to be positive")
    account = {name: {"balance": initial_balance, "transactions": []}}
    accounts.update(account)
    return account


def deposit(name: str, amount: float):
    if not validate_name_amount(name, amount):
        return
    account = accounts[name]
    account["balance"] += amount
    account["transactions"].append({"type": "Deposit", "amount": amount})


def withdraw(name: str, amount: float):
    if not validate_name_amount(name, amount):
        return

    account = accounts[name]

    if account["balance"] - amount < 0:
        raise ValueError("Insufficent funds")
    account["balance"] -= amount
    account["transactions"].append({"type": "Withdrawal", "amount": amount})


def validate_name_amount(name: str, amount: float) -> bool:
    if not amount > 0:
        raise ValueError("Amount not valid")
    if name not in accounts:
        raise ValueError(f"No account found for {name}")
    return True


def show_account(name: str) -> None:
    account = accounts[name]
    print(f"""
The name is {name} 
The current balance is {account["balance"]}
The transaction history is {account["transactions"]}
        """)


acc = create_account("Alice", 100)
assert "Alice" in accounts
assert accounts["Alice"]["balance"] == 100
assert accounts["Alice"]["transactions"] == []

try:
    create_account("Alice", 50)
    assert False, "Expected ValueError for duplicate account"
except ValueError:
    pass

try:
    create_account("Bob", 0)
    assert False, "Expected ValueError for non-positive balance"
except ValueError:
    pass

deposit("Alice", 50)
assert accounts["Alice"]["balance"] == 150
assert accounts["Alice"]["transactions"][-1]["type"] == "Deposit"

withdraw("Alice", 30)
assert accounts["Alice"]["balance"] == 120
assert accounts["Alice"]["transactions"][-1]["type"] == "Withdrawal"

try:
    withdraw("Alice", 1000)
    assert False, "Expected ValueError for insufficient funds"
except ValueError:
    pass

try:
    deposit("Alice", -10)
    assert False, "Expected ValueError for negative deposit"
except ValueError:
    pass

try:
    deposit("Charlie", 10)
    assert False, "Expected ValueError for missing account"
except ValueError:
    pass

assert len(accounts["Alice"]["transactions"]) == 2

print("All tests passed")
