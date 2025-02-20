# Selenium Search Functionality Test  

This project contains a **Selenium automation script** (`qa_selenium_test.py`) that tests the search functionality on the **Selenium Playground Table Sort Search Demo** page.  

##  Test Scenario  
1. Open Chrome and navigate to:  
   👉 [Selenium Playground Table Sort Search Demo](https://www.lambdatest.com/selenium-playground/table-sort-search-demo)  
2. Locate the **search box** and type `"New York"`.  
3. Validate that **5 search results are displayed** out of 24 total entries.  
4. Take a **screenshot** (`search_results.png`) of the search results.  
5. Close the browser after validation.  

---

## 📂 Project Structure  







selenium-test/ │── qa_selenium_test.py # Selenium test script │── requirements.txt # List of dependencies │── README.md # Project documentation │── search_results.png # Screenshot of test result (generated after running the test)
---

##  Setup Instructions  

### **1️⃣ Install Python (if not installed)**  
- Download and install Python **3.7 or later** from:  
   [https://www.python.org/downloads/](https://www.python.org/downloads/)  

- Verify installation by running:
  ```sh
  python --version


  2️⃣ Install Dependencies
Install Selenium, pytest, and Chrome WebDriver Manager by running:
sh

pip install -r requirements.txt
If requirements.txt is not available, manually install:


sh

pip install selenium pytest webdriver-manager

3️⃣ Run the Test

Execute the following command:

sh

pytest qa_selenium_test.py
4️⃣ Expected Output
✅ Chrome browser opens and navigates to the test page.
✅ The search box is filled with "New York".
✅ The table updates, showing exactly 5 rows matching "New York".
✅ A screenshot (search_results.png) is saved in the project folder.
✅ The test passes with no errors.

Troubleshooting
1️⃣ Chrome Browser Not Opening?
Ensure ChromeDriver is correctly installed:

sh

chromedriver --version
If not installed, download the ChromeDriver version matching your Chrome browser from:
https://chromedriver.chromium.org/downloads

2️⃣ Page Not Loading?
Check if the test site is accessible manually:
Selenium Playground Table Sort Search Demo

3️⃣ Test Fails with Incorrect Row Count?
Ensure the test is searching for "New York" exactly as it appears in the table.
Modify the XPath if the table structure has changed.
📜 License
This project is open-source and free to use.

yaml
---

### **How to Use It**  
1. Save this content as **`README.md`** in your project folder.  
2. When you upload this project to **GitHub**, the README will be displayed as the project’s documentation.  

Let me know if you need modifications! 😊🚀
