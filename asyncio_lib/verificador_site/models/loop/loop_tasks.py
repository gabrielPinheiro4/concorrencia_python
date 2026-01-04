from asyncio import create_task, to_thread


class LoopTasks:

    @staticmethod
    async def create_tasks(funcs):

        tasks_awaitable = []

        for func in funcs:
            tasks_awaitable.append(
                create_task(to_thread(func.get('func'), *func.get('args')))
            )

        return tasks_awaitable

    @staticmethod
    async def execute_tasks(tasks):

        results = []

        for task in tasks:
            results.append(await task)

        return results
