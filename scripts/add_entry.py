#!/usr/bin/env python3
# 役割: 今日(または--date)の日付から年度を判定し、study_log_FY{yy}.md の
#       正しい位置(新規日付は最上部/同日は下に追記)にエントリを挿入する。
# 年度: 日本の会計年度(4月始まり)。1〜3月は前年がFY。
import sys, argparse, datetime, zoneinfo, pathlib

HEADER_TMPL = "#### study_log (FY{fy2})\n----\n"

def jst_now():
    return datetime.datetime.now(zoneinfo.ZoneInfo("Asia/Tokyo"))

def fiscal_year(d):
    return d.year - 1 if d.month < 4 else d.year   # 例: 2026/03 -> 2025

def parse_date(s):
    return datetime.datetime.strptime(s, "%Y/%m/%d")

def build_details(label, body):
    return f"<details><summary>{label}</summary>\n\n{body.rstrip()}\n\n</details>\n"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--label", required=True)
    ap.add_argument("--date", default=None)   # 省略時はJST今日
    args = ap.parse_args()

    d = parse_date(args.date) if args.date else jst_now()
    date_str = d.strftime("%Y/%m/%d")
    fy = fiscal_year(d)
    fy2 = fy % 100                            # 26, 25 ...
    target = pathlib.Path(f"study_log_FY{fy2}.md")

    body = sys.stdin.read()
    details = build_details(args.label, body)

    text = target.read_text(encoding="utf-8") if target.exists() \
           else HEADER_TMPL.format(fy2=fy2)   # 新年度ファイルは自動でヘッダ付き作成
    heading = f"##### 📅 {date_str}"

    idx = text.find(heading)
    if idx != -1:
        after = idx + len(heading)
        next_h = text.find("\n##### ", after)
        insert_at = next_h if next_h != -1 else len(text)
        new_text = text[:insert_at].rstrip() + "\n\n" + details + text[insert_at:]
    else:
        h = text.find("----")
        pos = text.find("\n", h) + 1 if h != -1 else 0
        block = f"\n{heading}\n\n{details}"
        new_text = text[:pos] + block + text[pos:]

    target.write_text(new_text, encoding="utf-8")
    print(f"added: {args.label} @ {date_str} -> {target.name}")

if __name__ == "__main__":
    main()
