from pyscript import display, document

#NO AI WAS USED DURING THE MAKING OF THIS PROJECT
#Random generated names by using this website: https://www.fantasynamegenerators.com/filipino-names.php
def add_brand (e):
    document.getElementById('output1').innerHTML = ""
    grade_seven = {'Glenn Alcantara', 'Arthur Fernandez', 'Meagan Escano'}
    grade_eight = {'Raina Agcaoili', 'Immanuel Arce', 'Jerald Aguilar', 'Kassidy Santos'}
    grade_nine = {'Michelle Acosta', 'Aimee Catubig', 'Inez Estillore'}
    grade_ten = {'Hayden Alonzo', 'Reid Cunanan', 'Tyra Garcia'}
    name_one = document.getElementById('firstname').value
    name_two = document.getElementById('lastname').value
    new_Student = name_two + " " + name_one
    #assign the value to a set variable
    new_brand_set = {new_Student.title()}

    all_names = grade_seven | grade_eight | grade_nine | grade_ten | new_brand_set
    total_members = len(grade_seven | grade_eight | grade_nine | grade_ten | new_brand_set)
    name_list = "<br>".join(sorted(all_names))

    #display
    document.getElementById('output1').innerHTML = f'<br><h1><b>List of Club Members:</b></h1> <br> {name_list}'
    display(f'Number of Members: {total_members}',target="output1")