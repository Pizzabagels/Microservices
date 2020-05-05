import os
import time
from flask import Flask

app = Flask(__name__)

@app.route('/gettime/')
def epoch_time():
    return str(time.time().__round__())


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)