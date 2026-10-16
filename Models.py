SUPPORTED_CROPS = ("rice", "cassava", "groundnut", "cocoa", "maize")


class CropRecord:
    record_count = 0

    def __init__(self, crop, season, area_ha, harvest_kg):
        self.crop = crop.lower()
        self.season = season
        self.area_ha = area_ha
        self.harvest_kg = harvest_kg
        CropRecord.record_count += 1

    def yield_per_ha(self):
        return self.harvest_kg / self.area_ha

    def display_info(self):
        print(f"  {self.season} | {self.crop.title()} | {self.area_ha:g} ha | "
              f"{self.harvest_kg:g} kg | {self.yield_per_ha():.1f} kg/ha")

    @classmethod
    def get_record_count(cls):
        return cls.record_count

    @staticmethod
    def is_valid_crop(crop):
        return crop.lower() in SUPPORTED_CROPS


class Farm:
    def __init__(self, farm_id, district, chiefdom):
        self.farm_id = farm_id
        self.location = (district, chiefdom)
        self.total_area = 0
        self.total_harvest = 0
        self.seasons_recorded = 0
        self.last_record = None

    def add_record(self, record):
        self.total_area += record.area_ha
        self.total_harvest += record.harvest_kg
        self.seasons_recorded += 1
        self.last_record = record

    def average_yield(self):
        if self.total_area == 0:
            return 0
        return self.total_harvest / self.total_area

    def display_info(self):
        district, chiefdom = self.location
        print(f"Farm {self.farm_id} - {district}, {chiefdom}")
        print(f"  Records: {self.seasons_recorded} | "
              f"Average yield: {self.average_yield():.1f} kg/ha")
        if self.last_record:
            print("  Latest record:")
            self.last_record.display_info()

    @classmethod
    def from_text(cls, text):
        parts = [p.strip() for p in text.split(",")]
        if len(parts) != 3 or not all(parts):
            return None
        return cls(parts[0].upper(), parts[1], parts[2])
