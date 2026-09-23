from bs4 import BeautifulSoup

# Reading HTML file
items=[] # Collecting data into the list
for i in range(1,51):
    with open(f"htmls\page-{i}.html",'r',encoding="utf-8") as f:
            content = f.read()
            print(f"file-{i} Readed ")

    # Creating our soup by using content 

    soup = BeautifulSoup(content,"html.parser")

    # inspect the website ,understand the structure before extracting data
    # To all h3 from the website ,why because it has the book titles and we want them
    # h3s = soup.find_all("h3")

    # To get h3s first occurence <a title="---"></a>
    # It will give you book title
    # For understanding purpose only
    # for h3 in h3s:
    #     print(h3.find("a")['title'])

    # Selecting article because it includes title ,price and ratings of the book.
    articles = soup.select("article.product_pod") # To select by class name
    # print(articles) Testing Purpose Only 

    for article in articles:
        title = article.find('h3').find('a')['title']
        price= article.select_one("p.price_color").text.split("£")[1]
        # select_one is used because we want data from only one element ,.text is used to give only
        #  text part ,spilt() is used to spilt the string [1] index 1 means only value 34.5
        rating_element=article.select_one("p.star-rating") # It will take the all classes 
        # Why we are taking classes p.star-rating because it has the class by rating value
        # Eg : <p class="star-rating Three"> To get the rating we have to extract the class of the 
        # p class star-rating .
        rating= rating_element['class'][1]
        items.append([title,price,rating])

# Converting this into a DataFrame 
import pandas as pd

df = pd.DataFrame(items,columns=['Book Title','Price','Rating'])

# Moving data into CSV file
df.to_csv("data.csv",index=False)



     