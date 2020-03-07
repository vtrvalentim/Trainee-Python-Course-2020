# Requirements:
# Installation -> pip install google-cloud-vision
# Installation -> pip install matplotlib
# Valid account in Google Cloud and an active Vision API
# "GOOGLE_APPLICATION_CREDENTIALS" enviroment variable set to
#the path of Google Cloud Credentials .json file

def markText(path, polyCoordinates):
    """Marks text area on image"""
    import matplotlib.pyplot as plt
    import cv2 as cv

    # Load a color image
    img = cv.imread(path) # Read file
    cv.rectangle(img, polyCoordinates['upperLeft'], polyCoordinates['lowerRight'], (255, 0, 0), 2)

    # Show image
    plt.imshow(img)
    plt.show()


def readPlate(path, showPlate = True):
    """Detects text in the file."""

    from google.cloud import vision
    from google.protobuf.json_format import MessageToDict
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = MessageToDict(response)

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
    if showPlate:
        boundingBox = texts['textAnnotations'][0]['boundingPoly']['vertices']

        polyCoordinates = {}
        polyCoordinates['upperLeft'] = (boundingBox[0]['x'], boundingBox[0]['y'])
        polyCoordinates['lowerRight'] = (boundingBox[2]['x'], boundingBox[2]['y'])
        markText(path, polyCoordinates)

    return texts['fullTextAnnotation']['text'].replace("\n", " ")