import boto3
import time

client=boto3.client('elasticbeanstalk',region_name='us-east-1',
aws_access_key_id='ASIAWE5K43TXHSMOU66C',
aws_secret_access_key='pKosqiXjFNsyX9G2ydAx07jyz6SQBT3g0jJ2XWOG'
aws_session_token='FwoGZXIvYXdzEA0aDFqntokUm2pl2jA3oCLNAT0iR0mG3fR0L/w9Sgu8381ceGkLq7G0pvb9r25LRtWSIP1TCEXG4qvZarQAQ934LtqetMMNW7ulqjv7fidjT/sbJHX9wBT1NzF84mMFfp6LxUdm8CHGnkmWkmngqLQKcWjKcwy0FAscZHRwGpcmpCGxpw49mEtt+nKmPmEeFrEaHCrIpxq0ArCQ8Tio24CCYGupqgzhNDu+9r0vFDrE4MgA2aAqNBsgzHoslZ9aqVJq1j8n6Q00/pJ1C+QWMfIFmSwQVm8Hwq0mj7y5UcIoo9yFigYyLS+mM6ECWeEuTr7dMRf0oyCk0GXMwbxCb0+lJLfAkKweexs1etwZqRIscgioKw=='
#client=boto3.client('cloudfront',region_name='us-east-1',aws_access_key_id='ASIAUV6KQ6OIZRU6KDH3',
#aws_secret_access_key='SEsgEU0FPr2Fc2hEw31LmVedcKq8SxLDcB3GQB1/',aws_session_token='FwoGZXIvYXdzEPX//////////wEaDOxBR65w23SASCaRASLLAfwkOa6YU5gUpLgj4g48s/AClJEThFpgJ9gDChX3i1oCvOa2F7tzUDMQ+sO2gnFUz0E+9EJS9SNSDnReK62WpkJ0UhHfekL533LdZsXunFWVBYEwh8DFUAzXvkW5CFJIH9889wg50IisyGO5EPgQzND5MxqH+E3G6JkYYc1OsAzvPKTQGLFkkjoNqZbf3mdETyB6SqdmjzXxkl0Bk+Mdw/AMAXyQWbaNWfyhuRnE4PjYUkb2+AutH7O2u8HOCepC0UsPIHIJs1IftwzKKPa0gIoGMi20lLZJRK9ny06Q5//nZX1712Z1pon95eCkM53WP8bVhbw2vUhJZExJOadSDZo=')


def cloudFront_distribution():
    response = client.create_distribution(
            DistributionConfig={
                'CallerReference': 'my-distribution-cdn',
                
                'DefaultRootObject': 'index.html',
                'Origins': {
                    
                    'Items': [
                        {
                            
                            'DomainName': 'lab3dynamicwebsite.s3.us-east-1.amazonaws.com',
                        
                            
                            'S3OriginConfig': {
                                'OriginAccessIdentity': ''
                            },
                            'CustomOriginConfig': {
                                
                                'OriginProtocolPolicy': 'http-only'|'match-viewer'|'https-only',
                                
                            },
                        
                        },
                    ]
                },
                'OriginGroups': {
                
                    'ViewerProtocolPolicy': 'allow-all',
                    'AllowedMethods': {
                        
                        'Items': [
                            'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                        ],
                        'CachedMethods': {
                        
                            'Items': [
                                'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                            ]
                        }
                    },
                
                
            }
        }
    )
    print(response)

def create_version():
    response = client.create_application_version(
        ApplicationName='my-app-5',
        AutoCreateApplication=True,
        Description='my-app-v4',
        Process=True,
        SourceBundle={
        'S3Bucket': 'lab3dynamicwebsite',
        'S3Key': 'dynamicPortfolio.zip',
        },
        VersionLabel='v1',

    )
    print(response)

def create_environment():
    response = client.create_environment(
        ApplicationName='my-app-5',
        CNAMEPrefix='my-app-5',
        EnvironmentName='my-env-5',
        SolutionStackName='64bit Amazon Linux 2 v3.3.5 running PHP 8.0',
        VersionLabel='v1',
        OptionSettings=[
        {
            'Namespace':'aws:autoscaling:launchconfiguration',
            'OptionName': 'IamInstanceProfile',
            'Value':'EMR_EC2_DefaultRole'
            
            
        },{
            'Namespace':'aws:autoscaling:launchconfiguration',
            'OptionName': 'EC2KeyName',
            'Value':'CS351-2021'
        },{
            'Namespace':'aws:elasticbeanstalk:environment',
            'OptionName':'ServiceRole',
            'Value':'AWSServiceRoleForElasticBeanstalk'
        },{
            'Namespace':'aws:autoscaling:asg',
            'OptionName':'MaxSize',
            'Value':'2'
        }
    ],
    )

    print(response)

if __name__ == "__main__":
    #cloudFront_distribution
    create_version()
    time.sleep(5)
    create_environment()
