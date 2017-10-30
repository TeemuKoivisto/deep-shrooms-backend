#!/bin/bash

# Resizes images to 256x256 of target folder to a new folder inside specific image-folder.
# Requires Imagemagick to run.

TARGET_DIR=$1
OUTPUT_DIR=$2
IMG_DIR=$3

if [ -z "$TARGET_DIR" ]; then
  echo "Missing first argument TARGET_DIR. It should be the target folder you're trying to resize."
  exit 0
fi
if [ -z "$OUTPUT_DIR" ]; then
  echo "Missing second argument OUTPUT_DIR. It should be the name of the output folder."
  exit 0
fi
if [ -z "$IMG_DIR" ]; then
  echo "Missing third argument IMG_DIR. It should be the name of the folder containing images inside output-folder."
  exit 0
fi

cp -r ./$TARGET_DIR ./$OUTPUT_DIR
magick mogrify -resize 256x256 -gravity center -extent 256x256 ./$OUTPUT_DIR/$IMG_DIR/*.jpg