import selenium
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time



#                                                 \/QUESTION NUM                          \/QUESTION OPTION NUM
# /html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div
# /html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div

# /html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/span/div/div[1]/label/div/div[1]/div
# /html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/span/div/div[2]/label/div/div[1]/div
# /html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/span/div/div[3]/label/div/div[1]/div
# /html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/span/div/div[4]/label/div/div[1]/div


# /html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div/span/div/div[1]/label/div/div[1]/div
# /html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div/span/div/div[2]/label/div/div[1]/div
# /html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div/span/div/div[3]/label/div/div[1]/div

# /html/body/div/div[2]/form/div[2]/div  <-- chrome googleforms XPATH
# /html/body/div/div[2]/form/div[2]/div/div[2]








# mainform CLASS = o3Dpx
# questao class = nWQGrd zwllIb
# 
#                                                 \/QUESTION NUM                          \/QUESTION OPTION NUM
# /html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div
# /html/body/div/div[2]/form/div[2]/div/div[2]/div[{}]/div/div/div[2]/div/div/span/div/div[{}]/label/div/div[1]/div

def main():





    options = uc.ChromeOptions()
    options.add_argument("--window-size=1200,800")
    # formsURL = "https://docs.google.com/forms/d/e/1FAIpQLScpoq9tFo4xuGm22tQ2TfB9q8C5xQK4ztQlb9ME3-jih9rW6g/viewform"
    formsURL = "https://docs.google.com/forms/d/e/1FAIpQLSdd3RIqfQSJKVnyHy188js1aF5I8bm1cwRZh8mx0gJaGuzY5w/viewform"
    
    driver = uc.Chrome(options=options, headless=False, use_subprocess=False)



    def getQuestionsAndOptions():
        perguntas = 1 #Quantidade de questoes do forms
        opcoes = 0    #Quantidade de opcoes do forms

        nQuestao = 1 #Contador das divs de perguntas
        nOpcao = 1   #Contador de divs de opcoes

        questionDiv = driver.find_elements(By.CLASS_NAME, "Qr7Oae") #Lista com as questoes
        optionDiv = driver.find_elements(By.CLASS_NAME, "nWQGrd") #Lista com as opcoes


        for div in questionDiv:
            with open("teste.txt", "a") as f:
                f.write(f"{div.text}\n\n\n")








    driver.get(formsURL)
    driver.set_window_size(1200, 800)

    getQuestionsAndOptions()


    
    # time.sleep(50000)


if __name__ == "__main__":
    main()