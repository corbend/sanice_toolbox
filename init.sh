#bin/bash

python -m sanic main.core.bootstrap.app --workers 8 --host 127.0.0.1 --port 9000