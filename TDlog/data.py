groups = {
    "1": { "Denmark", "England", "France",      "Sweden" },
    "2": { "CIS",     "Germany", "Netherlands", "Scotland" }
}

matches = [
    ("Sweden",      1, 1, "France"),
    ("Denmark",     0, 0, "England"),
    ("Netherlands", 1, 0, "Scotland"),
    ("CIS",         1, 1, "Germany"),
    ("France",      0, 0, "England"),
    ("Sweden",      1, 0, "Denmark"),
]