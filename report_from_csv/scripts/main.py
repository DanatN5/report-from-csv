import argparse

def main():
    description = 'Формирует отчет из csv файла'

    parser = argparse.ArgumentParser(description=description)

    parser.add_argument('--format',
                        help='принимает один или несколько путей к файлам для отчета')
    