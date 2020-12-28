import time


class funcs:

    def format_date(time_stamp):
        # 转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
        time_array = time.localtime(time_stamp)
        other_style_time = time.strftime("%Y-%m-%d", time_array)

        return other_style_time


if __name__ == "__main__":
    print(funcs.format_date(1609141673000))
