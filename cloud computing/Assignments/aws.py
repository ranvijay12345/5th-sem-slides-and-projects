[js]
from boto.ec2.cloudwatch import MetricAlarm
import boto.ec2.cloudwatch
cloudwatch=boto.ec2.cloudwatch.connect_to_region(‘us-east-1′,profile_name=’selectcloud’)
alarm_dimensions={"AutoScalingGroupName":"boto_group"}
scale_down_alarm=MetricAlarm(name=’scale_down_cpu’,namespace=’AWS/EC2′,metric=’CPUUtilization’,statistic=’Average’,comparison='<‘,threshold=’40’,period=’60’, evaluation_periods=2,alarm_actions=[scale_down_policy_arn.policy_arn],dimensions=alarm_dimensions)
scale_up_alarm=MetricAlarm(name=’scale_up_cpu’, namespace=’AWS/EC2′,metric=’CPUUtilization’, statistic=’Average’,comparison=’>’, threshold=’70’,period=’60’, evaluation_periods=2,alarm_actions=[scale_up_policy_arn.policy_arn],dimensions=alarm_dimensions)
cloudwatch.create_alarm(scale_up_alarm)
cloudwatch.create_alarm(scale_down_alarm)
[/js]