from flask import Flask, render_template, request
import requests
import json
import time

app = Flask(__name__)

STATUS_EXPLANATIONS = {
    200: "Success — the request worked correctly.",
    201: "Created — a new resource was created successfully.",
    400: "Bad Request — the API could not understand your request.",
    401: "Unauthorized — authentication is required.",
    403: "Forbidden — you do not have permission to access this.",
    404: "Not Found — the API endpoint does not exist.",
    500: "Server Error — something went wrong on the server side."
}

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        url = request.form.get("url")
        method = request.form.get("method")
        body = request.form.get("body")

        try:
            start_time = time.time()

            if method == "GET":
                response = requests.get(url, timeout=5)

            elif method == "POST":
                data = {}
                if body:
                    data = json.loads(body)
                response = requests.post(url, json=data, timeout=5)

            end_time = time.time()

            try:
                response_data = response.json()
                response_text = json.dumps(response_data, indent=2)
            except:
                response_text = response.text

            status_code = response.status_code
            explanation = STATUS_EXPLANATIONS.get(
                status_code,
                "This status code means the request could not be completed as expected."
            )

            result = {
                "status": status_code,
                "response": response_text,
                "time": round(end_time - start_time, 3),
                "explanation": explanation
            }

        except json.JSONDecodeError:
            error = "Invalid JSON format in request body."
        except requests.exceptions.MissingSchema:
            error = "Invalid URL. Please include http:// or https://"
        except requests.exceptions.Timeout:
            error = "The request timed out. The API may be slow or unavailable."
        except requests.exceptions.ConnectionError:
            error = "Could not connect to the API. Check your internet or URL."
        except Exception as e:
            error = f"Unexpected error: {str(e)}"

    return render_template("index.html", result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True)
