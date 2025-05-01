import json

# Load JSON data
with open("data.json", "r") as f:
    data = json.load(f)

# Function to convert numbers to words
def number_to_words(n):
    num_words = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", 
                 "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve"]
    return num_words[n] if n < len(num_words) else str(n)  # Converts numbers to words, fallback to string

# Generate LaTeX macros
latex_output = ""


# ==============================================================
# Contact information
# ==============================================================

latex_output += "%------------------------------------\n"
latex_output += "% CONTACT INFORMATION\n"
latex_output += "%------------------------------------\n\n"
latex_output += f"\\newcommand{{\\name}}{{{data['contact']['name']}}}\n"
latex_output += f"\\newcommand{{\\designation}}{{{data['contact']['designation']}}}\n"
latex_output += f"\\newcommand{{\\phone}}{{{data['contact']['phone']}}}\n"
latex_output += f"\\newcommand{{\\location}}{{{data['contact']['location']}}}\n"
latex_output += f"\\newcommand{{\\email}}{{{data['contact']['email']}}}\n"
latex_output += f"\\newcommand{{\\github}}{{{data['contact']['github']}}}\n"
latex_output += f"\\newcommand{{\\linkedin}}{{{data['contact']['linkedin']}}}\n\n\n"


# ==============================================================
# Profile summary
# ==============================================================

latex_output += "%------------------------------------\n"
latex_output += "% PROFILE SUMMARY\n"
latex_output += "%------------------------------------\n\n"
latex_output += f"\\newcommand{{\\profile}}{{{data['profile']}}}\n\n\n"


# ==============================================================
# Skills
# ==============================================================

latex_output += "%------------------------------------\n"
latex_output += "% SKILLS\n"
latex_output += "%------------------------------------\n\n"

skills_items = list(data["skills"].items())  # Convert to list for iteration tracking

for index, (category, skills_list) in enumerate(skills_items, start=0):  # Start numbering from 1
    category_num = number_to_words(index)  # Convert number to words
    capitalized_category = category.capitalize()  # Ensure first letter is uppercase

    # Define macros for numbered skill categories and lists
    latex_output += f"\\newcommand{{\\skillsCategory{category_num}}}{{{capitalized_category}}}\n"
    latex_output += f"\\newcommand{{\\skills{category_num}}}{{" + ", ".join(skills_list) + "}"

    # Add spacing only if it's not the last iteration
    if index == len(skills_items) - 1:
        latex_output += "\n\n\n"
    else:
        latex_output += "\n\n"


# ============================================================== 
# Experience 
# ============================================================== 

latex_output += "%------------------------------------\n"
latex_output += "% EXPERIENCE\n"
latex_output += "%------------------------------------\n\n"

for i, exp in enumerate(data["experience"]):
    exp_num = number_to_words(i)  # Convert index to word
    latex_output += f"\\newcommand{{\\expTitle{exp_num}}}{{{exp['title']}}}\n"
    
    if "link" in exp and exp["link"]:
        latex_output += f"\\newcommand{{\\expCompany{exp_num}}}{{\\href{{{exp['link']}}}{{{exp['company']}}}}}\n"
    else:
        latex_output += f"\\newcommand{{\\expCompany{exp_num}}}{{{exp['company']}}}\n"

    latex_output += f"\\newcommand{{\\expStart{exp_num}}}{{{exp['start']}}}\n"
    latex_output += f"\\newcommand{{\\expEnd{exp_num}}}{{{exp['end']}}}\n"

    responsibilities = "".join(f"\n\\item {resp}" for resp in exp["responsibilities"])
    latex_output += f"\\newcommand{{\\expResponsibilities{exp_num}}}{{{responsibilities}}}"
    
    if i == len(data["experience"]) - 1:  # Last iteration
        latex_output += "\n\n\n"
    else:
        latex_output += "\n\n"
    

# ============================================================== 
# Education 
# ============================================================== 

latex_output += "%------------------------------------\n"
latex_output += "% EDUCATION\n"
latex_output += "%------------------------------------\n\n"

for i, edu in enumerate(data["education"]):
    edu_num = number_to_words(i)  # Convert index to word
    latex_output += f"\\newcommand{{\\eduDegree{edu_num}}}{{{edu['degree']}}}\n"

    if "link" in edu and edu["link"]:
        latex_output += f"\\newcommand{{\\eduInstitution{edu_num}}}{{\\href{{{edu['link']}}}{{{edu['institution']}}}}}\n"
    else:
        latex_output += f"\\newcommand{{\\eduInstitution{edu_num}}}{{{edu['institution']}}}\n"

    latex_output += f"\\newcommand{{\\eduStart{edu_num}}}{{{edu['start']}}}\n"
    latex_output += f"\\newcommand{{\\eduEnd{edu_num}}}{{{edu['end']}}}"

    if "coursework" in edu:
        coursework = ", ".join(edu["coursework"])
        latex_output += f"\n\\newcommand{{\\eduCoursework{edu_num}}}{{\n\\item Coursework: {coursework}}}"
    
    if i == len(data["education"]) - 1:  # Last iteration
        latex_output += "\n\n\n"
    else:
        latex_output += "\n\n"


# ==============================================================
# Projects
# ==============================================================

latex_output += "%------------------------------------\n"
latex_output += "% PROJECTS\n"
latex_output += "%------------------------------------\n\n"

for i, project in enumerate(data["projects"]):
    project_num = number_to_words(i)  # Convert index to word
    latex_output += f"\\newcommand{{\\projTech{project_num}}}{{{project['tech']}}}\n"
    latex_output += f"\\newcommand{{\\projTitle{project_num}}}{{{project['title']}}}\n"

    # Add project link if available
    if "link" in project and project["link"]:
        latex_output += f"\\newcommand{{\\projSource{project_num}}}{{\\href{{{project['link']}}}{{{project['source']}}}}}\n"
    else:
        latex_output += f"\\newcommand{{\\projSource{project_num}}}{{{project['source']}}}\n"

    # Format description list
    description = "".join(f"\n\\item {desc}" for desc in project["description"])
    latex_output += f"\\newcommand{{\\projDetails{project_num}}}{{{description}}}"

    if i == len(data["projects"]) - 1:  # Last iteration
        latex_output += "\n\n\n"
    else:
        latex_output += "\n\n"
    

# ==============================================================

# Save macros to a separate LaTeX file
with open("macros.tex", "w") as f:
    f.write(latex_output)

print("Resume macros saved to macros.tex")