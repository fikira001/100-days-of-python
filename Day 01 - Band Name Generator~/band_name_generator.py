#original code 
"""print("Welcome to the Company Name Genarator")

nick_name = input("Enter Your Nick Name:\n").capitalize()

business_sector  = input("Enter Your Business Sector:\n").capitalize()

print ("your Company name can be:", nick_name, business_sector, "Hope you like it")"""

#modified 

print("Welcome to the Company Name Generator")

# Common suffixes/preffixes organized by sector
sector_terms = {
    'tech': ['Solutions', 'Innovations', 'Technologies', 'Labs', 'Systems', 'Digital', 'Networks'],
    'food': ['Eats', 'Kitchen', 'Delights', 'Bites', 'Cuisine', 'Catering', 'Grill'],
    'fashion': ['Style', 'Boutique', 'Couture', 'Wear', 'Threads', 'Designs', 'Atelier'],
    'health': ['Care', 'Wellness', 'Therapy', 'Med', 'Vitality', 'Fitness', 'Clinics'],
    'general': ['Hub', 'Group', 'Enterprises', 'Ventures', 'Co', 'Corp', 'Global']
}

nick_name = input("Enter Your Nick Name:\n").strip().capitalize()
business_sector = input("Enter Your Business Sector:\n").strip().lower()

# Get relevant terms or default to general
sector_options = sector_terms.get(business_sector, sector_terms['general'])

# Generate multiple name combinations
name_options = [
    f"{nick_name} {sector_options[0]}",
    f"{nick_name} {business_sector.capitalize()} {sector_options[1]}",
    f"{business_sector.capitalize()} {nick_name} {sector_options[2]}",
    f"{nick_name}{sector_options[3]}",
    f"The {sector_options[4]} {nick_name}",
    f"{nick_name} & Co {sector_options[5]}"
]

print("\nSuggested Name Options:")
for i, name in enumerate(name_options, 1):
    print(f"{i}. {name}")

print("\nHope you find a name you love!")