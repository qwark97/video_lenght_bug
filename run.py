from playwright.sync_api import sync_playwright
import time


def start(slow_mo):
    start_time = time.time()
    print('**********')
    print(f'\tGiven slow_mo: {slow_mo}')
    with sync_playwright() as p:
        browser = p.chromium.launch(slow_mo=slow_mo)
        print('\tLaunched the browser')
        page = browser.new_page(
            record_video_dir='/tmp',
            )
        print('\tOpened the page')
        start_after_page = time.time()

        page.goto("https://en.wikipedia.org/w/index.php?title=Special:UserLogin&returnto=Main+Page")

        print('\tLoad logging page')
        iters = 20
        print(f'\tFill credentials -> reload iterations: {iters}')
        print(f'\t'+' '*20+'|')
        print('\t', end="")
        for i in range(iters):
            page.reload()
            page.fill('xpath=//input[@id="wpName1"]', 'test')
            page.fill('#wpPassword1', 'test')
            page.click('xpath=//button[@value="Log in"]')
            print(".", end="", flush=True)
        print()
        finish_before_closing = time.time()
        page.close()
        print('\tClosed page')
        video_name = f'video-slowmo{slow_mo}.webm'
        page.video.save_as(video_name)
        print(f'\tSaved video as: {video_name}')
        browser.close()
        print('\tClosed browser')
    outside = time.time()
    print()
    print(f"\tExpected length of the video: {finish_before_closing - start_after_page}s")
    print(f"\tClosing the page/browser/context took: {outside - finish_before_closing}")
    print(f"\tWhole function took: {time.time() - start_time}s")
    print('**********')



if __name__ == '__main__':
    print('===START TEST===')
    start(slow_mo=0)
    start(slow_mo=1000)