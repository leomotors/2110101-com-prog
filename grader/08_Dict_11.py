# pylint: disable=W

from typing import Dict


def reverse(d: Dict):
    # d เป็น dict ที่มี value ไม่ซ ้ำกนั
    # คืน dict ใหม่ที่เก็บ key,value ที่ค่ำเป็น value,key ของ d ที่ได ้รับ
    return {v: k for k, v in d.items()}


def keys(d: Dict, v):
    # คืนลิสต์ที่เก็บค่ำของ keys ใน d (เรียงยังไงก็ได ้) ที่มีค่ำ value เท่ำกับ v
    return list(filter(lambda x: d[x] == v, d.keys()))


exec(input().strip())
