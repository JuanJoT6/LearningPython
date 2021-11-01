from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
import time

trash = []

filename = "Tucarro_scraped_11.csv"
f = open(filename, "w")

headers = "Car name, Year car, Location car, Price car\n"

f.write(headers)

def seguir():
    slñ = input("Deseas continuar: ")
    if slñ == "y":
        tucarro_pages()
    if slñ == "n":
        f.close()


def tucarro_pages():
    
    print("1, 49, 97, 145, 193, 241, 289, 337, 385, 433")
    page = input("numero de la pagina:")

    
  
    url = "https://carros.tucarro.com.co/renault/duster/_Desde_" + str(page)

    uClient = uReq(url)
    page = uClient.read()
    uClient.close()

    page_soup = BeautifulSoup(page , "html.parser")

    containers = page_soup.find_all("div",{"class":"rowItem item highlighted item--grid new"})


    for container in containers:

        name_car_container = container.findAll("span",{"class":"main-title"})
        name_car = name_car_container[0].text

   
        year_car_container = container.findAll("div",{"class":"item__attrs"})
        year_car = year_car_container[0].text 


        location_car_container = container.findAll("div",{"class":"item__location"})
        location_car = location_car_container[0].text 

        price_car_container = container.findAll("span",{"class":"price__fraction"})
        price_car = price_car_container[0].text

        print("Car name: " + name_car)
        print("Car year: " + year_car)
        print("Car location: " + location_car)
        print("Car price: " + price_car)

        if price_car <= str(40000000) :
            f.write(name_car + "," + year_car + "," + location_car + "," + price_car + "\n")
        else:
            trash = name_car  + year_car  + location_car + price_car 
    seguir()

tucarro_pages()