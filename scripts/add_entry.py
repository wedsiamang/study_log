#!/usr/bin/env python3
# 役割:
#   日付→年度判定して study_log_FY{yy}.md に挿入。
#   --kind fe_b のときは環境変数から「進捗バー付きの表」を自作する(整形もここに集約)。
#   --kind plain(既定) のときは stdin の本文をそのまま details に入れる(手動CLI用)。
import os, sys, argparse, datetime, zoneinfo, pathlib

HEADER_TMPL = "#### study_log (FY{fy2})\n----\n"

def jst_now():
    return datetime.datetime.now(zoneinfo.ZoneInfo("Asia/Tokyo"))

def fiscal_year(d):
    return d.year - 1 if d.month < 4 else d.year

def parse_date(s):
    return datetime.datetime.strptime(s, "%Y/%m/%d")

def fmt_duration(raw):
    # "H:MM:SS" や "HH:MM:SS" -> "N時間M分"。負や異常は原文返し(直し忘れ検知用)
    try:
        parts = [int(x) for x in str(raw).split(":")]
        if len(parts) < 2 or parts[0] < 0:
            return str(raw)
        h, m = parts[0], parts[1]
        if h and m:  return f"{h}時間{m}分"
        if h:        return f"{h}時間"
        return f"{m}分"
    except Exception:
        return str(raw)

def bar(pct, width=10):
    # 正答率(%)を10ブロックのゲージに。■=達成, □=残り
    try:
        p = float(str(pct).replace("%", ""))
    except Exception:
        p = 0
    filled = round(p / 100 * width)
    return "█" * filled + "░" * (width - filled)

def build_fe_b():
    solved   = os.environ.get("SOLVED", "")
    correct  = os.environ.get("CORRECT", "")   # 正答数(AppSheetから追加送信)
    rate_raw = os.environ.get("RATE", "")
    # 正答率を整数に丸め
    try:
        rate = round(float(str(rate_raw).replace("%", "")))
    except Exception:
        rate = rate_raw
    time_h   = fmt_duration(os.environ.get("TIME_TOTAL", ""))
    text     = os.environ.get("TEXT", "")
    chapter  = os.environ.get("CHAPTER", "")
    category = os.environ.get("CATEGORY", "")
    lcat     = os.environ.get("LONGEST_CAT", "")
    lno      = os.environ.get("LONGEST_NO", "")
    ltime    = fmt_duration(os.environ.get("LONGEST_TIME", ""))
    wcat     = os.environ.get("WRONG_CAT", "").strip()
    wno      = os.environ.get("WRONG_NO", "").strip()

    head = f"`{bar(rate)}` {rate}%　{correct}/{solved}問 · {time_h}" if correct \
           else f"`{bar(rate)}` {rate}%　{solved}問 · {time_h}"

    rows = [
        f"| 教材 | {text} / {chapter} |",
        "|---|---|",
        f"| 分野 | {category} |",
        f"| 最長 | {lcat} No.{lno}（{ltime}） |",
    ]
    if wno and wno not in ("-", ""):   # 誤答が無ければ行を出さない
        rows.append(f"| 誤答 | {wcat} No.{wno} |")

    return head + "\n\n" + "\n".join(rows)

def build_details_fe_b(date_str):
    summary = f"📕 FE 科目B ・ {os.environ.get('SOLVED','')}問"
    return f"<details><summary>{summary}</summary>\n\n{build_fe_b()}\n\n</details>\n"

def build_details_plain(label, body):
    return f"<details><summary>{label}</summary>\n\n{body.rstrip()}\n\n</details>\n"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--label", default="FE_B")
    ap.add_argument("--kind", default="plain")   # fe_b / plain
    ap.add_argument("--date", default=None)
    args = ap.parse_args()

    d = parse_date(args.date) if args.date else jst_now()
    date_str = d.strftime("%Y/%m/%d")
    fy2 = fiscal_year(d) % 100
    target = pathlib.Path(f"study_log_FY{fy2}.md")

    if args.kind == "fe_b":
        details = build_details_fe_b(date_str)
    else:
        details = build_details_plain(args.label, sys.stdin.read())

    text = target.read_text(encoding="utf-8") if target.exists() \
           else HEADER_TMPL.format(fy2=fy2)
    heading = f"##### {date_str} · FE 科目B" if args.kind == "fe_b" else f"##### {date_str}"

    # 同日は既存見出しの下、なければ最上部に新規
    import re
    pat = re.compile(rf"^##### .*{re.escape(date_str)}", re.M)   # 📅 等を挟んでも一致
    m = pat.search(text)
    if m:
        after = m.start()
        next_h = text.find("\n##### ", after + 5)
        insert_at = next_h if next_h != -1 else len(text)
        new_text = text[:insert_at].rstrip() + "\n\n" + details + text[insert_at:]
    else:
        h = text.find("----")
        pos = text.find("\n", h) + 1 if h != -1 else 0
        new_text = text[:pos] + f"\n{heading}\n\n{details}" + text[pos:]
    target.write_text(new_text, encoding="utf-8")
    print(f"added: {args.kind} @ {date_str} -> {target.name}")

if __name__ == "__main__":
    main()
