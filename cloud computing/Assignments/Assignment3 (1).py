import boto3

startup_script = '''#!/bin/bash
sudo yum update -y
sudo amazon-linux-extras install -y lamp-mariadb10.2-php7.2 php7.2
sudo yum install -y httpd
sudo systemctl start httpd
sudo systemctl enable httpd
cd /var/www/html
rm index.html
wget https://staticwebsiteassignment2.s3.amazonaws.com/index.html
'''


print("Connecting to Autoscalling Service")

client = boto3.client('autoscaling')

print("Creating launch configuration")

response = client.create_launch_configuration(
    LaunchConfigurationName='MY-Launch-Config',
    ImageId='ami-0c2b8ca1dad447f8a',
    InstanceType='t2.micro',
    KeyName='cloud',
    SecurityGroups=[
        'sg-05931c6dedeed8c8b',
    ],
    UserData=startup_script)

print("Creating auto-scaling group")

response = client.create_auto_scaling_group(
    AutoScalingGroupName='My-Auto-Scaling-Group',
    LaunchConfigurationName='MY-Launch-Config',
    AvailabilityZones=[
        'us-east-1b',
    ],
    MinSize=1,
    MaxSize=2)

print("Creating auto-scaling policies")

response = client.put_scaling_policy(
    AutoScalingGroupName='My-Auto-Scaling-Group',
    PolicyName='scale_up',
    AdjustmentType='ChangeInCapacity',
    ScalingAdjustment=1,
    Cooldown=180)


response = client.put_scaling_policy(
    AutoScalingGroupName='My-Auto-Scaling-Group',
    PolicyName='scale_down',
    AdjustmentType='ChangeInCapacity',
    ScalingAdjustment=-1,
    Cooldown=180)

scale_up_policy = client.describe_policies(
    AutoScalingGroupName='My-Auto-Scaling-Group',
    PolicyNames=[
        'scale_up',
    ])

scale_down_policy = client.describe_policies(
    AutoScalingGroupName='My-Auto-Scaling-Group',
    PolicyNames=[
        'scale_down',
    ])

print("Connecting to CloudWatch")

cloudwatch = boto3.client('cloudwatch')

#alarm_dimensions = "AutoScalingGroupName": 'My-Auto-Scaling-Group'

print("Creating scale-up alarm")

response = cloudwatch.put_metric_alarm(
    AlarmName='scale_up_on_cpu',
    AlarmActions=[
        "scale_up_policy['ScalingPolicies'][0]['PolicyARN']",
    ],
    MetricName='CPUUtilization',
    Namespace='AWS/EC2',
    Statistic='Average',
    Dimensions=[
        {
            'Name': 'My-Auto-Scaling-Group',
        },
    ],
    Period=60,
    EvaluationPeriods=2,
    Threshold=70,
    ComparisonOperator='GreaterThanThreshold')

print("Creating scale-down alarm")

response = cloudwatch.put_metric_alarm(
    AlarmName='scale_down_on_cpu',
    AlarmActions=[
        "scale_down_policy['ScalingPolicies'][0]['PolicyARN']",
    ],
    MetricName='CPUUtilization',
    Namespace='AWS/EC2',
    Statistic='Average',
    Dimensions=[
        {
            'Name': 'My-Auto-Scaling-Group',
        },
    ],
    Period=60,
    EvaluationPeriods=2,
    Threshold=50,
    ComparisonOperator='LessThanThreshold')

print("Done")