import argparse

import nutrition_extractor.detection as detection
import nutrition_extractor.text_detection as text_detection


def test_detection(img_path, debug):
    detection.load_model()
    text_detection.load_text_model()
    nutrient_dict = detection.detect(img_path, debug)
    print(f"Nutritional dictionary: {nutrient_dict}")


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True,
                    help="Path to the input image")
    ap.add_argument("-d", "--debug", action='store_true', default=True,
                    help="print some debug info")
    args = ap.parse_args()

    test_detection(args.image, args.debug)
