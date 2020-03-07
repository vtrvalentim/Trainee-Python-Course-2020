def localize_objects(path):
    """Localize objects in the local image.

    Args:
    path: The path to the local file.
    """
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    with open(path, 'rb') as image_file:
        content = image_file.read()
    image = vision.types.Image(content=content)

    objects = client.object_localization(
        image=image).localized_object_annotations

    objetos = list()
    # Cria uma lista dos objetos encontrados na imagem
    for iten in objects:
        objetos.append(iten.name)

    ##
    # licensePlate = "License plate"
    # if (licensePlate in objetos):
    #     print("TEM PLACA")
    # else:
    #     print("NAO TEM PLACA")

    return objetos

    # print('Number of objects found: {}'.format(len(objects)))
    # for object_ in objects:
    #     print('\n{} (confidence: {})'.format(object_.name, object_.score))
    #     print('Normalized bounding polygon vertices: ')
    #     for vertex in object_.bounding_poly.normalized_vertices:
    #         print(' - ({}, {})'.format(vertex.x, vertex.y))

#localize_objects(r"F:\Paulo\Google Drive\Curso Python\imagens\patinete09.jpeg")