from anticaptchaofficial.imagecaptcha import *
import selenium
from selenium import webdriver
from selenium.webdriver import Chrome
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time
from Screenshot import Screenshot
import win32com.client
from getpass import getpass
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions as ex
from defs import *

#Para começar, irei perguntar para o usuario qual relatório ele(a) quer pegar.
while True:
    try:
        report = int(input(
            'Utilizando de 1 a 3, Selecione o NÚMERO do relatorio que você deseja, sendo: \n 1- Payouts Report \n 2- Physical Card Orders Report \n 3- Corporate Activation Report \n'))

    except ValueError:
        print('Resposta Invalida. Por favor escolha um valor NUMERICO de 1 a 3 \n')

    else:
        if report in range(1, 4):
            break

if report == '1':
    report = "Payouts Report"
if report == '2':
    report = "Physical Card Orders Report"
elif report == '3':
    report = "Corporate Activation Report"

print(f'deixa eu pegar o {report} Pra você. \n Mas para isso, por favor, digite:')
#pego as credenciais do cliente, mas não as armazeno. Eu poderia fazer uma conexão com um banco, mas pro proposito, não achei que valeria a pena.
login = input(' O email que você usa no report center \n')
senha = input(' Agora a senha para que eu possa pegar para você! \n mas fique tranquilo(a), não armazeno nenhum dado! \n')

#Agora é hora de entrar no site dos relatorios e baixar aquilo que o cliente quis.

#ob = Screenshot.Screenshot()
api = 'Chave_api'
url = '##################'

print('agora é comigo, vou abrir seu navegador ok? mas pode me minimizar. Meu tempo de processamento é 5-7 minutos, dependo da sua banda larga!')
#SEGUNDA FASE: entrando no site

navegador = webdriver.Chrome()
#op = webdriver.ChromeOptions()
#op.add_argument('headless')
#navegador = webdriver.Chrome(options=op)
navegador.get(url)
#navegador.maximize_window()

email = navegador.find_element_by_xpath('//*[@id="user-contact"]')
email.click()
email.send_keys(login)

time.sleep(3)


print('Resolvendo o captcha....')

try:
    # QUARTA FASE : resolvendo o captcha
    # pegando a imagem
    img = navegador.find_element_by_class_name('captcha')
    cap = img.find_element_by_xpath('//*[@id="captcha__image"]')
    cap = cap.screenshot('image.jpeg')

    time.sleep(2)
    # dando a imagem pra api e pedindo o texto
    solver = imagecaptcha()
    solver.set_verbose(1)
    solver.set_key(api)
    solver.set_soft_id(0)

    captcha_text = solver.solve_and_return_solution("image.jpeg")

    time.sleep(1)
    escrever_cap = navegador.find_element_by_xpath('//*[@id="captcha"]')
    escrever_cap.click()
    escrever_cap.send_keys(captcha_text)
    time.sleep(1)
    # apertando next
    prox = navegador.find_element_by_xpath('//*[@id="submit-identity-form"]/div[3]/button').click()



except:
    time.sleep(2)
    #QUARTA FASE : resolvendo o captcha
    #pegando a imagem
    img = navegador.find_element_by_class_name('captcha')
    cap = img.find_element_by_xpath('//*[@id="captcha__image"]')
    cap = cap.screenshot('image.jpeg')

    time.sleep(2)
    # dando a imagem pra api e pedindo o texto
    solver = imagecaptcha()
    solver.set_verbose(1)
    solver.set_key(api)
    solver.set_soft_id(0)

    captcha_text = solver.solve_and_return_solution("image.jpeg")

    time.sleep(1)
    escrever_cap = navegador.find_element_by_xpath('//*[@id="captcha"]')
    escrever_cap.click()
    escrever_cap.send_keys(captcha_text)
    time.sleep(1)
    # apertando next
    prox = navegador.find_element_by_xpath('//*[@id="submit-identity-form"]/div[3]/button').click()

print('Pegando o otp...')
#QUINTA FASE : resolvendo o otp
time.sleep(45)
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
inbox = outlook.GetDefaultFolder(6)
messages = inbox.Items
message = messages.GetLast()
txt = message.body
sender= message.Sender()
senA = message.Sender.Address

otp = txt[1328:1332]

preencher_otp = navegador.find_element_by_xpath('//*[@id="otp"]')
preencher_otp.click()
preencher_otp.send_keys(otp)
time.sleep(1)

preencher_otp.send_keys(Keys.ENTER)

#SEXTA FASE : Colocando a senha do input
time.sleep(1)
passw = navegador.find_element_by_xpath('//*[@id="v_password"]')
passw.click()
passw = passw.send_keys(senha)
time.sleep(1)
navegador.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[4]/form/div[2]/button').click()

time.sleep(8)

print('Agora deixa eu baixar o relatorio... Agora pode demorar um pouco pois depende da sua banda larga!\n média de tempo: 5-7 minutos')


relatorios = navegador.find_element_by_class_name('tabs__container')
div1 = relatorios.find_element_by_tag_name('div')
#separando em 2, a parte das abas e a parte dos relatorios que quero
abas = div1.find_element_by_tag_name('nav')
Parte_de_baixo = div1.find_element_by_tag_name('section')



#pt1 ) escolhendo os relatorios
tab_item = Parte_de_baixo.find_element_by_class_name('tab-item')
columns = tab_item.find_element_by_class_name('columns')
divs_col = columns.find_elements_by_tag_name('div')
box = columns.find_element_by_class_name('box')
ps= box.find_elements_by_tag_name('p')
#PAYOUTS REPORT

divs_botao = navegador.find_element_by_xpath(f'//p[2][contains(text(),"{report}")]/following-sibling::div')
button_tags = divs_botao.find_elements_by_tag_name('button')
generate = button_tags[0]
generate.click()
data_inicial = navegador.find_element_by_xpath('//div[@role="button"]')
data_inicial.click()

time.sleep(1)
pagination = navegador.find_element_by_class_name('background')
dd = navegador.find_element_by_class_name('dropdown-menu')
divs2 = dd.find_elements_by_tag_name('div')
dp_header = dd.find_element_by_class_name('datepicker-header')
div_head = dp_header.find_element_by_tag_name('div')
seta_esq = div_head.find_element_by_class_name('pagination-previous')
time.sleep(0.5)
for clicks in range (0,5):
    seta_esq.click()
time.sleep(0.4)
#escolher o dia
calendario = dd.find_element_by_class_name('datepicker-content')
tabela_data = calendario.find_element_by_tag_name('section')
body = tabela_data.find_element_by_class_name('datepicker-body')
primeira_linha = body.find_element_by_class_name('datepicker-row')
primeiro_dia = primeira_linha.find_element_by_tag_name('a')
primeiro_dia.click()
time.sleep(2)
generate_button = dd.find_element_by_xpath('/html/body/div/div/div[2]/div/section/div/div/div[3]/div[2]/div/button/span')
generate_button.click()
time.sleep(2)
close_sec = navegador.find_element_by_xpath('/html/body/div/div/div[2]/div/section/div/div/div[3]/div[2]/button')
close_sec.click()

time.sleep(1)

sessao= abas.find_elements_by_tag_name('span')
gen_reports = sessao[1]
gen_reports.click()

time.sleep(300)

download = navegador.find_element_by_xpath('//td[@data-label = "ACTION"]')
download.click()

print('Pronto! Procure na sua pasta DOWNLOADS. Caso não ache lá, pressione a tecla do windows e procure pelo nome "Payouts_Report.xlsx')
navegador.quit()
