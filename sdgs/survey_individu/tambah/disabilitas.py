import attr
from typing import Dict

MAPPING = {
    "1": "2",
    "2": "2",
    "3": "2",
    "4": "2",
    "5": "2",
    "6": "2",
    "7": "2",
    "8": "2",
    "9": "2",
    "10": "2",
    "11": "2",
    "12": "2",
    "13": "2",
    "14": "2",
    "15": "2",
    "16": "2",
    "17": "2",
    "18": "2",
    "19": "2",
}


@attr.dataclass
class Disabilitas:
    tunanetra: str
    tunarungu: str
    tunawicara: str
    tunarungu_wicara: str
    tunadaksa: str
    tunagrahita: str
    tunalaras: str
    cacat_eks_kusta: str
    cacat_ganda: str
    dipasung: str
