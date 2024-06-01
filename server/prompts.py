output_prompt = """Please extract the following details from the provided file:
    {
    "summary": "(1) The summary/abstract of the bill in 100-150 words.",
    "main_findings": "(2) More detailed description of the main finding in 500 words",
    "benefits": "(3) Benefits of the bill specific to the party's state/county, if any, else empty string",
    "concerns": "(4) Concerns of the bill specific to the party & their state/county, if any, else empty string",
    "amendments": "(5) Any amendments they would like to make to some claims of the bill based on their party perspective",
    "outcome_for_people": "(6) What would be the result of this outcome for the people" }
    (7) Provide this data back as a json text, but don't annotate it with 'json'
    """