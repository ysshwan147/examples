### dataset download: COCO 2014 train images
# mkdir data
# cd data
# wget http://images.cocodataset.org/zips/train2014.zip
# unzip train2014.zip
# cd ..


### train
DATASET_PATH="./data/train2014"
STYLE_IMAGE="./images/style-images/mount.png"
WEIGHT_PATH="./weights"

python neural_style/neural_style.py train \
    --dataset $DATASET_PATH \
    --style-image $STYLE_IMAGE \
    --save-model-dir $WEIGHT_PATH \
    --epochs 2 \
    --accel \
    --content-weight 1e5 \
    --style-weight 1e12


### test
# CONTENT_IMAGE="./images/content-images/amber.jpg"
# MODEL_PATH="./weights/mount.model"
# OUTPUT_PATH="./images/output-images/amber-mount.jpg"

# python neural_style/neural_style.py eval \
#     --content-image $CONTENT_IMAGE \
#     --model $MODEL_PATH \
#     --output-image $OUTPUT_PATH \
#     --accel
