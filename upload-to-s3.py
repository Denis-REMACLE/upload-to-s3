import argparse
import logging
import boto3
import os
from botocore.exceptions import ClientError


"""
Level	Numeric value
ERROR	40
WARNING	30
INFO	20
DEBUG	10
"""
logging_level = 40

""" Set log level """
logging.basicConfig(format="%(asctime)s - %(message)s", level=logging_level)

""" Set variables """
logger = logging.getLogger()

def connect(profile):
    """Connection to AWS

    Args:
        profile (str): Define the sso profile to use

    Returns:
        ApiGateway: Object used to handle AWS ApiGateway
    """
    try:
        # Connect to desired SSO profile
        session = boto3.Session(profile_name=profile)
        # Start all necessary sessions
        client_s3 = session.client("s3")
    except Exception as err:
        logging.error("Error on connection")
        logging.error(str(err), exc_info=True)

    return  client_s3

def main():
    parser = argparse.ArgumentParser(
        prog="S3 Uploader",
        description="This script documents the AWS SSO",
    )
    parser.add_argument(
        "-s",
        "--sso",
        type=str,
        default=False,
        help="This argument will set the account to use for the check",
    )
    parser.add_argument(
        "-b",
        "--bucket",
        type=str,
        default=False,
        help="This argument will set the account to use for the check",
    )
    parser.add_argument(
        "-f",
        "--files",
        type=str,
        nargs='+',
        help="This argument will set the identity store id to use for the check",
    )
    parser.add_argument(
        "-k",
        "--key",
        type=str,
        help="This argument will set the identity store id to use for the check",
    )
    args = parser.parse_args()

    client_s3 = connect(args.sso)
    
    for files in args.files:
        response = client_s3.upload_file(files, args.bucket, args.key+files)



if __name__ == "__main__":
    main()
