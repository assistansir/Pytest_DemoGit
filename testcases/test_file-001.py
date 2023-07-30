from selenium import webdriver


class Test_001:
    def test_Credence_001(self):
        driver = webdriver.Chrome()
        driver.get("https://credence.in/")
        if driver.title == "Credence":
            driver.save_screenshot("D:\\Pytest_Demo\\Screenshots\\Credence.PNG")
            driver.close()
            assert True
        else:
            print("you are in wrong place")
            driver.close()
            assert False


    def test_sum_002(self):
        a = 2
        b = 5
        sum = a + b
        print("this is sum of a&b :" + str(sum))
        if sum == 7:
            assert True
        else:
            assert False