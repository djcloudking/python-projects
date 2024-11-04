ec2_instance = [
    {
        "id": "instance-01",
        "type": "t2.micro"
    },
    {
        "id": "instance-02",
        "type": "t2.medium"
    },
    {
        "id": "instance-03",
        "type": "t2.xlarge"
    }
]

print(ec2_instance[1]["type"])