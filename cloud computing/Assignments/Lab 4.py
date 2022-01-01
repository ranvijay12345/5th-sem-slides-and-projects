import boto3
import time

client = boto3.client('elasticbeanstalk', region_name='us-east-1', aws_access_key_id='ASIARUB2E74VRXNCTOZX',
                      aws_secret_access_key='3sRO95tOGxTdt56VHeJpSmhINdfTxWf0lrZVg3ev',
                      aws_session_token='FwoGZXIvYXdzEA0aDO3TDDBBq0kMIu+zRCLJAcNxe/SKgiyq4ZTYRzomK6uobJFK43FxIg0oNlSfAexZbXeBSxnIZPFDwwN2xvZvua6DjBfKn83JeUSlIzEggMv9t+B85CxNckciNeeEVO7/Uu7+tXH4p/PtCeEfJwT7XSGyd3W4W0fmdwicRotoL+PAUOncV4zmBmfryyI5D2Jy/asVNU23TkMmc2PAVeOw/PjkwSldiP/DdqAO7yGDuGdBrB66X/tTs9cIQlyLOyBQSl+l6HcSltMWfcd0AB5Rzi4M9CfpjjHDmiiM3oWKBjItC8H/X9UZzZyb3QB2SXLYcIXzqde3ioDJ+b3I61btX/XKl7iXfV/g+12WudPY')


# client=boto3.client('cloudfront',region_name='us-east-1',aws_access_key_id='ASIAXT2EVHYJEQWGI3MZ',
# aws_secret_access_key='z2Vja9gxsSvB8hdmxYBOk8u725HZ9NzlhlQIJ1fV',aws_session_token='FwoGZXIvYXdzEAEaDO9Sttk4jdvkkJXCiCLHAR8SYzkuCDgKPwJ8pZ4ugjK/hxAlQ9hZCQ0xFUsXnfWkLPYObmiOToa4t+dKL+ie2cg3XWUs2HAQzUIXur6teWGgmgDy4ar81kxE7aB/04p+l63BUfU8V5lBM6AtEODdgooOxv77Q1anz3/S/YdT7LKwhwZ/gALjqBAAY/EggOAfUswxWEdGmcE7DwoPjhM8PKFaKLQJwdWmA6uAb/7wf+XuBV12gDUFf9hIg2Z6BRkEGslp4/5Txs/3FItMth4KYHo0vXHlVfEozPaCigYyLXGufkdrk7m7mzvYsuHMhK0AwHae4gxkPZ5CVKt07BX0DiHqiE7vsNQf4BKp0Q==')


def cloudFront_distribution():
    print('hi')
    response = client.create_distribution(
        DistributionConfig={
            'CallerReference': 'my-distribution-cdn',

            'DefaultRootObject': 'index.html',
            'Origins': {
                'Quantity': 1,

                'Items': [
                    {
                        'Id': 'lab3dynamicwebsite',
                        'DomainName': 'lab3dynamicwebsite.s3.us-east-1.amazonaws.com',

                        'S3OriginConfig': {
                            'OriginAccessIdentity': ''
                        },

                    },
                ]
            },
            'DefaultCacheBehavior': {
                'TargetOriginId': 'lab3dynamicwebsite',

                'ViewerProtocolPolicy': 'allow-all',
                'AllowedMethods': {
                    'Quantity': 1,
                    'Items': [
                        'GET', 'HEAD', 'POST', 'PUT', 'PATCH', 'OPTIONS', 'DELETE',
                    ],
                    'CachedMethods': {
                        'Quantity': 1,
                        'Items': [
                            'GET', 'HEAD', 'POST', 'PUT', 'PATCH', 'OPTIONS', 'DELETE',
                        ]
                    }
                },
            },
            'Comment': 'distribution to host portfolio',
            'Enabled': True,

        }
    )
    print(response)


def create_version():
    response = client.create_application_version(
        ApplicationName='my-app-12',
        AutoCreateApplication=True,
        Description='my-app-v4',
        Process=True,
        SourceBundle={
            'S3Bucket': 'cloudas2',
            'S3Key': 'cloud_4-20210915T034934Z-001.zip',
        },
        VersionLabel='v1',

    )
    print(response)


def create_environment():
    response = client.create_environment(
        ApplicationName='my-app-12',
        CNAMEPrefix='my-app-12',
        EnvironmentName='my-env-12',
        SolutionStackName='64bit Amazon Linux 2 v3.3.5 running PHP 8.0',
        VersionLabel='v1',
        OptionSettings=[
            {
                'Namespace': 'aws:autoscaling:launchconfiguration',
                'OptionName': 'IamInstanceProfile',
                'Value': 'EMR_EC2_DefaultRole'

            }, {
                'Namespace': 'aws:autoscaling:launchconfiguration',
                'OptionName': 'EC2KeyName',
                'Value': 'cs351-2021'
            }, {
                'Namespace': 'aws:autoscaling:asg',
                'OptionName': 'MaxSize',
                'Value': '2'
            }
        ],
    )

    print(response)


if _name_ == "_main_":
    # cloudFront_distribution()
    create_version()
    time.sleep(5)
    create_environment()
