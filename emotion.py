import os
import io
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:/Users/Ann Rose/Downloads/sample.json"

def detect_properties(path):
    """Detects image properties in the file."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.image_properties(image=image)
    props = response.image_properties_annotation
    print('Properties:')
    data=''
    for color in props.dominant_colors.colors:
        data=data+('fraction: {}'.format(color.pixel_fraction))
        data=data+('\tr: {}'.format(color.color.red))
        data=data+('\tg: {}'.format(color.color.green))
        data=data+('\tb: {}'.format(color.color.blue))
        data=data+('\ta: {}'.format(color.color.alpha))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
    
    return data
