import os


class Config(object):
    DD_ENDPOINT = ''
    API_ENDPOINT = ''
    AVAILABLE_IMAGE_TYPES = ['jpg', 'jpeg', 'png']

    RECOGNITION_SERVICE_HOST = os.environ.get('RECOGNITION_SERVICE_HOST',
                                              '%SERVICE_IP%')
    RECOGNITION_SERVICE_PORT = int(
        os.environ.get('RECOGNITION_SERVICE_HOST', 8049))
    RECOGNITION_SERVICE_SCHEME = os.environ.get('RECOGNITION_SERVICE_SCHEME',
                                                'https')
    RECOGNITION_SERVICE_TAG_AMOUNT = int(
        os.environ.get('RECOGNITION_SERVICE_TAG_AMOUNT', 3))
    RECOGNITION_SERVICE_NAME = os.environ.get('RECOGNITION_SERVICE_NAME',
                                              'imageserv')