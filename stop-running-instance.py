import boto3
from rich import print

ec2 = boto3.resource("ec2")
ec2_client = boto3.client("ec2")

# Terminate all the running instances
# all_the_instances = ec2.instances.all()
# print(all_the_instances)

# Ids=["i-0f84c00bb27d2d7fd","i-0dbc7e138fca62464","i-07ebe1124b541c9a4"]

# print(Ids)
# print(dir(ec2.instances.filter))
# instance_list=[]
# for i in all_the_instances:
#     instance_list.append(i.id)

# print(type(all_the_instances))
# print(instance_list)
# print(type(instance_list))

# ec2.instances.filter(InstanceIds=instance_list).terminate()


instanceIds_using_resource=ec2.instances.filter(
    Filters = [{
        "Name": "instance-state-name",
        "Values": ["stopped"]
    }]
)
running_instance_id=[]
for i in instanceIds_using_resource:
    print(dir(i))
    # running_instance_id.append(i.id)

# print(running_instance_id)
# ec2.instances.filter(InstanceIds=running_instance_id).terminate()

# running_inst_id_using_client=ec2_client.describe_instances(
#     Filters = [{
#         "Name": "instance-state-name",
#         "Values": ["running"]
#     }]
# )["Reservations"][0]["Instances"]

# # print(running_inst_id_using_client[0]["InstanceId"])
# # print(running_inst_id_using_client[1]["InstanceId"])
# instanceId_from_client=[]
# for i in range(len(running_inst_id_using_client)):
#     instanceId_from_client.append(running_inst_id_using_client[i]["InstanceId"])

# print(instanceId_from_client)
# print(ec2.instances.filter(InstanceIds=instanceId_from_client).terminate())
