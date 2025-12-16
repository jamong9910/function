import logging
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    name = req.params.get("name")
    if not name:
        try:
            req_body = req.get_json()
            name = req_body.get("name")
        except ValueError:
            pass

    if name:
        return func.HttpResponse(
            f"Hello, {name}! This is Azure Functions 🚀",
            status_code=200
        )
    else:
        return func.HttpResponse(
            "Hello from Azure Functions! Pass ?name=yourname",
            status_code=200
        )
