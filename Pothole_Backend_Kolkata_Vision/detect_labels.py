import os
import base64
credential_path = "C:/Users/GITANSHU/DjangoAPI/Pothole_Backend_Kolkata_Vision/key.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

def detect_web(path):
    flag = 0
    """Detects web annotations given an image."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()
        #my_string = base64.b64encode(content)

    image = vision.types.Image(content=content)

    response = client.web_detection(image=image)
    annotations = response.web_detection

    if annotations.best_guess_labels:
        for label in annotations.best_guess_labels:
            a = 1
            #print('\nBest guess label: {}'.format(label.label))

    if annotations.pages_with_matching_images:
        flag = 1
        #print('\n{} Pages with matching images found:'.format(len(annotations.pages_with_matching_images)))

        for page in annotations.pages_with_matching_images:
            a = 1
            #print('\n\tPage url   : {}'.format(page.url))

            if page.full_matching_images:
                a = 1
                #print('\t{} Full Matches found: '.format(len(page.full_matching_images)))

                for image in page.full_matching_images:
                    a = 1
                    #print('\t\tImage url  : {}'.format(image.url))

            if page.partial_matching_images:
                a = 1
                #print('\t{} Partial Matches found: '.format(len(page.partial_matching_images)))

                for image in page.partial_matching_images:
                    a = 1
                    #print('\t\tImage url  : {}'.format(image.url))

    if annotations.web_entities:
        a = 1
        #print('\n{} Web entities found: '.format(len(annotations.web_entities)))

        for entity in annotations.web_entities:
            a = 1
            #print('\n\tScore      : {}'.format(entity.score))
            #print(u'\tDescription: {}'.format(entity.description))

    if annotations.visually_similar_images:
        a = 1
        #print('\n{} visually similar images found:\n'.format(len(annotations.visually_similar_images)))

        for image in annotations.visually_similar_images:
            a = 1
            #print('\tImage url    : {}'.format(image.url))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

    return flag