
import zmq
import json

exchange_rates = {
    ("USD", "EUR"): 0.91,
    ("USD", "GBP"): 0.78,
    ("EUR", "USD"): 1.10,
    ("GBP", "USD"): 1.28,
    ("EUR", "GBP"): 0.85,
    ("GBP", "EUR"): 1.18
}

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

print("[microservice] Currency converter is running...")

while True:
    message = socket.recv_string()
    data = json.loads(message)

    try:
        price = float(data["price"])
        from_currency = data["currency"]
        to_currency = data["target"]
        name = data.get("name", "Unknown")

        rate = exchange_rates.get((from_currency, to_currency))
        if rate is None:
            raise ValueError(f"No exchange rate from {from_currency} to {to_currency}")

        converted_price = round(price * rate, 2)
        data["price"] = converted_price
        data["currency"] = to_currency

        socket.send_string(json.dumps(data))

        print(f"[converted] {name}: {price} {from_currency} → {converted_price} {to_currency}")

    except Exception as e:
        socket.send_string(json.dumps({"error": str(e)}))