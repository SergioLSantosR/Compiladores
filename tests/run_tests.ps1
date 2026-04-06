$root = Split-Path $PSScriptRoot -Parent
Set-Location $root
$py = @(
  (Get-Command python -ErrorAction SilentlyContinue).Source,
  (Get-Command py -ErrorAction SilentlyContinue).Source
) | Where-Object { $_ } | Select-Object -First 1
if (-not $py) { Write-Error "No se encontró python en PATH"; exit 1 }

$tests = @(
  @{ path = "tests/test_valido.ml"; expect = 0 },
  @{ path = "tests/test_error_lexico.ml"; expect = 1 },
  @{ path = "tests/test_error_sintactico.ml"; expect = 1 },
  @{ path = "tests/test_error_semantico.ml"; expect = 2 }
)
$fail = 0
foreach ($t in $tests) {
  & $py -m src.pipeline $t.path
  $c = $LASTEXITCODE
  if ($c -ne $t.expect) { Write-Host "FAIL $($t.path) esperado $($t.expect) obtuvo $c"; $fail++ }
  else { Write-Host "OK   $($t.path)" }
}
exit $fail
