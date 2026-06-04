"""Apply v4 D 维变更 to portrait.html
"""
import re
from pathlib import Path

# v4 变更清单（同 apply_v4.py）
CHANGES = {
    "高文": [("D4", 1, 0)],
    "林达华": [("D3", 3, 2)],
    "刘知远": [("D2", 1, 2)],
    "孙茂松": [("D4", 1, 0)],
    "唐杰": [("D2", 1, 2)],
    "张钹": [("D4", 1, 0)],
    "张亚勤": [("D1", 1, 2), ("D4", 2, 1), ("D6", 2, 1)],
    "周志华": [("D4", 1, 0)],
    "He Kaiming": [("D4", 1, 0)],
    "Li Feifei": [("D4", 2, 3), ("D6", 1, 2)],
    "Xie Saining": [("D3", 3, 2)],
    "Zhang Xiangyu": [("D4", 1, 0)],
    "Ian Goodfellow": [("D5", 0, 1), ("D6", 1, 0)],
    "李航": [("D5", 0, 1), ("D8", 3, 2)],
    "田奇": [("D6", 2, 3)],
    "王海峰": [("D4", 1, 0), ("D6", 3, 2)],
    "Xuedong Huang": [("D4", 1, 0)],
    "张正友": [("D1", 1, 2), ("D6", 2, 3)],
    "周靖人": [("D4", 1, 0), ("D6", 1, 2)],
    "余凯": [("D3", 2, 1), ("D6", 2, 3), ("D7", 2, 3)],
    "印奇": [("D3", 1, 0), ("D6", 1, 2), ("D7", 2, 3), ("D8", 1, 2)],
    "张一鸣": [("D3", 1, 0), ("D6", 1, 2), ("D7", 1, 2)],
    "张林峰": [("D5", 0, 1), ("D8", 1, 2)],
    "朱珑": [("D6", 1, 2), ("D7", 2, 3)],
    "杨植麟": [("D1", 3, 2), ("D3", 2, 1)],
    "梁文锋": [("D3", 1, 0)],
    "王小川": [("D2", 1, 2), ("D3", 1, 0), ("D6", 1, 2), ("D7", 2, 3)],
    "闫俊杰": [("D3", 1, 0), ("D6", 1, 2), ("D7", 2, 3), ("D8", 2, 3)],
    "陈天石": [("D6", 3, 2), ("D7", 1, 2)],
    "雷军": [("D2", 1, 2), ("D3", 1, 0)],
    "姜大昕": [("D1", 0, 1), ("D6", 1, 2), ("D7", 1, 2), ("D8", 1, 2)],
    "张鹏": [("D3", 1, 0), ("D8", 1, 2)],
    "王兴兴": [("D8", 1, 3)],
    "Andrew Ng": [("D6", 1, 2)],
    "Chris Olah": [("D5", 0, 1)],
    "Dario Amodei": [("D1", 1, 2)],
    "Demis Hassabis": [("D6", 1, 2)],
    "Nick Bostrom": [("D6", 0, 2)],
    "Sam Altman": [("D1", 1, 0), ("D6", 1, 2)],
    "Stuart Russell": [("D6", 2, 3)],
}

D_COLS = ["D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8"]


def apply_to_portrait():
    portrait_path = Path("docs/portrait.html")
    content = portrait_path.read_text(encoding="utf-8")
    lines = content.split("\n")
    new_lines = []
    changes_applied = 0
    prototype_changes = []  # for 张正友 P2 → P1

    for line in lines:
        new_line = line
        # 格式: {name:"中文名",p:"P1",d:[2,1,3,2,2,1,3,3],sum:17},
        m = re.search(r'\{name:"([^"]+)",p:"([^"]+)",d:\[([0-9,\s]+)\],sum:(\d+)\}', line)
        if m:
            name = m.group(1)
            proto = m.group(2)
            scores = [int(x.strip()) for x in m.group(3).split(",")]
            total = int(m.group(4))
            if name in CHANGES:
                new_scores = scores[:]
                for dim, old, new in CHANGES[name]:
                    idx = D_COLS.index(dim)
                    if new_scores[idx] == old:
                        new_scores[idx] = new
                new_total = sum(new_scores)
                # 特殊：张正友 D1 1→2 + D6 2→3 改 P1
                if name == "张正友" and new_scores[0] == 2 and new_scores[5] == 3:
                    proto = "P1"
                    prototype_changes.append(f"{name}: P2 -> P1")
                new_line = f'  {{name:"{name}",p:"{proto}",d:[{",".join(str(x) for x in new_scores)}],sum:{new_total}}},'
                if new_total != total:
                    print(f"[CHANGE] {name}: total {total}->{new_total}")
                changes_applied += 1
        new_lines.append(new_line)

    new_content = "\n".join(new_lines)
    portrait_path.write_text(new_content, encoding="utf-8")
    print(f"\n[INFO] Applied changes to {changes_applied} person rows")
    for c in prototype_changes:
        print(f"[PROTO] {c}")


if __name__ == "__main__":
    apply_to_portrait()
