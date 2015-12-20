import sys
import datetime
from selenium import webdriver

def capture(driver, site):
    driver.set_window_size(1024, 768)

    driver.get('https://%s/' % site)
    dt = datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S')
    fname = '%s_%s.png' % (site, dt)
    driver.save_screenshot(fname) # save a screenshot to disk
    print "%s captured" % (fname)

def main(args):
    driver = webdriver.PhantomJS()
    sites = ['www.naver.com', 'www.daum.net']
    for site in sites:
        capture(driver, site)

if __name__ == '__main__':
    main(sys.argv)
