# aws-lambda-minecraft-name-sniper
AWS Lambda Functions that Can be Used to Snipe Minecraft Names

## Resources

https://c4k3.github.io/wiki.vg/Mojang_API.html

https://wiki.vg/Mojang_API#Change_Name

https://urllib3.readthedocs.io/en/latest/user-guide.html

https://github.com/urllib3/urllib3

## Information

To get bearer token, login to Minecraft account and look for bearer_token cookie.
The token will expire in roughly 2 hours.

Use NameMC to find wanted names and release dates. Can schedule Cloudwatch rule at specific time to trigger the Lambda function, but unfortunately the smallest increments of time that the Cloudwatch rule supports are minutes.
