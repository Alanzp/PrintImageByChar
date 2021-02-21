from PIL import Image, ImageFont, ImageDraw
import numpy as np
import pandas as pd


def CalCharCount(startUnicodeID=33, endUnicodeID=127, fontFile="simsun.ttc"):
    '''
    calculate how many pixel use to draw a 36 size char in 72X72 area.
    the count will reflict occupy dense area of char.

    :return a dict with unicodeID,char,count.

    :Param startUnicodeID :start of calculate unicode id.

    :Param startUnicodeID :end of calculate unicode id.

    :Param fontFile       :font file name with suffix,it can be find in path
    like 'C:\\Windows\\Fonts',recommond use equalWidth font(occupy same width
    for every char).
    '''
    char_point_count = {"unicodeID": [], "char": [], "count": []}
    for idx in range(startUnicodeID, endUnicodeID):
        temp = Image.new(mode="L", size=(72, 72))
        font = ImageFont.truetype('simsun.ttc', 36)
        draw = ImageDraw.Draw(temp)
        draw.text((10, 10), chr(idx), font=font, fill=(255))
        x = np.array(temp)
        cnt = np.count_nonzero(x)
        print(idx, "\t", f"{chr(idx)}", "\t", cnt)
        char_point_count["unicodeID"].append(idx)
        char_point_count["char"].append(chr(idx))
        char_point_count["count"].append(cnt)
    return char_point_count


if __name__ == "__main__":
    char_point_count = CalCharCount()
    char_cnt = pd.DataFrame(char_point_count)
    char_cnt.to_csv("xinsun_char_count.csv", index=False)
    pass
