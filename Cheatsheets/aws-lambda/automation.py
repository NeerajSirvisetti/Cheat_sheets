import json
import boto3
import requests
import os
import logging
import sys
import re
from string import Formatter
logger = logging.getLogger()
logger.setLevel(logging.INFO)
# connecting with AWS services via boto3 for communication
s3 = boto3.resource('s3')
sns = boto3.client('sns')
class UnseenFormatter(Formatter):
    def get_value(self, key, args, kwds):
        if isinstance(key, str):
            try:
                return kwds[key]
            except KeyError:
                return ("No information available")
        else:
            return Formatter.get_value(key, args, kwds)
def webhook_response_info(event,parameter_list):
    webhook_response = {}
    infoFromJson = event
    for val in parameter_list:
        if val in infoFromJson.keys():
            webhook_response[val] = infoFromJson[val]
    logger.info('Retrieved Information from the Webhook Response')
    logger.info(webhook_response)
    return webhook_response
def rename_keys_dict(InfoToDict,rename_keys,webhook_response):
	for key, value in rename_keys.items():
		InfoToDict[value] = webhook_response[key]
	return InfoToDict
def write_file(InfoToDict,lambda_path):
    func = open(lambda_path,"w")
    # Adding input data to the  file
    func.write(json.dumps(InfoToDict))
    # Saving the data into the  file
    func.close()

def read_file(InfoFromBuild,lambda_path):
    func = open(lambda_path,"r")
    # Adding input data to the  file
    InfoFromBuild=json.load(func)
    # Saving the data into the  file
    func.close()
    return InfoFromBuild
def invoke_api(method, url, payload, header):
    response = requests.request(method, url, data=payload, headers=header, verify=False)
    return response
def retrieve_environment_details(response,environment_details, flag,version):
    infoFromJson2 = response.json()
    pie_data = infoFromJson2['data']
    for val in pie_data:
        if val['version_id'].strip() == InfoToDict["Version"].strip():
            logger.info('Required data from the deployments')
            environment_details['DeploymentId'] = val['id']
            environment_details['WorkspaceId'] = val['repo_id'].split("-")[0]
            environment_details['EnvironmentId'] = "<env id>"
            logger.info('Retrieved Environment information from deployment')
            flag = 1
        else:
            if flag == 1:
                break
    return environment_details
def write_file_html(InfoToDict,lambda_path):
    outputfile = open('template.html','r')
    outputfile.seek(0)
    data = outputfile.read()
    fmt = UnseenFormatter()
    htmlcontent = fmt.format(data,**InfoToDict)
    outputfile.close()
    func = open(lambda_path,"w")
    # Adding input data to the HTML file
    func.write(htmlcontent)
    # Saving the data into the HTML file
    func.close()
def lambda_handler(event, context):
    logger.info('## ENVIRONMENT VARIABLES')
    logger.info(os.environ)
    logger.info('## EVENT')
    logger.info(event)
    
    if "packageMetrics" in event.keys():
    # Function to extract required information from RIO Webhook response
        parameter_list = ["BuildNumber", "BuildId", "jenkinsBuildName", "gitBranch",
                      "startAt", "jenkinsBuildUrl", "completeAt", "gitAuthor", "projectName", "gitCommitMessage",
                      "projectId", "gitUrl"]
        webhook_response = webhook_response_info(event,parameter_list)
        InfoToDict={}
        rename_keys = {"projectName":"ProjectName","projectId":"ProjectId","startAt":"BuildStartAt","BuildId":"BuildId", "BuildNumber":"PipelineNumber", "jenkinsBuildName":"PipelineSpecId",
	"jenkinsBuildUrl":"JenkinsBuildUrl","gitAuthor":"GitAuthor","gitBranch":"GitBranch","gitCommitMessage":"GitCommitMessage",
	"gitUrl":"GitUrl","completeAt":"BuildCompleteAt"}
        InfoToDict = rename_keys_dict(InfoToDict,rename_keys,webhook_response)
        filename = InfoToDict["BuildId"] + ".txt"
        lambda_path = '/tmp/' + filename
        write_file(InfoToDict,lambda_path)
        logger.info(os.path.isfile(lambda_path))
        logger.info(lambda_path)
    else:
        parameter_list =["result", "completeAt", "startedAt", "pipelineInfo"]
        webhook_response = webhook_response_info(event,parameter_list)
        webhook_response["BuildId"] = webhook_response['pipelineInfo']['buildId']
        webhook_response["Version"] = webhook_response['pipelineInfo']['artifactsVersion']
        InfoToDict={}
        rename_keys = {"result":"Result","startedAt":"DeploymentStartAt","completeAt":"DeploymentCompleteAt","BuildId":"BuildId",
        "Version":"Version"}
        InfoToDict = rename_keys_dict(InfoToDict,rename_keys,webhook_response)
        InfoFromBuild={}
        filename = InfoToDict["BuildId"] + ".txt"
        lambda_path = '/tmp/' + filename
        logger.info(os.path.isfile(lambda_path))
        logger.info(lambda_path)
        build_file_exists = os.path.isfile(lambda_path)
        if build_file_exists == True:
        	InfoFromBuild=read_file(InfoFromBuild,lambda_path)
        	os.remove(lambda_path)
        	logger.info(InfoFromBuild)
        	logger.info(os.path.isfile(lambda_path))
        else:
        	return None
        InfoFromBuild.update(InfoToDict)
        logger.info(InfoToDict)
        
        # Function to invoke PIE API and getting response
        header = {'X-API-TOKEN': '<token>'}
        method = "GET"
        url = "<repos path>" + InfoFromBuild['ProjectId'] + "/deployments?limit=5"	
        payload = ""
        response = invoke_api(method, url, payload, header)
        logger.info(response)
		# Function to retrieve environment details from PIE
        flag = 0
        environment_details = {}
        version=InfoToDict["Version"]
        environment_details = retrieve_environment_details(response,environment_details, flag,version)
        logger.info(environment_details)
        InfoFromBuild.update(environment_details)
        InfoToDict = InfoFromBuild
        InfoToDict['style'] = '''
    table, th,td {border: 0.1px solid black;}
    th, td {padding: 4px;text-align: left;}
    '''
        filename = ("rdar/"+re.findall(r'\d+', InfoToDict["GitCommitMessage"])[0] + "_"+ InfoToDict["GitBranch"]+".html").replace("/","_")
        lambda_path = '/tmp/' + filename
        write_file_html(InfoToDict,lambda_path)
        logger.info("HTML File Written Successfully")
        # Function to write text file in the given bucket
        bucket = 'webhook-snapshot'
        s3.meta.client.upload_file(lambda_path,Bucket=bucket,Key=filename)
        return {
        'statusCode': 200,
        'body': "Completed"}