from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Flatten

# Build Model

model = Sequential()

model.add(
    Flatten(
        input_shape=(128, 128, 3)
    )
)

model.add(
    Dense(
        128,
        activation="relu"
    )
)

model.add(
    Dense(
        2,
        activation="softmax"
    )
)

model.summary()

print(
    "Brain Tumor Detection Model Ready"
)