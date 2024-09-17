def individual_serial(president) -> dict:
    return {
        "id": str(president.get("_id", "")),
        "name": president.get("name", ""),
        "party": president.get("party", ""),
        "birth_state": president.get("birth_state", ""),
        "death_state": president.get("death_state", ""),
        "education": president.get("education", ""),
        "served_ww": president.get("served_ww", False),
        "owned_dog": president.get("owned_dog", False),
        "faced_impeachment": president.get("faced_impeachment", False),
        "was_assassinated": president.get("was_assassinated", False),
        "former_general": president.get("former_general", False),
        "died_in_office": president.get("died_in_office", False),
        "former_vice_president": president.get("former_vice_president", False),
        "served_2more_terms": president.get("served_2more_terms", False),
        "faced_economic_crisis": president.get("faced_economic_crisis", False),
        "served_cold_war": president.get("served_cold_war", False),
        "served_military": president.get("served_military", False),
        "served_during_revolution": president.get("served_during_revolution", False),
        "notable_foreign_policy": president.get("notable_foreign_policy", ""),
        "served_amidst_infrastructure": president.get("served_amidst_infrastructure", False),
        "known_environmental_conservation": president.get("known_environmental_conservation", False),
        "involved_land_acquisition": president.get("involved_land_acquisition", False),
        "first_lady_name_elizabeth": president.get("first_lady_name_elizabeth", False),
        "above_6_feet": president.get("above_6_feet", False),
        "served_ambassador": president.get("served_ambassador", False),
        "pilot_certificate": president.get("pilot_certificate", False),
        "lawyer_previously": president.get("lawyer_previously", False),
        "governor_previously": president.get("governor_previously", False),
        "senator_previously": president.get("senator_previously", False),
        "autobiography": president.get("autobiography", ""),
        "medal_honor": president.get("medal_honor", False),
        "sons": president.get("sons", 0),
        "daughters": president.get("daughters", 0),
        "siblings": president.get("siblings", 0),
        "marriages": president.get("marriages", 0),
        "appointed_judges": president.get("appointed_judges", 0),
        "number_served_ambassador": president.get("number_served_ambassador", 0),
        "age_inauguration": president.get("age_inauguration", 0),
        "military_awards": president.get("military_awards", ""),
        "founded_companies": president.get("founded_companies", ""),
        "height": president.get("height", ""),
        "weight": president.get("weight", ""),
        "years_in_office": president.get("years_in_office", 0),
        "death_age": president.get("death_age", 0),
        "executive_orders": president.get("executive_orders", 0),
        "vetoes": president.get("vetoes", 0),
        "pardons": president.get("pardons", 0)
    }

def individual_serial_name(president) -> dict:
    return {
        "name": president.get("name", "")
    }

def list_serial(presidents, name_only=False) -> list:
    if name_only:
        return [individual_serial_name(president) for president in presidents]
    return [individual_serial(president) for president in presidents]