# Microservice__Currency-Converter

This microservice receives a product's name, price, and currency, and returns the product's price converted into a target currency using a fixed exchange rate table.

Communication Contract:
- **Protocol:** ZeroMQ
- **Pattern:** REQ/REP (Request-Reply)
- **Encoding:** JSON (UTF-8)
- **Port:** tcp://localhost:5555
- **Request Format:**
  json

How to Programmatically REQUEST Data:
<pre>
  #You can use ZeroMQ in Python to send a JSON request to the microservice like this:
  import zmq
  import json

  context = zmq.Context()
  socket = context.socket(zmq.REQ)
  socket.connect("tcp://localhost:5555")

  request_data = {
      "name": "Backpack",
      "price": 50.00,
      "currency": "EUR",
      "target": "USD",
      "url": "http://example.com/backpack"
  }

  socket.send_string(json.dumps(request_data))
</pre>
How to Programmatically RECEIVE Data:
<pre>
  #After sending the request, you can wait for a reply like this:
  response = socket.recv_string()
  result = json.loads(response)

  print(f"{result['name']}: {result['price']} {result['currency']}")
</pre>
