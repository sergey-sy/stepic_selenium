# stepic_selenium
this is repo for course from https://stepik.org/course/575/syllabus
it uses chromedriver and google chrome browser (driver and browser versions should be the same)

you can use chomedriver which located in global directory
$ sudo mv chromedriver /usr/local/bin
driver = webdriver.Chrome()

or you can save chromedriver in project folder
in this case you should transfer current location chromedriver
driver = webdriver.Chrome(executable_path='your_project_path/chromedriver')
