import os
import pandas as pd

# bridgeport_schools has a GPT4 sourced set of schools.

# There's 169 school districts in CT and this is just one below for bridgeport.
# Bridgeport is hard coded a few times in here, which isn't optimal.

# GPT Prompt I used:
# All bridgeport public school district (CT) schools in a python dict like so ```bridgeport_schools = [
#    {"school_name": "School Name", "address": "400 Street St+Town+CT 12345", "students": 1234,
#    "website": "URL, "phone": "123 456 7890"}]``` please

# After you generate the markdown from this script, also run `python3 make_grade_subtotals_and_totals.py`

bridgeport_schools = [
    {"school_name": "Beardsley School", "address": "500 Huntington Road+Bridgeport+CT 06610", "students": 400, "website": "https://www.bridgeportedu.net/Beardsley", "phone": "203-275-3401"},
    {"school_name": "Black Rock School", "address": "545 Brewster Street+Bridgeport+CT 06605", "students": 380, "website": "https://www.bridgeportedu.net/BlackRock", "phone": "203-275-4200"},
    {"school_name": "Blackham School", "address": "425 Thorme Street+Bridgeport+CT 06606", "students": 850, "website": "https://www.bridgeportedu.net/Blackham", "phone": "203-275-4200"},
    {"school_name": "Bryant School", "address": "230 Poplar Street+Bridgeport+CT 06605", "students": 310, "website": "https://www.bridgeportedu.net/Bryant", "phone": "203-275-4500"},
    {"school_name": "Classical Studies Academy", "address": "240 Linwood Avenue+Bridgeport+CT 06604", "students": 520, "website": "https://www.bridgeportedu.net/ClassicalStudies", "phone": "203-275-1557"},
    {"school_name": "Columbus School", "address": "275 George Street+Bridgeport+CT 06604", "students": 630, "website": "https://www.bridgeportedu.net/Columbus", "phone": "203-275-2100"},
    {"school_name": "Curiale School", "address": "300 Laurel Avenue+Bridgeport+CT 06605", "students": 570, "website": "https://www.bridgeportedu.net/Curiale", "phone": "203-275-2253"},
    {"school_name": "Discovery Magnet School", "address": "4510 Park Avenue+Bridgeport+CT 06606", "students": 460, "website": "https://www.bridgeportedu.net/Discovery", "phone": "203-275-1801"},
    {"school_name": "Dunbar School", "address": "445 Union Avenue+Bridgeport+CT 06607", "students": 620, "website": "https://www.bridgeportedu.net/Dunbar", "phone": "203-275-2300"},
    {"school_name": "Edison School", "address": "115 Boston Terrace+Bridgeport+CT 06610", "students": 340, "website": "https://www.bridgeportedu.net/Edison", "phone": "203-275-2500"},
    {"school_name": "Hall School", "address": "290 Clermont Avenue+Bridgeport+CT 06610", "students": 450, "website": "https://www.bridgeportedu.net/Hall", "phone": "203-275-3600"},
    {"school_name": "High Horizons Magnet School", "address": "700 Palisade Avenue+Bridgeport+CT 06610", "students": 500, "website": "https://www.bridgeportedu.net/HighHorizons", "phone": "203-275-4692"},
    {"school_name": "Hooker School", "address": "138 Roger Williams Road+Bridgeport+CT 06610", "students": 280, "website": "https://www.bridgeportedu.net/Hooker", "phone": "203-275-1701"},
    {"school_name": "Jettie S. Tisdale School", "address": "250 Hollister Avenue+Bridgeport+CT 06607", "students": 600, "website": "https://www.bridgeportedu.net/Tisdale", "phone": "203-275-1751"},
    {"school_name": "John Winthrop School", "address": "85 Eckart Street+Bridgeport+CT 06606", "students": 420, "website": "https://www.bridgeportedu.net/Winthrop", "phone": "203-275-1901"},
    {"school_name": "Luis Munoz Marin School", "address": "479 Helen Street+Bridgeport+CT 06608", "students": 760, "website": "https://www.bridgeportedu.net/Marin", "phone": "203-275-4900"},
    {"school_name": "Madison School", "address": "376 Wayne Street+Bridgeport+CT 06606", "students": 320, "website": "https://www.bridgeportedu.net/Madison", "phone": "203-275-3150"},
    {"school_name": "Multicultural Magnet School", "address": "700 Palisade Avenue+Bridgeport+CT 06610", "students": 470, "website": "https://www.bridgeportedu.net/MultiMagnet", "phone": "203-275-1802"},
    {"school_name": "New Beginnings Family Academy", "address": "184 Garden Street+Bridgeport+CT 06605", "students": 500, "website": "https://www.bridgeportedu.net/NewBeginnings", "phone": "203-384-2890"},
    {"school_name": "Park City Magnet School", "address": "1526 Chopsey Hill Road+Bridgeport+CT 06606", "students": 540, "website": "https://www.bridgeportedu.net/ParkCityMagnet", "phone": "203-275-3773"},
    {"school_name": "Read School", "address": "130 Ezra Street+Bridgeport+CT 06606", "students": 600, "website": "https://www.bridgeportedu.net/Read", "phone": "203-275-2600"},
    {"school_name": "Roosevelt School", "address": "680 Park Avenue+Bridgeport+CT 06604", "students": 500, "website": "https://www.bridgeportedu.net/Roosevelt", "phone": "203-275-2100"},
    {"school_name": "Six to Six Magnet School", "address": "601 Pearl Harbor Street+Bridgeport+CT 06610", "students": 400, "website": "https://www.bridgeportedu.net/SixtoSix", "phone": "203-366-8241"},
    {"school_name": "Thomas Hooker School", "address": "138 Roger Williams Road+Bridgeport+CT 06610", "students": 360, "website": "https://www.bridgeportedu.net/Hooker", "phone": "203-275-1701"},
    {"school_name": "Waltersville School", "address": "150 Hallett Street+Bridgeport+CT 06608", "students": 470, "website": "https://www.bridgeportedu.net/Waltersville", "phone": "203-275-1000"},
    {"school_name": "Wilbur Cross School", "address": "1775 Reservoir Avenue+Bridgeport+CT 06606", "students": 440, "website": "https://www.bridgeportedu.net/WilburCross", "phone": "203-275-4300"}
]


# Combine all school lists into one DataFrame
all_schools = (bridgeport_schools)
schools_data = pd.DataFrame(all_schools)

# Adjust the address column to replace "+" with ", "
schools_data['address'] = schools_data['address'].str.replace('+', ', ', regex=False)

# Define the output directory for the markdown files
output_dir = '.'
os.makedirs(output_dir, exist_ok=True)

# Adding district names to the DataFrame
districts = [
    ("Bridgeport Public School District", bridgeport_schools)
]

# Assign district names to each row in the DataFrame
schools_data['district_name'] = ""
for district_name, schools_list in districts:
    for school in schools_list:
        schools_data.loc[schools_data['school_name'] == school['school_name'], 'district_name'] = district_name


# Function to generate markdown files
def generate_markdown_by_index(row):
    # Simplify the school name for the directory and file
    district_name_simple = "Bridgeport/" + row['district_name'].replace(" ", "_").replace("/", "_").replace("\\", "_")
    school_name_simple = row['school_name'].replace(" ", "_").replace("/", "_").replace("\\", "_")
    path = os.path.join(output_dir, district_name_simple)
    os.makedirs(path, exist_ok=True)

    # Filename for the markdown
    file_path = os.path.join(path, f"{school_name_simple}.md")

    # Markdown content with front-matter and details
    with open(file_path, 'w') as file:
        file.write(f"---\nlayout: page\ntitle: {row['school_name']}\n---\n")  # School Name
        file.write(
            f"# Navigation\n\n[[All countries/states/provinces]](../../../..) > [[All Connecticut Districts]](../../..) > [[All In Bridgeport District]](../..) > [[All schools in district]](..)\n\n")

        file.write(f"# {row['school_name']} ({row['district_name']})\n\n")  # School Name and area as header

        # Loop through keys per school
        for key, value in row.items():
            if key not in ['district_name', 'school_name']:
                if str(value).startswith("http"):
                    value = "<" + value + ">"
                file.write(f"**{key.replace('_', ' ').title()}**: {value}\n\n")

        file.write(f"**School's overall airborne virus protection grade (0-5)**: 0\n\n")
        file.write(f"**Discord, Facebook, or WhatsApp group for discovery/advocacy for THIS school**: TODO\n\n")
        file.write(f"**School's policy on Ventilation**: TODO\n\n")
        file.write(f"**School's Ventilation Work Completion**: TODO\n\n")
        file.write(f"**School's Air-Purification**: TODO\n\n")
        file.write(f"**School's CO2 monitoring to actively drive ventilation and filtration**: TODO\n\n")
        file.write(f"**School's Wikidata URL**: TODO")
        file.write(f"\n\n\n[Edit this page](https://github.com/ventilate-schools/CT/edit/main/{file_path}).")
        file.write(f" See also [rules for contribution](../../../contribution-rules/)")


# Generate markdown files for each school
schools_data.apply(generate_markdown_by_index, axis=1)


def create_area_and_root_index():
    # Create a dictionary to keep track of schools in each district
    districts_dict = {}

    for index, row in schools_data.iterrows():
        district_name_simple = "Bridgeport/" + row['district_name'].replace(" ", "_").replace("/", "_").replace("\\", "_")
        school_name_simple = row['school_name'].replace(" ", "_").replace("/", "_").replace("\\", "_")

        # Check if the district already exists in the dictionary
        if district_name_simple not in districts_dict:
            districts_dict[district_name_simple] = []

        # Append the school name to the district's list
        districts_dict[district_name_simple].append(school_name_simple)

    # Write an index markdown file for each district and gather data for root index
    root_index_content = "---\ntitle: Schools in Connecticut and their ventilation status\n---\n"

    root_index_content += (
        "\n# Navigation\n\n[[All countries/states/provinces]](..)\n\n# Purpose of site\n\nGiven **COVID-19 is Airborne** and the world is pushing to better ventilate "
        "schools for long term student and teacher health, we're tracking the "
        "progress for that in Connecticut. This is ahead of government effort to do the same. If government starts to "
        "track this work, this effort will continue because that effort might be weak."
        "We're guided by 33 profs and PhDs who are pushing for a policy change in a "
        "March 2024 article on **Science.org**: [Mandating indoor air quality for public buildings](https://drive.google.com/file/d/16l_IH47cQtC7fFuafvHca7ORNVGITxx8/view). "
        "Not only active ventilation (which should "
        "be mechanical heat recovery type in this age), but air filtration/purification "
        "too and CO2 monitoring to drive ventilation levels, as CO2 inside is a proxy indicator "
        "for COVID risk. As it happens the WHO also have a [2023 airborne risk assessment guide](https://iris.who.int/handle/10665/376346)\n\n"
        "Know that other diseases are airborne too: Measles "
        "(studies [1](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2810934/pdf/10982072.pdf) "
        "[2](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3880795/pdf/nihms532643.pdf) "
        "[3](https://pubmed.ncbi.nlm.nih.gov/31257413/) "
        "[4](https://www.sciencedirect.com/science/article/pii/S0196655316305363)), "
        "Influenza, RSV and TB. The same "
        "ventilation and air filtration measures reduce transmission of those too.\n\n When we say "
        "student and teacher health, we're wanting absences to go down too. If we lower "
        "transmission in schools, we reduce multi-generation transmission too, as kids bring "
        "infections home to parents. With lowered transmission, we also reduce long COVID, "
        "where the worst sufferers have disappeared from education and the workplace.\n\n")

    root_index_content += (
        "\n## Leaderboard\n\n1. to be announced\n2. to be announced\n3. to be announced\n4. to be announced\n5. to be announced\n\n")

    root_index_content += ("{% include_relative grade.html %}\n\n")

    root_index_content += ("# Connecticut School Districts:\n\n")

    for district, schools in districts_dict.items():
        district_index_file_path = os.path.join(output_dir, district, "index.md")
        os.makedirs(os.path.join(output_dir, district), exist_ok=True)

        with open(district_index_file_path, 'w') as district_index_file:
            district_index_file.write(f"---\nlayout: page\ntitle: Schools in {district.replace('_', ' ')}\n---\n")
            district_index_file.write(
                f"# Navigation\n\n[[All countries/states/provinces]](../..) > [[All Connecticut districts]](..)\n\n")
            district_index_file.write(f"# Schools in {district.replace('_', ' ')}\n\n")
            district_index_file.write("{% include_relative grade.html %}\n\n")
            district_index_file.write(f"**Schools:**\n\n")
            for school in schools:
                school_file_path = school
                district_index_file.write(f"- [{school.replace('_', ' ')}]({school_file_path}.md)\n")

        # Add to root index content with cleaner URLs
        root_index_content += f"- [{district.replace('_', ' ')}]({district}/): {len(schools)} schools\n"

    root_index_content += ("\n\n# Site ownership\n\nThis site is edited by volunteers who're "
                           "interested in accelerating the work to complete the adequate ventilation of Connecticut schools. "
                           "This effort was not commissioned by education authorities or government.\n\n"
                           "[Edit this page](https://github.com/ventilate-schools/CT/edit/main/index.md). See also [rules for contribution](./contribution_rules/)")

    # Write the root index file
    root_index_path = os.path.join(output_dir, "index.md")
    with open(root_index_path, 'w') as root_index_file:
        root_index_file.write(root_index_content)


# Call the function to create index markdown files and root index
create_area_and_root_index()

# Print confirmation
print("Index markdown files with front matter and links have been created in each area directory and root directory.")
