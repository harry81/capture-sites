import sys
import datetime
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
    "Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/53 "
    "(KHTML, like Gecko) Chrome/15.0.87"
)

def capture(driver, site):
    #driver.set_window_size(1024, 768)
    driver.set_window_size(384, 567)

    driver.get('http://%s/' % site)
    dt = datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S')
    fname = '%s%s.png' % (site, dt)
    ret = driver.save_screenshot('shots/%s' % fname) # save a screenshot to disk
    print "%s captured" % (fname)

def main(args):
    driver = webdriver.PhantomJS(desired_capabilities=dcap)
    sites = ['www.naver.com', 'www.daum.net']
    for site in sites:
        capture(driver, site)

if __name__ == '__main__':
    main(sys.argv)
