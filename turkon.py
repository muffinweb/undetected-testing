from seleniumbase import SB

# TrackNumber

trackingNumber = ""

# Elements to use
input_element = "body > app-root > app-layout > div > div > div > app-tracking > div > div.col-12 > div > div > div.field.col-12.md\\:col-6.mt-3 > span > input"
submit_element = "body > app-root > app-layout > div > div > div > app-tracking > div > div.col-12 > div > div > div.field.col-12.md\\:col-2.mt-3 > button"

with SB(uc=True, test=True) as sb:
    url = "https://myturkonline.turkon.com/tracking"
    sb.uc_open_with_reconnect(url, 5)

    #Recaptcha solving thing
    sb.uc_gui_click_captcha()
    sb.sleep(2)
    sb.uc_gui_handle_captcha()

    sb.assert_element(input_element)
    sb.highlight(input_element)

    sb.sleep(1)

    sb.assert_element(submit_element)
    sb.highlight(submit_element)

    sb.post_message_and_highlight("All elements are available", "body")

    sb.sleep(1)

    print("seleniumbase successfully passed the case")



    # sb.assert_text("Username", '[for="user_login"]', timeout=3)
    # sb.assert_element('label[for="user_login"]')
    # sb.highlight('button:contains("Sign in")')
    # sb.highlight('h1:contains("GitLab.com")')
    # sb.post_message("SeleniumBase wasn't detected", duration=4)
    # print("Success! Website did not detect SeleniumBase!")
