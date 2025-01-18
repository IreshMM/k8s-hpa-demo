from flask import Flask, request
from threading import Thread
import uuid
import sys
import time

app = Flask(__name__)

def consume_cpu(n):
    fib_result = fibonacci(n)
    print(f'Fibonacci result for {n} : {fib_result}', file=sys.stderr)

def consume_mem(n):
    uniq_id = uuid.uuid4()
    mem = ' ' * (n * 1024 * 1024)
    print(f'Memory allocated for {uniq_id}', file=sys.stderr)
    time.sleep(10)

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

@app.route('/cpu')
def cpu():
    n = request.args.get('n', default=10, type=int)
    cpu_thread = Thread(target=consume_cpu, args=(n,))
    cpu_thread.start()
    return f'Hello CPU with {n}'

@app.route('/mem')
def mem():
    n = request.args.get('n', default=10, type=int)
    mem_thread = Thread(target=consume_mem, args=(n,))
    mem_thread.start()
    return 'Hello Memory with {} MiB'.format(n)

if __name__ == '__main__':
    app.run(debug=True)