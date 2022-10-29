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
                --resize_input_width 512 \
                --score_th 0.2 \
                --nms_th 0.5
```

#### Output

![Screenshot from 2022-10-29 16-18-56](https://user-images.githubusercontent.com/116471878/198819253-0c56c4f5-6e5f-4d7a-99ad-ab49dec985b0.png)

-----

### Calc mAP

```shell
python calc_map.py --answer_label_dir_path '~/.vaik-mnist-detection-dataset/valid' \
                --inference_label_dir_path '~/.vaik-mnist-detection-dataset/valid_inference' \
                --classes_txt_path '~/.vaik-mnist-detection-dataset/classes.txt'
```

#### Output

``` text
## CSV Format
"class", "iou_th", "ap",  "precision",  "recall", "num" 
"mAP(ALL)", "0.9112",  "",  "", ""
"zero", "0.5", "0.9327", "0.9890", "0.4998", "112", 
"one", "0.5", "0.9672", "0.9958", "0.5082", "82", 
"two", "0.5", "0.9638", "0.9921", "0.4983", "107", 
"three", "0.5", "0.9501", "0.9995", "0.4854", "106", 
"four", "0.5", "0.9685", "0.9843", "0.5260", "76", 
"five", "0.5", "0.9604", "0.9995", "0.4995", "79", 
"six", "0.5", "0.9206", "0.9868", "0.4889", "86", 
"seven", "0.5", "0.9503", "0.9994", "0.4942", "95", 
"eight", "0.5", "0.9595", "0.9986", "0.4987", "111", 
"nine", "0.5", "0.9662", "0.9940", "0.5093", "69", 
```

----

### Draw box

```shell
python draw_box.py --input_image_dir_path '~/.vaik-mnist-detection-dataset/valid' \
                --input_label_dir_path '~/.vaik-mnist-detection-dataset/valid_inference' \
                --input_classes_path '~/.vaik-mnist-detection-dataset/classes.txt' \
                --output_image_dir_path '~/.vaik-mnist-detection-dataset/valid_inference_draw'
```

#### Output

![valid_000000034 jpg](https://user-images.githubusercontent.com/116471878/198824432-53eb0f31-255b-4c87-9147-f255ea48be9f.png)
![valid_000000035 jpg](https://user-images.githubusercontent.com/116471878/198824436-cf78def9-eb50-4ec1-a5cd-7c9f26ff05ac.png)