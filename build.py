#!/usr/bin/env python3
"""data.csv から data.json / pokemon.sqlite / index.html を生成する。

使い方: python3 build.py
"""
import csv
import json
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def load_rows():
    with open(ROOT / "data.csv", encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    # ポケモン名が空 / エラー値の行は除外
    return [r for r in rows if r["ポケモン名"].strip() and not r["ID"].startswith("#")]


def write_json(rows):
    (ROOT / "data.json").write_text(
        json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8"
    )


def write_sqlite(rows):
    path = ROOT / "pokemon.sqlite"
    path.unlink(missing_ok=True)
    cols = list(rows[0].keys())
    con = sqlite3.connect(path)
    col_sql = ", ".join(f'"{c}" TEXT' for c in cols)
    con.execute(f"CREATE TABLE pokemon ({col_sql})")
    con.executemany(
        f'INSERT INTO pokemon VALUES ({", ".join("?" * len(cols))})',
        [[r[c] for c in cols] for r in rows],
    )
    con.commit()
    con.close()


def write_html(rows):
    tpl = (ROOT / "template.html").read_text(encoding="utf-8")
    payload = json.dumps(rows, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    (ROOT / "index.html").write_text(tpl.replace("/*__DATA__*/[]", payload), encoding="utf-8")


if __name__ == "__main__":
    rows = load_rows()
    write_json(rows)
    write_sqlite(rows)
    write_html(rows)
    print(f"{len(rows)} rows -> data.json, pokemon.sqlite, index.html")
