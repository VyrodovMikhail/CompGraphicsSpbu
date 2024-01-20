import argparse
from ultralytics import YOLO

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-m",
        "--model_path",
        required=True,
        type=str,
        help="Path to pretrained model that predicts whether object on image is red panda or other random animal.",
    )

    parser.add_argument(
        "-i",
        "--image_path",
        required=True,
        type=str,
        help="Path to image of some animal. Model will predict whether it is red panda or other random animal.",
    )

    args = parser.parse_args()

    model = YOLO(args.model_path)

    print(model(args.image_path))
