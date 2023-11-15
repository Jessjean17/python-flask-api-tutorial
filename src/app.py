from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False }
]

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body:", request_body)

    new_todo = {
        "label": request_body.get("label", ""),
        "done": request_body.get("done", False)
    }
    todos.append(new_todo)

    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ", position)
    if 0 <= position < len(todos):
        del todos[position]
        return jsonify(todos)
    else:
        return 'Invalid position for deletion'

# Keep the following lines at the bottom of your app.py file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
