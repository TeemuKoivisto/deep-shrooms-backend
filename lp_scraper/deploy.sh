#!/bin/bash

# Deploys output -folder as a zipped dataset to S3.

NAME=$1
PROFILE=$2

if [ -z "$NAME" ]; then
  echo "Missing first argument NAME for the deployed dataset."
  exit 0
fi
if [ -z "$PROFILE" ]; then
  echo "Missing second argument PROFILE for the AWS profile to be used for deploying."
  exit 0
fi

cp -r ./output ./$NAME
zip -r ./$NAME.zip ./$NAME
rm -r ./$NAME

aws s3 cp ./$NAME.zip s3://deep-shrooms \
  --region eu-central-1 \
  --acl bucket-owner-full-control \
  --cache-control max-age=2592000 \
  --profile $PROFILE

rm ./$NAME.zip
