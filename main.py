from selenium import webdriver
import time

# NUMBER GEN
while True:

    def get_var_value(filename="varstore.dat"):
        with open(filename, "a+") as f:
            f.seek(0)
            val = int(f.read() or 0) + 1
            f.seek(0)
            f.truncate()
            f.write(str(val))
            return val

    your_counter = get_var_value()


    # DIGICARD SIGNUPPER
    if __name__ == '__main__':
    
        email = f'UR_EMAIL{your_counter}@gmail.com'

    
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument('--log-level=3')
    
        driver = webdriver.Chrome(executable_path="D:/chromedriver/chromedriver.exe",
                                chrome_options=options)
        driver.set_window_size(1000,1000)
    
        # Send a get request to the url
        driver.get('https://www.ikea.ee/et/client/quickfamily')
        time.sleep(0.5)

        driver.find_element_by_name('email').send_keys(email)
        
        driver.find_element_by_id(
            'createEmailKiosk_submit').click()
        time.sleep(4)
  
        driver.close()