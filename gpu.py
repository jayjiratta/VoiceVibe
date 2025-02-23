import tensorflow as tf

print("Num GPUs Available:", len(tf.config.list_physical_devices('GPU')))
print("TensorFlow Version:", tf.__version__)

# List GPUs
for device in tf.config.list_physical_devices('GPU'):
    print("GPU detected:", device)
