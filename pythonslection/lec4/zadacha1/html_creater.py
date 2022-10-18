from user_interface import temperature_view
from user_interface import wind_speed_view
from user_interface import pressure_view


def create(device=1):
    style = 'style="font-size:30px;"'
    html = "<html>\n <head</head>\n <body>\n"
    html += '<p {}>wind ---: {} c</p>\n' \
        .format(style, wind_speed_view(device))
    html += '<p {}>temperature---: {} c</p>\n' \
        .format(style, temperature_view(device))
    html += '<p {}>pressure: {} c</p>\n' \
        .format(style, pressure_view(device))
    html += '   </body>\n</html>'
    with open('index.html', 'w') as page:
        page.write(html)

    return html
