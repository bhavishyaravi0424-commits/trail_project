from flask import Flask, request, jsonify

app = Flask(__name__)

# Home Route
@app.route("/")
def home():
    return "Python Backend Connected to Railway Successfully!"

# Calculator API
@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()

    num1 = data.get("num1")
    num2 = data.get("num2")
    operation = data.get("operation")

    try:
        if operation == "add":
            result = num1 + num2

        elif operation == "subtract":
            result = num1 - num2

        elif operation == "multiply":
            result = num1 * num2

        elif operation == "divide":
            if num2 == 0:
                return jsonify({"error": "Cannot divide by zero"})
            result = num1 / num2

        else:
            return jsonify({"error": "Invalid operation"})

        return jsonify({
            "num1": num1,
            "num2": num2,
            "operation": operation,
            "result": result
        })

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
