### **Web Scraping with Python Cheat Sheet:**

#### **1. Introduction to Web Scraping:**
   - **What is Web Scraping?**
     - Web scraping is the process of extracting data from websites, usually in HTML format, to obtain useful information.

#### **2. Basics of HTML:**
   - **HTML Structure:**
     ```html
     <!DOCTYPE html>
     <html>
     <head>
         <title>Page Title</title>
     </head>
     <body>
         <h1>This is a Heading</h1>
         <p>This is a paragraph.</p>
     </body>
     </html>
     ```
   - **HTML Tags:**
     - `<tag>`: Opening tag.
     - `</tag>`: Closing tag.
     - `<tag attribute="value">`: Tag with attribute.

#### **3. Python Libraries for Web Scraping:**
   - **Requests:**
     - Used for making HTTP requests to fetch HTML content.
     ```python
     import requests

     url = "https://example.com"
     response = requests.get(url)
     html_content = response.text
     ```
   - **Beautiful Soup:**
     - Parses HTML content and provides a convenient way to navigate and search the HTML tree.
     ```bash
     pip install beautifulsoup4
     ```
     ```python
     from bs4 import BeautifulSoup

     soup = BeautifulSoup(html_content, 'html.parser')
     ```
   - **Selenium:**
     - Automates web browsers, useful for dynamic content rendered by JavaScript.
     ```bash
     pip install selenium
     ```
     ```python
     from selenium import webdriver

     url = "https://example.com"
     driver = webdriver.Chrome()
     driver.get(url)
     html_content = driver.page_source
     ```

#### **4. Fetching HTML Content:**
   - **Using Requests:**
     ```python
     import requests

     url = "https://example.com"
     response = requests.get(url)
     html_content = response.text
     ```
   - **Using Selenium (with ChromeDriver):**
     ```python
     from selenium import webdriver

     url = "https://example.com"
     driver = webdriver.Chrome()
     driver.get(url)
     html_content = driver.page_source
     ```

#### **5. Parsing HTML with Beautiful Soup:**
   - **Installation:**
     ```bash
     pip install beautifulsoup4
     ```
   - **Basic Usage:**
     ```python
     from bs4 import BeautifulSoup

     soup = BeautifulSoup(html_content, 'html.parser')
     ```

#### **6. Navigating HTML Tree:**
   - **Finding Tags:**
     ```python
     tag = soup.find('tag_name')  # Find the first occurrence
     tags = soup.find_all('tag_name')  # Find all occurrences
     ```
   - **Accessing Attributes:**
     ```python
     attribute_value = tag['attribute_name']
     ```

#### **7. Extracting Data:**
   - **Text Content:**
     ```python
     text = tag.get_text()
     ```
   - **Attribute Values:**
     ```python
     value = tag['attribute_name']
     ```

#### **8. Handling Dynamic Content:**
   - **Using Selenium:**
     ```python
     from selenium.webdriver.common.by import By
     from selenium.webdriver.support.ui import WebDriverWait
     from selenium.webdriver.support import expected_conditions as EC

     element = WebDriverWait(driver, 10).until(
         EC.presence_of_element_located((By.ID, 'element_id'))
     )
     ```

#### **9. Handling Forms and Interactions:**
   - **Filling Forms (Selenium):**
     ```python
     input_element = driver.find_element(By.NAME, 'input_name')
     input_element.send_keys('input_value')
     ```

#### **10. Best Practices and Tips:**
   - **Respecting Robots.txt:**
     - Always check a website's `robots.txt` file to ensure you're allowed to scrape.
   - **User-Agent Header:**
     - Set a user-agent header in your requests to mimic a real browser.
     ```python
     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
     response = requests.get(url, headers=headers)
     ```

#### **11. Dealing with APIs:**
   - **Using Requests for API Calls:**
     ```python
     import requests

     api_url = "https://api.example.com/data"
     response = requests.get(api_url)
     data = response.json()
     ```


**Additional Notes:**
- When using Selenium, ensure you have the appropriate WebDriver (e.g., ChromeDriver) installed.
- For dynamic content, use Selenium with WebDriverWait for elements to load.
- Explore Beautiful Soup's advanced features for complex HTML parsing.