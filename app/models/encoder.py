import tensorflow as tf
from tensorflow.keras import layers

def build_encoder():
    input_layer = layers.Input(shape=(None, None, 3))
    x = layers.Conv2D(64, (3, 3), activation='relu', padding='same')(input_layer)
    x = layers.MaxPooling2D((2, 2), padding='same')(x)
    x = layers.Conv2D(128, (3, 3), activation='relu', padding='same')(x)
    x = layers.MaxPooling2D((2, 2), padding='same')(x)
    x = layers.Conv2D(256, (3, 3), activation='relu', padding='same')(x)
    latent_output = layers.GlobalAveragePooling2D()(x)
    return tf.keras.Model(input_layer, latent_output)
