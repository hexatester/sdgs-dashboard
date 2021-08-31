import attr
from typing import Dict


@attr.dataclass
class PenyakitDiderita:
    # P404
    mutaber_diare: bool
    demam_berdarah: bool
    campak: bool
    malaria: bool
    flu_burung_sars: bool
    covid19: bool
    hepatitis_b: bool
    hepatitis_e: bool
    difteri: bool
    chikungunya: bool
    leptospirosis: bool
    kolera: bool
    gizi_buruk: bool
    jantung: bool
    tbc_paru_paru: bool
    kanker: bool
    diabetes: bool
    lumpuh: bool
    lainnya: bool

    def todict(self) -> Dict[str, str]:
        return {
            "1": "1" if self.mutaber_diare else "2",
            "2": "1" if self.demam_berdarah else "2",
            "3": "1" if self.campak else "2",
            "4": "1" if self.malaria else "2",
            "5": "1" if self.flu_burung_sars else "2",
            "6": "1" if self.covid19 else "2",
            "7": "1" if self.hepatitis_b else "2",
            "8": "1" if self.hepatitis_e else "2",
            "9": "1" if self.difteri else "2",
            "10": "1" if self.chikungunya else "2",
            "11": "1" if self.leptospirosis else "2",
            "12": "1" if self.kolera else "2",
            "13": "1" if self.gizi_buruk else "2",
            "14": "1" if self.jantung else "2",
            "15": "1" if self.tbc_paru_paru else "2",
            "16": "1" if self.kanker else "2",
            "17": "1" if self.diabetes else "2",
            "18": "1" if self.lumpuh else "2",
            "19": "1" if self.lainnya else "2",
        }
