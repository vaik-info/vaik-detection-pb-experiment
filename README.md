# vaik-detection-pb-experiment

Create Pascal VOC xml file by inference model. Calc mAP and draw a box with score.

## Install

```shell
pip install -r requirements.txt
```

## Usage

### Create Pascal VOC xml file
```shell
python inference.py --input_saved_model_dir_path '~/.mnist_detection_model/saved_model' \
                --input_classes_path '~/.vaik-mnist-detection-dataset/classes.txt' \
                --input_image_dir_path '~/.vaik-mnist-detection-dataset/valid' \
                --output_xml_dir_path '~/.vaik-mnist-detection-dataset/valid_inference' \
                --resize_input_height 512 \
                --resize_input_width 512
```

### Calc mAP
```shell

```

### Draw box