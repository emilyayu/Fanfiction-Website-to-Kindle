from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from ebooklib import epub


def get_text(website):
    """opens firefox and scrapes data from website"""
    driver = webdriver.Firefox()
    driver.get(website)
    driver.minimize_window()
    # Checks if robot
    # element = driver.find_element( By.CSS_SELECTOR, 'cb-lb')
    # action = ActionChains(driver)
    # action.click(element)
    # action.perform()
    time.sleep(10)
    # action.release(element)
    # action.perform()
    time.sleep(0.2)
    # action.release(element)
    try:
        text = driver.find_element(By.ID, "storytext").get_attribute('innerHTML')
    except:
        return {"text": "", "code":1}
    driver.close()
    return {"text":(text), "code": 0}

def get_book(link):
    """Gets the 8 digits of the book ID"""
    str = link[-8:]
    return str

def to_html(website, id):
    """writes to .html file"""
    code = 0 #0 indicates page exists
    page = 1
    # make sure file is empty
    with open('%s.html' % id, 'w') as f:
            f.write("")

    while code == 0:
        chapter = website + '/' + str(page)
        data = get_text(chapter)
        code =  data["code"]

        # Append to html file
        with open('%s.html' % id, 'a') as f:
            f.write(data["text"])
        page += 1     

    return 



def convert_html_to_mobi(id):
    book = epub.EpubBook()
    with open(html_file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    htmlfile= './'+id+'.html'
    print(htmlfile)
    mobi='./'+id+'.mobi'
    book = epub.read_epub(htmlfile)
    epub.write_epub(mobi, book)
    print("Conversion completed successfully!")
    return




def convert(website):
    book_id = get_book(website)
    # to_html(website, id=book_id)
    convert_html_to_mobi(book_id)


if __name__ == "__main__":
    convert("https://www.fanfiction.net/s/13662783")