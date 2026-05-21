import boto3

s3 = boto3.client("s3")

bucket_name = "plant-disease-models-vanshika"

response = s3.list_objects_v2(Bucket=bucket_name)

print("Connected to bucket successfully!")
print(response)