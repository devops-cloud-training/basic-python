import boto3
from rich import print

iam = boto3.resource("iam")

print(iam.policies.all())

# all_policies_resources = iam.policies.all()
all_policies_client = iam.meta.client.list_policies()['Policies']
# print(len(all_policies_client))

paginator = iam.meta.client.get_paginator('list_policies')

pages = paginator.paginate()
page_count = 0
policy_count = 0
for i in pages:
    # print(i)
    page_count += 1
    for j in i['Policies']:
        policy_count += 1

print(page_count)
print(policy_count)
# count = 0
# for i in all_policies_resources:
#     print(i)
#     count += 1

# print(count)