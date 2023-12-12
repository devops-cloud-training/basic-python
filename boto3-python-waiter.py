import boto3
from rich import print

ec2 = boto3.resource("ec2")

all_the_instances = ec2.instances.all()
inst_id=[]
for i in all_the_instances:
    inst_id.append(i.id)
    instance_details=ec2.meta.client.describe_instances(InstanceIds=[i.id])

# print(instance_details)
print(inst_id)


ec2.meta.client.stop_instances(InstanceIds=inst_id)
waiter=ec2.meta.client.get_waiter("instance_stopped")
waiter.wait(InstanceIds=inst_id)
print("Instance Stopped")