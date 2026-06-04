"""Apply v4 D 维变更到 matrix.md
读取 5 份 audit 文件，提取 v3→v4 变更，应用到 matrix.md
"""
import re
from pathlib import Path

# v3 矩阵路径
MATRIX_PATH = Path("data/clusters/matrix.md")

# v4 变更清单（按组+人物组织）
CHANGES = {
    # Group 1: domestic_cn (13 人)
    "高文": [("D4", 1, 0)],
    "黄铁军": [],
    "贾佳亚": [],
    "林达华": [("D3", 3, 2)],
    "刘铁岩": [],
    "刘知远": [("D2", 1, 2)],
    "孙茂松": [("D4", 1, 0)],
    "唐杰": [("D2", 1, 2)],
    "汤晓鸥": [],
    "张钹": [("D4", 1, 0)],
    "张亚勤": [("D1", 1, 2), ("D4", 2, 1), ("D6", 2, 1)],
    "周志华": [("D4", 1, 0)],
    "朱军": [],
    # Group 2: academic (10 人)
    "Hinton": [],
    "LeCun": [],
    "Bengio": [],
    "He Kaiming": [("D4", 1, 0)],
    "Li Feifei": [("D4", 2, 3), ("D6", 1, 2)],
    "E Weinan": [],
    "Zhu Songchun": [],
    "Xie Saining": [("D3", 3, 2)],
    "Yan Shuicheng": [],
    "Zhang Xiangyu": [("D4", 1, 0)],
    # Group 3: industry (10 人)
    "Ian Goodfellow": [("D5", 0, 1), ("D6", 1, 0)],
    "Ilya Sutskever": [],
    "Jeff Dean": [],
    "李航": [("D5", 0, 1), ("D8", 3, 2)],
    "沈向洋": [],
    "田奇": [("D6", 2, 3)],
    "王海峰": [("D4", 1, 0), ("D6", 3, 2)],
    "Xuedong Huang": [("D4", 1, 0)],
    "张正友": [("D1", 1, 2), ("D6", 2, 3)],
    "周靖人": [("D4", 1, 0), ("D6", 1, 2)],
    # Group 4: entrepreneur_cn (16 人)
    "余凯": [("D3", 2, 1), ("D6", 2, 3), ("D7", 2, 3)],
    "印奇": [("D3", 1, 0), ("D6", 1, 2), ("D7", 2, 3), ("D8", 1, 2)],
    "张一鸣": [("D3", 1, 0), ("D6", 1, 2), ("D7", 1, 2)],
    "张林峰": [("D5", 0, 1), ("D8", 1, 2)],
    "朱珑": [("D6", 1, 2), ("D7", 2, 3)],
    "李开复": [],
    "杨植麟": [("D1", 3, 2), ("D3", 2, 1)],
    "梁文锋": [("D3", 1, 0)],
    "王小川": [("D2", 1, 2), ("D3", 1, 0), ("D6", 1, 2), ("D7", 2, 3)],
    "王慧文": [],
    "闫俊杰": [("D3", 1, 0), ("D6", 1, 2), ("D7", 2, 3), ("D8", 2, 3)],
    "陈天石": [("D6", 3, 2), ("D7", 1, 2)],
    "雷军": [("D2", 1, 2), ("D3", 1, 0)],
    "姜大昕": [("D1", 0, 1), ("D6", 1, 2), ("D7", 1, 2), ("D8", 1, 2)],
    "张鹏": [("D3", 1, 0), ("D8", 1, 2)],
    "王兴兴": [("D8", 1, 3)],
    # Group 5: entrepreneur_mixed (11 人)
    "Aidan Gomez": [],
    "Andrej Karpathy": [],
    "Andrew Ng": [("D6", 1, 2)],
    "Chris Olah": [("D5", 0, 1)],
    "Dario Amodei": [("D1", 1, 2)],
    "Demis Hassabis": [("D6", 1, 2)],
    "Nick Bostrom": [("D6", 0, 2)],
    "Paul Christiano": [],
    "Rich Sutton": [],
    "Sam Altman": [("D1", 1, 0), ("D6", 1, 2)],
    "Stuart Russell": [("D6", 2, 3)],
}

# D 维列顺序
D_COLS = ["D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8"]


def apply_changes_to_matrix():
    """读 matrix.md, 按变更清单改分数, 重算总分, 写回"""
    content = MATRIX_PATH.read_text(encoding="utf-8")
    lines = content.split("\n")
    new_lines = []
    changes_applied = 0

    for line in lines:
        new_line = line
        # 检查是否是人物行
        # 格式：| 人物 | D1 | D2 | ... | D8 | 总分 | 关键证据 |
        # 提取第 1 列（人物名）
        if line.startswith("|") and not line.startswith("|---") and not line.startswith("| 人物") and not line.startswith("| 排名"):
            cells = [c.strip() for c in line.split("|")]
            # 去除首尾空
            if cells and cells[0] == "":
                cells = cells[1:]
            if cells and cells[-1] == "":
                cells = cells[:-1]
            if len(cells) >= 10:  # 人物 + D1-D8 + 总分 + 关键证据
                name = cells[0]
                if name in CHANGES:
                    new_scores = cells[1:9]  # D1-D8
                    total = cells[9] if cells[9].isdigit() else "0"
                    for dim, old, new in CHANGES[name]:
                        idx = D_COLS.index(dim)
                        if new_scores[idx] == str(old):
                            new_scores[idx] = str(new)
                        else:
                            print(f"[WARN] {name} {dim}: expected {old}, got {new_scores[idx]}")
                    new_total = sum(int(s) for s in new_scores)
                    new_cells = [name] + new_scores + [str(new_total)] + cells[10:]
                    new_line = "| " + " | ".join(new_cells) + " |"
                    if str(new_total) != total:
                        print(f"[CHANGE] {name}: total {total}->{new_total} ({sum(1 for c in CHANGES[name] if c[0] in D_COLS)} changes)")
                    changes_applied += 1
        new_lines.append(new_line)

    new_content = "\n".join(new_lines)
    MATRIX_PATH.write_text(new_content, encoding="utf-8")
    print(f"\n[INFO] Applied changes to {changes_applied} person rows")
    print(f"[INFO] Output: {MATRIX_PATH}")


if __name__ == "__main__":
    apply_changes_to_matrix()
