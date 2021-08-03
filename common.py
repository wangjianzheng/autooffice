from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def login():
    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    d = webdriver.Chrome("/Users/wangjianzheng/webdriver/chromedriver", options=chrome_options)
    d.get("https://km.sankuai.com/")
    time.sleep(0.2)
    d.find_element_by_id("form-img").click()
    time.sleep(0.2)
    d.find_element_by_id("login-username").send_keys("wangjianzheng")
    d.find_element_by_id("login-password").send_keys("641515QWEasd@")
    time.sleep(0.5)
    d.find_element_by_id("btn-login").click()
    time.sleep(2)
    return d


def wait_get(d, xpath):
    x = None
    try:
        x = WebDriverWait(d, 10, 0.5).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
    except NoSuchElementException:
        print("no such element")
    finally:
        return x


def move_to_item_bottom(d, item):
    js_str = '''
    function scrollToBottom() {
     const domWrapper = document.querySelector('{item}'); 
     console.log(domWrapper);
     (function smoothscroll() {
         const currentScroll = domWrapper.scrollTop;
         const clientHeight = domWrapper.offsetHeight; 
         const scrollHeight = domWrapper.scrollHeight;
         if (scrollHeight - 10 > currentScroll + clientHeight) {
             window.requestAnimationFrame(smoothscroll);
             domWrapper.scrollTo(0, currentScroll + (scrollHeight - currentScroll - clientHeight) / 300);
        }
     })();
    }
    setTimeout(scrollToBottom, 3000);
    '''
    js_str = js_str.replace(" ", "").replace("\n", "").replace("{item}", item).replace("function", "function ").replace(
        "const", "const ")
    print(js_str)
    d.execute_script(js_str)


def move_to_bottom(d):
    js_str = '''
    scrollToBottom = () => {
     console.log('scrollToBottom');
     (function smoothscroll() {
        const currentScroll = document.documentElement.scrollTop || document.body.scrollTop;
     const clientHeight = document.documentElement.clientHeight; 
     const scrollHeight = document.documentElement.scrollHeight;
     if (scrollHeight - 10 > currentScroll + clientHeight) {
          window.requestAnimationFrame(smoothscroll);
     window.scrollTo(0, currentScroll + (scrollHeight - currentScroll - clientHeight) / 2);
     }
      })();
    };
    setTimeout(scrollToBottom, 100);
    '''
    js_str = js_str.replace(" ", "").replace("\n", "").replace("function", "function ").replace("const", "const ")
    print(js_str)
    d.execute_script(js_str)
