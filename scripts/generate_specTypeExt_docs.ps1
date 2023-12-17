Write-Host "start"
$SCRIPT_FOLDER = (Get-Item $MyInvocation.MyCommand.Path).Directory.FullName
$SOURCE_BASE = "../../../iSamples/metadata_profile_earth_science/vocabulary/"
$SOURCES = @("earthenv_specimen_type.ttl")
$DEST_FOLDER = "../../../iSamples/metadata_profile_earth_science/docs/"

# Create destination folder if it doesn't exist
New-Item -ItemType Directory -Force -Path $DEST_FOLDER | Out-Null

foreach ($src in $SOURCES) {
    $fname = [System.IO.Path]::ChangeExtension($src, "md")
    Write-Host ("Generating {0}..." -f $fname)
	# call via conda to get the correct python env
    & "C:\Users\smrTu\miniconda3\Scripts\conda.exe" run -n quarto python ("{0}\vocab2md.py" -f $SCRIPT_FOLDER) ("{0}{1}" -f $SOURCE_BASE, $src) | Out-File -FilePath ("{0}{1}" -f $DEST_FOLDER, $fname)
	# Assuming quarto is in the system PATH
    quarto render ("{0}{1}" -f $DEST_FOLDER, $fname) --to html
}

Write-Host "Done. "
# run in the C:\Users\smrTu\OneDrive\Documents\GithubC\smrgeoinfo\vocabulary\scripts directory
# powershell generate_specTypeExt_docs.ps1
