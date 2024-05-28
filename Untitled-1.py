from tensorflow.keras.applications import VGG16

base_model = VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))



for layer in base_model.layers:
    layer.trainable = False



from tensorflow.keras.models import Model
from tensorflow.keras.layers import Flatten, Dense

x = Flatten()(base_model.output)
x = Dense(256, activation='relu')(x)
predictions = Dense(num_classes, activation='softmax')(x)

model = Model(inputs=base_model.input, outputs=predictions)



model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])




features = base_model.predict(input_data)


