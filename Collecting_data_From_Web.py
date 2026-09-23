import requests

# This will hit a request to the website for the data
a = requests.get("https://books.toscrape.com/")
# print(a.text)

# To Store the Data, We will store all pages of this website which is 50
# with open('htmls/page1.html','w') as f:
#     f.write(a.text) To get 1 page only

# Now to get all 50 pages 
for i in range(1,51):
    a = requests.get(f"https://books.toscrape.com/catalogue/page-{i}.html")
    with open(f"htmls/page-{i}.html","w",encoding="utf-8") as f:
        f.write(a.text)
        print(f"Downloaded Pages {i} Successfully ")
