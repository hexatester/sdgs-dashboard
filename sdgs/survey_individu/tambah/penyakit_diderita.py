import attr
from typing import Dict


@attr.dataclass
class PenyakitDiderita:
    mutaber_diare: str
    demam_berdarah: str
    campak: str
    malaria: str
    flu_burung_sars: str
    covid19: str
    hepatitis_b: str
    hepatitis_e: str
    difteri: str
    chikungunya: str
    leptospirosis: str
    kolera: str
    gizi_buruk: str
    jantung: str
    tbc_paru_paru: str
    kanker: str
    diabetes: str
    lumpuh: str
    lainnya: str

    def todict(self) -> Dict[str, str]:
        return {
            "1": self.mutaber_diare,
            "2": self.demam_berdarah,
            "3": self.campak,
            "4": self.malaria,
            "5": self.flu_burung_sars,
            "6": self.covid19,
            "7": self.hepatitis_b,
            "8": self.hepatitis_e,
            "9": self.difteri,
            "10": self.chikungunya,
            "11": self.leptospirosis,
            "12": self.kolera,
            "13": self.gizi_buruk,
            "14": self.jantung,
            "15": self.tbc_paru_paru,
            "16": self.kanker,
            "17": self.diabetes,
            "18": self.lumpuh,
            "19": self.lainnya,
        }
