/**
  *
  * main() will be run when you invoke this action
  *
  * @param Cloud Functions actions accept a single parameter, which must be a JSON object.
  *
  * @return The output of this action, which must be a JSON object.
  *
  */
const { CloudantV1 } = require('@ibm-cloud/cloudant');
const { IamAuthenticator } = require('ibm-cloud-sdk-core');

async function main(params) {
  const authenticator = new IamAuthenticator({ apikey: params.IAM_API_KEY })
  const cloudant = CloudantV1.newInstance({ authenticator: authenticator });
  cloudant.setServiceUrl(params.COUCH_URL);
  try {
  let code = 200;
  if (params.state) {
    const response = await cloudant.postFind({db: 'dealerships', selector: { state: { $eq: params.state, },},})
    if (response.result.docs.length == 0) { code = 404; }
    return {statusCode: code, headers: { 'Content-Type': 'application/json' }, body: response.result.docs,}
   } else {
     const response = await cloudant.postAllDocs({db: 'dealerships', includeDocs: true})
     if (response.result.rows.length == 0) { code = 404; }
     return {statusCode: code, headers: { 'Content-Type': 'application/json' }, body: response.result.rows,}
   }        
  } catch (error) {
    return { error: error.description };
  }
}
