import dlib
import cv2
import os 
import face_recognition
import struct
import numpy as np
from database import DataBase
from querys import Querys

class register:

    def __init__(self,):
        self.querys = Querys()
        self.database = DataBase()

        self.path_dir="./img"
        self.path_dir="data"


    def regitro_usuarios(self, document_number, names, last_names, gender):
            path_img = os.path.join(self.path_dir, self.name_dir)
            if not os.path.exists(path_img):
                os.makedirs(path_img) 

            # Iniciamos la captura de frames en tiempo real
            cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

            # Determinamos si se encuentra una cara en el frame capturado
            detector = dlib.get_frontal_face_detector()

            # Creamos una variable, la cual tendrá la función de determinar la cantidad de frames a capturar
            cont = 0

            while True:
                ret, frame = cap.read()
                if ret == False:
                    break

                # Convertimos la imagen a escala de grises
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                # Comprobamos que en la imagen se encuentre un rostro
                faces = detector(gray)
                if faces is not None:

                    # Iteramos sobre el rostro para determinar sus dimensiones y coordenadas
                    for face in faces:
                        x, y, w, h = face.left(), face.top(), face.width(), face.height()
                        
                        # Redimensionamos el rostro
                        face = cv2.resize(frame[y:y + h, x:x + w], (224, 224))

                        # Guardamos el rostro capturado en una carpeta llamada 'data'
                        cv2.imwrite(path_img + '/rostros_{}.jpg'.format(document_number), face)

                    # Iteramos sobre el rostro para determinar sus dimensiones y coordenadas
                    for face in faces:
                        x, y, w, h = face.left(), face.top(), face.width(), face.height()
                        
                        # Redimensionamos el rostro
                        face = cv2.resize(frame[y:y + h, x:x + w], (224, 224))

                        try:
                            # Vector embedding con face-recognition
                            embedding = face_recognition.face_encodings(face)[0]

                        except Exception as e:
                            print(f"Error al identificar un rostro: {e}")

                        # Vector embedding con deepface
                        #embedding = DeepFace.extract_faces(face)[0]

                        # Convertimos el vector embedding en un array de bytes
                        byte_array = bytearray(struct.pack("f" * len(embedding), *embedding))
                        
                        #Trasladamos el array de bytes a un formato hexadecimal
                        hexadecimal = byte_array.hex()
                    
                        # Establecemos conexión con la base de datos
                        self.database.connect()

                        # Ejecutamos la sentencia SQL para crear el registro en la base de datos
                        cursor = self.database.get_cursor()
                        cursor.execute(self.querys.insert_user(document_number, names, last_names, hexadecimal, gender))

                        # Confirmamos los cambios realizados en la base de datos
                        save = self.database.connection
                        save.commit()

                        cont +=1

                        if save:
                            print("Sentencia ejecutada correctamente.")
                        else:
                            print("No se puedo ejecutar la sentencia.")

                        # Terminamos la conexión con la base de datos
                        self.database.disconnect()

                else:
                    print("No se encontro un rostro")

                # Terminamos el ciclo cuando se haya encontrado un rostro
                if cont == 1:
                    break
                cap.release()
                cv2.destroyAllWindows()
