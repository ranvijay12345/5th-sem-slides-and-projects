import boto3
ebsClient = boto3.client('elasticbeanstalk')
version_label = 'version_demo'
application_name = 'protfolio4'
environment_name = 'ProtfolioEnv4'
def createNewVersion():
 try:
 ebsClient.create_application_version(
 ApplicationName=application_name,
 VersionLabel=version_label,
 Description='Portfolio website',
 SourceBundle={
 'S3Bucket': 'elasticbeanstalk-us-east-1-651372988659',
 'S3Key': 'import boto3
ebsClient = boto3.client('elasticbeanstalk')
version_label = 'version_demo'
application_name = 'protfolio4'
environment_name = 'ProtfolioEnv4'
def createNewVersion():
 try:
 ebsClient.create_application_version(
 ApplicationName=application_name,
 VersionLabel=version_label,
 Description='Portfolio website',
 SourceBundle={
 'S3Bucket': 'elasticbeanstalk-us-east-1-651372988659',
 'S3Key': 'import boto3
ebsClient = boto3.client('elasticbeanstalk')
version_label = 'version_demo'
application_name = 'protfolio4'
environment_name = 'ProtfolioEnv4'
def createNewVersion():
 try:
 ebsClient.create_application_version(
 ApplicationName=application_name,
 VersionLabel=version_label,
 Description='Portfolio website',
 SourceBundle={
 'S3Bucket': 'elasticbeanstalk-us-east-1-651372988659',
 'S3Key': 'import boto3
ebsClient = boto3.client('elasticbeanstalk')
version_label = 'version_demo'
application_name = 'protfolio4'
environment_name = 'ProtfolioEnv4'
def createNewVersion():
 try:
 ebsClient.create_application_version(
 ApplicationName=application_name,
 VersionLabel=version_label,
 Description='Portfolio website',
 SourceBundle={
 'S3Bucket': 'assign4ran',
 'S3Key': 'ezyzip.zip'
 },
 AutoCreateApplication=True,
 Process=False
 )
 print('application Created')
 except Exception as e:
 print('some error has occured: ', e)
def createEnvironment():
 try:
 ebsClient.create_environment(
 ApplicationName=application_name,
 EnvironmentName=environment_name,
 Description='Portfolio web app ',
 CNAMEPrefix='ranvijay',
 Tier={
 'Name': 'WebServer',
 'Type': 'Standard',
 },
 VersionLabel=version_label,
 SolutionStackName='64bit Amazon Linux 2 v5.4.5 running
Node.js 14',
 OptionSettings=[
 {
 'Namespace':
'aws:autoscaling:launchconfiguration',
 'OptionName': 'IamInstanceProfile',
 'Value': 'aws-elasticbeanstalk-ec2-role'
 },
 ],
 )
 print('Environment Created')
 except Exception as e:
 print('some error has occured: ', e)
def init():
 createNewVersion()
 createEnvironment()
if _name_ == '_main_':
 init()'
 },
 AutoCreateApplication=True,
 Process=False
 )
 print('application Created')
 except Exception as e:
 print('some error has occured: ', e)
def createEnvironment():
 try:
 ebsClient.create_environment(
 ApplicationName=application_name,
 EnvironmentName=environment_name,
 Description='Portfolio web app JSP environment',
 CNAMEPrefix='ranvijay',
 Tier={
 'Name': 'WebServer',
 'Type': 'Standard',
 },
 VersionLabel=version_label,
 SolutionStackName='64bit Amazon Linux 2018.03 v3.4.10
running Tomcat 8.5 Java 8',
 OptionSettings=[
 {
 'Namespace':
'aws:autoscaling:launchconfiguration',
 'OptionName': 'IamInstanceProfile',
 'Value': 'aws-elasticbeanstalk-ec2-role'
 },
 ],
 )
 print('Environment Created')
 except Exception as e:
 print('some error has occured: ', e)
def init():
 createNewVersion()
 createEnvironment()
if __name__ == '__main__':
 init()'
 },
 AutoCreateApplication=True,
 Process=False
 )
 print('application Created')
 except Exception as e:
 print('some error has occured: ', e)
def createEnvironment():
 try:
 ebsClient.create_environment(
 ApplicationName=application_name,
 EnvironmentName=environment_name,
 Description='Portfolio web app JSP environment',
 CNAMEPrefix='OMPRAKASH',
 Tier={
 'Name': 'WebServer',
 'Type': 'Standard',
 },
 VersionLabel=version_label,
 SolutionStackName='64bit Amazon Linux 2018.03 v3.4.10
running Tomcat 8.5 Java 8',
 OptionSettings=[
 {
 'Namespace':
'aws:autoscaling:launchconfiguration',
 'OptionName': 'IamInstanceProfile',
 'Value': 'aws-elasticbeanstalk-ec2-role'
 },
 ],
 )
 print('Environment Created')
 except Exception as e:
 print('some error has occured: ', e)
def init():
 createNewVersion()
 createEnvironment()
if _name_ == '_main_':
 init()'
 },
 AutoCreateApplication=True,
 Process=False
 )
 print('application Created')
 except Exception as e:
 print('some error has occured: ', e)
def createEnvironment():
 try:
 ebsClient.create_environment(
 ApplicationName=application_name,
 EnvironmentName=environment_name,
 Description='Portfolio web app JSP environment',
 CNAMEPrefix='OMPRAKASH',
 Tier={
 'Name': 'WebServer',
 'Type': 'Standard',
 },
 VersionLabel=version_label,
 SolutionStackName='64bit Amazon Linux 2018.03 v3.4.10
running Tomcat 8.5 Java 8',
 OptionSettings=[
 {
 'Namespace':
'aws:autoscaling:launchconfiguration',
 'OptionName': 'IamInstanceProfile',
 'Value': 'aws-elasticbeanstalk-ec2-role'
 },
 ],
 )
 print('Environment Created')
 except Exception as e:
 print('some error has occured: ', e)
def init():
 createNewVersion()
 createEnvironment()
if _name_ == '_main_':
 init()