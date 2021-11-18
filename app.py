#!/usr/bin/env python3
import os

from aws_cdk import core as cdk

from aws_cdk import core

from lambda_within_vpc.lambda_within_vpc_stack import LambdaWithinVpcStack


app = core.App()
LambdaWithinVpcStack(app, "LambdaWithinVpcStack", env=core.Environment(
    account=os.environ["CDK_DEFAULT_ACCOUNT"], region=os.environ["CDK_DEFAULT_REGION"])
    )

app.synth()
