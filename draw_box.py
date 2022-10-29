import argparse
import os


def main(input_image_dir_path, input_label_dir_path, input_classes_path, output_image_dir_path):
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='draw box')
    parser.add_argument('--input_image_dir_path', type=str, default='~/.vaik-mnist-detection-dataset/valid')
    parser.add_argument('--input_label_dir_path', type=str, default='~/.vaik-mnist-detection-dataset/valid_inference')
    parser.add_argument('--input_classes_path', type=str, default='~/.vaik-mnist-detection-dataset/classes.txt')
    parser.add_argument('--output_image_dir_path', type=str, default='~/.vaik-mnist-detection-dataset/valid_inference')
    args = parser.parse_args()

    args.input_image_dir_path = os.path.expanduser(args.input_image_dir_path)
    args.input_label_dir_path = os.path.expanduser(args.input_label_dir_path)
    args.input_classes_path = os.path.expanduser(args.input_classes_path)
    args.output_image_dir_path = os.path.expanduser(args.output_image_dir_path)

    main(**args.__dict__)
