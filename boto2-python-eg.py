import boto3
from rich import print

ec2 = boto3.resource("ec2")

# print(ec2.instances.all())

all_the_instances = ec2.instances.all()

# for i in all_the_instances:
#     print(i.id)
#     instance_details=ec2.meta.client.describe_instances(InstanceIds=[i.id])
#     print(instance_details)
#     print(instance_details["Reservations"][0]["Instances"][0]["ImageId"])
    # print()

my_instances = ec2.create_instances(
    ImageId = "ami-05c13eab67c5d8861",
    MinCount = 1,
    MaxCount = 1,
    InstanceType = "t2.micro"
)
print(my_instances)

# print(dir(ec2))

# ec2_client = boto3.client("ec2")

# print(dir(ec2_client))