from xml.dom.minidom import Identified
import face_recognition as fr
from engine import get_rostos, identificar_faces

desconhecido = identificar_faces("./fotos/desconhecido.jpg")

if (desconhecido[0]):
    rosto_desconhecido = desconhecido[1][0]
    rostos_conhecidos, nomes_conhecidos = get_rostos()
    print
    resultados = fr.compare_faces(rosto_desconhecido, rostos_conhecidos)
    print(resultados)

    for i in range(len(rostos_conhecidos)):
        resultado = resultados[i]
        if resultado:
            print(f'Rosto do {nomes_conhecidos[i]} foi reconhecido')

else:
    print('NÃO FOI ENCONTRADO NENHUM ROSTO')