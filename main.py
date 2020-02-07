from selenium import webdriver
from secret import passwd
import time

class Igbot:
    def __init__(self, username, passwd):
        self.driver = webdriver.Chrome()
        self.username = username
        self.passwd = passwd

        self.driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
        time.sleep(3)

        self.driver.find_element_by_css_selector("#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(2) > div > label > input").send_keys(username)
        self.driver.find_element_by_css_selector("#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(3) > div > label > input").send_keys(passwd)
        time.sleep(2)
        self.driver.find_element_by_css_selector("#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4) > button > div").click()
        time.sleep(3)

        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()
        time.sleep(1)

    def get_unfollowers(self):
        # enters profile page
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[3]/a').click()
        time.sleep(1)

        # get following names
        self.driver.find_element_by_css_selector('#react-root > section > main > div > header > section > ul > li:nth-child(3) > a').click()
        time.sleep(1)
        following = self.get_names()
        self.driver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div:nth-child(1) > div > div:nth-child(3) > button').click()
        time.sleep(1)

        #get followers name
        self.driver.find_element_by_css_selector('#react-root > section > main > div > header > section > ul > li:nth-child(2) > a').click()
        time.sleep(1)
        followers = self.get_names()
        self.driver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div:nth-child(1) > div > div:nth-child(3) > button').click()
        time.sleep(1)

        unfollowers = [name for name in following if name not in followers]
        print('{} traídores foram encontrados.\n'.format(len(unfollowers)))
        return unfollowers
    
    def unfollow_unfollowers(self):
        unfollowers = self.get_unfollowers()
        unfollowersNum = len(unfollowers)
        self.driver.find_element_by_css_selector('#react-root > section > main > div > header > section > ul > li:nth-child(3) > a').click()
        time.sleep(1)
        print('Limpando o lixo... \n')

        for name in unfollowers:
            # print(name)
            # print('Scrolling')
            self.driver.execute_script('arguments[0].scrollIntoViewIfNeeded()', self.driver.find_element_by_class_name('PZuss').find_element_by_link_text(name))
            time.sleep(1)
            # print('Clicking')
            self.driver.find_element_by_link_text(name).click() # unfollower profile page
            time.sleep(3)
            # print('Click unfollow')
            self.driver.find_elements_by_tag_name('header')[0].find_elements_by_tag_name('button')[0].click() # unfollow
            time.sleep(0.8)
            # print('Confirm')
            self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]').click() # confirm
            time.sleep(1)

            # enters profile page
            print('Profile page again')
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[3]/a').click()
            time.sleep(1)
            # following tab
            print('following tab')
            self.driver.find_element_by_css_selector('#react-root > section > main > div > header > section > ul > li:nth-child(3) > a').click()
            time.sleep(1)
            print('Betrayer {} was unfollowed. \n'.format(name))
            unfollowers.remove(name)
        print('All {} betrayers are now unfollowed. \n'.format(unfollowersNum))

    def get_names(self):
        try:
            names = []
            for name in self.driver.find_elements_by_css_selector('.FPmhX.notranslate._0imsa'):
                names.append(name.text)
            return names
        except:
            return []

        

if __name__ == '__main__':
    igbot = Igbot('', passwd)
    try:
        igbot.unfollow_unfollowers()
    except:
        print('Error...')