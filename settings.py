QUESTION_DATA_PATH = "data/PAT10_12_test.csv"
USER_DATA_PATH = 'data/user_data_sample.csv'

# PAT topics (default 8: dynamics, thermodynamics, electricity, algebra, geometry, calculus, probability)
PAT_TOPICS = ['Dynamics', 'Thermodynamics', 'Electricity', "Optics and Modern Physics", 'Analysis',
              'Algebra', 'Geometry', 'Calculus', 'Probability']
NUM_PAT_TOPICS = len(PAT_TOPICS)

LABEL2CATEGORY = {

    # Dynamics
    11: "Mechanics-Statics",
    12: "Mechanics-Newtonian Laws and Dynamics",
    13: "Mechanics-Energy",
    14: "Mechanics-Gravitational Force and Astrophysics",
    15: "Mechanics-Vibrations and Waves",

    # Thermodynamics
    21: "Macroscopic Thermodynamics",
    22: "Microscopic Thermodynamics",

    # Electricity
    31: "Electricity - Static electricity",
    32: "Electricity - Circuits",
    33: "Electricity - Magnetic fields",
    34: "Eletricity - Eletromagnetic induction",

    # Optics and Modern Physics
    41: "Optics - classical optics",
    42: "Optics - wave optics",
    43: "Modern physics - Relativity",
    44: "Modern physics - nuclear physics",

    91: "Numerical methods",
    92: "Dimensional Analysis",

    5: "Proof",

    61: "Algebra and Functions",
    62: "Sequences and series",
    63: "Trigonometry",
    64: "Exponentials and logarithms",

    71: "Differentiation",
    72: "Integration",

    81: "Geometry (Cartesian)",
    82: "Geometry (Curve sketching)",
    83: "Geometry (General)",
    84: "Vectors",

    "A": "Probability - statistics"
}

CATEGORY2LABEL = {v: k for k, v in LABEL2CATEGORY.items()}

# Number of questions asked per session - for simplification it is a static number now. But we can make it dynamic, e.g.
# as a function of the user and question data, if necessary and desirable
NUM_QNS_PER_SESSION = 10