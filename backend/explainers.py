import numpy as np
import cv2
import matplotlib.pyplot as plt

class GradCAM:
    def __init__(self, model):
        self.model = model
        self.grad_model = self.build_grad_model()  

    def build_grad_model(self):
        # Create a model that returns the gradient and last convolutional layer output
        model_input = self.model.input
        model_output = self.model.output
        last_conv_layer = self.model.get_layer('last_conv_layer_name')  # Substitute with your last conv layer's name
        return tf.keras.Model(inputs=model_input, outputs=[model_output, last_conv_layer.output])

    def compute_gradients(self, images, class_index):
        with tf.GradientTape() as tape:
            model_output, conv_output = self.grad_model(images)
            loss = model_output[:, class_index]
        grads = tape.gradient(loss, conv_output)
        return grads, conv_output

    def generate_heatmap(self, grads, conv_output):
        # Generate a heatmap from the gradients and conv output
        pooled_grads = tf.reduce_mean(grads, axis=(0, 1, 2))
        heatmap = tf.reduce_mean(tf.multiply(pooled_grads, conv_output), axis=-1)
        heatmap = np.maximum(heatmap, 0)
        heatmap /= np.max(heatmap)
        return heatmap

    def overlay_heatmap(self, img, heatmap, alpha=0.4, colormap=cv2.COLORMAP_JET):
        # Resize heatmap to match the image size
        heatmap_resized = cv2.resize(heatmap, (img.shape[1], img.shape[0]))
        heatmap_colored = cv2.applyColorMap(np.uint8(255 * heatmap_resized), colormap)
        superimposed_img = heatmap_colored * alpha + img
        return superimposed_img

    def generate_gradcam(self, img, class_index):
        # Prepare image
        img = np.expand_dims(img, axis=0)
        grads, conv_output = self.compute_gradients(img, class_index)
        heatmap = self.generate_heatmap(grads, conv_output)
        superimposed_img = self.overlay_heatmap(img[0], heatmap)
        return superimposed_img
