import boto3

# Define resource
s3 = boto3.resource('s3')

# List Buckets
print("This is your buckets list: \n")
for bucket in s3.buckets.all():
    print(bucket.name)

#Input data
mybucket = input("Choose bucket name? \n")
filedata = input("What's the file path? \n")
rename_filedata = input("Write the name of your file/folder: \n")

# Upload a new file
data = open(filedata, 'rb')
s3.Bucket(mybucket).put_object(Key=rename_filedata, Body=data)

# Rename the uploaded file
'''
s3.Object(mybucket,rename_filedata).copy_from(CopySource= mybucket+"/"+filedata)
s3.Object(mybucket,filedata).delete()
'''
print("File uploaded.")