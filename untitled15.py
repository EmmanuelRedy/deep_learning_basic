# -*- coding: utf-8 -*-
"""Untitled15.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-NcmM801_cGLO-WwIzvrdA-DEKH68sQv
"""

#import libraries
import numpy as np
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense,Flatten
from keras.utils import to_categorical

#load the data
(X_train,y_train),(X_test,y_test)=mnist.load_data()

#one-hot encoding
y_train=to_categorical(y_train)
y_test=to_categorical(y_test)

#build the architecture
model=Sequential()
model.add(Flatten(input_shape=(28,28)))
model.add(Dense(64,activation='relu'))
model.add(Dense(32,activation='relu'))
model.add(Dense(10,activation='softmax'))

#compile the model
model.compile(optimizer='Adam',loss='categorical_crossentropy',metrics=['accuracy'])

#train the model
model.fit(X_train,y_train,epochs=100,batch_size=64)

#compile the model
model.compile(optimizer='sgd',loss='categorical_crossentropy',metrics=['accuracy'])

#train the model
model.fit(X_train,y_train,epochs=10,batch_size=32)

model.fit(X_train,y_train,epochs=10,batch_size=16)

#evaluate
model.evaluate(X_test,y_test)

sample_images=X_test[:5]
sample_label=y_test[:5]

predictions=model.predict(sample_images)
result=np.argmax(predictions,axis=1)
print(result)