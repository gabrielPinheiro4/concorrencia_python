from dotenv import load_dotenv
from os import getenv
from asyncio import run
from models.loop.loop_input import LoopInput
from models.input.input import Input
from models.requests_api.conn_api import ConnApi
from models.loop.loop_tasks import LoopTasks
from models.sites.sites import Sites
from consts.phrases import INPUT_PHRASE


class Main:

    @staticmethod
    async def main():

        load_dotenv()
        api_url = getenv('API')
        api_key = getenv('API_KEY')

        sites_to_verify = LoopInput.loop_input(
            Input.input_result, 'sair', 'str', INPUT_PHRASE
        )

        if sites_to_verify:

            conn = ConnApi(api_url, api_key)

            sites_to_verify = [
                {
                    'func': conn.request,

                    'args': ('POST', {'url': f'https://{site}', 'visibility': 'public'}, 'application/json', 'scan')
                }

                for site in sites_to_verify
            ]

            sites_uuid = await LoopTasks.execute_tasks(sites_to_verify)

            sites_response = [
                {
                    'func': conn.request,
                    'args': ('GET', None, 'application/json', 'result', f'{site.get('uuid')}')
                }

                for site in sites_uuid
            ]

            result = await LoopTasks.execute_tasks(sites_response)

            sites = Sites(result)

            sites.verify_sites()


if __name__ == '__main__':
    run(Main.main())
