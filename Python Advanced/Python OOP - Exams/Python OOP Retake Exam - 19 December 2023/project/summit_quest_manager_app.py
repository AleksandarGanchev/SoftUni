from typing import List

from project import ArcticClimber
from project import SummitClimber
from project import ArcticPeak
from project import SummitPeak


class SummitQuestManagerApp:
    def __init__(self):
        self.climbers = []
        self.peaks = []

    @property
    def valid_climbers(self):
        return {"ArcticClimber": ArcticClimber, "SummitClimber": SummitClimber}

    @staticmethod
    def find_object(value: str, attribute: str, collection: list):
        for obj in collection:
            if getattr(obj, attribute) == value:
                return obj

    def register_climber(self, climber_type: str, climber_name: str):
        if climber_type not in self.valid_climbers:
            return f"{climber_type} doesn't exist in our register."

        searched_climber = self.find_object(climber_name, "name", self.climbers)
        if searched_climber:
            return f"{climber_name} has been already registered."

        self.climbers.append(self.valid_climbers[climber_type](climber_name))
        return f"{climber_name} is successfully registered as a {climber_type}."

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):
        if peak_type not in ["ArcticPeak", "SummitPeak"]:
            return f"{peak_type} is an unknown type of peak."

        if peak_type == "ArcticPeak":
            self.peaks.append(ArcticPeak(peak_name, peak_elevation))

        elif peak_type == "SummitPeak":
            self.peaks.append(SummitPeak(peak_name, peak_elevation))
        return f"{peak_name} is successfully added to the wish list as a {peak_type}."

    def check_gear(self, climber_name: str, peak_name: str, gear: List[str]):
        searched_climber = self.find_object(climber_name, "name", self.climbers)
        searched_peak = self.find_object(peak_name, "name", self.peaks)
        missing_tools = set(searched_peak.get_recommended_gear()).difference(set(gear))

        if not missing_tools:
            return f"{climber_name} is prepared to climb {peak_name}."

        searched_climber.is_prepared = False

        return f"{climber_name} is not prepared to climb {peak_name}. Missing gear: {', '.join(sorted(missing_tools))}."

    def perform_climbing(self, climber_name: str, peak_name: str):
        searched_climber = self.find_object(climber_name, "name", self.climbers)
        searched_peak = self.find_object(peak_name, "name", self.peaks)

        if not searched_climber:
            return f"Climber {climber_name} is not registered yet."

        if not searched_peak:
            return f"Peak {peak_name} is not part of the wish list."

        if not searched_climber.is_prepared:
            return f"{climber_name} will need to be better prepared next time."

        if not searched_climber.can_climb():
            searched_climber.rest()
            return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."

        searched_climber.climb(searched_peak)

        return f"{climber_name} conquered {peak_name} whose difficulty level is {searched_peak.difficulty_level}."

    def get_statistics(self):
        output = []
        climbers = [climber for climber in self.climbers if len(climber.conquered_peaks)]
        peaks = set()

        for climber in climbers:
            climber.sort_peaks()

            for peak in climber.conquered_peaks:
                peaks.add(peak)

        output.append(f"Total climbed peaks: {len(peaks)}")
        output.append("**Climber's statistics:**")

        for name in sorted(climbers, key=lambda x: (-len(x.conquered_peaks), x.name)):
            output.append(str(name))

        return '\n'.join(output)

