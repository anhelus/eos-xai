from algs.gradcam import GradCAM
from tensorflow.keras.applications import VGG16, imagenet_utils
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import numpy as np
import argparse
import imutils
import cv2


def run(args):
    model = VGG16(weights='imagenet')
    # carico e ridimensiono l'immagine
    img = cv2.imread(args.image)
    resized = cv2.resize(img, (224, 224))
    image = load_img(args.image, target_size=(224, 224))
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = imagenet_utils.preprocess_input(image)
    # predizione
    preds = model.predict(image)
    i = np.argmax(preds[0])
    # decodifica delle predizioni di imagenet
    decoded = imagenet_utils.decode_predictions(preds)
    (imagenetID, label, prob) = decoded[0][0]
    print(f'{label}: {prob*100}')
    gc = GradCAM(model, i)
    heatmap = gc.get_heatmap(image)
    heatmap = cv2.resize(heatmap, (img.shape[1], img.shape[0]))
    (heatmap, output) = gc.sovrapponi(heatmap, img, alpha=0.5)
    cv2.rectangle(output, (0, 0), (340, 40), (0, 0, 0), -1)
    output = np.vstack([img, heatmap, output])
    output = imutils.resize(output, height=700)
    cv2.imshow('Risultati gradCAM', output)
    cv2.waitKey(0)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-i',
        '--image',
        help='Percorso dell\'immagine di input')
    args = parser.parse_args()
    run(args)