from aws_cdk import (
    core as cdk,
    aws_ec2 as ec2
)


class LambdaWithinVpcStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc = ec2.Vpc(self, 'demoVpc',
                      cidr="10.0.0.0/16",
                      max_azs=2,
                      enable_dns_hostnames=True,
                      enable_dns_support=True,
                      subnet_configuration=[
                          ec2.SubnetConfiguration(
                              name="Public",
                              subnet_type=ec2.SubnetType.PUBLIC,
                              cidr_mask=24
                          ),
                          ec2.SubnetConfiguration(
                              name="Private",
                              subnet_type=ec2.SubnetType.PRIVATE,
                              cidr_mask=24
                          )
                      ],
                      nat_gateways=1
                      )
