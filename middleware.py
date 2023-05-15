import time

class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()

        response = self.get_response(request)

        execution_time = time.time() - start_time

        with open('logs.txt', 'a') as file:
            file.write(f"Path: {request.path}, Method: {request.method}, Execution Time: {execution_time}\n")

        return response
