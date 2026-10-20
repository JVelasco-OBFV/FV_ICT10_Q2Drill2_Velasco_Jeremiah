from pyscript import display, document

def add_brand (e):
    document.getElementById('output1').innerHTML = ""
    grade_seven = {'Bahay Kubo', 'Singkamas Talong', 'Sigarilyas Mani'}
    grade_eight = {'Kundol Patola', 'Upo Kalabasa', 'Labanos Mustasa', 'Sibuyas Kamatis'}
    grade_nine = {'Bawang Luya', 'Halamang Linga', 'Sitaw Patani'}
    grade_ten = {'Sili Labuyo', 'Saging Saba', 'Ube Kamote'}
    name_one = document.getElementById('firstname').value
    name_two = document.getElementById('lastname').value
    new_Student = name_two + " " + name_one
    #assign the value to a set variable
    new_brand_set = {new_Student.title()}

    all_names = grade_seven | grade_eight | grade_nine | grade_ten | new_brand_set
    total_members = len(grade_seven | grade_eight | grade_nine | grade_ten | new_brand_set)
    name_list = "<br>".join(sorted(all_names))

    #display
    document.getElementById('output1').innerHTML = f'<br><h1><b>All Brands:</b></h1> <br> {name_list}'
    display(f'Total Brands: {total_members}',target="output1")