import argparse
from pathlib import Path

from tabulate import tabulate

from report_from_csv.reports.average_gdp import average_gdp_report

REPORTS = {
    "average-gdp": average_gdp_report
}


def csv_file(path: str) -> str:
    p = Path(path)

    if not p.exists():
        raise argparse.ArgumentTypeError(f"Файл не найден: {path}")
    
    if p.suffix.lower() != '.csv':
        raise argparse.ArgumentTypeError(f"Ожидался CSV-файл, получен: {path}")
    
    return path
    

def main() -> None:
    description = 'Формирует отчет из csv файла'

    parser = argparse.ArgumentParser(description=description)

    parser.add_argument('--files',
                        type=csv_file,
                        nargs='+',
                        required=True,
                        help='принимает один или несколько '
                        'путей к CSV-файлам для отчета',
                        )
    parser.add_argument('--report',
                        required=True,
                        help='принимает тип отчета')
    
    args = parser. parse_args()

    result = REPORTS[args.report](args.files)

    print(tabulate(result, 
                   headers='keys', 
                   showindex=True, 
                   tablefmt="grid", 
                   floatfmt=".2f"))


if __name__ == "__main__":
    main()
    