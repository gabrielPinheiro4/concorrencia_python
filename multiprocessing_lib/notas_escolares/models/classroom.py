import pandas as pd
from const.paths import FILE_PATH
from const.lists import ATTRIBUTES


class Classroom:

    def __init__(self, file_name):

        self.df = pd.read_csv(
            f'{FILE_PATH}/csv/{file_name}', index_col=False
        )

    def students_amount(self):
        return len(self.df)

    def student_best_avarege(self, start, end):

        self.df = self.df[start:end]

        if all([attr in self.df for attr in ATTRIBUTES]):

            self.df['media'] = (
                (
                    self.df.nota_primeiro_bimestre
                    + self.df.nota_segundo_bimestre
                    + self.df.nota_terceiro_bimestre
                    + self.df.nota_quarto_bimestre
                )
                / 4
            )

            best_avarege = max(self.df.media)

            row_student = (
                self.df.loc[self.df['media'] == best_avarege]
            ).to_dict()

            return {'aluno': row_student.get('nome'), 'media': row_student.get('media')}
