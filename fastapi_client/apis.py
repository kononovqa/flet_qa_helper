import json

from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from fastapi_client.data import DESCRIPTION_SWAGGER, TAGS_METADATA
from autotest_requests.fake_do_something import do_something


def custom_openapi():
    api.openapi_schema = get_openapi(
        title=f"Flet QA Helper Swagger",
        version="3.1.0",
        summary=f"Вспомогательный клиент для помощи ручным тестировщикам",
        description=DESCRIPTION_SWAGGER,
        routes=api.routes,
        tags=TAGS_METADATA,
        servers=[{'url': '/api'}],
        contact={'name': 'Кононов Михаил. @KononovQA',
                 'email': 'mk@kononovqa.ru'}
    )
    return api.openapi_schema


api = FastAPI(docs_url=None)
api.openapi = custom_openapi


@api.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url="/api/openapi.json",
        title='Flet QA Helper - Swagger Ui',
        oauth2_redirect_url=api.swagger_ui_oauth2_redirect_url,
        swagger_js_url="/static/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger-ui.css",
    )


@api.get("/main_service/get_all_users", tags=['Main Service'],
         name='Получить всех пользователей')
async def get_users():
    await do_something()
    return "list users = [1, 2, 3, 4]"


@api.post("/main_service/create_user", tags=['Main Service'],
          name='Создать пользователя')
async def create_user(user_login: str):
    await do_something()
    return f'user {user_login} created'


@api.delete("/main_service/delete/{user_login}", tags=['Main Service'],
            name='Удалить пользователя')
async def delete_user(user_login: str):
    return f"User {user_login} deleted"


@api.post('/autotests/send_data', tags=['Autotests'],
          name='Отправить данные по автотестам на график')
def get_result_autotests(service_name: str, date: str, total_tests: int,
                         test_failed: int, autotests_build_id: int,
                         service_path: str = ''):
    service_name = service_name[:20]
    service_name = service_name.replace(' ', '_')
    date = date[:13]
    total_tests = 99999 if total_tests > 99999 else total_tests
    test_failed = 99999 if test_failed > 99999 else test_failed
    autotests_build_id = 99999 if autotests_build_id > 99999 else autotests_build_id
    service_path = service_path[:500]
    json_data = {'service_name': service_name,
                 'date': date,
                 'total_tests': total_tests,
                 'test_failed': test_failed,
                 'autotests_build_id': autotests_build_id,
                 'service_path': service_path}
    with open(f'allure_json_results/{service_name} '
              f'{autotests_build_id}.json', "w") as json_file:
        json.dump(json_data, json_file, ensure_ascii=False)
    return json_data
