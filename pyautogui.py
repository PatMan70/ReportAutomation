import pyautogui
from time import sleep


# res = pyautogui.locateAllOnScreen('edit.png')
# print(res)

# channel_name = pyautogui.prompt(text='', title='Enter the Channel Name')

pyautogui.hotkey('ctrl', 't')
sleep(2)
pyautogui.write('https://us-east-1.console.aws.amazon.com/cost-management/home?region=ap-southeast-2#/cost-explorer?chartStyle=STACK&costAggregate=unBlendedCost&endDate=2023-06-30&excludeForecasting=false&filter=%5B%5D&futureRelativeRange=CUSTOM&granularity=Monthly&groupBy=%5B%22Service%22%5D&historicalRelativeRange=LAST_6_MONTHS&isDefault=true&reportName=New%20cost%20and%20usage%20report&showOnlyUncategorized=false&showOnlyUntagged=false&startDate=2023-01-01&usageAggregate=undefined&useNormalizedUnits=false')
pyautogui.hotkey('enter')

pyautogui.locateCenterOnScreen('intro-example.jpg', confidence=0.7)
sleep(2)


screenshot = pyautogui.screenshot()
screenshot.save('intro-output.jpg')


