import argparse
from ultralytics import YOLO

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    dataset_help_str = """
    path to dataset for training, validation and test.
    To see correct dataset format visit this link:
    https://docs.ultralytics.com/datasets/classify/.
    """

    parser.add_argument(
        "-d",
        "--dataset",
        required=True,
        type=str,
        help=dataset_help_str,
    )

    parser.add_argument(
        "-e",
        "--epochs_count",
        required=True,
        type=int,
        help="Number of epochs for training model",
    )

    parser.add_argument(
        "-img_size",
        "--image_size",
        required=True,
        type=int,
        help="Desired size of each image in pixels during model training and evaluating.",
    )

    args = parser.parse_args()

    # Load pretrained model
    model = YOLO("yolov8n-cls.pt")

    results = model.train(
        data=args.dataset, epochs=args.epochs_count, imgsz=args.image_size
    )
