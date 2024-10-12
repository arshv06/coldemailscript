def generate_emails(names, company_domain):
    all_emails = []
    
    for first_name, last_name in names:
        # Capitalize first and last names
        first_name = first_name.capitalize()
        last_name = last_name.capitalize()

        # Pre-calculate the necessary parts for slicing
        first_initial = first_name[0]
        last_initial = last_name[0]
        first_three = first_name[:3]
        last_three = last_name[:3]
        first_two = first_name[:2]
        last_two = last_name[:2]

        # Define all email formats with pre-calculated variables
        email_formats = [
            f"{first_initial}{last_name}@{company_domain}",         # FLast@company.com
            f"{first_name}{last_name}@{company_domain}",            # FirstLast@company.com
            f"{last_name}{first_initial}@{company_domain}",         # LastF@company.com
            f"{first_name}{last_initial}@{company_domain}",         # FirstL@company.com
            f"{first_three}{last_name}@{company_domain}",           # FirLast@company.com
            f"{first_name}{last_two}@{company_domain}",             # FirstLa@company.com
            f"{last_initial}{first_name}@{company_domain}",         # LFirst@company.com
            f"{first_two}{last_name}@{company_domain}",             # FiLast@company.com
            f"{first_name}{last_three}@{company_domain}",           # FirstLas@company.com
            f"{first_name}.{last_name}@{company_domain}",           # First.Last@company.com
            f"{last_name}@{company_domain}",                        # Last@company.com
            f"{last_name}{first_two}@{company_domain}",             # LastFi@company.com
            f"{last_name}{first_three}@{company_domain}",           # LastFir@company.com
            f"{first_name}@{company_domain}",                       # First@company.com
            f"{first_name}{first_initial}{last_initial}@{company_domain}"  # FirstML@company.com
        ]

        # Join the emails into a comma-separated string and add to the list
        all_emails.append(', '.join(email_formats))

    return all_emails

# Example Usage
company_domain = input("Enter company domain (e.g., qualcomm.com): ")

# Input multiple names
names_input = input("Enter names (first and last) separated by commas (e.g., Ken French, Suze Balatsos): ")
names = [tuple(name.strip().split()) for name in names_input.split(",")]

emails_list = generate_emails(names, company_domain)

# Print results for each name
for i, (first, last) in enumerate(names):
    print(f"Emails for {first} {last} at {company_domain}: {emails_list[i]}\n")
