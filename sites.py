from dataclasses import dataclass

@dataclass
class Site:
    Home="https://webapp.yuntech.edu.tw/YunTechSSO/"
    student="https://webapp.yuntech.edu.tw/eStudent/eStud/"
    Couese="https://webapp.yuntech.edu.tw/WebNewCAS/StudentFile/Course/"
    srore="https://webapp.yuntech.edu.tw/WebNewCAS/StudentFile/Score/"
    coursestudents="https://webapp.yuntech.edu.tw/WebNewCAS/Course/StudList.aspx?acad_year={}&seme_type={}&current_subj={}"
    