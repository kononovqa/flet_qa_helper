import json
import copy
import os

import flet as ft

from pathlib import Path

from components.chart_axis_label.chart_axis_label import ChartsAxisLabels
from components.container.container import Containers
from components.line_chart.line_chart import LineCharts
from components.line_chart.line_chart_data import LineChartDatas
from components.line_chart.line_chart_data_point import LineChartDataPoints
from components.row.row import Rows
from components.text.text import Texts
from components.text.text_span import TextSpans


def autotests_page(page):

    example_horizontal_data = ChartsAxisLabels().example_horizontal_data
    example_container = Containers().example_container
    example_linechart = LineCharts().example_linechart
    example_data_points = LineChartDatas().example_data_points
    example_linechart_data_point = LineChartDataPoints().example_linechart_data_point
    example_raw_with_linechart = Rows().example_raw_with_linechart
    example_raw_between_linecharts = Rows().example_raw_between_linecharts
    name_service = Texts().name_service
    example_horizontal_text = Texts().example_horizontal_text
    example_textspan = TextSpans().example_textspan

    page.auto_scroll = ft.ScrollMode.HIDDEN
    list_linecharts = []

    path = Path(Path(__file__).parent.parent)
    if not os.path.isdir(f'{path}/allure_json_results'):
        os.mkdir(f'{path}/allure_json_results')

    def json_samples():
        result = {}
        for path in Path(Path(__file__).parent.parent,
                         'allure_json_results').rglob('*.json'):
            result[path.stem] = open_json_payload(str(path))
        return result

    def open_json_payload(file_name: str):
        with open(file_name, 'r') as json_file:
            json_data = json.load(json_file)
        return json_data

    def get_jsons_for_services(service_name):
        jsons_data = json_samples()
        build_id = []

        for key in jsons_data.keys():
            service_name_to_check, teamcity_build_id = key.split(' ')
            if service_name_to_check == service_name:
                build_id.append(teamcity_build_id)

        build_id.sort()
        list_data_points_green = []
        list_data_points_red = []
        list_data_points_grey = []
        list_total_tests = []
        list_horizontal_data = []
        count_test_scenario = len(build_id) - 1

        for i in range(len(build_id)):
            json_to_get = jsons_data[f'{service_name} {build_id[i]}']

            new_data_point_green = copy.deepcopy(example_linechart_data_point)
            new_data_point_red = copy.deepcopy(example_linechart_data_point)
            new_data_point_grey = copy.deepcopy(example_linechart_data_point)
            new_example_horizontal_text = copy.deepcopy(example_horizontal_text)
            new_example_textspan = copy.deepcopy(example_textspan)
            new_example_horizontal_data = copy.deepcopy(example_horizontal_data)

            new_data_point_green.x = i
            new_data_point_red.x = i
            new_data_point_grey.x = i

            new_data_point_green.y = (int(json_to_get['total_tests']) -
                                      int(json_to_get['test_failed']))
            new_data_point_red.y = int(json_to_get['test_failed'])
            new_data_point_grey.y = int(json_to_get['total_tests'])

            list_total_tests.append(int(json_to_get['total_tests']))
            new_example_textspan.text = f"#{build_id[i]} {json_to_get['date']}"
            new_example_textspan.url = \
                (f"https://www.google.ru/search?q="
                 f"{json_to_get['service_path']}{build_id[i]}")

            new_example_horizontal_text.spans = [new_example_textspan]
            new_example_container = copy.deepcopy(example_container)
            new_example_container.content = new_example_horizontal_text

            new_example_horizontal_data.label = new_example_container
            new_example_horizontal_data.value = i
            list_horizontal_data.append(new_example_horizontal_data)

            list_data_points_green.append(new_data_point_green)
            list_data_points_red.append(new_data_point_red)
            list_data_points_grey.append(new_data_point_grey)

        if len(list_total_tests):
            maximum_total_tests = max(list_total_tests)
        else:
            maximum_total_tests = 0

        new_example_data_points_green = copy.deepcopy(example_data_points)
        new_example_data_points_red = copy.deepcopy(example_data_points)
        new_example_data_points_grey = copy.deepcopy(example_data_points)

        new_example_data_points_red.color = ft.colors.RED
        new_example_data_points_red.below_line_bgcolor = (
            ft.colors.with_opacity(0.5, ft.colors.RED))

        new_example_data_points_grey.color = ft.colors.GREY
        new_example_data_points_grey.below_line_bgcolor = (
            ft.colors.with_opacity(0.5, ft.colors.GREY))

        new_example_data_points_green.data_points = list_data_points_green
        new_example_data_points_red.data_points = list_data_points_red
        new_example_data_points_grey.data_points = list_data_points_grey

        new_example_data_list = [new_example_data_points_green,
                                 new_example_data_points_red,
                                 new_example_data_points_grey]

        return (new_example_data_list, maximum_total_tests, count_test_scenario,
                list_horizontal_data)

    def get_name_service(service_name):
        new_name_service = copy.deepcopy(name_service)
        new_name_service.value = service_name
        return new_name_service

    def get_value_left_boarder(maximum_total_tests):
        return [round(maximum_total_tests * 0.2),
                round(maximum_total_tests * 0.4),
                round(maximum_total_tests * 0.6),
                round(maximum_total_tests * 0.8)]

    def get_all_name_services():
        jsons_data = json_samples()
        lists_services = []
        for key in jsons_data.keys():
            service_name, _ = key.split(' ')
            lists_services.append(service_name)
        unique_services = list(set(lists_services))
        return unique_services

    unique_services = get_all_name_services()

    for service in unique_services:
        (new_example_data_list, maximum_total_tests, count_test_scenario,
         list_horizontal_data) = get_jsons_for_services(
            service)
        new_name_service = get_name_service(service)
        list_values_left_border = get_value_left_boarder(maximum_total_tests)

        new_example_list_chart = copy.deepcopy(example_linechart)
        new_example_list_chart.data_series = new_example_data_list
        new_example_list_chart.left_axis.labels = [
            ft.ChartAxisLabel(
                value=0,
                label=ft.Text(f"0", size=14, weight=ft.FontWeight.BOLD,
                              color=ft.colors.WHITE,
                              text_align=ft.TextAlign.RIGHT, offset=(-0.2, 0)),
            ),
            ft.ChartAxisLabel(
                value=list_values_left_border[0],
                label=ft.Text(f"{list_values_left_border[0]}", size=14,
                              weight=ft.FontWeight.BOLD,
                              color=ft.colors.WHITE, text_align=ft.TextAlign.RIGHT,
                              offset=(-0.2, 0)),
            ),
            ft.ChartAxisLabel(
                value=list_values_left_border[1],
                label=ft.Text(f"{list_values_left_border[1]}", size=14,
                              weight=ft.FontWeight.BOLD,
                              color=ft.colors.WHITE, text_align=ft.TextAlign.RIGHT,
                              offset=(-0.2, 0)),
            ),
            ft.ChartAxisLabel(
                value=list_values_left_border[2],
                label=ft.Text(f"{list_values_left_border[2]}", size=14,
                              weight=ft.FontWeight.BOLD,
                              color=ft.colors.WHITE, text_align=ft.TextAlign.RIGHT,
                              offset=(-0.2, 0)),
            ),
            ft.ChartAxisLabel(
                value=list_values_left_border[3],
                label=ft.Text(f"{list_values_left_border[3]}", size=14,
                              weight=ft.FontWeight.BOLD,
                              color=ft.colors.WHITE, text_align=ft.TextAlign.RIGHT,
                              offset=(-0.2, 0)),
            ),
            ft.ChartAxisLabel(
                value=maximum_total_tests,
                label=ft.Text(f"{maximum_total_tests}", size=14,
                              weight=ft.FontWeight.BOLD, color=ft.colors.WHITE,
                              text_align=ft.TextAlign.RIGHT, offset=(-0.2, 0)),
            ),
        ]

        new_example_list_chart.bottom_axis = ft.ChartAxis(
            labels=list_horizontal_data,
            labels_size=32,
            labels_interval=1
        )
        new_example_list_chart.top_axis = ft.ChartAxis(title=new_name_service,
                                                       title_size=40,
                                                       labels_size=0)
        new_example_list_chart.max_x = count_test_scenario
        new_example_list_chart.max_y = maximum_total_tests

        new_example_raw_with_linechart = copy.deepcopy(example_raw_with_linechart)
        new_example_raw_with_linechart.controls = [new_example_list_chart]
        list_linecharts.append(new_example_raw_with_linechart)
        list_linecharts.append(example_raw_between_linecharts)

    def resize():
        width_page = int(page.width)
        if width_page < 1330:
            width_linechart = width_page - 40
        else:
            width_linechart = 1309
        for linechart in list_linecharts:
            linechart.width = width_linechart
    resize()

    async def page_resize(e):
        resize()
        await page.update_async()

    page.on_resize = page_resize

    content = ft.Column(list_linecharts)

    return content
