
months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'April',
    'September',
    'October',
    'November',
    'December'
]


def parse_date(stri:str):
    date = stri.split('-')
    return f'{date[2]} {months[int(date[1])]} {date[0]}'
