"""
Data mappings and constants for the Student Success Predictor app
Contains all the human-readable mappings for categorical features
"""


def create_feature_mappings():
    """Create human-readable mappings for categorical features"""

    # Marital status mapping
    marital_status_map = {
        1: "Single",
        2: "Married",
        3: "Widowed",
        4: "Divorced",
        5: "Civil Union",
        6: "Legally Separated",
    }

    # Application mode mapping (from data dictionary)
    application_mode_map = {
        1: "1st phase - general contingent",
        2: "Ordinance No. 612/93",
        5: "1st phase - special contingent (Azores Island)",
        7: "Holders of other higher courses",
        10: "Ordinance No. 854-B/99",
        15: "International student (bachelor)",
        16: "1st phase - special contingent (Madeira Island)",
        17: "2nd phase - general contingent",
        18: "3rd phase - general contingent",
        26: "Ordinance No. 533-A/99, item b2 (Different Plan)",
        27: "Ordinance No. 533-A/99, item b3 (Other Institution)",
        39: "Over 23 years old",
        42: "Transfer",
        43: "Change of course",
        44: "Technological specialization diploma holders",
        51: "Change of institution/course",
        53: "Short cycle diploma holders",
        57: "Change of institution/course (International)",
    }

    # Course mapping
    course_map = {
        33: "Biofuel Production Technologies",
        171: "Animation and Multimedia Design",
        8014: "Social Service (evening attendance)",
        9003: "Agronomy",
        9070: "Communication Design",
        9085: "Veterinary Nursing",
        9119: "Informatics Engineering",
        9130: "Equinculture",
        9147: "Management",
        9238: "Social Service",
        9254: "Tourism",
        9500: "Nursing",
        9556: "Oral Hygiene",
        9670: "Advertising and Marketing Management",
        9773: "Journalism and Communication",
        9853: "Basic Education",
        9991: "Management (evening attendance)",
    }

    # Previous qualification mapping (from data dictionary)
    qualification_map = {
        1: "Secondary education",
        2: "Higher education - bachelor's degree",
        3: "Higher education - degree",
        4: "Higher education - master's",
        5: "Higher education - doctorate",
        6: "Frequency of higher education",
        9: "12th year of schooling - not completed",
        10: "11th year of schooling - not completed",
        12: "Other - 11th year of schooling",
        14: "10th year of schooling",
        15: "10th year of schooling - not completed",
        19: "Basic education 3rd cycle (9th/10th/11th year) or equiv.",
        38: "Basic education 2nd cycle (6th/7th/8th year) or equiv.",
        39: "Technological specialization course",
        40: "Higher education - degree (1st cycle)",
        42: "Professional higher technical course",
        43: "Higher education - master (2nd cycle)",
    }

    # Occupation mapping
    occupation_map = {
        0: "Student",
        1: "Representatives of the Legislative Power and Executive Bodies",
        2: "Specialists in Intellectual and Scientific Activities",
        3: "Intermediate Level Technicians and Professions",
        4: "Administrative staff",
        5: "Personal Services, Security and Safety Workers",
        6: "Farmers and Skilled Workers in Agriculture",
        7: "Skilled Workers in Industry, Construction and Craftsmen",
        8: "Installation and Machine Operators and Assembly Workers",
        9: "Unskilled Workers",
        10: "Armed Forces Professions",
        90: "Other Situation",
        99: "Unspecified",
        122: "Health professionals",
        123: "Teachers",
        125: "Specialists in information and communication technologies",
        131: "Intermediate level science and engineering technicians",
        132: "Technicians and associate professionals, health",
        134: "Intermediate level technicians from legal, social, sports",
        141: "Office workers, secretaries in general and data processing",
        143: "Data, accounting, statistical, financial services",
        144: "Other administrative support staff",
        151: "Personal service workers",
        152: "Sellers",
        153: "Personal care workers and the like",
        171: "Skilled construction workers and the like, except electricians",
        173: "Skilled workers in printing, precision instrument manufacturing",
        175: "Workers in food processing, woodworking, clothing",
        191: "Cleaning workers",
        192: "Unskilled workers in agriculture, animal production",
        193: "Unskilled workers in extractive industry, construction",
        194: "Meal preparation assistants",
    }

    # Nationality mapping (from data dictionary)
    nationality_map = {
        1: "Portuguese",
        2: "German", 
        6: "Spanish",
        11: "Italian",
        13: "Dutch",
        14: "English",
        17: "Lithuanian",
        21: "Angolan",
        22: "Cape Verdean",
        24: "Guinean",
        25: "Mozambican",
        26: "Santomean",
        32: "Turkish",
        41: "Brazilian",
        62: "Romanian",
        100: "Moldova (Republic of)",
        101: "Mexican",
        103: "Ukrainian",
        105: "Russian",
        108: "Cuban",
        109: "Colombian",
    }

    return {
        "marital_status": marital_status_map,
        "application_mode": application_mode_map,
        "course": course_map,
        "qualification": qualification_map,
        "occupation": occupation_map,
        "nationality": nationality_map,
    }


# Preset configurations for quick form filling
PRESET_CONFIGURATIONS = {
    "Custom Entry": {
        "age": 20,
        "gender": 0,
        "marital": 1,
        "app_mode": 1,
        "course": 9254,
        "prev_grade": 120,
        "adm_grade": 120,
        # Family background
        "mothers_qualification": 1,  # Secondary education
        "fathers_qualification": 1,  # Secondary education
        "mothers_occupation": 4,     # Administrative staff
        "fathers_occupation": 7,     # Skilled workers
        # Financial & social
        "displaced": 0,
        "educational_special_needs": 0,
        "debtor": 0,
        "tuition_fees_up_to_date": 1,
        "scholarship_holder": 0,
        "international": 0,
    },
    "Typical Graduate Student": {
        "age": 18,  # Slightly younger, traditional student age
        "gender": 0,  # Female students often have slightly higher graduation rates
        "marital": 1,  # Single
        "app_mode": 1,  # 1st phase general contingent (most competitive)
        "course": 9500,  # Nursing (typically high graduation rate)
        "prev_grade": 170,  # Higher previous qualification grade
        "adm_grade": 150,  # Higher admission grade
        # Family background
        "mothers_qualification": 2,  # Higher education - bachelor's degree
        "fathers_qualification": 2,  # Higher education - bachelor's degree
        "mothers_occupation": 2,     # Specialists in intellectual activities
        "fathers_occupation": 2,     # Specialists in intellectual activities
        # Financial & social
        "displaced": 0,
        "educational_special_needs": 0,
        "debtor": 0,
        "tuition_fees_up_to_date": 1,
        "scholarship_holder": 1,     # Has scholarship (positive factor)
        "international": 0,
    },
    "At-Risk Student": {
        "age": 22,
        "gender": 1,
        "marital": 1,
        "app_mode": 17,
        "course": 171,
        "prev_grade": 100,
        "adm_grade": 110,
        # Family background
        "mothers_qualification": 19,  # Basic education 3rd cycle
        "fathers_qualification": 19,  # Basic education 3rd cycle
        "mothers_occupation": 9,      # Unskilled workers
        "fathers_occupation": 9,      # Unskilled workers
        # Financial & social
        "displaced": 0,
        "educational_special_needs": 0,
        "debtor": 1,                  # Has debts (risk factor)
        "tuition_fees_up_to_date": 0, # Behind on tuition
        "scholarship_holder": 0,
        "international": 0,
    },
    "International Student": {
        "age": 21,
        "gender": 0,
        "marital": 1,
        "app_mode": 15,  # International student (bachelor)
        "course": 9238,
        "prev_grade": 135,
        "adm_grade": 130,
        # Family background
        "mothers_qualification": 2,  # Higher education - bachelor's degree
        "fathers_qualification": 2,  # Higher education - bachelor's degree
        "mothers_occupation": 2,     # Specialists in intellectual activities
        "fathers_occupation": 2,     # Specialists in intellectual activities
        # Financial & social
        "displaced": 0,
        "educational_special_needs": 0,
        "debtor": 0,
        "tuition_fees_up_to_date": 1,
        "scholarship_holder": 0,
        "international": 1,          # Is international student
    },
}

# Academic performance defaults for presets
ACADEMIC_DEFAULTS = {
    "Custom Entry": {
        "1st_sem": {
            "enrolled": 6,
            "approved": 6,
            "grade": 13,
            "credited": 0,
            "evaluations": 6,
            "without": 0,
        },
        "2nd_sem": {
            "enrolled": 6,
            "approved": 6,
            "grade": 13,
            "credited": 0,
            "evaluations": 6,
            "without": 0,
        },
    },
    "Typical Graduate Student": {
        "1st_sem": {
            "enrolled": 6,
            "approved": 6,
            "grade": 16,  # Higher grade (closer to maximum of 20)
            "credited": 0,
            "evaluations": 6,
            "without": 0,
        },
        "2nd_sem": {
            "enrolled": 6,
            "approved": 6,
            "grade": 16,  # Higher grade (closer to maximum of 20)
            "credited": 0,
            "evaluations": 6,
            "without": 0,
        },
    },
    "At-Risk Student": {
        "1st_sem": {
            "enrolled": 6,
            "approved": 0,
            "grade": 0,
            "credited": 0,
            "evaluations": 0,
            "without": 0,
        },
        "2nd_sem": {
            "enrolled": 6,
            "approved": 0,
            "grade": 0,
            "credited": 0,
            "evaluations": 0,
            "without": 0,
        },
    },
    "International Student": {
        "1st_sem": {
            "enrolled": 6,
            "approved": 6,
            "grade": 13,
            "credited": 0,
            "evaluations": 6,
            "without": 0,
        },
        "2nd_sem": {
            "enrolled": 6,
            "approved": 6,
            "grade": 14,
            "credited": 0,
            "evaluations": 6,
            "without": 0,
        },
    },
}

# Validation constants
VALIDATION_RULES = {
    "min_age": 17,
    "max_age": 70,
    "min_grade": 0,
    "max_grade": 20,
    "min_qualification_grade": 95,
    "max_qualification_grade": 190,
}
