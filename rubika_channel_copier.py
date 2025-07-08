
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
# import schedule
# import time
# import re
# import os

# # آدرس کانال منبع و مقصد
# SOURCE_CHANNEL = "https://web.rubika.ir/#c=c0O2uV05fc5a8d95859039bbca48ddd6"  # ← تغییر بده
# TARGET_CHANNEL = "https://web.rubika.ir/#c=c0BKxXs03b1db7aecdc6888ed7aa5589"              # ← کانال خودت
# # فایل ذخیره پیام آخر
# LAST_POST_FILE = "last_post.txt"

# # تابع تمیز کردن پیام
# def clean_text(text):
#     # حذف آیدی‌ها (@something)
#     text = re.sub(r'@\w+', '', text)
#     # حذف لینک‌ها (http:// یا https:// یا rubika.ir لینک‌ها)
#     text = re.sub(r'http[s]?://\S+', '', text)
#     text = re.sub(r'(rubika\.ir|rubika\.me)/\S+', '', text)
#     # حذف فاصله‌های اضافی
#     return text.strip()

# def get_last_saved_post():
#     if not os.path.exists(LAST_POST_FILE):
#         return ''
#     with open(LAST_POST_FILE, 'r', encoding='utf-8') as f:
#         return f.read().strip()

# def save_last_post(text):
#     with open(LAST_POST_FILE, 'w', encoding='utf-8') as f:
#         f.write(text.strip())

# def job():
#     print("🚀 اجرای ربات ساعتی...")

#     service = Service("D:\chromedriver-win64\chromedriver.exe")
#     driver = webdriver.Chrome(service=service)
#     driver.get("https://web.rubika.ir")
#     input("📲 وارد حساب روبیکا شو و Enter بزن...")

#     driver.get(SOURCE_CHANNEL)
#     time.sleep(6)

#     posts = driver.find_elements(By.CLASS_NAME, "message--text")
#     if not posts:
#         print("❌ پستی پیدا نشد.")
#         driver.quit()
#         return

#     last_raw = posts[-1].text
#     last_cleaned = clean_text(last_raw)
#     if not last_cleaned.strip():
#         print("⚠️ پیام پس از پاک‌سازی خالی بود. ارسال نشد.")
#         driver.quit()
#         return

#     last_sent = get_last_saved_post()
#     if last_cleaned == last_sent:
#         print("🟡 پیام تکراری بود. ارسال نشد.")
#         driver.quit()
#         return

#     # رفتن به کانال مقصد و ارسال
#     driver.get(TARGET_CHANNEL)
#     time.sleep(5)

#     try:
#         message_box = driver.find_element(By.CLASS_NAME, "composer_rich_textarea")
#         message_box.send_keys(last_cleaned)
#         time.sleep(1)
#         message_box.send_keys(Keys.ENTER)
#         save_last_post(last_cleaned)
#         print("✅ پیام جدید ارسال شد.")
#     except Exception as e:
#         print("❌ خطا در ارسال پیام:", e)

#     driver.quit()

# # تنظیم برنامه‌ریزی هر 1 ساعت
# schedule.every(5).seconds.do(job)

# print("🤖 ربات هر ساعت یک‌بار اجرا خواهد شد.")
# while True:
#     schedule.run_pending()
#     time.sleep(10)
#------------------------------------------------

# import time
# import schedule
# import re
# import random
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options

# # def get_chrome_driver():
# #     chrome_options = Options()
# #     chrome_options.debugger_address = "127.0.0.1:9222"  # پورت دیباگ فعال

# #     # نیازی به مسیر chromedriver نداری اگر توی سیستم اضافه شده، در غیر این صورت مسیر کامل بده:
# #     service = Service("C:/Users/Salam/Desktop/chromedriver.exe")

# #     driver = webdriver.Chrome(service=service, options=chrome_options)
# #     return driver

# # تست
# # driver = get_chrome_driver()
# # driver.get("https://web.rubika.ir/")
# # print("✅ متصل شد به مرورگر کروم باز شده")


# # تنظیمات مسیرها
# CHROMEDRIVER_PATH = "C:/Users/Salam/Desktop/chromedriver.exe"
# CHROME_PROFILE_PATH = "C:/Users/Salam/AppData/Local/Google/Chrome/User Data"
# PROFILE_NAME = "Default"  # یا Profile 1 اگر از پروفایل جداگانه استفاده می‌کنی

# SOURCE_CHANNEL_URL = "https://web.rubika.ir/#c=c0ByGjT058c10a1950b4a00a73b17cf8"  # کانال منبع
# TARGET_CHANNEL_URL = "https://web.rubika.ir/#c=c0BKxXs03b1db7aecdc6888ed7aa5589"  # کانال مقصد خودت
# LAST_POST_FILE = "last_post.txt"

# def remove_ids_links(text):
#     text = re.sub(r"@\w+", "", text)
#     text = re.sub(r"http\S+", "", text)
#     return text.strip()

# def get_last_saved_text():
#     try:
#         with open(LAST_POST_FILE, "r", encoding="utf-8") as f:
#             return f.read().strip()
#     except:
#         return ""

# def save_last_text(text):
#     with open(LAST_POST_FILE, "w", encoding="utf-8") as f:
#         f.write(text.strip())

# def get_chrome_driver():
#     chrome_options = Options()
#     chrome_options.debugger_address = "127.0.0.1:9222"  # اتصال به کروم باز شده

#     # بدون استفاده از Service چون در حال اتصال به کروم باز شده هستیم
#     driver = webdriver.Chrome(options=chrome_options)
#     return driver

# def scroll_up(driver, times=10, delay=1):
#             post_container = driver.find_element(By.TAG_NAME, "body")  # یا المنت اصلی پست‌ها
#             for _ in range(times):
#                 post_container.send_keys(Keys.PAGE_UP)
#                 time.sleep(delay)
                
# def job():
#     print("🤖 اجرای ربات...")
#     driver = get_chrome_driver()
#     try:
        
#         # ورود به کانال منبع

#         driver.get(SOURCE_CHANNEL_URL)

#         body = driver.find_element(By.TAG_NAME, "body")
#         for _ in range(2):  # اسکرول برای بارگذاری حدود ۱۰۰ پست
#             scroll_up(driver, times=10,delay=0.2)
        
#         posts = driver.find_elements(By.CSS_SELECTOR, "div.bubble-content div[dir=rtl] ")
#         print(f"📄 پست‌های پیدا شده: {len(posts)}")

#         all_texts = [p.text.strip() for p in posts if len(p.text.strip()) > 10]
#         random.shuffle(all_texts)

#         last_post = get_last_saved_text()
#         for text in all_texts:
#             clean_text = remove_ids_links(text)
#             if clean_text and clean_text != last_post:
#                 break
#         else:
#             print("🟡 پست جدیدی یافت نشد.")
#             driver.quit()
#             return

#         # ورود به کانال مقصد
#         driver.get(TARGET_CHANNEL_URL)

#         try:
#             driver.get(TARGET_CHANNEL_URL)
#             time.sleep(5)
#             message_box = driver.find_element(By.CLASS_NAME, "composer_rich_textarea")
#             message_box.send_keys(clean_text)
#             time.sleep(1)
#             message_box.send_keys(Keys.ENTER)
#             save_last_text(clean_text)
#             print("✅ پیام جدید ارسال شد.")
#         except Exception as e:
#             print("❌ خطا در ارسال پیام:", e)
            
        
#         # driver.get("https://web.rubika.ir/#c=c0BKxXs03b1db7aecdc6888ed7aa5589")
#         # time.sleep(4)
        
#         # driver.find_element(By.TAG_NAME, "textarea").click()
#         # time.sleep(2)
        
#         # driver.find_element(By.CLASS_NAME, "composer_rich_textarea").click()
#         # time.sleep(2)

#         # driver.find_element(By.CLASS_NAME, "rr").click()
#         # print("✅ پست ارسال شد.")
#         # save_last_text(clean_text)

#     except Exception as e:
#         print("❌ خطا:", e)

#     driver.quit()

# # برنامه‌ریزی ساعتی
# print("⏰ ربات فعال شد - هر ساعت یک پست جدید منتشر می‌شود.")
# schedule.every(1).seconds.do(job)

# while True:
#     schedule.run_pending()
#     time.sleep(5)

#-----------------------------------------------------
# import time
# import schedule
# import re
# import random
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# # تنظیمات مسیرها
# CHROMEDRIVER_PATH = "C:/Users/Salam/Desktop/chromedriver.exe"
# CHROME_PROFILE_PATH = "C:/Users/Salam/AppData/Local/Google/Chrome/User Data"
# PROFILE_NAME = "Default"  # یا "Profile 1" اگر از پروفایل جداگانه استفاده می‌کنی

# SOURCE_CHANNEL_URL = "https://web.rubika.ir/#c=c0ByGjT058c10a1950b4a00a73b17cf8"  # کانال منبع
# TARGET_CHANNEL_URL = "https://web.rubika.ir/#c=c0BKxXs03b1db7aecdc6888ed7aa5589"  # کانال مقصد
# LAST_POST_FILE = "last_post.txt"

# def get_chrome_driver():
#     chrome_options = Options()
#     chrome_options.debugger_address = "127.0.0.1:9222"  # اتصال به کروم باز شده
#     driver = webdriver.Chrome(options=chrome_options)
#     return driver

# def remove_ids_links(text):
#     text = re.sub(r"@\w+", "", text)
#     text = re.sub(r"http\S+", "", text)
#     return text.strip()

# def get_last_saved_text():
#     try:
#         with open(LAST_POST_FILE, "r", encoding="utf-8") as f:
#             return f.read().strip()
#     except:
#         return ""

# def save_last_text(text):
#     with open(LAST_POST_FILE, "w", encoding="utf-8") as f:
#         f.write(text.strip())

# def scroll_up(driver, times=10, delay=1):
#     post_container = driver.find_element(By.TAG_NAME, "body")
#     for _ in range(times):
#         post_container.send_keys(Keys.PAGE_UP)
#         time.sleep(delay)

# def job():
#     print("\U0001F916 اجرای ربات...")
#     driver = get_chrome_driver()
#     wait = WebDriverWait(driver, 15)

#     try:
#         # ورود به کانال منبع
#         driver.get(SOURCE_CHANNEL_URL)
#         time.sleep(5)

#         # اسکرول به بالا برای بارگذاری پست‌های بیشتر
        

#         posts = driver.find_elements(By.CLASS_NAME, "bubble-content")
#         print(f"\U0001F4C4 پست‌های پیدا شده: {len(posts)}")

#         all_texts = [p.text.strip() for p in posts if len(p.text.strip()) > 10]
#         random.shuffle(all_texts)

#         last_post = get_last_saved_text()
#         for text in all_texts:
#             clean_text = remove_ids_links(text)
#             if clean_text and clean_text != last_post:
#                 break
#         else:
#             print("\U0001F7E1 پست جدیدی یافت نشد.")
#             driver.quit()
#             return

#         # ورود به کانال مقصد
#         driver.get(TARGET_CHANNEL_URL)
#         time.sleep(4)

#         # کلیک روی textarea اگر قابل کلیک بود
#         try:
#             # input_box = driver.find_element(By.CSS_SELECTOR, "div.input-message-container div[contenteditable='true']")
#             # input_box.click()
#             # input_box.send_keys()
#             # input_box.send_keys(Keys.ENTER)
#             textarea_container = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "input-message-input")))
#             driver.execute_script("arguments[0].scrollIntoView(true);", textarea_container)
#             driver.execute_script("arguments[0].click();", textarea_container)
#         except Exception as e:
#             print("❌ خطا در کلیک روی textarea:", e)
#             driver.quit()
#             return

#         # نوشتن متن در textarea
#         try:
#             textarea = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "input-message-input")))
#             textarea.send_keys(clean_text)
#             time.sleep(1)
#         except Exception as e:
#             print("❌ خطا در نوشتن متن:", e)
#             driver.quit()
#             return

#         # کلیک روی دکمه ارسال
#         try:
#             send_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea")))
#             driver.execute_script("arguments[0].scrollIntoView(true);", send_button)
#             driver.execute_script("arguments[0].click();", send_button)
#             print("✅ پست ارسال شد.")
#             save_last_text(clean_text)
#         except Exception as e:
#             print("❌ خطا در ارسال پست:", e)

#     except Exception as e:
#         print("❌ خطای کلی:", e)

#     driver.quit()

# # برنامه‌ریزی زمانی برای اجرای خودکار
# print("⏰ ربات فعال شد - هر 5 ثانیه اجرا می‌شود (برای تست).")
# schedule.every(5).seconds.do(job)

# while True:
#     schedule.run_pending()
#     time.sleep(10)
#---------------------------------------------------------------------
import time
import schedule
import re
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import hashlib



# تنظیمات
CHROME_PROFILE_PATH = "C:/Users/Salam/AppData/Local/Google/Chrome/User Data"
PROFILE_NAME = "Default"
SOURCE_CHANNEL_URL = ["https://web.rubika.ir/#c=c0ByGjT058c10a1950b4a00a73b17cf8",
                      "https://web.rubika.ir/#c=c0Nuuk0b1e997ec98b91ef5f148a063a",
                      "https://web.rubika.ir/#c=c0Ha2g0a0c226f70bf82d47e488de654",
                      "https://web.rubika.ir/#c=c0BRJvc0463f47cc42ff265ec7a4bb95",
                      "https://web.rubika.ir/#c=c0WWpp05c9fae87df955ddac2f0b1bd8",
                      "https://web.rubika.ir/#c=c01SHk091deabd28d05f2daad792ec1a",
                      "https://web.rubika.ir/#c=c0O2uV05fc5a8d95859039bbca48ddd6",
                      "https://web.rubika.ir/#c=c0BTL11015a86df1bbdf546a8e360d4d",
                      "https://web.rubika.ir/#c=c0BjcZU066157c9930d13bc872f4b5da",
                      "https://web.rubika.ir/#c=c0BHH8N0aa3ee36da9e7551f09f46319"
                      ]
TARGET_CHANNEL_URL = "https://web.rubika.ir/#c=c0CJUdv030f648af9380a28636155e89"
LAST_POST_FILE = "last_post.txt"


def get_text_hash(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

SENT_HASH_FILE = "sent_hashes.txt"

def get_sent_hashes():
    try:
        with open(SENT_HASH_FILE, "r", encoding="utf-8") as f:
            return set(line.strip() for line in f if line.strip())
    except FileNotFoundError:
        return set()

def save_sent_hash(text):
    text_hash = get_text_hash(text)
    with open(SENT_HASH_FILE, "a", encoding="utf-8") as f:
        f.write(text_hash + "\n")
        
# پاک‌سازی لینک و آیدی
def remove_ids_links(text):
    text = re.sub(r"@\w+", "", text)
    text = re.sub(r"http\S+", "", text)
    return text.strip()

# حذف کاراکترهای خارج از محدوده یونیکد BMP
def is_bmp_safe(text):
    return all(ord(char) <= 0xFFFF for char in text)

# گرفتن آخرین پست ذخیره‌شده
def get_last_saved_text():
    try:
        with open(LAST_POST_FILE, "r", encoding="utf-8") as f:
            return f.read().strip()
    except:
        return ""

# ذخیره آخرین پست
def save_last_text(text):
    with open(LAST_POST_FILE, "w", encoding="utf-8") as f:
        f.write(text.strip())

# اتصال به مرورگر باز شده با Chrome Debugging
def get_chrome_driver():
    chrome_options = Options()
    chrome_options.debugger_address = "127.0.0.1:9222"
    return webdriver.Chrome(options=chrome_options)

# اسکرول به بالا برای بارگذاری پیام‌ها
def scroll_up(driver, times=100, delay=0.05):
    body = driver.find_element(By.TAG_NAME, "body")
    for _ in range(times):
        body.send_keys(Keys.PAGE_UP)
        time.sleep(delay)
        
def scroll_using_mouse(driver, scroll_count=50, delay=0.01):
    try:
        for _ in range(scroll_count):
            # پیدا کردن آخرین پیام روی صفحه
            messages = driver.find_elements(By.CLASS_NAME, "bubble-content")
            if not messages:
                print("⛔ پیام پیدا نشد.")
                break
            last_msg = messages[1]  # یا messages[-1] برای آخرین پیام
            ActionChains(driver).move_to_element(last_msg).perform()
            time.sleep(delay)
    except Exception as e:
        print("❌ خطا در اسکرول با موس:", e)
        
# وظیفه اصلی
def job():
    print("🤖 اجرای ربات...")

    driver = get_chrome_driver()
    try:
        
        # ۱. ورود به کانال منبع
        driver.get(random.choice(SOURCE_CHANNEL_URL))
        time.sleep(1)
        scroll_using_mouse(driver, scroll_count=20)
        # scroll_up(driver, times=50)
        # first_message = driver.find_element(By.CLASS_NAME, "bubble-content-wrapper")
        # first_message.click()
        # time.sleep(1)
        # print("🖱️ روی اولین پیام کلیک شد.")
        

        posts = driver.find_elements(By.CSS_SELECTOR, "div.bubble-content div[dir=rtl]")
        print(f"📄 تعداد پست‌ها: {len(posts)}")

        texts = [p.text.strip() for p in posts if 200 > len(p.text.strip()) > 10]
        random.shuffle(texts)
        driver.get("https://web.rubika.ir")
        time.sleep(0.5)
        sent_hashes = get_sent_hashes()

        chosen_msg = None
        for text in texts:
            cleaned = remove_ids_links(text)
            text_hash = get_text_hash(cleaned)
            if cleaned and is_bmp_safe(cleaned) and text_hash not in sent_hashes:
                chosen_msg = cleaned
                break


        if not chosen_msg:
            print("🟡 پست جدید مناسب برای ارسال یافت نشد.")
            driver.get("https://web.rubika.ir")
            return

        # ۲. ورود به کانال مقصد و ارسال

        
        driver.get(TARGET_CHANNEL_URL)
        time.sleep(1)
        message_box = driver.find_element(By.CLASS_NAME, "composer_rich_textarea")
        message_box.send_keys(chosen_msg)
        time.sleep(1)
        message_box.send_keys(Keys.ENTER)
        save_sent_hash(chosen_msg)
        print("✅ پیام ارسال شد:", chosen_msg[:50], "...")
        time.sleep(1)

    except Exception as e:
        print("❌ خطا:", e)

    finally:
        driver.get("https://web.rubika.ir")

# زمان‌بندی اجرای ربات
print("✅ ربات آماده است - اجرای خودکار فعال شد.")
schedule.every(6).minutes.do(job)  # هر شش دقیقه یک بار

while True:
    schedule.run_pending()
    time.sleep(3)
