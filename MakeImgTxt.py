from pathlib import Path
from PIL import Image
import numpy as np
import pandas as pd
import math


def makeChar(imgPath, width=256, charCnt=32):
    """
    convert image to charset with suffix .txt.

    :param imgPath: A path (string) of image.

    :param width: The width of output file line width.

    :param width: num of replce chars.

    :returns: make a file name with txt suffix at cwd.
    """
    path = Path(imgPath)
    img = Image.open(path)
    img = img.convert(mode="L")

    # calculate height to keep H:W rate
    height = width * img.size[1] // img.size[0]

    img = img.resize((width, height))
    array = np.array(img)
    if Path(r"xinsun_char_count.csv").exists():
        chars = pd.read_csv("xinsun_char_count.csv")\
            .drop_duplicates("count", ignore_index=True)\
            .sort_values(by="count", ascending=False)[::94//charCnt]\
            .reset_index(drop=True)["char"]
    else:
        chars = [
            '@', '%', '&', '#', 'B', '9', '6', 'S', 'D', 'A', 'd', '*', 'V',
            'b', 'q', 'a', '4', 'e', 'u', 'n', 'J', '7', '[', '1', '/', 'i',
            '"', '{', '+', "'", ';', '_'
        ]
    ln = math.ceil(255 / len(chars))
    with open(path.with_suffix(".txt"), "w+") as f:
        for row in array:
            line = []
            for x in row:
                char = chars[x // ln]
                line.append(char)
                line.append(char)
            line.append("\n")
            f.writelines(line)


if __name__ == "__main__":
    img_path = r"sample.jpg"
    makeChar(img_path)
    pass
