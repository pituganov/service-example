from bottle import route, run, request, response, HTTPResponse
from utils import CONFIG
from dotenv import load_dotenv
from os import getenv
import logging

load_dotenv()

api_logger = logging.getLogger('api')
info_logger = logging.getLogger('api.service_info')


@route('/', method='GET')
@route('/', method='OPTIONS')
def index():
    """
    Метод показывающий что сервис работает, с выводом отладочной информации
    """
    return '<h1>API service is running!</h1>'


@route('/post', method='POST')
def example_post():
    """
    Пример POST запроса с получением JSON значений

    http://127.0.0.1:8080/post
    """
    response.content_type = 'application/json'
    try:
        data = request.json
        name = data["name"]
        result = {'message': f'Hello {name}'}
        api_logger.info(f'post: {name}')
    except Exception as error:
        # Выводим тип ошибки и саму ошибку
        api_logger.error(f'{str(type(error))}: {str(error)}')
        return HTTPResponse(status=400, body={'error': str(error)})

    return result


if __name__ == '__main__':
    info_logger.info(f'Api started with secret: {getenv("VERY_SECRET_VALUE")}')
    info_logger.info(f'Version: {CONFIG["info"]["api_version"]}')

    run(host='0.0.0.0', port=8080, reload=True, debug=CONFIG["info"]["debug"])
