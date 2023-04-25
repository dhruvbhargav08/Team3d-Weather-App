import datetime
import flet 
from flet import *

def current_info(_current):
    _extra_info = []
    _extra = [
        [
            int(_current.json()["current"]["visibility"] // 1000),
            "Km",
            "Visibility",
            "../assests/visibility.png",
        ],
        [
            round(_current.json()["current"]["pressure"] * 0.03, 2),
            "inHg",
            "Pressure",
            "../assests/pressure.png",
        ],
        [
            datetime.datetime.fromtimestamp(
                _current.json()["current"]["sunrise"]
            ).strftime("%I:%M %p"),
            "",
            "Sunrise",
            "../assests/sunrise.png"
        ],
        [
            datetime.datetime.fromtimestamp(
                _current.json()["current"]["sunset"]
            ).strftime("%I:%M %p"),
            "",
            "Sunset",
            "../assests/sunset.png"
        ],

    ]
    for data in _extra:
        _extra_info.append(
            Container(
                bgcolor="white10",
                border_radius=12,
                alignment=alignment.center,
                content=Column(
                    alignment="center",
                    horizontal_alignment="center",
                    spacing=25,
                    controls=[
                        Container(
                            alignment=alignment.center,
                            content=Image(
                                src=data[3],
                                color="white",
                            ),
                            width=32,
                            height=32,
                        ),
                        Container(
                            content=Column(
                                alignment="center",
                                horizontal_alignment="center",
                                spacing=0,
                                controls=[
                                    Text(
                                        str(data[0]) + " " + data[1],
                                        size=14,
                                    ),
                                    Text(
                                        data[2],
                                        size=11,
                                        color="white54",
                                    ),
                                ],
                            ),
                        ),
                    ],
                ),
            ),
        )
    return _extra_info