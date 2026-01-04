class Input:

    @staticmethod
    def input_result(type, phrase):

        input_res = input(phrase)

        return str(input_res) if type == 'str' else input_res
