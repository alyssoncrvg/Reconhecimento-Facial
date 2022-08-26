import numpy as np
import face_recognition as fr
import cv2
from engine import get_rostos

rostos_conhecidos, nomes_conhecidos = get_rostos()
camera = cv2.VideoCapture(0)
while True:
    ret, frame= camera.read()

    rgb_frame = frame[:, :, ::-1]

    localizar_faces = fr.face_locations(rgb_frame)
    rosto_desconhecidos = fr.face_encodings(rgb_frame, localizar_faces)

    for (top, rigth, bottom, left), rosto_desconhecidos in zip(localizar_faces, rosto_desconhecidos):
        resultados = fr.compare_faces(rostos_conhecidos, rosto_desconhecidos)
        print(resultados)

        distancia_rosto = fr.face_distance(rostos_conhecidos, rosto_desconhecidos)

        melhor_id = np.argmin(distancia_rosto)
        if resultados[melhor_id]:
            name = nomes_conhecidos[melhor_id]
        else:
            name = "Desconhecido"
        
        #retangulo rosto
        cv2.rectangle(frame, (left, top), (rigth, bottom), (0,0,255), 2)

        #texto abaixo
        # cv2.rectangle(frame, (left, bottom -35), (rigth, bottom), (0,0,255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_COMPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255,255,255), 1)

        cv2.imshow('Reconhecer rostos', frame)
    
    if cv2.waitKey(5) == 27:
        break

camera.release()
cv2.destroyAllWindows()