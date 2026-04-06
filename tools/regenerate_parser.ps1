# Regenera gen/grammar/* desde grammar/MiniLang.g4
$ErrorActionPreference = "Stop"
$root = (Resolve-Path "$PSScriptRoot\..").Path
$jar = Join-Path $PSScriptRoot "antlr-4.13.1-complete.jar"
if (-not (Test-Path $jar)) {
  Invoke-WebRequest -Uri "https://www.antlr.org/download/antlr-4.13.1-complete.jar" -OutFile $jar -UseBasicParsing
}
$java = (Get-ChildItem "C:\Program Files\Eclipse Adoptium" -Recurse -Filter "java.exe" -ErrorAction SilentlyContinue | Select-Object -First 1).FullName
if (-not $java) { $java = "java" }
Push-Location $root
try {
  & $java -jar $jar -Dlanguage=Python3 -visitor -no-listener -o gen/grammar grammar/MiniLang.g4
} finally { Pop-Location }
Write-Host "Listo: gen/grammar/"
