Import-Module Selenium

$geckoDriverPath = "C:\Users\mateu\.nuget\packages\selenium.firefox.webdriver\0.27.0\driver\geckodriver.exe" # Upewnij się, że ścieżka jest poprawna
$firefoxOptions = New-Object OpenQA.Selenium.Firefox.FirefoxOptions
$firefoxOptions.AddArgument("-profile")
$firefoxOptions.AddArgument("C:\Users\mateu\AppData\Local\Mozilla\Firefox\Profiles\gestbvxi.default-release") # Ścieżka do profilu użytkownika Firefox

$driverService = [OpenQA.Selenium.Firefox.FirefoxDriverService]::CreateDefaultService($geckoDriverPath)
$driver = New-Object OpenQA.Selenium.Firefox.FirefoxDriver -ArgumentList $driverService, $firefoxOptions

$driver.Navigate().GoToUrl("https://web.whatsapp.com")

# Poczekaj na załadowanie WhatsApp Web i zeskanowanie kodu QR (jeśli wymagane)
Start-Sleep -Seconds 30

# Wybierz kontakt/grupę
$contactName = "Grzegorz Sarnowski" # Zmień na nazwę kontaktu lub grupy
$searchBox = $driver.FindElementByXPath("//div[@contenteditable='true'][@data-tab='3']")
$searchBox.SendKeys($contactName)
Start-Sleep -Seconds 2
$searchBox.SendKeys([OpenQA.Selenium.Keys]::Enter)

# Wpisz wiadomość
$message = "To jest automatyczna wiadomość wysłana przez PowerShell. Przygotowałem ją przy pomocy skryptu. Miłego popołudnia."
$messageBox = $driver.FindElementByXPath("//div[@contenteditable='true'][@data-tab='6']")
$messageBox.SendKeys($message)
Start-Sleep -Seconds 1
$messageBox.SendKeys([OpenQA.Selenium.Keys]::Enter)

# Zamknij przeglądarkę
$driver.Quit()