from models.classroom import Classroom
from multiprocessing import cpu_count
from concurrent.futures.process import ProcessPoolExecutor


class Main:

    @staticmethod
    def main():

        best_students = []
        cpu_cores = cpu_count()

        classroom = Classroom('notas.csv')

        with ProcessPoolExecutor(cpu_cores) as executor:

            for number in range(1, (cpu_cores + 1)):

                student_amount = classroom.students_amount()

                start = round(
                    (student_amount * (number - 1)) / cpu_cores
                )

                end = round((student_amount * number) / cpu_cores)

                best_students.append(

                    executor.submit(
                        classroom.student_best_avarege, start=start, end=end
                    ).result()
                )

        best_students = list(
            map(
                lambda x: {
                    'aluno': list(x.get('aluno').values())[0],
                    'media': list(x.get('media').values())[0]
                },

                best_students
            )
        )

        best = max(best_students, key=lambda x: x.get('media'))

        return (f'O melhor estudante foi {best.get('aluno')} com {best.get('media')} de media')

if __name__ == '__main__':
    print(Main.main())
