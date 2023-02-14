#
#
# main() will be run when you invoke this action
#
# @param Cloud Functions actions accept a single parameter, which must be a JSON object.
#
# @return The output of this action, which must be a JSON object.
#
#
import sys
from ibmcloudant.cloudant_v1 import CloudantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def main(param_dict):
    authenticator = IAMAuthenticator(param_dict["IAM_API_KEY"])
    service = CloudantV1(authenticator=authenticator)
    service.set_service_url(param_dict["COUCH_URL"])
    if "review" in param_dict and param_dict["review"]:
        response = service.post_document(db='reviews', document=param_dict["review"])
        return {'statusCode':200, 'headers':{'Content-Type':'application/json'}, 'body':{}}
    else:    
        return {'statusCode':404, 'headers':{'Content-Type':'application/json'}, 'body':{}}

