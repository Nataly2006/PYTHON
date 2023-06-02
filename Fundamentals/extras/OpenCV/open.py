import cv2

# Cargar el clasificador pre-entrenado para detección de rostros
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Cargar la imagen en la que se desea realizar el reconocimiento facial
image_path = 'ruta/a/la/imagen.jpg'
image = cv2.imread(image_path)

# Convertir la imagen a escala de grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Realizar la detección de rostros en la imagen
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Dibujar rectángulos alrededor de los rostros detectados
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Mostrar la imagen con los rostros detectados
cv2.imshow('Reconocimiento Facial', image)
cv2.waitKey(0)
cv2.destroyAllWindows()