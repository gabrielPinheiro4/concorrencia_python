class LoopInput:

    @staticmethod
    def loop_input(func, stop_word, *args):

        final_result = []

        user_input = ''

        while user_input.lower().strip() != stop_word:
            user_input = func(*args)

            if user_input.lower().strip() != stop_word:
                final_result.append(user_input)

        return final_result
