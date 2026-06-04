"""Apply v4 D 维变更 to scoring_process.html score grids + meta (v2: handle Chinese cases)
"""
import re
from pathlib import Path

# ID -> v4 scores
ID_TO_SCORES = {
    "hinton": [3, 1, 3, 1, 3, 3, 3, 3],
    "jeffdean": [1, 3, 3, 0, 1, 3, 2, 2],
    "liutieyan": [1, 2, 2, 1, 1, 2, 3, 2],
    "zhanglinfeng": [2, 1, 2, 2, 0, 1, 3, 1],
    "samaltman": [0, 2, 1, 3, 3, 2, 3, 3],   # v4: D1 1->0, D6 1->2
    "yanshuicheng": [2, 2, 2, 2, 0, 1, 3, 2],
    "zhangxiangyu": [3, 1, 1, 0, 0, 1, 2, 2],  # v4: D4 1->0
    "xiesaining": [3, 1, 2, 2, 1, 1, 2, 2],
    "demis": [3, 1, 3, 3, 2, 2, 3, 3],          # v4: D6 1->2
}


def find_case_block(lines, case_id):
    """找到 case 的 score-grid 块 via id attribute"""
    for i, line in enumerate(lines):
        if f'id="{case_id}"' in line and 'person-card' in line:
            for j in range(i, min(i+50, len(lines))):
                if 'score-grid' in lines[j]:
                    return j + 1
    return None


def apply_to_scoring():
    path = Path("docs/scoring_process.html")
    content = path.read_text(encoding="utf-8")
    lines = content.split("\n")
    new_lines = lines[:]
    total_changes = 0

    for case_id, scores in ID_TO_SCORES.items():
        idx = find_case_block(new_lines, case_id)
        if idx is None:
            print(f"[SKIP] {case_id}: case block not found")
            continue
        new_total = sum(scores)
        changed = 0
        for k in range(8):
            cell_line = new_lines[idx + k]
            old_value_match = re.search(r'value sp-(\d+)">(\d+)</div>', cell_line)
            if old_value_match:
                old_class = f"sp-{old_value_match.group(1)}"
                old_value = int(old_value_match.group(2))
                new_value = scores[k]
                if old_value != new_value:
                    new_class = f"sp-{new_value}"
                    new_cell = cell_line.replace(f'value {old_class}">{old_value}</div>',
                                                f'value {new_class}">{new_value}</div>')
                    new_lines[idx + k] = new_cell
                    changed += 1
        # total
        for j in range(idx, min(idx + 30, len(new_lines))):
            if '总分' in new_lines[j]:
                new_total_line = re.sub(r'总分 <strong[^>]*>\d+</strong>', f'总分 <strong style="color: #fff;">{new_total}</strong>', new_lines[j])
                new_lines[j] = new_total_line
                break
        print(f"[CHANGE] {case_id}: {changed} cells, total->{new_total}")
        total_changes += 1

    new_content = "\n".join(new_lines)
    path.write_text(new_content, encoding="utf-8")
    print(f"\n[INFO] Applied changes to {total_changes} case score grids")


if __name__ == "__main__":
    apply_to_scoring()
