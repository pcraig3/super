import os
from superapp import create_app


PORT = os.environ.get("PORT", 8080)
app = create_app('dev')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=PORT)
