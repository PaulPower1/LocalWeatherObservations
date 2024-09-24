import azure.functions as func
import logging
import sys

sys.path.append("./src")

import LocalWeatherObservations as lwo

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="HelloWorld")
def HelloWorld(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError: 
            pass
    else:
        name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
    
@app.route(route="Getlocations")
def Getlocations(req: func.HttpRequest) -> func.HttpResponse:
    """
    
    """
    logging.info('Python HTTP trigger function processed a request.')
    
    locations = req.params.get('locations')
    if not locations:
        try:
            req_body = req.get_json()
        except ValueError: 
            pass
    
    return func.HttpResponse(f"Location coordinates: {lwo.get_locations()}. This HTTP triggered function executed successfully.")     
    #return func.HttpResponse(f"Location coordinates: 0 and 0. This HTTP triggered function executed successfully.")     
