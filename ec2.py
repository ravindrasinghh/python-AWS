import boto3
import pprint

#Creating session  to connect with AWS Account
session=boto3.Session(profile_name="default",region_name = "us-east-1")



#List out all the regions
client=session.client(service_name = 'ec2')
all_regions=client.describe_regions()

#Taking region in  array
list_of_Regions = []

for each_reg in all_regions['Regions']:
    list_of_Regions.append(each_reg['RegionName'])

#Running in loop  to fetch ec2 from all regions 
print(list_of_Regions)    
for each_reg in list_of_Regions:
    session=boto3.Session(profile_name="default",region_name = each_reg)
    resource=session.resource(service_name ='ec2')
    print("InsttanceID",each_reg)
    for each_in in resource.instances.all():
        print(each_in.id,each_in.state['Name'])

