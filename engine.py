import face_recognition as fr

def identificar_faces(foto_url):
    foto = fr.load_image_file(foto_url)
    rostos = fr.face_encodings(foto)
    if (len(rostos) > 0):
        return True, rostos
    
    return False, []

def get_rostos():
    rostos_conhecidos = []
    nomes_conhecidos = []

    alysson1 = identificar_faces("./fotos/alysson.jpg")

    if(alysson1[0]):
        rostos_conhecidos.append(alysson1[1][0])
        nomes_conhecidos.append("Alysson")

    return rostos_conhecidos, nomes_conhecidos