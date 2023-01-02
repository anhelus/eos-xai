from algs.gradcam import GradCAM
from tensorflow.keras.applications import VGG16, imagenet_utils
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import numpy as np
import argparse
import imutils
import cv2
from numpy import typing as npt


def visualize(
    org_img: npt.ArrayLike,
    heatmap: npt.ArrayLike,
    title: str = '') -> None:
    """ Metodo per visualizzare i risultati di GradCAM.

    Argomenti:
        org_img: immagine originaria
        heatmap: heatmap ottenuta mediante GradCAM
        title: titolo da associare alla figura visualizzata
    """
    heatmap = cv2.resize(
        heatmap,
        (org_img.shape[1], org_img.shape[0]))
    (heatmap, output) = GradCAM.overlap(
        heatmap,
        org_img,
        alpha=0.5)
    cv2.rectangle(output, (0, 0), (340, 40), (0, 0, 0), -1)
    output = np.vstack([org_img, heatmap, output])
    output = imutils.resize(output, height=700)
    cv2.imshow(title, output)
    cv2.waitKey(0)


def run(args):
    model = VGG16(weights='imagenet')
    # Carico l'immagine mediante OpenCV. Questa
    # sarà usata per la visualizzazione.
    image = cv2.imread(args.image)
    # Carico l'immagine con Keras per il processing.
    im_array = load_img(args.image, target_size=(224, 224))
    im_array = img_to_array(im_array)
    im_array = np.expand_dims(im_array, axis=0)
    im_array = imagenet_utils.preprocess_input(im_array)
    # Predico la classe dell'immagine.
    preds = model.predict(im_array)
    pred = np.argmax(preds[0])
    # Decodifico le predizioni di ImageNet
    # per associare un'etichetta al valore numerico.
    decoded = imagenet_utils.decode_predictions(preds)
    (_, label, prob) = decoded[0][0]
    print(f'{label}: {prob*100}')
    gc = GradCAM(model, pred)
    heatmap = gc.get_heatmap(im_array)
    visualize(image, heatmap, args.title)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-i',
        '--image',
        help="Percorso dell'immagine di input",
        required=True)
    parser.add_argument(
        '-t',
        '--title',
        help="Titolo da visualizzare nell'immagine",
        default='Risultati GradCAM')
    args = parser.parse_args()
    run(args)