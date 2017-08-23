import os
from emerson import app
port = int(os.environ.get('PORT', 5000))
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    print(port)
    app.run(host='127.0.0.1', port=port)
