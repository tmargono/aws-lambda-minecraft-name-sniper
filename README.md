# aws-lambda-minecraft-name-sniper
AWS Lambda Functions that Can be Used to Snipe Minecraft Names

## Resources

https://c4k3.github.io/wiki.vg/Mojang_API.html

https://wiki.vg/Mojang_API#Change_Name

https://urllib3.readthedocs.io/en/latest/user-guide.html

https://github.com/urllib3/urllib3

## Information/Setup

To get bearer token, login to Minecraft account and look for bearer_token cookie.
The token will expire in roughly 2 hours.

Use NameMC to find wanted names and release dates. Can schedule Cloudwatch rule at specific time to trigger the Lambda function, but unfortunately the smallest increments of time that the Cloudwatch rule supports are minutes. A configurable delay in seconds has been added to account for this, but according to https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/CWE_Troubleshooting.html#RuleDidNotTriggerOntime 
```
Due to the distributed nature of the CloudWatch Events and the target services, 
the delay between the time the scheduled rule is triggered and the time the target service 
honors the execution of the target resource might be several seconds. 
Your scheduled rule will be triggered within that minute but not on the precise 0th second.
```
It is therefore difficult to schedule exactly when the Lambda function will run.

When scheduling the Cloudwatch alarm, times in cron expression are UTC. See https://docs.aws.amazon.com/lambda/latest/dg/services-cloudwatchevents-expressions.html for more information. Pass into the Lambda function a json object containing the name, bearer token, and delay (seconds).

JSON Format:
`{'name':'test', 'token':'test', 'delay':1}`

When setting up the Lambda function, be sure to change the timeout to a larger value (default is 3 sec) so that the function doesn't timeout while it is being delayed.


