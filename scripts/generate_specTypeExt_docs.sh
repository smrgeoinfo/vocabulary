#!/bin/bash
#
# Regenerates the vocabulary markdown files from the GH sources
#
#
echo "start"

SCRIPT_FOLDER="$(dirname ${0})"
SOURCE_BASE="../../../iSamples/vocabularies/src/extensions/"
SOURCES=(  "specimenTypeExtension.ttl" )
DEST_FOLDER="../../../iSamples/vocabularies/src/extensions/html/"
mkdir -p "${DEST_FOLDER}"
for src in ${SOURCES[@]}; do
    fname="${src%%.*}.md"
    echo "Generating ${fname}..."
    python "${SCRIPT_FOLDER}/vocab2md.py" "${SOURCE_BASE}${src}" > "${DEST_FOLDER}${fname}"
	quarto render "${DEST_FOLDER}${fname}" --to html
done

echo "Done.  Type 'exit' to close window. "

# this is just to keep the window open to see the console output and any error messages
powershell
