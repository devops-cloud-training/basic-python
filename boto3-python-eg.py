import boto3
from rich import print

ec2 = boto3.resource("ec2")

# print(ec2.instances.all())


# for i in all_the_instances:
#     print(i.id)
#     instance_details=ec2.meta.client.describe_instances(InstanceIds=[i.id])
#     print(instance_details)
#     print(instance_details["Reservations"][0]["Instances"][0]["ImageId"])
    # print()

my_instances = ec2.create_instances(
    ImageId = "ami-05c13eab67c5d8861",
    MinCount = 3,
    MaxCount = 3,
    InstanceType = "t2.micro"
)
print(my_instances)

# print(dir(ec2))

# ec2_client = boto3.client("ec2")

# print(dir(ec2_client))

# Terminate all the running instances
# all_the_instances = ec2.instances.all()
# print(all_the_instances)

# Ids=["i-0f84c00bb27d2d7fd","i-0dbc7e138fca62464","i-07ebe1124b541c9a4"]

# print(Ids)
# print(dir(ec2.instances))
# instance_list=[]
# for i in all_the_instances:
#     instance_list.append(i.id)

# print(type(all_the_instances))
# print(instance_list)
# print(type(instance_list))

# ec2.instances.filter(InstanceIds=instance_list).terminate()