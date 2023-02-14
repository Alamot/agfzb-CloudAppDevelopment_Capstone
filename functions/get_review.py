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
    code = 200
    try:         
        if "dealerId" in param_dict and param_dict["dealerId"]:
            response = service.post_find(db='reviews',
                                     selector={'dealership': {'$eq': int(param_dict["dealerId"])}},).get_result()
            if (len(response["docs"]) == 0): code = 404
            return  {'statusCode':code, 'headers':{'Content-Type':'application/json'}, 'body': response}
        else:
           response = service.post_all_docs(db='reviews', include_docs=True).get_result()
           return  {'statusCode':code, 'headers':{'Content-Type':'application/json'}, 'body': response["rows"]}
    except:
        return {'statusCode':500, 'headers':{'Content-Type':'application/json'}, 'body':{}}

