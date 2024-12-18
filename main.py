from flask import Flask, request, Response
import requests

app = Flask(__name__)

API_BASE_URL = 'https://cfw-se4458-midterm.babur-g.workers.dev/v1'

# Route mapping
routes = {
    '/all': '/all',
    '/auth': '/auth',
    '/host/insert-listing': '/host/insert-listing',
    '/guest/query-listings': '/guest/query-listings',
    '/guest/book': '/guest/book',
    '/guest/rate': '/guest/rate',
    '/admin/listing-by-rating': '/admin/listing-by-rating',
}

@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def proxy_request(path):
    if f'/{path}' not in routes:
        return Response(f"Route /{path} not found.", status=404)

    target_url = f"{API_BASE_URL}{routes[f'/{path}']}"
    print(f"Incoming request to /{path}: {request.method} {request.url}")

    try:
        # Forward the request to the target URL
        resp = requests.request(
            method=request.method,
            url=target_url,
            headers={key: value for key, value in request.headers.items() if key.lower() != 'host'},
            data=request.get_data(),
            cookies=request.cookies,
            allow_redirects=False,
            stream=True  # Enable streaming for chunked responses
        )

        # Stream the response back to the client
        def generate():
            for chunk in resp.iter_content(chunk_size=8192):
                if chunk:
                    yield chunk

        response = Response(generate(), status=resp.status_code)
        response.headers = {key: value for key, value in resp.headers.items() if key.lower() != 'transfer-encoding'}
        return response

    except requests.RequestException as e:
        print(f"Error forwarding request to {target_url}: {str(e)}")
        return Response(f"Internal Server Error: Could not forward request to {target_url}", status=500)

if __name__ == '__main__':
    port = 3000
    print(f"API Gateway listening on port {port}")
    app.run(host='0.0.0.0', port=port)
