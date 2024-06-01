import tensorflow as tf
from tensorflow.keras import layers

def build_decoder():
    latent_input = layers.Input(shape=(256,))
    x = layers.Dense(8*8*256, activation='relu')(latent_input)
    x = layers.Reshape((8, 8, 256))(x)
    x = layers.Conv2DTranspose(128, (3, 3), strides=(2, 2), activation='relu', padding='same')(x)
    x = layers.Conv2DTranspose(64, (3, 3), strides=(2, 2), activation='relu', padding='same')(x)
    output_layer = layers.Conv2D(3, (3, 3), activation='sigmoid', padding='same')(x)
    return tf.keras.Model(latent_input, output_layer)
