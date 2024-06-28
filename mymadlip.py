name = input("Enter Your Name : ").capitalize()
university_name = input("Enter Your University Name : ").upper()
degree_name = input("Enter Your Degree Name : ").upper()
branch_name = input("Enter Your Branch Name : ").upper()
programming_language_name = input("Enter Programming Name in which You Know Very Well : ").capitalize()
experience = int(input("Enter Your Professional Experience in Year : "))
old_company_name = input("Enter Your Previous Company Name : ").capitalize()
project_name = input("Enter Project Name that Made by You : ").capitalize()
technology_name = input("Enter Which Technology You Know Well : ")
tools_name = input("Enter Which Tools You Know Well : ")
framework_name = input("Enter Which Framework You Know Well : ")

print("\n----------------------------------------------------------\n")
print(f'''“Thank you for inviting me for this interview. My name is {name}, and I am thrilled to be here today to discuss my qualifications for the software developer position.
“My strong passion for programming and problem-solving led me to pursue a career as a software developer. I hold a {degree_name} Degree in {branch_name} from {university_name}, where I gained a solid foundation in programming languages such as {programming_language_name}. I have {experience} years of experience as a software developer in {old_company_name}.“
“I successfully designed, developed, and deployed {project_name} in my previous job. I am experienced in {technology_name}, {framework_name} or {tools_name} and constantly strive to stay updated with industry trends.”''')

print("\n----------------------------------------------------------\n")

