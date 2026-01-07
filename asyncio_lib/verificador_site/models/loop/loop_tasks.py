from asyncio import create_task, to_thread, gather


class LoopTasks:

    @staticmethod
    async def execute_tasks(funcs):

        tasks_awaitable = [
            create_task(to_thread(func.get('func'), *func.get('args'))) for func in funcs
        ]

        return await gather(*tasks_awaitable, return_exceptions=True)
