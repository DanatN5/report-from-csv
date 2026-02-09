from tabulate import tabulate

from report_from_csv.reports.average_gdp import average_gdp_report


def test_average_gdp_report():
    with open('tests/test_data/expected.txt', encoding='utf-8') as file:
        expected_result = file.read()
    
    file1 = 'tests/test_data/economic1.csv'
    file2 = 'tests/test_data/economic2.csv'
    
    data = average_gdp_report([file1, file2])

    result = tabulate(data, 
                   headers='keys', 
                   showindex=True, 
                   tablefmt="grid", 
                   floatfmt=".2f")
    
    assert result == expected_result