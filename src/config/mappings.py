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

    # Application mode mapping
    application_mode_map = {
        1: "1st Phase - General Contingent",
        2: "Ordinance No. 612/93",
        5: "1st Phase - Special Contingent (Azores)",
        7: "Holders of Other Higher Courses",
        10: "Ordinance No. 854-B/99",
        15: "International Student (Bachelor)",
        16: "1st Phase - Special Contingent (Madeira)",
        17: "2nd Phase - General Contingent",
        18: "3rd Phase - General Contingent",
        26: "Ordinance No. 533-A/99, item b2",
        27: "Ordinance No. 533-A/99, item b3",
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

    # Previous qualification mapping
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
        42: "Professional course",
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

    return {
        "marital_status": marital_status_map,
        "application_mode": application_mode_map,
        "course": course_map,
        "qualification": qualification_map,
        "occupation": occupation_map,
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
    },
    "Typical Graduate Student": {
        "age": 19,
        "gender": 1,
        "marital": 1,
        "app_mode": 15,
        "course": 9254,
        "prev_grade": 160,
        "adm_grade": 142,
    },
    "At-Risk Student": {
        "age": 22,
        "gender": 1,
        "marital": 1,
        "app_mode": 17,
        "course": 171,
        "prev_grade": 100,
        "adm_grade": 110,
    },
    "International Student": {
        "age": 21,
        "gender": 0,
        "marital": 1,
        "app_mode": 1,
        "course": 9238,
        "prev_grade": 135,
        "adm_grade": 130,
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
            "grade": 14,
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
