import base64
from flask import current_app as app
from logging import getLogger

logger = getLogger(__name__)

def get_tags(image_bytes: bytes) -> list:
    """Get tags according to image.

    Args:
        image_bytes:

    Returns:

    """
    encoded_image = base64.b64encode(image_bytes)
    parameters_output = {
        'best': app.config.get('RECOGNITION_SERVICE_TAG_AMOUNT')
    }
    data = [encoded_image.decode()]
    recognition_service_name = app.config.get('RECOGNITION_SERVICE_NAME')
    post_predict_result = app.deep_detect.post_predict(
        recognition_service_name, data, {}, {}, parameters_output)
    classes = []
    try:
        results_classes = post_predict_result['body']['predictions'][0][
            'classes']
    except (KeyError, IndexError):
        logger.warning(f'Invalid answer from server: {post_predict_result}')
        return classes

    for i in results_classes:
        try:
            # delete class number
            classes.append(i['cat'].split(' ', 1)[1])
        except IndexError:
            classes.append(i['cat'])

    return classes