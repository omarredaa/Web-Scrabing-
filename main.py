import requests
import bs4
list_links = []
list_links.append('https://www.amazon.eg/s?k=%D9%85%D8%B1%D8%A7%D9%88%D8%AD+%D8%AA%D8%A8%D8%B1%D9%8A%D8%AF+%D9%84%D8%A7%D8%A8%D8%AA%D9%88%D8%A8&page=2&crid=ULJUBMN5YSGK&qid=1671303093&sprefix=%D9%85%D8%B1%D8%A7%D9%88%D8%AD+%D9%84%D8%A7%D8%A8%2Caps%2C5033&ref=sr_pg_2')
list_links.append('https://www.amazon.eg/s?k=%D9%85%D8%B1%D8%A7%D9%88%D8%AD+%D8%AA%D8%A8%D8%B1%D9%8A%D8%AF+%D9%84%D8%A7%D8%A8%D8%AA%D9%88%D8%A8&page=3&crid=ULJUBMN5YSGK&qid=1671305228&sprefix=%D9%85%D8%B1%D8%A7%D9%88%D8%AD+%D9%84%D8%A7%D8%A8%2Caps%2C5033&ref=sr_pg_3')
list_links.append('https://www.amazon.eg/s?k=%D9%85%D8%B1%D8%A7%D9%88%D8%AD+%D8%AA%D8%A8%D8%B1%D9%8A%D8%AF+%D9%84%D8%A7%D8%A8%D8%AA%D9%88%D8%A8&page=2&crid=ULJUBMN5YSGK&qid=1671303093&sprefix=%D9%85%D8%B1%D8%A7%D9%88%D8%AD+%D9%84%D8%A7%D8%A8%2Caps%2C5033&ref=sr_pg_4')
list_links.append('https://www.amazon.eg/s?k=%D9%85%D8%B1%D8%A7%D9%88%D8%AD+%D8%AA%D8%A8%D8%B1%D9%8A%D8%AF+%D9%84%D8%A7%D8%A8%D8%AA%D9%88%D8%A8&page=5&crid=ULJUBMN5YSGK&qid=1671305784&sprefix=%D9%85%D8%B1%D8%A7%D9%88%D8%AD+%D9%84%D8%A7%D8%A8%2Caps%2C5033&ref=sr_pg_5')
list_links.append('https://www.amazon.eg/s?k=%D9%85%D8%B1%D8%A7%D9%88%D8%AD+%D8%AA%D8%A8%D8%B1%D9%8A%D8%AF+%D9%84%D8%A7%D8%A8%D8%AA%D9%88%D8%A8&page=6&crid=ULJUBMN5YSGK&qid=1671305817&sprefix=%D9%85%D8%B1%D8%A7%D9%88%D8%AD+%D9%84%D8%A7%D8%A8%2Caps%2C5033&ref=sr_pg_6')
list_links.append('https://www.amazon.eg/s?k=%D9%85%D8%B1%D8%A7%D9%88%D8%AD+%D8%AA%D8%A8%D8%B1%D9%8A%D8%AF+%D9%84%D8%A7%D8%A8%D8%AA%D9%88%D8%A8&page=7&crid=ULJUBMN5YSGK&qid=1671305868&sprefix=%D9%85%D8%B1%D8%A7%D9%88%D8%AD+%D9%84%D8%A7%D8%A8%2Caps%2C5033&ref=sr_pg_7')

f_name = []
f_price = []
f_rate = []

# (first)---> using requests to fetch the url
for i in range (len(list_links)) :
    Fans = requests.get(list_links[i])

    # (second)---> save page content
    src = Fans.content

    # (third)---> creat soup object to parse content
    soup = bs4.BeautifulSoup(Fans.content, "html.parser")

    # (fourth)---> find the element containing information we need
    f_names = soup.find_all("div", {"class": "a-section a-spacing-none a-spacing-top-small s-title-instructions-style"})
    f_prices = soup.find_all("div", {"class": "a-row a-size-base a-color-base"})
    f_rates = soup.find_all("div", {"class": "a-row a-size-small"})

    for i in range(len(f_rates)):
        f_rate.append(f_rates[i].text)

    for i in range(len(f_names)):
        f_name.append(f_names[i].text)

    for i in range(len(f_prices)):
        ans = ""
        value = f_prices[i].text
        for j in value:
            if not j.isdigit() and j != '.':
                break
            else:
                ans += j
        f_price.append(ans + " جنيه")

j = 1
print()
for i in zip(f_name, f_price, f_rate):
    print("details of Laptop cooling fan number", j)
    print("Name is " + i[0])
    print("Price is " + i[1])
    print("Rate is " + i[2])
    print()
    j += 1
