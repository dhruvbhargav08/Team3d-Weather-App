from flet import *
from math import pi
import call
import animation 
import current_extra
import current_temp
import bot_data
def main(page: Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    City = ""
    def update_city_name(new_value):
        nonlocal City
        City = new_value.data

    def btn_click(e):
        nonlocal City
        city=City
        _current = call.calling(City)

        def _expand(e):
            if e.data == "true":
                _show.content.controls[1].height = 560
                _show.content.controls[1].update()
            else:
                _show.content.controls[1].height = 600 * 0.46
                _show.content.controls[1].update()

        def _top():
            _today =current_temp.temp(_current)
            _today_extra = GridView(
                max_extent=150,
                expand=1,
                run_spacing=5,
                spacing=5,
            )
            for info in current_extra.current_info(_current):
                _today_extra.controls.append(info)
            top = Container(
                width=310,
                height=600 * 0.46,
                gradient=LinearGradient(
                    begin=alignment.bottom_left,
                    end=alignment.top_right,
                    colors=["lightblue600", "lightblue900"],
                ),
                border_radius=35,
                animate=animation.Animation(
                    duration=450,
                    curve="decelerate"
                ),
                on_hover=lambda e: _expand(e),
                padding=15,
                content=Column(
                    alignment="start",
                    spacing=10,
                    controls=[
                        Row(
                            alignment="center",
                            controls=[
                                Text(
                                    f"{city.title()}",
                                    size=16,
                                    width="w500",
                                ),
                            ],
                        ),
                        Container(
                            padding=padding.only(
                                bottom=5
                            ),
                        ),
                        Row(
                            alignment="center",
                            spacing=30,
                            controls=[
                                Column(
                                    controls=[
                                        Container(
                                            width=90,
                                            height=90,
                                            image_src="../assests/cloudy.png",
                                        ),
                                    ],
                                ),
                                Column(
                                    spacing=5,
                                    horizontal_alignment="center",
                                    controls=[
                                        Text(
                                            "Today",
                                            size=16,
                                            text_align="center",
                                        ),
                                        Row(
                                            vertical_alignment="start",
                                            spacing=0,
                                            controls=[
                                                Container(
                                                    content=Text(
                                                        str(_today[0]) + "°",
                                                        size=52,
                                                    ),
                                                ),
                                                Container(
                                                    content=Text(
                                                        "",
                                                        size=28,
                                                        text_align="center",
                                                    ),
                                                ),
                                            ],
                                        ),
                                        Text(
                                            _today[1] + " - Overcast",
                                            size=10,
                                            color="white54",
                                            text_align="center",
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        Divider(
                            height=8,
                            thickness=1,
                            color="white10",
                        ),
                        Row(
                            alignment="spaceAround",
                            controls=[
                                Container(
                                    content=Column(
                                        horizontal_alignment="center",
                                        spacing=2,
                                        controls=[
                                            Container(
                                                alignment=alignment.center,
                                                content=Image(
                                                    src="../assests/wind.png",
                                                    color="white",
                                                ),
                                                width=20,
                                                height=20,
                                            ),
                                            Text(
                                                str(_today[2]) + "km/h",
                                                size=11,
                                            ),
                                            Text(
                                                "Wind",
                                                size=9,
                                                color="white54",
                                            ),
                                        ],
                                    ),
                                ),
                                Container(
                                    content=Column(
                                        horizontal_alignment="center",
                                        spacing=2,
                                        controls=[
                                            Container(
                                                alignment=alignment.center,
                                                content=Image(
                                                    src="../assests/humidity.png",
                                                    color="white",
                                                ),
                                                width=20,
                                                height=20,
                                            ),
                                            Text(
                                                str(_today[3]) + "%",
                                                size=11,
                                            ),
                                            Text(
                                                "Humidity",
                                                size=9,
                                                color="white54",
                                            ),
                                        ],
                                    ),
                                ),
                                Container(
                                    content=Column(
                                        horizontal_alignment="center",
                                        spacing=2,
                                        controls=[
                                            Container(
                                                alignment=alignment.center,
                                                content=Image(
                                                    src="../assests/celsius.png",
                                                    color="white",
                                                ),
                                                width=20,
                                                height=20,
                                            ),
                                            Text(
                                                str(_today[4]) + "°",
                                                size=11,
                                            ),
                                            Text(
                                                "Feels Like",
                                                size=9,
                                                color="white54",
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                        ),
                        _today_extra,
                    ],
                ),
            )
            return top

        def new_city(e):
            page.go("/")
            del dictt["/show"]

        def _bottom():
            _bot_column = Column(
                alignment="center",
                horizontal_alignment="center",
                spacing=25,
            )
            for data in bot_data.bot_data(_current):
                _bot_column.controls.append(data)
            bottom = Container(
                alignment=alignment.center,
                content=Column(
                    controls=[
                        Container(
                            margin=margin.only(top=270),
                            padding=padding.only(top=20, left=20, right=20, bottom=20),
                            content=_bot_column
                        ),
                        Container(
                            expand=5,
                            border_radius=35,
                            alignment=alignment.center,
                            content=ElevatedButton(
                                "Change City",
                                bgcolor="transparent",
                                color="white",
                                on_click=new_city
                            ),
                        ),
                    ],
                )
            )
            return bottom

        _show = Container(
            width=310,
            height=660,
            border_radius=35,
            bgcolor="black",
            padding=10,
            content=Stack(
                width=210,
                height=550,
                controls=[
                    _bottom(),
                    _top(),

                ],
            ),
        )
        if "/show" not in dictt.keys():
            dictt['/show'] = View(
                horizontal_alignment="center",
                vertical_alignment="center",
                route='/show',
                controls=[
                    _show,
                ]
            )
        page.go("/show")
    _input = Container(
        width=310,
        height=660,
        gradient=LinearGradient(
            begin=alignment.bottom_left,
            end=alignment.top_right,
            colors=["black", "black"],
        ),
        border_radius=35,
        padding=10,
        content=Stack(
            width=210,
            height=550,
            controls=[
                Container(
                    content=Column(
                        controls=[
                            Container(
                                width=310,
                                height=100,
                                alignment=alignment.center,
                                content=Stack(
                                    controls=[
                                        Container(
                                            width=48,
                                            height=48,
                                            border=border.all(2.5, "#e9665a"),
                                            bgcolor=None,
                                            border_radius=2,
                                            rotate=transform.Rotate(0, alignment.center),
                                            animate_rotation=animation.Animation(700, "easeInOut"),
                                        ),
                                        Container(
                                            width=48,
                                            height=48,
                                            border=border.all(2.5, "#7df6dd"),
                                            bgcolor="#23262a",
                                            border_radius=2,
                                            rotate=transform.Rotate(pi / 4, alignment.center),
                                            animate_rotation=animation.Animation(700, "easeInOut"),
                                        ),
                                    ],
                                ),
                            ),
                            Container(
                                alignment=alignment.center,
                                content=Column(
                                    controls=[
                                        Container(
                                            alignment=alignment.center,
                                            content=Column(
                                                controls=[
                                                    Text(
                                                        "Weathy",
                                                        text_align="center",
                                                        size=20,
                                                    ),
                                                ],
                                            ),
                                        ),
                                        Container(
                                            alignment=alignment.center,
                                            content=Column(
                                                controls=[
                                                    Text(
                                                        "Your Weather Buddy",
                                                        text_align="center",
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                ),
                            ),
                            Container(
                                margin=margin.only(top=50),
                                height=40,
                                border=border.only(bottom=border.BorderSide(0.5, "white")),
                                content=Row(
                                    controls=[
                                        Icon(
                                            name=icons.ADD_LOCATION,
                                            size=20,
                                            opacity=0.8,
                                        ),
                                        TextField(
                                            border_radius=35,
                                            border_width=0,
                                            width=200,
                                            label="Enter city name",
                                            color="white54",
                                            on_change=update_city_name,
                                        ),
                                    ],
                                ),
                            ),
                            Container(
                                margin=margin.only(top=10),
                                border_radius=35,
                                alignment=alignment.center,
                                content=ElevatedButton(
                                    "Show",
                                    bgcolor="transparent",
                                    color="white",
                                    on_click=btn_click,
                                ),
                            ),
                        ],
                    ),
                ),
            ],
        ),
    )
    dictt = {
        '/': View(
            horizontal_alignment="center",
            vertical_alignment="center",
            route='/',
            controls=[
                _input,
            ],
        ),
    }
    def route_change(route):
        page.views.clear()
        page.views.append(
            dictt[page.route]
        )

    page.title = "Weathy"
    page.on_route_change = route_change
    page.go('/')
    animation.animation(dictt)
if __name__=='__main__':
    app(target=main, assets_dir="assests")
