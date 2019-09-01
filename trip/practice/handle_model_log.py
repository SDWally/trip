# -*- coding:utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import re


def read_log():
    # return pd.read_csv("/Users/wally/source/trip/tmp/gcae.txt")

    lines = []
    with open("/Users/wally/source/trip/tmp/gcae.txt", "r") as f:
        for line in f.readlines():
            lines.append(line)

    return lines


def handle_lines():
    common_infos = []
    eval_infos = []
    lines = read_log()
    for i, line in enumerate(lines):
        if line.startswith("E"):
            info_dic = handle_100_line(lines[i+1])

            eval_infos.append(info_dic)
        elif line.startswith("2019") or line.startswith("Saved") or line.startswith("start"):
            pass
        else:
            try:
                info_dic = handle_common_line(line[7:])
            except ValueError:
                print(line[:])
                print("some other lines")
            else:
                common_infos.append(info_dic)
    return eval_infos, common_infos


def handle_common_line(line):
    line = [l.replace(",", "").replace(":", "") for l in line.split()]
    info_dic = {k: float(v) for k, v in zip(line[::2], line[1::2])}
    return info_dic


def handle_100_line(line):
    # m = re.match(r'^*step: (\s{3}3)-(\d{3,8})$', line)
    line = line.split(",")
    info_dic = {}
    for l in line[1:]:
        words = l.split(":")
        info_dic[words[0].strip()] = float(words[1].strip())

    return info_dic


def info_to_df(eval_infos):
    eval_df = pd.DataFrame(
        eval_infos
    )
    return eval_df


def filter_df_by_loss(df):
    # print(df)
    df = df[(df["loss"] > 0.2) & (df["loss"] < 0.35)]
    return df


def filter_df_by_step(df, min, max):
    return df[(df["step"] >= min) & (df["step"] <= max)]


def draw_df(df):
    df=df.set_index("step")
    df.plot()


def find_min(df, nums=3):
    return df.sort_values(by="loss").head(nums)["step"].values


def main_draw():
    eval_info, common_info = handle_lines()
    eval_df = info_to_df(eval_info)
    common_df = info_to_df(common_info)

    # 添加下面这行，则执行过滤条件，对gcae可以过滤，对lstmae，需要改变过滤条件，否则会因数据过滤后为空报错。
    # eval_df = filter_df_by_loss(eval_df)
    draw_df(eval_df)
    for step in find_min(eval_df):
        draw_df(filter_df_by_step(common_df, step-99, step))
    plt.show()


if __name__ == '__main__':
    # line  = "2019-08-30T09:14:28.907209, step: 100, loss: 0.32191809075998096, acc: 0.9174447408536586,precision: 0.4429336994254434, recall: 0.44601245690568103, f_beta: 0.44346731439614967"
    # print()
    # print(find_min(info_to_df(handle_lines())))
    # common_line = "train: step: 1, loss: 2.407233715057373, acc: 0.2578125, recall: 0.13121003443187407, precision: 0.2277777777777778, f_beta: 0.13765404929577463"
    # print(draw_df(filter_df_by_step()))
    main_draw()
