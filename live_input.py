
import zmq
import json

# Load product list from file
with open("requests.json", "r") as f:
    products = json.load(f)

# Connect to microservice
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

# Input loop
while True:
    name = input("\nEnter product name (or 'exit' to quit): ").strip().lower()
    if name == "exit":
        print("Goodbye!")
        break

    matched = None
    for product in products:
        if product["name"].strip().lower() == name:
            matched = product
            break

    if matched:
        socket.send_string(json.dumps(matched))
        response = socket.recv_string()
        result = json.loads(response)

        if "error" in result:
            print("Error:", result["error"])
        else:
            print(f"{result['name']}: {result['price']} {result['currency']}")
    else:
        print("Product not found.")