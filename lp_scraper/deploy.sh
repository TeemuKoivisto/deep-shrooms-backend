#!/bin/bash

# Deploys a folder as a zip-file to S3 bucket "deep-shrooms".

TARGET_DIR=$1
ZIP_NAME=$2
PROFILE=$3

if [ -z "$ZIP_NAME" ]; then
  echo "Missing first argument TARGET_DIR. It should be the target folder you're trying to deploy."
  exit 0
fi
if [ -z "$ZIP_NAME" ]; then
  echo "Missing second argument ZIP_NAME. It will be used as the name of the dataset."
  exit 0
fi
if [ -z "$PROFILE" ]; then
  echo "Missing third argument PROFILE. It's the AWS profile you want to use for deploying."
  exit 0
fi

cp -r ./$TARGET_DIR ./$ZIP_NAME
zip -r ./$ZIP_NAME.zip ./$ZIP_NAME
rm -r ./$ZIP_NAME

aws s3 cp ./$ZIP_NAME.zip s3://deep-shrooms \
  --region eu-central-1 \
  --acl bucket-owner-full-control \
  --cache-control max-age=2592000 \
  --profile $PROFILE

rm ./$ZIP_NAME.zip
