def average_gdp_report(lines: list[dict]) -> list[dict]:
    data: dict = {}
    for line in lines:
        if line['country'] in data.keys():
            country = line['country']
            data[country]['years'] += 1
            data[country]['gdp'] += float(line['gdp'])
            data[country]['average_gdp'] = data[country]['gdp']/data[country]['years']
        else:
            data[line['country']] = {
                'years': 1,
                'gdp': float(line['gdp']),
                'average_gdp': float(line['gdp'])
            }

    report = [{'country': country, 'average_gdp': info['average_gdp']} 
              for country, info in data.items()]
    
    return report
    
