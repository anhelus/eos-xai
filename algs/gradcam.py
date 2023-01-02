from tensorflow.keras.models import Model
import tensorflow as tf
import numpy as np
import cv2


class GradCAM():
    """ Implementa il metodo GradCAM.

    Attributi:
        * base_model: modello base
        * cls_idx: indice di classe usato per le
            class activation map
        * layer_name: nome dell'ultimo layer 
            convoluzionale
    """

    def __init__(
        self,
        base_model: Model,
        cls_idx: int,
        layer_name: str = None):
        self.base_model = base_model
        self.cls_idx = cls_idx
        self.layer_name = layer_name
    
    @property
    def layer_name(self):
        return self.__layer_name
    
    @layer_name.setter
    def layer_name(self, value):
        if value is None:
            self.__layer_name = GradCAM.get_conv_layer(self.base_model)
        else:
            self.__layer_name = value
    
    @staticmethod
    def get_conv_layer(model: Model):
        """ Trova l'ultimo layer convoluzionale.

        Funzione che trova l'ultimo layer convoluzionale
        ciclando alc ontrario sui layer della rete.
        """
        for layer in reversed(model.layers):
            if len(layer.output_shape) == 4:
                return layer.name
        raise ValueError('Il modello non ha un layer convoluzionale.')
    
    def get_heatmap(self, image):
        """ Calcola la mappa di attivazione mediante GradCAM
        """
        # creiamo il modello per l'explainability
        expl_model = Model(
            inputs=[self.base_model.inputs],
            outputs=[
                self.base_model.get_layer(self.layer_name).output,
                self.base_model.output
            ])
        # calcoliamo le predizioni del modello
        with tf.GradientTape() as tape:
            inputs = tf.cast(image, tf.float32)
            (conv_out, preds) = expl_model(inputs)
            loss = preds[:, self.cls_idx]
        # calcolo i gradienti
        grads = tape.gradient(loss, conv_out)
        # calcolo i guided grads
        guided_grads = tf.cast(conv_out > 0, tf.float32) \
            * tf.cast(grads > 0, tf.float32) * grads
        # rimuoviamo la dimensione relativa al batch (non necessaria)
        conv_out = conv_out[0]
        guided_grads = guided_grads[0]
        # calcolo media dei gradienti
        weights = tf.reduce_mean(guided_grads, axis=(0, 1))
        # calcolo la media pesata dei filtri 
        # convoluzionali rispetto ai pesi
        cam = tf.reduce_sum(tf.multiply(weights, conv_out), axis=-1)
        # rescaling della CAM alle dimensioni originarie dell'immagine
        (w, h) = (image.shape[2], image.shape[1])
        heatmap = cv2.resize(cam.numpy(), (w, h))
        # normalizzazione della heatmap
        heatmap = (heatmap - np.min(heatmap)) / ((heatmap.max() - heatmap.min()) + 1e-18)
        return (heatmap * 255).astype('uint8')
    
    @staticmethod
    def overlap(
        heatmap,
        image,
        alpha: float = 0.5,
        cmap: int = cv2.COLORMAP_JET):
        """
        """
        heatmap = cv2.applyColorMap(heatmap, cmap)
        output = cv2.addWeighted(image, alpha, heatmap, 1-alpha, 0)
        return (heatmap, output)
