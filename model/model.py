import tensorflow as tf
import tensorflow_datasets as tfds


(train_data, test_data), ds_info = tfds.load(
    'mnist',
    split=['train', 'test'],
    shuffle_files=True,
    as_supervised=True,
    with_info=True,
)

def normalize_img(image, label):
  """Normalizes images: `uint8` -> `float32`."""
  return tf.cast(image, tf.float32) / 255., label

train_data = train_data.map(normalize_img, num_parallel_calls=tf.data.AUTOTUNE)
train_data = train_data.cache()
train_data = train_data.shuffle(ds_info.splits['train'].num_examples)
train_data = train_data.batch(128)
train_data = train_data.prefetch(tf.data.AUTOTUNE)

test_data = test_data.map(normalize_img, num_parallel_calls=tf.data.AUTOTUNE)
test_data = test_data.batch(128)
test_data = test_data.cache()
test_data = test_data.prefetch(tf.data.AUTOTUNE)


model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)), 
    tf.keras.layers.Dense(128, activation="relu"), 
    tf.keras.layers.Dense(10)
])

model.compile(
    optimizer = tf.keras.optimizers.Adam(0.01), 
    loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True), 
    metrics = [tf.keras.metrics.SparseCategoricalAccuracy()], 
)

model.fit(train_data, epochs=20, validation_data=test_data)
